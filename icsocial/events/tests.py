from django.test import TestCase
from django.utils import unittest
from events.models import *
from events.methods import *


class SimpleTest(unittest.TestCase):
    def test_is_added(self):
    	Event.objects.create(title='Group Meeting', location='huxley', date='2012-03-03', time='10:30', description='Work on our project.')
    	self.assertEqual(get_event_count(0), 1)

    def test_get_attend(self):
    	Attend.objects.create(attendee=1, event_id=2)
    	self.assertEqual(get_event_count(1), 1)

