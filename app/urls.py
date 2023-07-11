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
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('',views.base,name='base'),
    path('',views.home.as_view(),name='home'),
    path("DanhSachDeThi/",views.listTest.as_view(), name="listTest"),
    path("DanhSachCauHoi/",views.listQuesion.as_view(), name="listQuesion"),
    path("DanhSachLopHoc/",views.listGroupClass.as_view(), name="listGroupClass"),
    path("DanhSachHocSinh/<malh>",views.listStudent.as_view(), name="listStudent"),
    path("DanhSachDiemThi/<makt>=<mhs>",views.listScoreStudent.as_view(), name="listScoreStudent"),
    path("DanhSachCauHoiHocSinh/<mlh>=<mhs>",views.listStudentQuesion.as_view(), name="listStudentQuesion"),
    path("DanhSachLamBaiHocSinh/<makt>",views.listStudentLamBai.as_view(), name="listStudentLamBai"),
    path("DiemThiHocSinh/<makt>=<malskt>/<mhs>",views.resultTest.as_view(), name="resultTest"),
    path("Dapanchitiet/<makt>=<malskt>/<mhs>",views.detailResultTest.as_view(), name="detailResultTest"),
    #===========================Edit/ADD============================
    path("deleteTest/<makt>", views.delete_test.as_view(), name="delete_test"),
    path("changeTrangThai/<makt>-<trangthai>", views.changeTrangThai.as_view(), name="changeTrangThai"),
    path("addNewStudent/", views.addNewStudent.as_view(), name="addNewStudent"),
    #===========================API View============================
    path('api_chuong/<mamon>-<lop>',views.API_getChuong_getBai_byMon.as_view(),name='api_chuong_mon'),
    path('api_bai/<machuong>',views.API_getBai_byChuong.as_view(),name='api_bai_chuong'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
