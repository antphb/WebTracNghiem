"""
URL configuration for WebTracNghiem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.views.generic.base import RedirectView
from . import views
from django.contrib.auth import views as auth_views
from .forms import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('',views.base,name='base'),
    path('', RedirectView.as_view(url='/login/'),name='index'),

    path('profile/',views.home.as_view(),name='home'),
    path("DanhSachDeThi/",views.listTest.as_view(), name="listTest"),
    path("DanhSachCauHoi/",views.listQuesion.as_view(), name="listQuesion"),
    path("DanhSachLopHoc/",views.listGroupClass.as_view(), name="listGroupClass"),
    path("DanhSachHocSinh/<malh>",views.listStudent.as_view(), name="listStudent"),
    path("DanhSachDiemThi/<makt>=<mhs>",views.listScoreStudent.as_view(), name="listScoreStudent"),
    path("DanhSachCauHoiHocSinh/<mlh>=<mhs>",views.listStudentQuesion.as_view(), name="listStudentQuesion"),
    path("DanhSachLamBaiHocSinh/<makt>",views.listStudentLamBai.as_view(), name="listStudentLamBai"),
    path("DiemThiHocSinh/<makt>=<malskt>/<mhs>",views.resultTest.as_view(), name="resultTest"),
    path("Dapanchitiet/<makt>=<malskt>/<mhs>",views.detailResultTest.as_view(), name="detailResultTest"),
    path("Dapanchitietcauhoi/<makt>",views.detailTest.as_view(), name="detailTest"),
    path("pdf/<makt>",views.printTestPDF.as_view(), name="printTestPDF"),
    path("Thongke/",views.StatisticResultTest.as_view(), name="statisticResultTest"),


    #===========================Edit/ADD============================
    path("deleteTest/<makt>", views.delete_test.as_view(), name="delete_test"),
    path("changeTrangThai/<makt>-<trangthai>", views.changeTrangThai.as_view(), name="changeTrangThai"),

    path("addNewStudent/", views.addNewStudent.as_view(), name="addNewStudent"),
    path("deleteStudent/<mhs>", views.deleteStudent.as_view(), name="deleteStudent"),


    #===========================API View============================
    path('api_chuong/<mamon>-<lop>',views.API_getChuong_getBai_byMon.as_view(),name='api_chuong_mon'),
    path('api_bai/<machuong>',views.API_getBai_byChuong.as_view(),name='api_bai_chuong'),

    path('api_getScore/<makt>',views.API_Get_Score.as_view(),name='api_getScore'),
    path('api_getQuestionTF/<makt>', views.API_Get_Question_True_False.as_view(), name='api_getQuestionTF'),
    path('api_get_lop_baikt/', views.API_Get_Lop_BaiKT.as_view(), name='api_get_lop_baikt'),
    
    #==========================Login/Logout=========================
    path('login/',auth_views.LoginView.as_view(template_name='login/login.html', authentication_form=LoginForm),name='login'),
    
    path('change-password/',auth_views.PasswordChangeView.as_view(template_name='login/changepassword.html',form_class=MyPasswordChangeForm,success_url='/passwordchangedone'),name='change_password'),

    path('passwordchangedone/',auth_views.PasswordChangeDoneView.as_view(template_name='login/changepassworddone.html'),name='password_change_done'),

    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='login/resetPassword.html',form_class=MyPasswordResetForm),name='password_reset'),

    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='login/resetPasswordDone.html'),name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='login/resetPasswordConfirm.html',form_class=MySetPasswordForm),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='login/resetPasswordComplete.html'),name='password_reset_complete'),

    path("logout_user",views.logout_user,name="logout_user"),

]
