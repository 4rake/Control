from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from django.contrib.auth import login, authenticate, logout
from django.http.response import Http404, HttpResponse
from datetime import datetime
from django.http import JsonResponse
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views import View
from django.db.models import Q
from .filters import *
import xlwt
from django.core.mail import send_mail
from django.contrib.admin.models import LogEntry

from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile
from django.db.models import Sum

from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.http import HttpResponse
from .models import BlogPost







def index(request):
    data = {
        'title': 'Главная страница'
    }
    return render(request, 'main/index.html', data)


def export_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Group_name' + \
        str(datetime.now())+'.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Group_name')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['name', 'description', 'course', 'fk_discipline']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    rows = Group_name.objects.all().values_list('name', 'description', 'course', 'fk_discipline')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)
    return response

def export_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; attachment; filename=Group_name' + \
        str(datetime.now()) + '.pdf'
    response['Content-Transfer-Encoding'] = 'binary'

    #sum = group_name.aggregate(Sum('amount'))

    html_string = render_to_string(
        'group_name/pdf-output.html', {'group_name': [], 'total': 0})
    html = HTML(string=html_string)

    result = html.write_pdf()

    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')
        response.write(output.read())

    return response


def diary(request, pk):
    homework_check = Homework_check.objects.filter(Q(fk_employee=pk))

    return render(request, "diary/diary.html", {"homework_check": homework_check})

#def create_diary(request):
    #form = DiaryForm()
    #if request.method == 'POST':
    #    form = DiaryForm(request.POST)
    #    if form.is_valid():
    #        form.save()
    #        return redirect('diary')
    #context = {'form':form}
    #return render(request, 'diary/create_diary.html', context)

def about(request):
    return render(request, "main/about.html")

def student(request):
    student = Student.objects.all()
    myFilter = StudentFilter(request.GET, queryset=student)
    student = myFilter.qs
    context = {'myFiler':myFilter, "student": student}
    return render(request, "student/students.html", {"student":student, "myFilter":myFilter})

def cr_st(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student')
    context = {'form':form}
    return render(request, 'student/cr_st.html', context)


def distribution(request):
    distribution = Distribution.objects.all()
    return render(request, "distribution/distribution.html", {"distribution": distribution})

def create_distribution(request):
    form = DistributionForm()
    if request.method == 'POST':
        form = DistributionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('distribution')
    context = {'form': form}
    return render(request, 'distribution/create_distribution.html', context)

def update_distribution(request, pk):
    distribution = Distribution.objects.get(id=pk)

    form = DistributionForm(instance=distribution)

    if request.method == 'POST':
        form = DistributionForm(request.POST, instance=distribution)
        if form.is_valid():
            form.save()
            return redirect('distribution')
    context = {'form': form}

    return render(request, 'distribution/update_distribution.html', context)

def delete_distribution(request, pk):
    distribution = Distribution.objects.get(id=pk)
    if request.method == "POST":
        distribution.delete()
        return redirect('distribution')
    return render(request, 'distribution/delete_distribution.html')



def authorization(request):
    return render(request, "main/authorization.html")

def personal_area(request):
    return render(request, "personal_area/personal_area.html")

def user_profiile(request):
    user_profiile = User.objects.all()
    return render(request, "employee/employee.html", {"user_profile": user_profiile})

def create_employee(request):
    form = UserProfileForm()
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    context = {'form':form}
    return render(request, 'employee/create_employee.html', context)

def position(request):
    position = Position.objects.all()
    return render(request, "position/position.html", {"position": position})

def create_position(request):
    form = PositionForm()
    if request.method == 'POST':
        form = PositionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('position')
    context = {'form':form}
    return render(request, 'position/create_position.html', context)

def group_name(request):
    group_name = Group_name.objects.all()
    return render(request, "group_name/group_name.html", {"group_name": group_name})

def create_group_name(request):
    form = Grop_nameForm()
    if request.method == 'POST':
        form = Grop_nameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('group_name')
    context = {'form':form}
    return render(request, 'group_name/create_group_name.html', context)

def homework(request):
    homework = Homework.objects.all()
    return render(request, "homework/homework.html", {"homework": homework})

def create_homework(request):
    form = HomeworkForm()
    if request.method == 'POST':
        form = HomeworkForm(request.POST)
        if form.is_valid():

            form.save()
            return redirect('homework')
    context = {'form':form}

    return render(request, 'homework/create_homework.html', context)

def homework_check(request):
    homework_check = Homework_check.objects.all()
    return render(request, "homework_check/homework_check.html", {"homework_check": homework_check})

def create_homework_check(request):
    form = Homework_checkForm()
    if request.method == 'POST':
        form = Homework_checkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homework_check')
    context = {'form':form}
    return render(request, 'homework_check/create_homework_check.html', context)

def update_employee(request, pk):

    user_profiile = UserProfile.objects.get(id=pk)

    form = UserProfileForm(instance=user_profiile)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profiile)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    context = {'form':form}

    return render(request, 'employee/create_employee.html', context)

def delete_employee(request, pk):

    user_profile = UserProfile.objects.get(id=pk)
    if request.method == "POST":
        user_profiile.delete()
        return redirect('user_profile')


def update_group_name(request, pk):

    group_name = Group_name.objects.get(id=pk)

    form = Grop_nameForm(instance=group_name)

    if request.method == 'POST':
        form = Grop_nameForm(request.POST, instance=group_name)
        if form.is_valid():
            form.save()
            return redirect('group_name')
    context = {'form':form}

    return render(request, 'group_name/update_group_name.html', context)

def delete_group_name(request, pk):
    group_name = Group_name.objects.get(id=pk)
    if request.method == "POST":
        group_name.delete()
        return redirect('group_name')
    return render(request, 'group_name/delete_group_name.html')



def update_homework(request, pk):

    homework = Homework.objects.get(id=pk)

    form = HomeworkForm(instance=homework)

    if request.method == 'POST':
        form = HomeworkForm(request.POST, instance=homework)
        if form.is_valid():
            form.save()
            return redirect('homework')
    context = {'form':form}

    return render(request, 'homework/update_homework.html', context)

def delete_homework(request, pk):
    homework = Homework.objects.get(id=pk)
    if request.method == "POST":
        homework.delete()
        return redirect('homework')
    return render(request, 'homework/delete_homework.html')

def update_student(request, pk):

    student = Student.objects.get(id=pk)

    form = StudentForm(instance=student)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student')
    context = {'form': form}

    return render(request, 'student/update_student.html', context)

def delete_student(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == "POST":
        student.delete()
        return redirect('student')
    return render(request, 'student/delete_student.html')

def update_homework_check(request, pk):

    homework_check = Homework_check.objects.get(id=pk)

    form = Homework_checkForm(instance=homework_check)

    if request.method == 'POST':
        form = Homework_checkForm(request.POST, instance=homework_check)
        if form.is_valid():
            form.save()
            return redirect('homework_check')
    context = {'form':form}

    return render(request, 'homework_check/update_homework_check.html', context)

def delete_homework_check(request, pk):
    homework_check = Homework_check.objects.get(id=pk)
    if request.method == "POST":
        homework_check.delete()
        return redirect('homework_check')
    return render(request, 'homework_check/delete_homework_check.html')

def update_position(request, pk):

    position = Position.objects.get(id=pk)

    form = PositionForm(instance=position)

    if request.method == 'POST':
        form = PositionForm(request.POST, instance=position)
        if form.is_valid():
            form.save()
            return redirect('position')
    context = {'form':form}

    return render(request, 'position/update_position.html', context)

def delete_position(request, pk):
    position = Position.objects.get(id=pk)
    if request.method == "POST":
        position.delete()
        return redirect('position')
    return render(request, 'position/delete_position.html')




def discipline(request):
    discipline = Discipline.objects.all()
    return render(request, "discipline/discipline.html", {"discipline": discipline})


def create_discipline(request):
    form = DisciplineForm()
    if request.method == 'POST':
        form = DisciplineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('discipline')
    context = {'form':form}
    return render(request, 'discipline/create_discipline.html', context)

def update_discipline(request, pk):

    discipline = Discipline.objects.get(id=pk)

    form = DisciplineForm(instance=discipline)

    if request.method == 'POST':
        form = DisciplineForm(request.POST, instance=discipline)
        if form.is_valid():
            form.save()
            return redirect('discipline')
    context = {'form':form}

    return render(request, 'discipline/update_discipline.html', context)

def delete_discipline(request, pk):
    discipline = Discipline.objects.get(id=pk)
    if request.method == "POST":
        discipline.delete()
        return redirect('discipline')
    return render(request, 'discipline/delete_discipline.html')

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('registerPage')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('loginPage')

        context = {'form': form}
        return render(request, 'accounts/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('loginPage')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('loginPage')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'], 'a.b.puzanov@gmail.com', ['lexa90russss9@gmail.com'], fail_silently=True)
            if mail:
                messages.success(request, 'Письмо отправлено')
                return redirect('contact')
            else:
                messages.error(request, 'Ошибка отправка')

        else:
            messages.error(request, 'Ошибка заполнения')
    else:
        form = ContactForm()
        return render(request, 'contact/contact.html', {"form": form})

# Логирование действия в административной панели
@login_required(login_url='login')
def logging_action(request):
    logging_count = LogEntry.objects.all()
    context = {'logging_counts': logging_count}
    return render(request, 'loging/logging.html', context=context)


def attendance(request):
    attendance = Attendance.objects.all()
    myattendanceFilter = AttendanceFilter(request.GET, queryset=attendance)
    attendance = myattendanceFilter.qs
    context = {'myFiler':myattendanceFilter, "attendance": attendance}
    return render(request, "attendance/attendance.html", {"attendance": attendance, "myattendanceFilter":myattendanceFilter})


def create_attendance(request):
    form = AttendanceForm()
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendance')
    context = {'form':form}
    return render(request, 'attendance/create_attendance.html', context)


def update_attendance(request, pk):
    attendance = Attendance.objects.get(id=pk)

    form = AttendanceForm(instance=attendance)

    if request.method == 'POST':
        form = AttendanceForm(request.POST, instance=attendance)
        if form.is_valid():
            form.save()
            return redirect('attendance')
    context = {'form': form}

    return render(request, 'attendance/update_attendance.html', context)


def delete_attendance(request, pk):
    attendance = Attendance.objects.get(id=pk)
    if request.method == "POST":
        attendance.delete()
        return redirect('attendance')
    return render(request, 'attendance/delete_attendance.html')


def create_blog_view(request):

	context = {}

	user = request.user
	if not user.is_authenticated:
		return redirect('must_authenticate')

	form = CreateBlogPostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		obj = form.save(commit=False)
		author = User.objects.filter(email=user.email).first()
		obj.author = author
		obj.save()
		form = CreateBlogPostForm()

	context['form'] = form

	return render(request, "information/create_blog.html", context)


def detail_blog_view(request, slug):

	context = {}

	blog_post = get_object_or_404(BlogPost, slug=slug)
	context['blog_post'] = blog_post

	return render(request, 'information/detail_blog.html', context)



def edit_blog_view(request, slug):

	context = {}

	user = request.user
	if not user.is_authenticated:
		return redirect("must_authenticate")

	blog_post = get_object_or_404(BlogPost, slug=slug)

	if blog_post.author != user:
		return HttpResponse("You are not the author of that post.")

	if request.POST:
		form = UpdateBlogPostForm(request.POST or None, request.FILES or None, instance=blog_post)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
			context['success_message'] = "Updated"
			blog_post = obj

	form = UpdateBlogPostForm(
			initial = {
					"title": blog_post.title,
					"body": blog_post.body,
					"image": blog_post.image,
			}
    )

	context['form'] = form
	return render(request, 'information/edit_blog.html', context)


def get_blog_queryset(query=None):
	queryset = []
	queries = query.split(" ") # python install 2019 = [python, install, 2019]
	for q in queries:
		posts = BlogPost.objects.filter(
				Q(title__icontains=q) |
				Q(body__icontains=q)
			).distinct()

		for post in posts:
			queryset.append(post)

	return list(set(queryset))






def export_excel_attendance(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Attendance' + \
        str(datetime.now())+'.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Attendance')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['fk_student', 'fk_discipline', 'date_of_visit', 'presence']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    rows = Attendance.objects.all().values_list('fk_student', 'fk_discipline', 'date_of_visit', 'presence')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)
    return response
