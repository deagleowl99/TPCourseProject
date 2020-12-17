from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.conf import settings

class Mark(models.Model):
	Mark=models.IntegerField(primary_key=True)
	Mark_Text=models.CharField(max_length=1, unique=True)
	class Meta:
		db_table = "table_marks"
	def __str__(self):
		return self.Mark_Text
	
class User_Type(models.Model):
	User_Type=models.IntegerField(primary_key=True)
	User_Type_Name=models.CharField(max_length=30, unique=True)
	class Meta:
		db_table = "table_usertypes"
	def __str__(self):
		return self.User_Type_Name
		
class Year(models.Model):
    Year_ID=models.IntegerField(primary_key=True)
    Year_Name=models.CharField(max_length=30, unique=True)
    class Meta:
        db_table = "table_years"
    def __str__(self):
        return self.Year_Name

class Faculty(models.Model):
	Faculty_ID=models.IntegerField(primary_key=True)
	Faculty_Name=models.CharField(max_length=100, unique=True)
	class Meta:
		db_table = "table_faculties"
	def __str__(self):
		return self.Faculty_Name

class Department(models.Model):
	Department_ID=models.IntegerField(primary_key=True)
	Department_Name=models.CharField(max_length=100, unique=True)
	Faculty_ID=models.ForeignKey(Faculty, null=True, on_delete=models.CASCADE)
	class Meta:
		db_table = "table_departments"
	def __str__(self):
		return self.Department_Name
	
class Branch(models.Model):
	Branch_ID=models.CharField(max_length=10, primary_key=True)
	Branch_Name=models.CharField(max_length=100, unique=True)
	class Meta:
		db_table = "table_branches"
	def __str__(self):
		return self.Branch_Name
		
class Group(models.Model):
	Group_ID=models.CharField(max_length=20, primary_key=True)
	Year_ID=models.ForeignKey(Year, null=True, on_delete=models.CASCADE)
	Branch_ID=models.ForeignKey(Branch, null=True, on_delete=models.CASCADE)
	class Meta:
		db_table = "table_groups"
	def __str__(self):
		return self.Group_ID	
	
class UserU(AbstractUser):
	Surname=models.CharField(max_length=50)
	Name=models.CharField(max_length=50)
	Fathername=models.CharField(max_length=50)
	User_Type=models.ForeignKey(User_Type, default=None, null=True, on_delete=models.CASCADE)
	Start_Date=models.DateField(null=True)
	StartWork_Date=models.DateField(null=True)
	Group_ID=models.ForeignKey(Group, null=True, on_delete=models.CASCADE)
	Department_ID=models.ForeignKey(Department, null=True, on_delete=models.CASCADE)
	Faculty_ID=models.ForeignKey(Faculty, null=True, on_delete=models.CASCADE)
	Points=models.IntegerField(null=True)
	class Meta:
		db_table = "table_users"
	def __str__(self):
		return self.Surname + " " + self.Name + " " + self.Fathername
		
class Subject(models.Model):
	Subject_ID=models.IntegerField(primary_key=True)
	Subject_Name=models.CharField(max_length=50, unique=True)
	Department_ID=models.ForeignKey(Department, null=True, on_delete=models.CASCADE)
	class Meta:
		db_table = "table_subjects"
	def __str__(self):
		return self.Subject_Name
	
class SubjectDuringYear(models.Model):
	Subject2_ID=models.IntegerField(primary_key=True)
	Branch_ID=models.ForeignKey(Branch, null=True, on_delete=models.CASCADE)
	Subject_ID=models.ForeignKey(Subject, null=True, on_delete=models.CASCADE)
	Teacher_ID=models.ForeignKey(UserU, null=True, on_delete=models.CASCADE)
	Semester=models.IntegerField()
	class Meta:
		db_table = "table_subjectsduringyear"
	def __str__(self):
		return self.Subject2_ID

class Task(models.Model):
	Task_ID=models.CharField(max_length=100, primary_key=True)
	Teacher_ID=models.ForeignKey(UserU, null=True, on_delete=models.CASCADE)
	Group_ID=models.ForeignKey(Group, null=True, on_delete=models.CASCADE)
	Subject2_ID=models.ForeignKey(SubjectDuringYear, null=True, on_delete=models.CASCADE)
	Text=models.FileField(upload_to='', blank=True)
	Date_Give=models.DateTimeField(default=timezone.now)
	Deadline=models.DateTimeField()
	class Meta:
		db_table = "table_tasks"
	def __str__(self):
		return self.Task_ID

class TaskGive(models.Model):
    GiveTask_ID=models.IntegerField(primary_key=True)
    Task_ID=models.ForeignKey(Task, null=True, on_delete=models.CASCADE)
    Student_ID=models.ForeignKey(UserU, null=True, on_delete=models.CASCADE)
    TextGive=models.FileField(null=True)
    Date_Complete=models.DateTimeField(default=timezone.now)
    Mark_ID=models.ForeignKey(Mark, null=True, on_delete=models.CASCADE)
    class Meta:
        db_table = "table_taskgives"
    def __str__(self):
        return self.GiveTask_ID
		
class Present_Type(models.Model):
    Present_Type_ID=models.IntegerField(primary_key=True)
    Present_Type_Name=models.CharField(max_length=20, unique=True)
    class Meta:
        db_table = "table_presenttypes"
    def __str__(self):
        return self.Present_Type_Name	
		
class Present(models.Model):
    Present_ID=models.IntegerField(primary_key=True)
    Student_ID=models.ForeignKey(UserU, null=True, on_delete=models.CASCADE)
    Present_Type_ID=models.ForeignKey(Present_Type, null=True, on_delete=models.CASCADE)
    Quality=models.IntegerField()
    class Meta:
        db_table = "table_presents"
    def __str__(self):
        return self.Quality
	
# Create your models here.