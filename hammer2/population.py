import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
'hammer2.settings')

import django
django.setup()
from job.models import Script




# class Script(models.Model):
# 	script_id = models.AutoField(primary_key=True)
# 	script_name = models.CharField(max_length=128)
# 	script_number = models.IntegerField()
# 	version_number = models.IntegerField()

def populate():
# First, we will create lists of dictionaries containing the pages
# we want to add into each category.
# Then we will create a dictionary of dictionaries for our categories.
# This might seem a little bit confusing, but it allows us to iterate
# through each data structure, and add the data to our models.

	scripts = [
	{"script_nm":"test script 1"},
	{"script_nm":"test script 2"},
	{"script_nm":"test script 3"},
	{"script_nm":"test script 4"},
	{"script_nm":"test script 5"},
	{"script_nm":"test script 6"},
	{"script_nm":"test script 1"},
	{"script_nm":"test script 2"},
	{"script_nm":"test script 1"},
	]
	     
 
	for s in scripts:
		add_script(s["script_nm"])
		# print (s["script_nm"])

	# Print out the categories we have added.
	for s in Script.objects.all():
		print( str(s))

def add_script(script_nm):
	s = Script(script_name=script_nm) 
	print (s)
	s.save() 
 
# Start execution here!
if __name__ == '__main__':
	print("Starting job population script...")
	populate()