from urllib.parse import urljoin

from captcha.fields import ReCaptchaField
from django.conf import settings
from django.urls import reverse
from django import forms
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

from bartenders.models import Bartender, BartenderShift, BartenderApplication
from fredagscafeen.email import send_template_email


class BartenderInfoForm(forms.ModelForm):
	class Meta:
		model = Bartender
		fields = ('name', 'username', 'email', 'studentNumber', 'phoneNumber', 'tshirt_size')
		# email isn't currently editable as we need to handle
		# removing the old and possibly adding the new to the mailing list
		widgets = {
			'username': forms.TextInput(attrs={'readonly': True}),
			'email': forms.EmailInput(attrs={'readonly': True}),
		}


class LoginForm(forms.Form):
	email = forms.EmailField()
	captcha = ReCaptchaField()

	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			Bartender.objects.get(email=email)
		except Bartender.DoesNotExist:
			raise forms.ValidationError('Ukendt email')

		return email

	def send_email(self):
		email_address = self.cleaned_data['email']
		bartender = Bartender.objects.get(email=email_address)

		url = urljoin(settings.SELF_URL, reverse('email_login', args=(bartender.username, bartender.email_token)))

		return send_template_email(
			subject='fredagscafeen.dk login',
			body_template='''{link} for at logge ind.

/snek''',
			text_format={'link': f'Gå ind på {url}'},
			html_format={'link': mark_safe(f'<a href="{url}">Klik her</a>')},
			to=[email_address]
		)


class BartenderApplicationForm(forms.ModelForm):
	captcha = ReCaptchaField()

	class Meta:
		model = BartenderApplication
		fields = '__all__'

	def send_email(self, pk):
		d = self.cleaned_data

		url = urljoin(settings.SELF_URL, reverse('admin:bartenders_bartenderapplication_change', args=(pk,)))

		extra_info = ''
		if d['info']:
			extra_info = f'''
Extra info:
{d["info"]}
'''
		d['extra_info'] = extra_info

		return send_template_email(
			subject=f'Bartender application: {d["name"]}',
			body_template='''This is an automated email.

{name} has applied to become a bartender:
{name} ({username})
{studentNumber} - {email}
{phoneNumber}
{extra_info}
The application can be accepted or denied through {link}.

/snek''',
			text_format={'link': f'the admin interfacec: {url}', **d},
			html_format={'link': mark_safe(f'<a href="{url}">the admin interface</a>'), **d},
			to=['best@fredagscafeen.dk']
		)


class SwapForm1(forms.Form):
	bartender1 = forms.ModelChoiceField(label='Bartender 1', queryset=Bartender.objects)
	bartender2 = forms.ModelChoiceField(label='Bartender 2', queryset=Bartender.objects)
	swap = forms.BooleanField(help_text='(or replace 1 with 2)', initial=True, required=False)


class SwapForm2(SwapForm1):
	bartender_shift1 = forms.ModelChoiceField(label='Shift 1', queryset=BartenderShift.objects.none())
	bartender_shift2 = forms.ModelChoiceField(label='Shift 2', queryset=BartenderShift.objects.none())

	def __init__(self, *args, swap, bartender1, bartender2, **kwargs):
		super().__init__(*args, **kwargs)

		self.fields['bartender1'].initial = bartender1
		self.fields['bartender2'].initial = bartender2
		self.fields['swap'].initial = swap

		self.fields['bartender_shift1'].queryset = BartenderShift.with_bartender(bartender1)
		self.fields['bartender_shift2'].queryset = BartenderShift.with_bartender(bartender2)

		if not swap:
			del self.fields['bartender_shift2']
