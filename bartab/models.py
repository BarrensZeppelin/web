import datetime

from django.db import models
from django.db.models import F, Sum, Value
from django.db.models.functions import Coalesce
from django.utils import timezone

from .forms import SumValue, SumField as SumFormField


class SumField(models.TextField):
	def from_db_value(self, value, expression, connection):
		if value == '' or value == None:
			return None
		return SumFormField._parse_sum(value)

	def to_python(self, value):
		if isinstance(value, SumValue) or value == None:
			return value
		return SumFormField._parse_sum(value)

	def get_prep_value(self, value):
		if value == '' or value == None:
			return None

		if isinstance(value, str):
			return value

		return value.string

	def value_to_string(self, obj):
		""" Allows serialization of SumFields (dumpdata/loaddata) """
		value = self.value_from_object(obj)
		return self.get_prep_value(value)

	def formfield(self, **kwargs):
		return super().formfield(**{'form_class': SumFormField, **kwargs})


class BarTabUser(models.Model):
	ACTIVE_TIME_LIMIT = datetime.timedelta(weeks=4)
	CREDIT_HOLD_LIMIT = -100

	name = models.CharField(max_length=140)
	email = models.EmailField(blank=True, null=True)
	hidden_from_tab = models.BooleanField(default=False)

	class Meta:
		ordering = ('name',)

	@property
	def balance(self):
		return self.entries.aggregate(balance=Coalesce(Sum(F('added') - F('used')), Value(0)))['balance']

	@property
	def balance_str(self):
		return str(self.balance).replace('.', ',')

	@property
	def has_credit_hold(self):
		return self.balance <= self.CREDIT_HOLD_LIMIT

	@property
	def is_active(self):
		last_entry = self.entries.last()
		if not last_entry:
			return False

		return timezone.now() - last_entry.snapshot.timestamp < self.ACTIVE_TIME_LIMIT

	def __str__(self):
		return self.name


class BarTabSnapshot(models.Model):
	timestamp = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('-timestamp',)

	def __str__(self):
		return f'{self.timestamp.date()}: {self.entries.count()} entries'


class BarTabEntry(models.Model):
	added = models.DecimalField(max_digits=9 + 2, decimal_places=2)
	used = models.DecimalField(max_digits=9 + 2, decimal_places=2)
	raw_added = SumField(blank=True)
	raw_used = SumField(blank=True)
	user = models.ForeignKey(BarTabUser, on_delete=models.CASCADE, related_name='entries')
	snapshot = models.ForeignKey(BarTabSnapshot, on_delete=models.CASCADE, related_name='entries')

	class Meta:
		unique_together = ('user', 'snapshot')
		ordering = ('snapshot__timestamp',)

	def __str__(self):
		return f'{self.user} - {self.snapshot.timestamp.date()}'

	def clean(self):
		if self.raw_added:
			self.added = self.raw_added.value

		if self.raw_used:
			self.used = self.raw_used.value