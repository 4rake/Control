from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.i18n import i18n_patterns
from django.views.generic import ListView, DetailView
from main.models import *

urlpatterns = [
    path('', views.index, name='home'),


    path('registerPage', views.registerPage, name='registerPage'),
    path('loginPage', views.loginPage, name='loginPage'),
    path('logoutUser', views.logoutUser, name='logoutUser'),
    path('auth/', include('rest_framework_social_oauth2.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    path('student', views.student, name='student'),
    path('cr_st', views.cr_st, name='cr_st'),
    path('update_student/<str:pk>/', views.update_student, name='update_student'),
    path('delete_student/<str:pk>/', views.delete_student, name='delete_student'),

    path('diary', views.diary, name='diary'),
    path('create_diary', views.create_diary, name='create_diary'),
    path('update_diary/<str:pk>/', views.update_diary, name='update_diary'),
    path('delete_diary/<str:pk>/', views.delete_diary, name='delete_diary'),

    path('personal_area', views.personal_area, name='personal_area'),

    path('news', views.news, name='news'),
    path('post', views.post, name='post'),

    path('create_posts', views.create_posts, name='create_posts'),
    path('update_posts/<str:pk>/', views.update_posts, name='update_posts'),
    path('delete_posts/<str:pk>/', views.delete_posts, name='delete_posts'),
    path('distribution', views.distribution, name='distribution'),
    path('distribution/<str:pk>/', views.distribution, name='distribution'),
    path('create_distribution', views.create_distribution, name='create_distribution'),
    path('update_distribution/<str:pk>/', views.update_distribution, name='update_distribution'),
    path('delete_distribution/<str:pk>/', views.delete_distribution, name='delete_distribution'),
    path('user_profile', views.user_profiile, name='user_profile'),
    path('create_employee', views.create_employee, name='create_employee'),
    path('update_employee/<str:pk>/', views.update_employee, name='update_employee'),
    path('delete_employee/<str:pk>/', views.delete_employee, name='delete_employee'),

    path('position', views.position, name='position'),
    path('create_position', views.create_position, name='create_position'),
    path('update_position/<str:pk>/', views.update_position, name='update_position'),
    path('delete_position/<str:pk>/', views.delete_position, name='delete_position'),

    path('group_name', views.group_name, name='group_name'),
    path('create_group_name', views.create_group_name, name='create_group_name'),

    path('homework', views.homework, name='homework'),
    path('homework_student', views.homework_student, name='homework_student'),

    path('create_homework', views.create_homework, name='create_homework'),
    path('update_homework/<str:pk>/', views.update_homework, name='update_homework'),
    path('delete_homework/<str:pk>/', views.delete_homework, name='delete_homework'),
    path('update_group_name/<int:pk>/', views.update_group_name, name='update_group_name'),
    path('delete_group_name/<str:pk>/', views.delete_group_name, name='delete_group_name'),

    path('homework_check', views.homework_check, name='homework_check'),
    path('create_homework_check', views.HomeworkCheckCreate.as_view(), name='create_homework_check'),
    #path('create_homework_check', views.create_homework_check, name='create_homework_check'),
    path('update_homework_check/<int:pk>/', views.update_homework_check, name='update_homework_check'),
    path('delete_homework_check/<str:pk>/', views.delete_homework_check, name='delete_homework_check'),

    #path('information', views.information, name='information'),
    #path('create_information', views.create_information, name='create_information'),
    #path('update_information/<str:pk>/', views.update_information, name='update_information'),
    #path('delete_information/<str:pk>/', views.delete_information, name='delete_information '),

   # path('homework/<int:product_id>', homework_detail, name = 'homework_url'),
    #path('homework/<int:homework_id>/update', Homework_Update.as_view(),
                                                 #name = 'update_homework_url'),
    #path('homework/<int:homework_id>/delete', Homework_Delete.as_view(),
    #                                             name = 'delete_homework_url'),



    path('discipline', views.discipline, name='discipline'),
    path('create_discipline', views.create_discipline, name='create_discipline'),
    path('update_discipline/<str:pk>/', views.update_discipline, name='update_discipline'),
    path('delete_discipline/<str:pk>/', views.delete_discipline, name='delete_discipline'),

    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/',
        auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"),
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"),
     name="password_reset_confirm"),

    path('export_excel', views.export_excel, name="export-excel"),
    path('export_excel_attendance', views.export_excel_attendance, name="export_excel-attendance"),

    #path('export_pdf', views.export_pdf, name="export-pdf"),

    path('attendance', views.attendance, name='attendance'),
    path('create_attendance', views.create_attendance, name='create_attendance'),
    path('update_attendance/<str:pk>/', views.update_attendance, name='update_attendance'),
    path('delete_attendance/<str:pk>/', views.delete_attendance, name='delete_attendance'),

    path('reset_password_complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"),
        name="password_reset_complete"),

    path('contact', views.contact, name='contact'),

    path('News/<int:pk>',
    ListView.as_view(queryset=News.objects.all().order_by("-date")[:20],
    template_name="news/posts.html")),
    path('News/<int:pk>',
    DetailView.as_view(model=News,
    template_name="news/post.html"),name='post'),
    path('Homework/<int:pk>',
    ListView.as_view(queryset=Homework.objects.all(),
    template_name="homework/homework_student.html")),
    path('Homework/<int:pk>',
    DetailView.as_view(model=Homework,
    template_name="homework/homework_student.html"), name='homework_url'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
