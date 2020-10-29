from .models import UserU, User_Type, Faculty, Department, Branch, Year, Mark, Group, Subject, SubjectDuringYear
from django.shortcuts import render
from django.http import Http404
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.urls import reverse

def create_user(request):
    usertype=User_Type.objects.all()
    if request.method == "POST":
        form = {
			'surname': request.POST["surname"],
			'name': request.POST["name"],
			'fathername': request.POST["fathername"],
            'login': request.POST["login"],
            'mail': request.POST["mail"],
            'password': request.POST["password"],
			'start_date': request.POST["start_date"],
			'startwork_date': request.POST["startwork_date"],
			'group_id': request.POST["group_id"],
			'department_id': request.POST["department_id"],
			'faculty_id': request.POST["faculty_id"],			
        }
        if form["surname"] and form["name"] and form["fathername"] and form["login"] and form["mail"] and form["password"]:
            try:
                UserU.objects.get(username = form["login"])
                form['errors'] = u"Не уникальное имя пользователя!"
                return render(request, 'create_user.html', {'form': form})
            except UserU.DoesNotExist:
                user=UserU.objects.create_user(form["login"], form["mail"], form["password"])
                user.Surname=form["surname"] 
                user.Name=form["name"] 
                user.Fathername=form["fathername"]           
                user.save()
                return redirect('sammtuci')
        else:
            form['errors'] = u"У вас имеются пустые поля!"
            return render(request, 'create_user.html', {"usertype": usertype, "form": form})
    else:
        return render(request, 'create_user.html', {"usertype": usertype})
		
def login_user(request):
    if request.method == "POST":
        form = {
            'login': request.POST["login"],
            'password': request.POST["password"]
        }
        if form["login"] and form["password"]:
            user = authenticate(username=form["login"], password=form["password"])
            if user == None:
                form['errors'] = u"Неверный логин или пароль"
                return render(request, 'login.html', {'form': form})
            else:
                login(request, user) 
                return redirect('sammtuci')
        else:
            form['errors'] = u"У вас имеются пустые поля!"
            return render(request, 'login.html', {'form': form})
    else:
        return render(request, 'login.html', {})
def logout_user(request):
	logout(request)
	return HttpResponseRedirect(reverse('sammtuci'))
	
def sammtuci(request):
    branch=Branch.objects.all().order_by("Branch_ID")
    return render(request, 'sammtuci.html', {"branch": branch})

def create_branch(request):
    if request.method == "POST":
        form = {
			    'branch_id': request.POST["branch_id"],
                'branch_name': request.POST["branch_name"],			
        }
        if form["branch_id"] and form["branch_name"]:		
            try:
                Branch.objects.get(Branch_ID = form["branch_id"])
                form['errors'] = u"Это направление уже существует! Проверьте поле кода!"
                return render(request, 'create_branch.html', {'form': form})
            except Branch.DoesNotExist:
                try:
                    Branch.objects.get(Branch_Name = form["branch_name"])
                    form['errors'] = u"Это направление уже существует! Проверьте поле названия!"
                    return render(request, 'create_branch.html', {'form': form})
                except Branch.DoesNotExist:
                    branch=Branch.objects.create(Branch_ID=form["branch_id"], Branch_Name=form["branch_name"])
                    return redirect('sammtuci')          
        else:
            form['errors'] = u"У вас имеются пустые поля!"
            return render(request, 'create_branch.html', {"form": form})
    else:
        return render(request, 'create_branch.html', {})

def read_branch(request):
    branch=Branch.objects.all().order_by("Branch_ID")
    return render(request, 'read_branch.html', {"branch": branch})
	
def update_branch(request):
    branch=Branch.objects.all().order_by("Branch_ID")
    if request.method == "POST":
        form = {
			    'branch_name': request.POST["branch_name"],
                'branch_name2': request.POST["branch_name2"],			
        }
        if form["branch_name2"]:
            try:
                Branch.objects.get(Branch_Name = form["branch_name2"])
                form['errors'] = u"Придумайте другое название направления!"
                return render(request, 'update_branch', {"branch": branch})
            except Branch.DoesNotExist:
                if request.POST.get("branch_name"):
                    savebranchname=Branch()
                    savebranchname.Branch_Name=request.POST.get("branch_name")
                branch2=Branch.objects.all().filter(Branch_Name=savebranchname).update(Branch_Name=form["branch_name2"])
                return redirect('sammtuci')          
        else:
            form['errors'] = u"У вас имеются пустые поля!"
            return render(request, 'update_branch.html', {"branch": branch, "form": form})
    else:
        return render(request, 'update_branch.html', {"branch": branch})
		
def delete_branch(request):
    branch=Branch.objects.all().order_by("Branch_ID")
    if request.method == "POST":
        form = {
                'branch_name': request.POST["branch_name"],			
        }
        if request.POST.get("branch_name"):
            savebranchname=Branch()
            savebranchname.Branch_Name=request.POST.get("branch_name")
        branch2=Branch.objects.filter(Branch_Name=savebranchname).delete()
        return redirect('sammtuci')
    else:
        return render(request, 'delete_branch.html', {"branch": branch})
    return render(request, 'delete_branch.html', {"branch": branch})
	
def create_faculty(request):
    if request.method == "POST":
        form = {
			    'faculty_id': request.POST["faculty_id"],
                'faculty_name': request.POST["faculty_name"],			
        }
        if form["faculty_id"] and form["faculty_name"]:		
            try:
                Faculty.objects.get(Faculty_ID = form["faculty_id"])
                form['errors'] = u"Этот факультет уже существует! Проверьте поле номера!"
                return render(request, 'create_faculty.html', {'form': form})
            except Faculty.DoesNotExist:
                try:
                    Faculty.objects.get(Faculty_Name = form["faculty_name"])
                    form['errors'] = u"Этот факультет уже существует! Проверьте поле названия!"
                    return render(request, 'create_faculty.html', {'form': form})
                except Faculty.DoesNotExist:
                    faculty=Faculty.objects.create(Faculty_ID=form["faculty_id"], Faculty_Name=form["faculty_name"])
                    return redirect('sammtuci')          
        else:
            form['errors'] = u"У вас имеются пустые поля!"
            return render(request, 'create_faculty.html', {"form": form})
    else:
        return render(request, 'create_faculty.html', {})

def read_faculty(request):
    faculty=Faculty.objects.all()
    return render(request, 'read_faculty.html', {"faculty": faculty})
	
def update_faculty(request):
    faculty=Faculty.objects.all()
    if request.method == "POST":
        form = {
			    'faculty_name': request.POST["faculty_name"],
                'faculty_name2': request.POST["faculty_name2"],			
        }
        if form["faculty_name2"]:
            try:
                Faculty.objects.get(Faculty_Name = form["faculty_name2"])
                form['errors'] = u"Придумайте другое название факультета!"
                return render(request, 'update_faculty', {"faculty": faculty})
            except Faculty.DoesNotExist:
                if request.POST.get("faculty_name"):
                    savefacultyname=Faculty()
                    savefacultyname.Faculty_Name=request.POST.get("faculty_name")
                faculty2=Faculty.objects.all().filter(Faculty_Name=savefacultyname).update(Faculty_Name=form["faculty_name2"])
                return redirect('sammtuci')          
        else:
            form['errors'] = u"У вас имеются пустые поля!"
            return render(request, 'update_faculty.html', {"faculty": faculty, "form": form})
    else:
        return render(request, 'update_faculty.html', {"faculty": faculty})

def delete_faculty(request):
    faculty=Faculty.objects.all()
    if request.method == "POST":
        form = {
                'faculty_name': request.POST["faculty_name"],			
        }
        if request.POST.get("faculty_name"):
            savefacultyname=Faculty()
            savefacultyname.Faculty_Name=request.POST.get("faculty_name")
        faculty2=Faculty.objects.filter(Faculty_Name=savefacultyname).delete()
        return redirect('sammtuci')
    else:
        return render(request, 'delete_faculty.html', {"faculty": faculty})
    return render(request, 'delete_faculty.html', {"faculty": faculty})
		
def create_department(request):
    faculty=Faculty.objects.all()
    if request.method == "POST":
        form = {
			    'department_id': request.POST["department_id"],
                'department_name': request.POST["department_name"],	
				'faculty_name': request.POST["faculty_name"]
        }
        if form["department_id"] and form["department_name"]:
            try:
                Department.objects.get(Department_ID = form["department_id"])
                form['errors'] = u"Эта кафедра уже существует! Проверьте поле номера!"
                return render(request, 'create_department.html', {"faculty": faculty, 'form': form})
            except Department.DoesNotExist:
                try:
                    Department.objects.get(Department_Name = form["department_name"])
                    form['errors'] = u"Эта кафедра уже существует! Проверьте поле названия!"
                    return render(request, 'create_department.html', {"faculty": faculty, 'form': form})
                except Department.DoesNotExist:
                    department=Department.objects.create(Department_ID=form["department_id"], Department_Name=form["department_name"])
                    if request.POST.get("faculty_name"):
                        savefacultyname=Faculty()
                        savefacultyname.Faculty_Name=request.POST.get("faculty_name")
                    faculty_id=Faculty.objects.get(Faculty_Name=savefacultyname)
                    department.Faculty_ID=faculty_id
                    department.save()
                    return redirect('sammtuci')           
        else:
            form['errors'] = u"У вас имеются пустые поля!"
            return render(request, 'create_department.html', {"faculty": faculty, "form": form})
    else:
        return render(request, 'create_department.html', {"faculty": faculty})
		
def read_department(request):
    department=Department.objects.all()
    return render(request, 'read_department.html', {"department": department})

def update_department(request):
    faculty=Faculty.objects.all()
    department=Department.objects.all()
    if request.method == "POST":
        form = {
			    'department_name': request.POST["department_name"],
                'department_name2': request.POST["department_name2"],
                'faculty_name': request.POST["faculty_name"],				
        }
        if form["department_name2"]:
            try:
                Department.objects.get(Department_Name = form["department_name2"])
                form['errors'] = u"Придумайте другое название кафедры!"
                return render(request, 'update_department', {"faculty": faculty, "department": department})
            except Department.DoesNotExist:
                if request.POST.get("department_name"):
                    savedepartmentname=Department()
                    savedepartmentname.Department_Name=request.POST.get("department_name")
                if request.POST.get("faculty_name"):
                    savefacultyname=Faculty()
                    savefacultyname.Faculty_Name=request.POST.get("faculty_name")
                faculty_id=Faculty.objects.get(Faculty_Name=savefacultyname)
                department2=Department.objects.all().filter(Department_Name=savedepartmentname).update(Department_Name=form["department_name2"], Faculty_ID=faculty_id.Faculty_ID)
                return redirect('sammtuci')          
        else:
            form['errors'] = u"У вас имеются пустые поля!"
            return render(request, 'update_department.html', {"faculty": faculty, "form": form})
    else:
        return render(request, 'update_department.html', {"faculty": faculty, "department": department})	

def delete_department(request):
    department=Department.objects.all()
    if request.method == "POST":
        form = {
                'department_name': request.POST["department_name"],			
        }
        if request.POST.get("department_name"):
            savedepartmentname=Department()
            savedepartmentname.Department_Name=request.POST.get("department_name")
        department2=Department.objects.filter(Department_Name=savedepartmentname).delete()
        return redirect('sammtuci')
    else:
        return render(request, 'delete_department.html', {"department": department})
    return render(request, 'delete_department.html', {"department": department})
	
def create_usertype(request):
    if request.method == "POST":
        form = {
			    'usertype_id': request.POST["usertype_id"],
                'usertype_name': request.POST["usertype_name"],			
        }
        if form["usertype_id"] and form["usertype_name"]:		
            try:
                User_Type.objects.get(User_Type = form["usertype_id"])
                form['errors'] = u"Этот тип пользователя уже существует! Проверьте поле номера!"
                return render(request, 'create_usertype.html', {'form': form})
            except User_Type.DoesNotExist:
                try:
                    User_Type.objects.get(User_Type_Name = form["usertype_name"])
                    form['errors'] = u"Этоn тип пользователя уже существует! Проверьте поле названия!"
                    return render(request, 'create_usertype.html', {'form': form})
                except User_Type.DoesNotExist:
                    usertype=User_Type.objects.create(User_Type=form["usertype_id"], User_Type_Name=form["usertype_name"])
                    return redirect('sammtuci')          
        else:
            form['errors'] = u"У вас имеются пустые поля!"
            return render(request, 'create_usertype.html', {"form": form})
    else:
        return render(request, 'create_usertype.html', {})

def read_usertype(request):
    usertype=User_Type.objects.all()
    return render(request, 'read_usertype.html', {"usertype": usertype})
	
def update_usertype(request):
    usertype=User_Type.objects.all()
    if request.method == "POST":
        form = {
			    'usertype_name': request.POST["usertype_name"],
                'usertype_name2': request.POST["usertype_name2"],			
        }
        if form["usertype_name2"]:
            try:
                User_Type.objects.get(User_Type_Name = form["usertype_name2"])
                form['errors'] = u"Придумайте другое название типа пользователя!"
                return render(request, 'update_usertype', {"usertype": usertype})
            except User_Type.DoesNotExist:
                if request.POST.get("usertype_name"):
                    saveusertypename=User_Type()
                    saveusertypename.User_Type_Name=request.POST.get("usertype_name")
                usertype2=User_Type.objects.all().filter(User_Type_Name=saveusertypename).update(User_Type_Name=form["usertype_name2"])
                return redirect('sammtuci')          
        else:
            form['errors'] = u"У вас имеются пустые поля!"
            return render(request, 'update_usertype.html', {"usertype": usertype, "form": form})
    else:
        return render(request, 'update_usertype.html', {"usertype": usertype})
		
def delete_usertype(request):
    usertype=User_Type.objects.all()
    if request.method == "POST":
        form = {
                'usertype_name': request.POST["usertype_name"],			
        }
        if request.POST.get("usertype_name"):
            saveusertypename=User_Type()
            saveusertypename.User_Type_Name=request.POST.get("usertype_name")
        usertype2=User_Type.objects.filter(User_Type_Name=saveusertypename).delete()
        return redirect('sammtuci')
    else:
        return render(request, 'delete_usertype.html', {"usertype": usertype})
    return render(request, 'delete_usertype.html', {"usertype": usertype})
		
def create_deaneryuser(request):
    faculty=Faculty.objects.all()
    if request.method == "POST":
        form = {
			'surname': request.POST["surname"],
			'name': request.POST["name"],
			'fathername': request.POST["fathername"],
            'login': request.POST["login"],
            'mail': request.POST["mail"],
            'password': request.POST["password"],
			'startwork_date': request.POST["startwork_date"],
			'faculty_name': request.POST["faculty_name"],			
        }
        if form["surname"] and form["name"] and form["fathername"] and form["login"] and form["mail"] and form["password"] and form["startwork_date"]:
            try:
                UserU.objects.get(username = form["login"])
                form['errors'] = u"Не уникальное имя пользователя!"
                return render(request, 'create_deaneryuser.html', {"faculty": faculty, 'form': form})
            except UserU.DoesNotExist:
                user=UserU.objects.create_user(form["login"], form["mail"], form["password"])
                user.Surname=form["surname"] 
                user.Name=form["name"] 
                user.Fathername=form["fathername"]
                user.StarkWork_Date=form["startwork_date"]  
                user.set_password(form["password"])
                if request.POST.get("faculty_name"):
                    savefacultyname=Faculty()
                    savefacultyname.Faculty_Name=request.POST.get("faculty_name")
                faculty_id=Faculty.objects.get(Faculty_Name=savefacultyname)
                user.Faculty_ID=faculty_id
                saveusertype=User_Type()
                saveusertype.User_Type=1
                user_type=User_Type.objects.get(User_Type=saveusertype.User_Type)
                user.User_Type=user_type
                user.save()
                return redirect('sammtuci')
        else:
            form['errors'] = u"У вас имеются пустые поля!"
            return render(request, 'create_deaneryuser.html', {"faculty": faculty, "form": form})
    else:
        return render(request, 'create_deaneryuser.html', {"faculty": faculty})
	
def read_deaneryuser(request):
    deaneryuser=UserU.objects.all().filter(User_Type=1)
    return render(request, 'read_deaneryuser.html', {"deaneryuser": deaneryuser})
	
def update_deaneryuser(request):
    deaneryuser=UserU.objects.all().filter(User_Type=1)
    faculty=Faculty.objects.all()
    if request.method == "POST":
        form = {
            'deaneryuser_id': request.POST["deaneryuser_id"],
			'surname': request.POST["surname"],
			'name': request.POST["name"],
			'fathername': request.POST["fathername"],
            'login': request.POST["login"],
            'mail': request.POST["mail"],
			'startwork_date': request.POST["startwork_date"],
			'faculty_name': request.POST["faculty_name"],			
        }
        if form["surname"] and form["name"] and form["fathername"] and form["login"] and form["mail"] and form["startwork_date"]:
            try:
                UserU.objects.get(username = form["login"])
                form['errors'] = u"Не уникальное имя пользователя!"
                return render(request, 'update_deaneryuser.html', {"deaneryuser": deaneryuser, "faculty": faculty, 'form': form})
            except UserU.DoesNotExist:
                if request.POST.get("deaneryuser_id"):
                    savedeaneryuserid=UserU()
                    savedeaneryuserid.id=request.POST.get("deaneryuser_id")
                if request.POST.get("faculty_name"):
                    savefacultyname=Faculty()
                    savefacultyname.Faculty_Name=request.POST.get("faculty_name")	               
                faculty_id=Faculty.objects.get(Faculty_Name=savefacultyname)
                deaneryuser=UserU.objects.all().filter(id=savedeaneryuserid.id).update(Surname=form["surname"], 
				Name=form["name"], Fathername=form["fathername"], username=form["login"], 
				StartWork_Date=form["startwork_date"], Faculty_ID=faculty_id.Faculty_ID)
                return redirect('sammtuci')
        else:
            form['errors'] = u"У вас имеются пустые поля!"
            return render(request, 'update_deaneryuser.html', {"deaneryuser": deaneryuser, "faculty": faculty, "form": form})			
    return render(request, 'update_deaneryuser.html', {"deaneryuser": deaneryuser, "faculty": faculty})
	
def delete_deaneryuser(request):
    deaneryuser=UserU.objects.all().filter(User_Type=1)
    if request.method == "POST":
        form = {
                'deaneryuser_id': request.POST["deaneryuser_id"],			
        }
        if request.POST.get("deaneryuser_id"):
            savedeaneryuserid=UserU()
            savedeaneryuserid.id=request.POST.get("deaneryuser_id")
        deaneryuser2=UserU.objects.filter(id=savedeaneryuserid.id).delete()
        return redirect('sammtuci')
    else:
        return render(request, 'delete_deaneryuser.html', {"deaneryuser": deaneryuser})
    return render(request, 'delete_deaneryuser.html', {"deaneryuser": deaneryuser})
	
def create_mark(request):
    if request.method == "POST":
        form = {
			    'mark_id': request.POST["mark_id"],
                'mark_text': request.POST["mark_text"],			
        }
        if form["mark_id"] and form["mark_text"]:		
            try:
                Mark.objects.get(Mark = form["mark_id"])
                form['errors'] = u"Эта оценка уже существует! Проверьте поле кода!"
                return render(request, 'create_mark.html', {'form': form})
            except Mark.DoesNotExist:
                try:
                    Mark.objects.get(Mark_Text = form["mark_text"])
                    form['errors'] = u"Эта оценка уже существует! Проверьте поле текста!"
                    return render(request, 'create_mark.html', {'form': form})
                except Mark.DoesNotExist:
                    mark=Mark.objects.create(Mark=form["mark_id"], Mark_Text=form["mark_text"])
                    return redirect('sammtuci')          
        else:
            form['errors'] = u"У вас имеются пустые поля!"
            return render(request, 'create_mark.html', {"form": form})
    else:
        return render(request, 'create_mark.html', {})

def read_mark(request):
    mark=Mark.objects.all()
    return render(request, 'read_mark.html', {"mark": mark})
	
def update_mark(request):
    mark=Mark.objects.all()
    if request.method == "POST":
        form = {
			    'mark_text': request.POST["mark_text"],
                'mark_text2': request.POST["mark_text2"],			
        }
        if form["mark_text2"]:
            try:
                Mark.objects.get(Mark_Text = form["mark_text2"])
                form['errors'] = u"Придумайте другой текст для оценки!"
                return render(request, 'update_mark', {"mark": mark})
            except Mark.DoesNotExist:
                if request.POST.get("mark_text"):
                    savemarktext=Mark()
                    savemarktext.Mark_Text=request.POST.get("mark_text")
                mark2=Mark.objects.all().filter(Mark_Text=savemarktext).update(Mark_Text=form["mark_text2"])
                return redirect('sammtuci')          
        else:
            form['errors'] = u"У вас имеются пустые поля!"
            return render(request, 'update_mark.html', {"mark": mark, "form": form})
    else:
        return render(request, 'update_mark.html', {"mark": mark})
		
def delete_mark(request):
    mark=Mark.objects.all()
    if request.method == "POST":
        form = {
                'mark_text': request.POST["mark_text"],			
        }
        if request.POST.get("mark_text"):
            savemarktext=Mark()
            savemarktext.Mark_Text=request.POST.get("mark_text")
        mark2=Mark.objects.filter(Mark_Text=savemarktext).delete()
        return redirect('sammtuci')
    else:
        return render(request, 'delete_mark.html', {"mark": mark})
    return render(request, 'delete_mark.html', {"mark": mark})
	
def create_year(request):
    if request.method == "POST":
        form = {
			    'year_id': request.POST["year_id"],
                'year_name': request.POST["year_name"],			
        }
        if form["year_id"] and form["year_name"]:		
            try:
                Year.objects.get(Year_ID = form["year_id"])
                form['errors'] = u"Этот тип пользователя уже существует! Проверьте поле номера!"
                return render(request, 'create_year.html', {'form': form})
            except Year.DoesNotExist:
                try:
                    Year.objects.get(Year_Name = form["year_name"])
                    form['errors'] = u"Этоn тип пользователя уже существует! Проверьте поле названия!"
                    return render(request, 'create_year.html', {'form': form})
                except Year.DoesNotExist:
                    year=Year.objects.create(Year_ID=form["year_id"], Year_Name=form["year_name"])
                    return redirect('sammtuci')          
        else:
            form['errors'] = u"У вас имеются пустые поля!"
            return render(request, 'create_year.html', {"form": form})
    else:
        return render(request, 'create_year.html', {})

def read_year(request):
    year=Year.objects.all()
    return render(request, 'read_year.html', {"year": year})
	
def update_year(request):
    year=Year.objects.all()
    if request.method == "POST":
        form = {
			    'year_name': request.POST["year_name"],
                'year_name2': request.POST["year_name2"],			
        }
        if form["year_name2"]:
            try:
                Year.objects.get(Year_Name = form["year_name2"])
                form['errors'] = u"Придумайте другое название типа пользователя!"
                return render(request, 'update_year', {"year": year})
            except Year.DoesNotExist:
                if request.POST.get("year_name"):
                    saveyearname=Year()
                    saveyearname.Year_Name=request.POST.get("year_name")
                year2=Year.objects.all().filter(Year_Name=saveyearname).update(Year_Name=form["year_name2"])
                return redirect('sammtuci')          
        else:
            form['errors'] = u"У вас имеются пустые поля!"
            return render(request, 'update_year.html', {"year": year, "form": form})
    else:
        return render(request, 'update_year.html', {"year": year})
		
def delete_year(request):
    year=Year.objects.all()
    if request.method == "POST":
        form = {
                'year_name': request.POST["year_name"],			
        }
        if request.POST.get("year_name"):
            saveyearname=Year()
            saveyearname.Year_Name=request.POST.get("year_name")
        year2=Year.objects.filter(Year_Name=saveyearname).delete()
        return redirect('sammtuci')
    else:
        return render(request, 'delete_year.html', {"year": year})
    return render(request, 'delete_year.html', {"year": year})
	
def create_group(request):
    year=Year.objects.all().order_by("Year_ID")
    branch=Branch.objects.all().order_by("Branch_ID")
    if request.method == "POST":
        form = {
			    'group_id': request.POST["group_id"],
                'year_id': request.POST["year_id"],
                'branch_id': request.POST["branch_id"],				
        }
        if form["group_id"]:		
            try:
                Group.objects.get(Group_ID = form["group_id"])
                form['errors'] = u"Эта группа уже существует! Проверьте поле номера!"
                return render(request, 'create_group.html', {"year": year, "branch": branch, 'form': form})
            except Group.DoesNotExist:
                group=Group.objects.create(Group_ID=form["group_id"])
                if request.POST.get("year_id"):
                    saveyearname=Year()
                    saveyearname.Year_Name=request.POST.get("year_id")
                if request.POST.get("branch_id"):
                    savebranchname=Branch()
                    savebranchname.Branch_Name=request.POST.get("branch_id")
                year_id=Year.objects.get(Year_Name=saveyearname)
                branch_id=Branch.objects.get(Branch_Name=savebranchname)
                group.Year_ID=year_id
                group.Branch_ID=branch_id
                group.save()
                return redirect('sammtuci')          
        else:
            form['errors'] = u"У вас имеются пустые поля!"
            return render(request, 'create_group.html', {'year': year, "branch": branch, 'form': form})
    else:
        return render(request, 'create_group.html', {"year": year, "branch": branch})

def read_group(request):
    group=Group.objects.all().order_by("Group_ID")
    return render(request, 'read_group.html', {"group": group})
	
def update_group(request):
    group=Group.objects.all()
    year=Year.objects.all()
    branch=Branch.objects.all()
    if request.method == "POST":
        form = {
			    'group_name': request.POST["group_name"],
                'year_id': request.POST["year_id"],
                'branch_id': request.POST["branch_id"]				
        }
        if request.POST.get("group_name"):
            savegroupname=Group()
            savegroupname.Group_ID=request.POST.get("group_name")
        if request.POST.get("year_id"):
            saveyearname=Year()
            saveyearname.Year_Name=request.POST.get("year_id")
        if request.POST.get("branch_id"):
            savebranchname=Branch()
            savebranchname.Branch_Name=request.POST.get("branch_id")
        year_id=Year.objects.get(Year_Name=saveyearname)
        branch_id=Branch.objects.get(Branch_Name=savebranchname)
        group2=Group.objects.all().filter(Group_ID=savegroupname.Group_ID).update(Year_ID=year_id.Year_ID, Branch_ID=branch_id.Branch_ID)
        return redirect('sammtuci')          
    else:
        return render(request, 'update_group.html', {"group": group, "year": year, "branch": branch})
		
def delete_group(request):
    group=Group.objects.all()
    if request.method == "POST":
        form = {
                'group_name': request.POST["group_name"],			
        }
        if request.POST.get("group_name"):
            savegroupname=Group()
            savegroupname.Group_ID=request.POST.get("group_name")
        group2=Group.objects.filter(Group_ID=savegroupname).delete()
        return redirect('sammtuci')
    else:
        return render(request, 'delete_group.html', {"group": group})
    return render(request, 'delete_group.html', {"group": group})

def create_teacher(request):
    department=Department.objects.all()
    if request.method == "POST":
        form = {
			'surname': request.POST["surname"],
			'name': request.POST["name"],
			'fathername': request.POST["fathername"],
            'login': request.POST["login"],
            'mail': request.POST["mail"],
            'password': request.POST["password"],
			'startwork_date': request.POST["startwork_date"],
			'department_name': request.POST["department_name"],			
        }
        if form["surname"] and form["name"] and form["fathername"] and form["login"] and form["mail"] and form["password"] and form["startwork_date"]:
            try:
                UserU.objects.get(username = form["login"])
                form['errors'] = u"Не уникальное имя пользователя!"
                return render(request, 'create_deaneryuser.html', {"faculty": faculty, 'form': form})
            except UserU.DoesNotExist:
                user=UserU.objects.create_user(form["login"], form["mail"], form["password"])
                user.Surname=form["surname"] 
                user.Name=form["name"] 
                user.Fathername=form["fathername"]
                user.StarkWork_Date=form["startwork_date"]                
                if request.POST.get("department_name"):
                    savedepartmentname=Department()
                    savedepartmentname.Department_Name=request.POST.get("department_name")
                department_id=Department.objects.get(Department_Name=savedepartmentname)
                user.Department_ID=department_id
                saveusertype=User_Type()
                saveusertype.User_Type=2
                user_type=User_Type.objects.get(User_Type=saveusertype.User_Type)
                user.User_Type=user_type
                user.save()
                return redirect('sammtuci')
        else:
            form['errors'] = u"У вас имеются пустые поля!"
            return render(request, 'create_teacher.html', {"department": department, "form": form})
    else:
        return render(request, 'create_teacher.html', {"department": department})	
		
def read_teacher(request):
    teacher=UserU.objects.all().filter(User_Type=2)
    return render(request, 'read_teacher.html', {"teacher": teacher})
	
def update_teacher(request):
    teacher=UserU.objects.all().filter(User_Type=2)
    department=Department.objects.all()
    if request.method == "POST":
        form = {
            'teacher_id': request.POST["teacher_id"],
			'surname': request.POST["surname"],
			'name': request.POST["name"],
			'fathername': request.POST["fathername"],
            'login': request.POST["login"],
            'mail': request.POST["mail"],
			'startwork_date': request.POST["startwork_date"],
			'department_name': request.POST["department_name"],			
        }
        if form["surname"] and form["name"] and form["fathername"] and form["login"] and form["mail"] and form["startwork_date"]:
            try:
                UserU.objects.get(username = form["login"])
                form['errors'] = u"Не уникальное имя пользователя!"
                return render(request, 'update_teacher.html', {"teacher": teacher, "department": department, 'form': form})
            except UserU.DoesNotExist:
                if request.POST.get("teacher_id"):
                    saveteacherid=UserU()
                    saveteacherid.id=request.POST.get("teacher_id")
                if request.POST.get("department_name"):
                    savedepartmentname=Department()
                    savedepartmentname.Department_Name=request.POST.get("department_name")	               
                department_id=Department.objects.get(Department_Name=savedepartmentname)
                teacher=UserU.objects.all().filter(id=saveteacherid.id).update(Surname=form["surname"], 
				Name=form["name"], Fathername=form["fathername"], username=form["login"], 
				StartWork_Date=form["startwork_date"], Department_ID=department_id.Department_ID)
                return redirect('sammtuci')
        else:
            form['errors'] = u"У вас имеются пустые поля!"
            return render(request, 'update_teacher.html', {"teacher": teacher, "department": department, "form": form})			
    return render(request, 'update_teacher.html', {"teacher": teacher, "department": department})
	
def delete_teacher(request):
    teacher=UserU.objects.all().filter(User_Type=2)
    if request.method == "POST":
        form = {
                'teacher_id': request.POST["teacher_id"],			
        }
        if request.POST.get("teacher_id"):
            saveteacherid=UserU()
            saveteacherid.id=request.POST.get("teacher_id")
        teacher2=UserU.objects.filter(id=saveteacherid.id).delete()
        return redirect('sammtuci')
    else:
        return render(request, 'delete_teacher.html', {"teacher": teacher})
    return render(request, 'delete_teacher.html', {"teacher": teacher})

def create_student(request):
    group=Group.objects.all()
    if request.method == "POST":
        form = {
			'surname': request.POST["surname"],
			'name': request.POST["name"],
			'fathername': request.POST["fathername"],
            'login': request.POST["login"],
            'mail': request.POST["mail"],
            'password': request.POST["password"],
			'start_date': request.POST["start_date"],
			'group_name': request.POST["group_name"],
            'points': request.POST["points"],			
        }
        if form["surname"] and form["name"] and form["fathername"] and form["login"] and form["mail"] and form["password"] and form["start_date"] and form["points"]:
            try:
                UserU.objects.get(username = form["login"])
                form['errors'] = u"Не уникальное имя пользователя!"
                return render(request, 'create_student.html', {"group": group, 'form': form})
            except UserU.DoesNotExist:
                user=UserU.objects.create_user(form["login"], form["mail"], form["password"])
                user.Surname=form["surname"] 
                user.Name=form["name"] 
                user.Fathername=form["fathername"]
                user.Stark_Date=form["start_date"]     
                user.Points=form["points"]				
                if request.POST.get("group_name"):
                    savegroupname=Group()
                    savegroupname.Group_ID=request.POST.get("group_name")
                group_id=Group.objects.get(Group_ID=savegroupname)
                user.Group_ID=group_id
                saveusertype=User_Type()
                saveusertype.User_Type=3
                user_type=User_Type.objects.get(User_Type=saveusertype.User_Type)
                user.User_Type=user_type
                user.save()
                return redirect('sammtuci')
        else:
            form['errors'] = u"У вас имеются пустые поля!"
            return render(request, 'create_student.html', {"group": group, "form": form})
    else:
        return render(request, 'create_student.html', {"group": group})	
		
def read_student(request):
    student=UserU.objects.all().filter(User_Type=3)
    return render(request, 'read_student.html', {"student": student})
	
def update_student(request):
    student=UserU.objects.all().filter(User_Type=3)
    group=Group.objects.all()
    if request.method == "POST":
        form = {
            'student_id': request.POST["student_id"],
			'surname': request.POST["surname"],
			'name': request.POST["name"],
			'fathername': request.POST["fathername"],
            'login': request.POST["login"],
            'mail': request.POST["mail"],
			'start_date': request.POST["start_date"],
			'group_name': request.POST["group_name"],
            'points': request.POST["points"],			
        }
        if form["surname"] and form["name"] and form["fathername"] and form["login"] and form["mail"] and form["start_date"] and form["points"]:
            try:
                UserU.objects.get(username = form["login"])
                form['errors'] = u"Не уникальное имя пользователя!"
                return render(request, 'update_student.html', {"student": student, "group": group, 'form': form})
            except UserU.DoesNotExist:
                if request.POST.get("student_id"):
                    savestudentid=UserU()
                    savestudentid.id=request.POST.get("student_id")
                if request.POST.get("group_name"):
                    savegroupname=Group()
                    savegroupname.Group_ID=request.POST.get("group_name")	               
                group_id=Group.objects.get(Group_ID=savegroupname)
                student=UserU.objects.all().filter(id=savestudentid.id).update(Surname=form["surname"], 
				Name=form["name"], Fathername=form["fathername"], username=form["login"], email=form["mail"],
				Start_Date=form["start_date"], Group_ID=group_id.Group_ID, Points=form["points"])
                return redirect('sammtuci')
        else:
            form['errors'] = u"У вас имеются пустые поля!"
            return render(request, 'update_student.html', {"student": student, "group": group, "form": form})			
    return render(request, 'update_student.html', {"student": student, "group": group})
	
def delete_student(request):
    student=UserU.objects.all().filter(User_Type=3)
    if request.method == "POST":
        form = {
                'student_id': request.POST["student_id"],			
        }
        if request.POST.get("student_id"):
            savestudentid=UserU()
            savestudentid.id=request.POST.get("student_id")
        student2=UserU.objects.filter(id=savestudentid.id).delete()
        return redirect('sammtuci')
    else:
        return render(request, 'delete_student.html', {"student": student})
    return render(request, 'delete_student.html', {"student": student})
	
def create_subject(request):
    department=Department.objects.all()
    if request.method == "POST":
        form = {
			    'subject_id': request.POST["subject_id"],
                'subject_name': request.POST["subject_name"],	
				'department_name': request.POST["department_name"]
        }
        if form["subject_id"] and form["subject_name"]:
            try:
                Subject.objects.get(Subject_ID = form["subject_id"])
                form['errors'] = u"Эта учебная дисциплина уже существует! Проверьте поле номера!"
                return render(request, 'create_subject.html', {"department": department, 'form': form})
            except Subject.DoesNotExist:
                try:
                    Subject.objects.get(Subject_Name = form["subject_name"])
                    form['errors'] = u"Эта учебная дисциплина уже существует! Проверьте поле названия!"
                    return render(request, 'create_subject.html', {"department": department, 'form': form})
                except Subject.DoesNotExist:
                    subject=Subject.objects.create(Subject_ID=form["subject_id"], Subject_Name=form["subject_name"])
                    if request.POST.get("department_name"):
                        savedepartmentname=Department()
                        savedepartmentname.Department_Name=request.POST.get("department_name")
                    department_id=Department.objects.get(Department_Name=savedepartmentname)
                    subject.Department_ID=department_id
                    subject.save()
                    return redirect('sammtuci')           
        else:
            form['errors'] = u"У вас имеются пустые поля!"
            return render(request, 'create_subject.html', {"department": department, "form": form})
    else:
        return render(request, 'create_subject.html', {"department": department})
		
def read_subject(request):
    subject=Subject.objects.all()
    return render(request, 'read_subject.html', {"subject": subject})

def update_subject(request):
    subject=Subject.objects.all()
    department=Department.objects.all()
    if request.method == "POST":
        form = {
			    'subject_name': request.POST["subject_name"],
                'subject_name2': request.POST["subject_name2"],
                'department_name': request.POST["department_name"],				
        }
        if form["subject_name2"]:
            try:
                Subject.objects.get(Subject_Name = form["subject_name2"])
                form['errors'] = u"Придумайте другое название учебной дисциплины!"
                return render(request, 'update_subject', {"department": department, "subject": subject})
            except Subject.DoesNotExist:
                if request.POST.get("subject_name"):
                    savesubjectname=Subject()
                    savesubjectname.Subject_Name=request.POST.get("subject_name")
                if request.POST.get("department_name"):
                    savedepartmentname=Department()
                    savedepartmentname.Department_Name=request.POST.get("department_name")
                department_id=Department.objects.get(Department_Name=savedepartmentname)
                subject2=Subject.objects.all().filter(Subject_Name=savesubjectname).update(Subject_Name=form["subject_name2"], Department_ID=department_id.Department_ID)
                return redirect('sammtuci')          
        else:
            form['errors'] = u"У вас имеются пустые поля!"
            return render(request, 'update_subject.html', {"department": department, "subject": subject, "form": form})
    else:
        return render(request, 'update_subject.html', {"department": department, "subject": subject})	

def delete_subject(request):
    subject=Subject.objects.all()
    if request.method == "POST":
        form = {
                'subject_name': request.POST["subject_name"],			
        }
        if request.POST.get("subject_name"):
            savesubjectname=Subject()
            savesubjectname.Subject_Name=request.POST.get("subject_name")
        subject2=Subject.objects.filter(Subject_Name=savesubjectname).delete()
        return redirect('sammtuci')
    else:
        return render(request, 'delete_subject.html', {"subject": subject})
    return render(request, 'delete_subject.html', {"subject": subject})
	
def create_subjectduringyear(request):
	branch=Branch.objects.all()
	subject=Subject.objects.all()
	teacher=UserU.objects.all().filter(User_Type=2)
	if request.method == "POST":
		form = {
			    'subjectduringyear_id': request.POST["subjectduringyear_id"],
                'subject_name': request.POST["subject_name"],	
				'branch_name': request.POST["branch_name"],
                'teacher_id': request.POST["teacher_id"],
				'semester': request.POST["semester"]
        }
		if  form["semester"]:
			try:
				SubjectDuringYear.objects.get(Subject2_ID = form["subjectduringyear2_id"])
				form['errors'] = u"Эта учебная дисциплина уже существует! Проверьте поле н!"
				return render(request, 'create_subjectduringyear.html', {"branch": branch, "subject": subject, "teacher": teacher, 'form': form})
			except SubjectDuringYear.DoesNotExist:
				subjectduringyear=SubjectDuringYear.objects.create(Subject2_ID=form["subjectduringyear_id"], Semester=form["semester"])
				if request.POST.get("branch_name"):
					savebranchname=Branch()
					savebranchname.Branch_Name=request.POST.get("branch_name")
				if request.POST.get("subject_name"):
					savesubjectname=Subject()
					savesubjectname.Subject_Name=request.POST.get("subject_name")
				if request.POST.get("teacher_id"):
					saveteacherid=UserU()
					saveteacherid.id=request.POST.get("teacher_id")
				branch_id=Branch.objects.get(Branch_Name=savebranchname)
				subject_id=Subject.objects.get(Subject_Name=savesubjectname)
				teacher_id=UserU.objects.get(id=saveteacherid.id)
				subjectduringyear.Branch_ID=branch_id
				subjectduringyear.Subject_ID=subject_id
				subjectduringyear.Teacher_ID=teacher_id
				subjectduringyear.save()
				return redirect('sammtuci')           
		else:
			form['errors'] = u"У вас имеются пустые поля!"
			return render(request, 'create_subjectduringyear.html', {"branch": branch, "subject": subject, "teacher": teacher,  "form": form})
	else:
		return render(request, 'create_subjectduringyear.html', {"branch": branch, "subject": subject, "teacher": teacher})
		
def read_subjectduringyear(request):
    subjectduringyear=SubjectDuringYear.objects.all()
    return render(request, 'read_subjectduringyear.html', {"subjectduringyear": subjectduringyear})

def update_subjectduringyear(request):
    subjectduringyear=SubjectDuringYear.objects.all()
    subject=Subject.objects.all()
    branch=Branch.objects.all()
    teacher=UserU.objects.all()
    if request.method == "POST":
        form = {
			    'subjectduringyear_name': request.POST["subjectduringyear_name"],
                'subject_name': request.POST["subject_name"],	
				'branch_name': request.POST["branch_name"],
                'teacher_id': request.POST["teacher_id"],
				'semester': request.POST["semester"]				
        }
        if form["semester"]:
            if request.POST.get("subjectduringyear_name"):
                savesubjectduringyearname=SubjectDuringYear()
                savesubjectduringyearname.Subject2_ID=request.POST.get("subjectduringyear_name")
            if request.POST.get("branch_name"):
                savebranchname=Branch()
                savebranchname.Branch_Name=request.POST.get("branch_name")
            if request.POST.get("subject_name"):
                savesubjectname=Subject()
                savesubjectname.Subject_Name=request.POST.get("subject_name")
            if request.POST.get("teacher_id"):
                saveteacherid=UserU()
                saveteacherid.id=request.POST.get("teacher_id")
            branch_id=Branch.objects.get(Branch_Name=savebranchname)
            subject_id=Subject.objects.get(Subject_Name=savesubjectname)
            teacher_id=UserU.objects.get(id=saveteacherid.id)
            subjectduringyear2=SubjectDuringYear.objects.all().filter(Subject2_ID=savesubjectduringyearname.Subject2_ID).update(Semester=form["semester"], 
			Branch_ID=branch_id.Branch_ID, Subject_ID=subject_id.Subject_ID, Teacher_ID=teacher_id.id)
            return redirect('sammtuci')          
        else:
            form['errors'] = u"У вас имеются пустые поля!"
            return render(request, 'update_subjectduringyear.html', {"branch": branch, "subject": subject,  "subjectduringyear": subjectduringyear, "teacher": teacher, "form": form})
    else:
        return render(request, 'update_subjectduringyear.html', {"branch": branch, "teacher": teacher, "subject": subject, "subjectduringyear": subjectduringyear})	

def delete_subjectduringyear(request):
    subjectduringyear=SubjectDuringYear.objects.all()
    if request.method == "POST":
        form = {
                'subjectduringyear_name': request.POST["subjectduringyear_name"],			
        }
        if request.POST.get("subjectduringyear_name"):
            savesubjectduringyearname=SubjectDuringYear()
            savesubjectduringyearname.Subject2_ID=request.POST.get("subjectduringyear_name")
        subjectduringyear2=SubjectDuringYear.objects.filter(Subject2_ID=savesubjectduringyearname.Subject2_ID).delete()
        return redirect('sammtuci')
    else:
        return render(request, 'delete_subjectduringyear.html', {"subjectduringyear": subjectduringyear})
    return render(request, 'delete_subjectduringyear.html', {"subjectduringyear": subjectduringyear})
# Create your views here.
