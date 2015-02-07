from django.db import models

class ZeltlagerDurchgang(models.Model):
	number = models.IntegerField()
	place = models.CharField(max_length=200)
	start = models.DateTimeField()
	end = models.DateTimeField()
	lagerleiter = models.CharField(max_length=200)

class Participant(models.Model):
	name = models.CharField(max_length=200)
	firstname = models.CharField(max_length=200)
	zeltlager_durchgang = models.ForeignKey(ZeltlagerDurchgang)