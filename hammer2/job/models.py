from django.db import models

# Create your models here.
import datetime
from django.utils import timezone

class Script(models.Model):
	script_id = models.AutoField(primary_key=True, editable=False)
	script_name = models.CharField(max_length=128)
	# script_number = models.IntegerField()
	# version_number = models.IntegerField()
	# script_description = models.CharField(max_length = 1000)
	created_date = models.DateTimeField(editable=False)
	modified_date = models.DateTimeField()

	def save(self, *args, **kwargs):
		''' On save, update timestamps '''
		if not self.script_id:
			self.created_date = timezone.now()
		self.modified_date = timezone.now()
		return super(Script, self).save(*args, **kwargs)

	def __str__(self):
		return self.script_name 

# Create your models here.
