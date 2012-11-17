from django.db import models
from events.models import *

def get_event_count(binary):
	if(binary==0):
		return Event.objects.count()
	elif(binary==1):
		return Attend.objects.count()
