from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.utils import timezone
from datetime import datetime
from .models import Task, User_Type
class SigninTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test', password='12test12', 
		email='test@example.com')
        self.user.save()
    def tearDown(self):
        self.user.delete()
    def test_correct(self):
        user = authenticate(username='test', password='12test12')
        self.assertTrue((user is not None) and user.is_authenticated)
    def test_wrong_username(self):
        user = authenticate(username='wrong', password='12test12')
        self.assertFalse(user is not None and user.is_authenticated)
    def test_wrong_password(self):
        user = authenticate(username='test', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)
    def test_user_usertype(self):
        self.assertNotEqual(self.User_Type, 4)
		
class TestTask(TestCase):
    def setUp(self):
        self.task = Task().objects.create(Task_ID=1, Subject2_ID=3, 
		Deadline='2010-10-10 10:10:10')
        self.task.save()
    def tearDown(self):
        self.task.delete()
    def test_taskcorrect(self):
        task = Task().objects.create(Task_ID=1, Subject2_ID=3, Deadline='2020-12-10 10:10:10')
        task.save()
        self.assertTrue((task is not None))
    def test_wrong_deadlline(self):
        task = Task().objects.create(Task_ID=1, Subject2_ID=3, Deadline='2010-12-10 10:10:10')
        task.save()
        self.assertFalse(task is not None)
# Create your tests here.
