from django.test import TestCase, SimpleTestCase, Client
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.utils import timezone
from datetime import datetime
from django.http import *
from .models import *
from .views import *
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse, resolve

class TestUrls(SimpleTestCase):

    def test_create_user(self):
        url = reverse('registration')
        self.assertEquals(resolve(url).func, create_user)
		
    def test_create_user2(self):
        url = reverse('create_user')
        self.assertEquals(resolve(url).func, create_user)

    def test_login_user(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, login_user)

    def test_login_user2(self):
        url = reverse('login_user')
        self.assertEquals(resolve(url).func, login_user)		
		
    def test_sammtuci(self):
        url = reverse('sammtuci')
        self.assertEquals(resolve(url).func, sammtuci)
	
    def test_create_branch(self):
        url = reverse('create_branch')
        self.assertEquals(resolve(url).func, create_branch)
		
    def test_read_branch(self):
        url = reverse('read_branch')
        self.assertEquals(resolve(url).func, read_branch)
		
    def test_update_branch(self):
        url = reverse('update_branch')
        self.assertEquals(resolve(url).func, update_branch)
		
    def test_delete_branch(self):
        url = reverse('delete_branch')
        self.assertEquals(resolve(url).func, delete_branch)
		
    def test_create_faculty(self):
        url = reverse('create_faculty')
        self.assertEquals(resolve(url).func, create_faculty)
		
    def test_read_faculty(self):
        url = reverse('read_faculty')
        self.assertEquals(resolve(url).func, read_faculty)
		
    def test_update_faculty(self):
        url = reverse('update_faculty')
        self.assertEquals(resolve(url).func, update_faculty)
		
    def test_delete_faculty(self):
        url = reverse('delete_faculty')
        self.assertEquals(resolve(url).func, delete_faculty)
		
    def test_create_department(self):
        url = reverse('create_department')
        self.assertEquals(resolve(url).func, create_department)
		
    def test_read_department(self):
        url = reverse('read_department')
        self.assertEquals(resolve(url).func, read_department)
		
    def test_update_department(self):
        url = reverse('update_department')
        self.assertEquals(resolve(url).func, update_department)
		
    def test_delete_department(self):
        url = reverse('delete_department')
        self.assertEquals(resolve(url).func, delete_department)
		
    def test_create_usertype(self):
        url = reverse('create_usertype')
        self.assertEquals(resolve(url).func, create_usertype)
		
    def test_read_usertype(self):
        url = reverse('read_usertype')
        self.assertEquals(resolve(url).func, read_usertype)
		
    def test_update_usertype(self):
        url = reverse('update_usertype')
        self.assertEquals(resolve(url).func, update_usertype)
		
    def test_delete_usertype(self):
        url = reverse('delete_usertype')
        self.assertEquals(resolve(url).func, delete_usertype)
		
    def test_create_deaneryuser(self):
        url = reverse('create_deaneryuser')
        self.assertEquals(resolve(url).func, create_deaneryuser)
		
    def test_read_deaneryuser(self):
        url = reverse('read_deaneryuser')
        self.assertEquals(resolve(url).func, read_deaneryuser)
		
    def test_update_deaneryuser(self):
        url = reverse('update_deaneryuser')
        self.assertEquals(resolve(url).func, update_deaneryuser)
		
    def test_delete_deaneryuser(self):
        url = reverse('delete_deaneryuser')
        self.assertEquals(resolve(url).func, delete_deaneryuser)
		
    def test_create_mark(self):
        url = reverse('create_mark')
        self.assertEquals(resolve(url).func, create_mark)
		
    def test_read_mark(self):
        url = reverse('read_mark')
        self.assertEquals(resolve(url).func, read_mark)
		
    def test_update_mark(self):
        url = reverse('update_mark')
        self.assertEquals(resolve(url).func, update_mark)
		
    def test_delete_mark(self):
        url = reverse('delete_mark')
        self.assertEquals(resolve(url).func, delete_mark)
		
    def test_create_year(self):
        url = reverse('create_year')
        self.assertEquals(resolve(url).func, create_year)
		
    def test_read_year(self):
        url = reverse('read_year')
        self.assertEquals(resolve(url).func, read_year)
		
    def test_update_year(self):
        url = reverse('update_year')
        self.assertEquals(resolve(url).func, update_year)
		
    def test_delete_year(self):
        url = reverse('delete_year')
        self.assertEquals(resolve(url).func, delete_year)
		
    def test_create_presenttype(self):
        url = reverse('create_presenttype')
        self.assertEquals(resolve(url).func, create_presenttype)
		
    def test_read_presenttype(self):
        url = reverse('read_presenttype')
        self.assertEquals(resolve(url).func, read_presenttype)
		
    def test_update_presenttype(self):
        url = reverse('update_presenttype')
        self.assertEquals(resolve(url).func, update_presenttype)
		
    def test_delete_presenttype(self):
        url = reverse('delete_presenttype')
        self.assertEquals(resolve(url).func, delete_presenttype)
		
    def test_create_group(self):
        url = reverse('create_group')
        self.assertEquals(resolve(url).func, create_group)
		
    def test_read_group(self):
        url = reverse('read_group')
        self.assertEquals(resolve(url).func, read_group)
		
    def test_update_group(self):
        url = reverse('update_group')
        self.assertEquals(resolve(url).func, update_group)
		
    def test_delete_group(self):
        url = reverse('delete_group')
        self.assertEquals(resolve(url).func, delete_group)
		
    def test_create_teacher(self):
        url = reverse('create_teacher')
        self.assertEquals(resolve(url).func, create_teacher)
		
    def test_read_teacher(self):
        url = reverse('read_teacher')
        self.assertEquals(resolve(url).func, read_teacher)
		
    def test_update_teacher(self):
        url = reverse('update_teacher')
        self.assertEquals(resolve(url).func, update_teacher)
		
    def test_delete_teacher(self):
        url = reverse('delete_teacher')
        self.assertEquals(resolve(url).func, delete_teacher)
		
    def test_create_student(self):
        url = reverse('create_student')
        self.assertEquals(resolve(url).func, create_student)
		
    def test_read_student(self):
        url = reverse('read_student')
        self.assertEquals(resolve(url).func, read_student)
		
    def test_update_student(self):
        url = reverse('update_student')
        self.assertEquals(resolve(url).func, update_student)
		
    def test_delete_student(self):
        url = reverse('delete_student')
        self.assertEquals(resolve(url).func, delete_student)
		
    def test_create_subject(self):
        url = reverse('create_subject')
        self.assertEquals(resolve(url).func, create_subject)
		
    def test_read_subject(self):
        url = reverse('read_subject')
        self.assertEquals(resolve(url).func, read_subject)
		
    def test_update_subject(self):
        url = reverse('update_subject')
        self.assertEquals(resolve(url).func, update_subject)
		
    def test_delete_subject(self):
        url = reverse('delete_subject')
        self.assertEquals(resolve(url).func, delete_subject)
		
    def test_create_subjectduringyear(self):
        url = reverse('create_subjectduringyear')
        self.assertEquals(resolve(url).func, create_subjectduringyear)
		
    def test_read_subjectduringyear(self):
        url = reverse('read_subjectduringyear')
        self.assertEquals(resolve(url).func, read_subjectduringyear)
		
    def test_update_subjectduringyear(self):
        url = reverse('update_subjectduringyear')
        self.assertEquals(resolve(url).func, update_subjectduringyear)
		
    def test_delete_subjectduringyear(self):
        url = reverse('delete_subjectduringyear')
        self.assertEquals(resolve(url).func, delete_subjectduringyear)
		
    def test_create_task(self):
        url = reverse('create_task')
        self.assertEquals(resolve(url).func, create_task)
		
    def test_read_task(self):
        url = reverse('read_task')
        self.assertEquals(resolve(url).func, read_task)
		
    def test_update_task(self):
        url = reverse('update_task')
        self.assertEquals(resolve(url).func, update_task)
		
    def test_delete_task(self):
        url = reverse('delete_task')
        self.assertEquals(resolve(url).func, delete_task)
		
    def test_create_present(self):
        url = reverse('create_present')
        self.assertEquals(resolve(url).func, create_present)
		
    def test_read_present(self):
        url = reverse('read_present')
        self.assertEquals(resolve(url).func, read_present)
		
    def test_update_present(self):
        url = reverse('update_present')
        self.assertEquals(resolve(url).func, update_present)
		
    def test_delete_present(self):
        url = reverse('delete_present')
        self.assertEquals(resolve(url).func, delete_present)
		
    def test_create_taskgive(self):
        url = reverse('create_taskgive')
        self.assertEquals(resolve(url).func, create_taskgive)
		
    def test_read_taskgive(self):
        url = reverse('read_taskgive')
        self.assertEquals(resolve(url).func, read_taskgive)
		
    def test_teacher_read_student(self):
        url = reverse('teacher_read_student')
        self.assertEquals(resolve(url).func, teacher_read_student)
		
    def test_teacher_read_subjectduringyear(self):
        url = reverse('teacher_read_subjectduringyear')
        self.assertEquals(resolve(url).func, teacher_read_subjectduringyear)
		
    def test_teacher_read_taskgive(self):
        url = reverse('teacher_read_taskgive')
        self.assertEquals(resolve(url).func, teacher_read_taskgive)
		
    def test_teacher_update_taskgive(self):
        url = reverse('teacher_update_taskgive')
        self.assertEquals(resolve(url).func, teacher_update_taskgive)
		
    def test_student_read_task(self):
        url = reverse('student_read_task')
        self.assertEquals(resolve(url).func, student_read_task)

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
		
    def test_create_user_GET(self):
        response=self.client.get(reverse('registration'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_user.html')
		
    def test_create_user_GET2(self):
        response=self.client.get(reverse('create_user'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_user.html')
		
    def test_login_user_GET(self):
        response=self.client.get(reverse('login_user'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
		
    def test_login_user_GET2(self):
        response=self.client.get(reverse('login'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
		
    def test_login_user_GET3(self):
        response=self.client.get(reverse('login_user'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'login_user.html')
		
    def test_sammtuci_GET(self):
        response=self.client.get(reverse('sammtuci'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'sammtuci.html')
		
    def test_create_branch_GET(self):
        response=self.client.get(reverse('create_branch'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_branch.html')
		
    def test_read_branch_GET(self):
        response=self.client.get(reverse('read_branch'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'read_branch.html')
		
    def test_update_branch_GET(self):
        response=self.client.get(reverse('update_branch'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'update_branch.html')
		
    def test_delete_branch_GET(self):
        response=self.client.get(reverse('delete_branch'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete_branch.html')
		
    def test_create_faculty_GET(self):
        response=self.client.get(reverse('create_faculty'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_faculty.html')
		
    def test_read_faculty_GET(self):
        response=self.client.get(reverse('read_faculty'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'read_faculty.html')
		
    def test_update_faculty_GET(self):
        response=self.client.get(reverse('update_faculty'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'update_faculty.html')
		
    def test_delete_faculty_GET(self):
        response=self.client.get(reverse('delete_faculty'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete_faculty.html')
		
    def test_create_department_GET(self):
        response=self.client.get(reverse('create_department'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_department.html')
		
    def test_read_department_GET(self):
        response=self.client.get(reverse('read_department'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'read_department.html')
		
    def test_update_department_GET(self):
        response=self.client.get(reverse('update_department'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'update_department.html')
		
    def test_delete_department_GET(self):
        response=self.client.get(reverse('delete_department'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete_department.html')
		
    def test_create_usertype_GET(self):
        response=self.client.get(reverse('create_branch'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_branch.html')
		
    def test_read_usertype_GET(self):
        response=self.client.get(reverse('read_branch'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'read_branch.html')
		
    def test_update_usertype_GET(self):
        response=self.client.get(reverse('update_branch'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'update_branch.html')
		
    def test_delete_usertype_GET(self):
        response=self.client.get(reverse('delete_branch'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete_branch.html')
		
    def test_create_deaneryuser_GET(self):
        response=self.client.get(reverse('create_branch'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_branch.html')
		
    def test_read_deaneryuser_GET(self):
        response=self.client.get(reverse('read_branch'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'read_branch.html')
		
    def test_update_deaneryuser_GET(self):
        response=self.client.get(reverse('update_branch'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'update_branch.html')
		
    def test_delete_deaneryuser_GET(self):
        response=self.client.get(reverse('delete_branch'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete_branch.html')
		
    def test_create_mark_GET(self):
        response=self.client.get(reverse('create_branch'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_branch.html')
		
    def test_read_mark_GET(self):
        response=self.client.get(reverse('read_branch'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'read_branch.html')
		
    def test_update_mark_GET(self):
        response=self.client.get(reverse('update_branch'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'update_branch.html')
		
    def test_delete_mark_GET(self):
        response=self.client.get(reverse('delete_branch'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete_branch.html')
		
    def test_create_year_GET(self):
        response=self.client.get(reverse('create_branch'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_branch.html')
		
    def test_read_year_GET(self):
        response=self.client.get(reverse('read_branch'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'read_branch.html')
		
    def test_update_year_GET(self):
        response=self.client.get(reverse('update_branch'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'update_branch.html')
		
    def test_delete_year_GET(self):
        response=self.client.get(reverse('delete_branch'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete_branch.html')
		
    def test_create_presenttype_GET(self):
        response=self.client.get(reverse('create_presenttype'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_presenttype.html')
		
    def test_read_presenttype_GET(self):
        response=self.client.get(reverse('read_presenttype'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'read_presenttype.html')
		
    def test_update_presenttype_GET(self):
        client=Client()
        response=self.client.get(reverse('update_presenttype'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'update_presenttype.html')
		
    def test_delete_presenttype_GET(self):
        client=Client()
        response=self.client.get(reverse('delete_presenttype'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete_presenttype.html')
		
    def test_create_group_GET(self):
        response=self.client.get(reverse('create_group'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_group.html')
		
    def test_read_group_GET(self):
        response=self.client.get(reverse('read_group'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'read_group.html')
		
    def test_update_group_GET(self):
        response=self.client.get(reverse('update_group'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'update_group.html')
		
    def test_delete_group_GET(self):
        response=self.client.get(reverse('delete_group'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete_group.html')
		
    def test_create_teacher_GET(self):
        response=self.client.get(reverse('create_teacher'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_teacher.html')
		
    def test_read_teacher_GET(self):
        response=self.client.get(reverse('read_teacher'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'read_teacher.html')
		
    def test_update_teacher_GET(self):
        response=self.client.get(reverse('update_teacher'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'update_teacher.html')
		
    def test_delete_teacher_GET(self):
        response=self.client.get(reverse('delete_teacher'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete_teacher.html')
		
    def test_create_student_GET(self):
        response=self.client.get(reverse('create_student'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_student.html')
		
    def test_read_student_GET(self):
        response=self.client.get(reverse('read_student'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'read_student.html')
		
    def test_update_student_GET(self):
        response=self.client.get(reverse('update_student'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'update_student.html')
		
    def test_delete_student_GET(self):
        response=self.client.get(reverse('delete_student'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete_student.html')
		
    def test_create_subject_GET(self):
        response=self.client.get(reverse('create_subject'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_subject.html')
		
    def test_read_subject_GET(self):
        response=self.client.get(reverse('read_subject'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'read_subject.html')
		
    def test_update_subject_GET(self):
        response=self.client.get(reverse('update_subject'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'update_subject.html')
		
    def test_delete_subject_GET(self):
        response=self.client.get(reverse('delete_subject'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete_subject.html')
		
    def test_create_subjectduringyear_GET(self):
        response=self.client.get(reverse('create_subjectduringyear'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_subjectduringyear.html')
		
    def test_read_subjectduringyear_GET(self):
        response=self.client.get(reverse('read_subjectduringyear'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'read_subjectduringyear.html')
		
    def test_update_subjectduringyear_GET(self):
        response=self.client.get(reverse('update_subjectduringyear'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'update_subjectduringyear.html')
		
    def test_delete_subjectduringyear_GET(self):
        response=self.client.get(reverse('delete_subjectduringyear'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete_subjectduringyear.html')
		
    def test_create_task_GET(self):
        response=self.client.get(reverse('create_task'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_task.html')
		
    def test_read_task_GET(self):
        response=self.client.get(reverse('read_task'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'read_task.html')
		
    def test_update_task_GET(self):
        response=self.client.get(reverse('update_task'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'update_task.html')
		
    def test_delete_task_GET(self):
        response=self.client.get(reverse('delete_task'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete_task.html')
		
    def test_create_present_GET(self):
        response=self.client.get(reverse('create_present'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_present.html')
		
    def test_read_present_GET(self):
        response=self.client.get(reverse('read_present'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'read_present.html')
		
    def test_update_present_GET(self):
        response=self.client.get(reverse('update_present'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'update_present.html')
		
    def test_delete_present_GET(self):
        response=self.client.get(reverse('delete_present'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete_present.html')
		
    def test_create_taskgive_GET(self):
        response=self.client.get(reverse('create_taskgive'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_taskgive.html')
		
    def test_read_taskgive_GET(self):
        response=self.client.get(reverse('read_taskgive'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'read_taskgive.html')
		
    def test_teacher_read_student_GET(self):
        response=self.client.get(reverse('teacher_read_student'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'teacher_read_student.html')
		
    def test_teacher_read_subjectduringyear_GET(self):
        response=self.client.get(reverse('teacher_read_subjectduringyear'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'teacher_read_subjectduringyear.html')
		
    def test_teacher_read_taskgive_GET(self):
        response=self.client.get(reverse('teacher_read_taskgive'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'teacher_read_taskgive.html')
		
    def test_teacher_update_taskgive_GET(self):
        response=self.client.get(reverse('teacher_update_taskgive'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'teacher_update_taskgive.html')
		
    def test_student_read_task_GET(self):
        response=self.client.get(reverse('student_read_task'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'student_read_task.html')

class TestRegLogin(TestCase):

    def setUp(self):
        self.usertype=User_Type.objects.create(User_Type=4, User_Type_Name='Преподаватель в отставке')
        self.department=Department.objects.create(Department_ID=1, Department_Name='')
        self.teacher=UserU.objects.create(Surname="dddd", Name="wfwfwf", Fathername="ffffff", username="kirill", email="", 
        password="adwwf", User_Type=self.usertype, StartWork_Date="2010-10-10", Department_ID=self.department)
		
    def test_create_teacher_correctemail(self):
        self.assertNotEquals(self.teacher.email, '')
		
    def test_create_teacher_correctusertype(self):
        correctusertype=(1,2,3)
        self.assertIn(self.usertype.User_Type, correctusertype)
    
    def test_login(self):
        user=UserU(username=self.teacher.username)
        self.assertIsNotNone(user)

    def test_login_password(self):
        self.assertNotEquals(self.teacher.password, '')
		
    def test_login_password_equality(self):
        loginuser=UserU.objects.create(password="ddd")
        self.assertEquals(loginuser.password, self.teacher.password)
		
class TestTaskCreate(TestCase):

    def setUp(self):
        self.year=Year.objects.create(Year_ID=1, Year_Name="wowo")
        self.branch=Branch.objects.create(Branch_ID=1, Branch_Name="wofmwof")
        self.usertype=User_Type.objects.create(User_Type=2, User_Type_Name='Преподаватель в отставке')
        self.department=Department.objects.create(Department_ID=1, Department_Name='1')
        self.subject=Subject.objects.create(Subject_ID=1, Department_ID=self.department, Subject_Name="dddd")
        self.teacher=UserU.objects.create(Surname="dddd", Name="wfwfwf", Fathername="ffffff", username="kirill", email="", 
        password="adwwf", User_Type=self.usertype, StartWork_Date="2010-10-10", Department_ID=self.department)
        self.group=Group.objects.create(Group_ID="111", Year_ID=self.year, Branch_ID=self.branch)
        self.subject2=SubjectDuringYear.objects.create(Subject2_ID=1, Branch_ID=self.branch, Semester=1)
        self.task=Task.objects.create(Task_ID=1, Teacher_ID=self.teacher, Subject2_ID=self.subject2, Group_ID=self.group, Text="", Deadline="2020-10-10 10:10:10",
		Date_Give="2010-10-10")
		
    def test_create_task_correctfile(self):
        self.assertNotEquals(self.task.Text, '')
		
    def test_create_task_correctsubject(self):		
        self.assertNotEquals(self.task.Subject2_ID, '')
		
    def test_create_task_correctteacher(self):	
        self.assertNotEquals(self.task.Teacher_ID, '')
		
    def test_create_task_correcttaskid(self):	
        self.assertNotEquals(self.task.Task_ID, '')
		
    def test_create_task_correctgroup(self):	
        self.assertNotEquals(self.task.Group_ID, '')
		
    def test_create_task_correctdeadline(self):	
        self.assertNotEquals(self.task.Deadline, '')
		
    def test_create_task_correctdategive(self):	
        self.assertNotEquals(self.task.Date_Give, '')
		

		
class TestPresentCreate(TestCase):

    def setUp(self):
        self.year=Year.objects.create(Year_ID=1, Year_Name="wowo")
        self.branch=Branch.objects.create(Branch_ID=1, Branch_Name="wofmwof")
        self.usertype=User_Type.objects.create(User_Type=2, User_Type_Name='Преподаватель в отставке')
        self.usertype2=User_Type.objects.create(User_Type=3, User_Type_Name='Студент-заочник')
        self.department=Department.objects.create(Department_ID=1, Department_Name='1')
        self.group=Group.objects.create(Group_ID="111", Year_ID=self.year, Branch_ID=self.branch)
        self.subject=Subject.objects.create(Subject_ID=1, Department_ID=self.department, Subject_Name="dddd")
        self.presenttype=Present_Type.objects.create(Present_Type_ID=1, Present_Type_Name="wfwf")
        self.teacher=UserU.objects.create(Surname="dddd", Name="wfwfwf", Fathername="ffffff", username="kirill", email="", 
        password="adwwf", User_Type=self.usertype, StartWork_Date="2010-10-10", Department_ID=self.department)
        self.student=UserU.objects.create(Surname="уууу", Name="прпрпр", Fathername="утуитшущтиу", username="polk", email="polk@mtuci.ru", 
        password="eigneing", User_Type=self.usertype2, Start_Date="2010-12-10", Group_ID=self.group)
        self.present=Present.objects.create(Present_ID=1, Student_ID=self.student, Present_Type_ID=self.presenttype, Quality=-123)
		
    def test_create_present_correctpresentid(self):	
        self.assertNotEquals(self.present.Present_ID, '')
		
    def test_create_present_correctstudentid(self):	
        self.assertNotEquals(self.present.Student_ID, '')
		
    def test_create_present_correctpresenttypeid(self):	
        self.assertNotEquals(self.present.Present_Type_ID, '')
		
    def test_create_present_correctquality(self):	
        self.assertNotEquals(self.present.Quality, '')
		
    def test_create_present_correctquality2(self):	
        self.assertGreater(self.present.Quality, 0)
						
# Create your tests here.
