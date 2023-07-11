from django.contrib import admin

# Register your models here.

from .models import *

# @admin.register(Bai)
# class BaiModelAdmin(admin.ModelAdmin):
#     list_display = ['mabai','mabai','machuong']

# admin.site.register(Baikiemtra)

@admin.register(Cauhoi)
class CauhoiModelAdmin(admin.ModelAdmin):
    list_display = ['macauhoi','noidung','dapana','dapanb','dapanc','dapand','dapandung','mucdo']

@admin.register(Bai)
class BaiModelAdmin(admin.ModelAdmin):
    list_display = ['mabai','tenbai','machuong']

@admin.register(Chuong)
class ChuongModelAdmin(admin.ModelAdmin):
    list_display = ['machuong','tenchuong','mamon']

@admin.register(Baikiemtra)
class BaikiemtraModelAdmin(admin.ModelAdmin):
    list_display = ['makt','tenkt','matkhaubkt','monkt','thoigian','socauhoi','trangthai','lopkt','ghichu']

@admin.register(Cauhoikiemtra)
class CauhoikiemtraModelAdmin(admin.ModelAdmin):
    list_display = ['machkt','cauhoi_macauhoi','makt']

@admin.register(Chitiedapancauhoi)
class ChitiedapancauhoiModelAdmin(admin.ModelAdmin):
    list_display = ['malsch','machkt','mals','dapantraloi']

@admin.register(Chitietmonhoc)
class ChitietmonhocModelAdmin(admin.ModelAdmin):
    list_display = ['malop','mamon']

@admin.register(ChitietMonChuongBai)
class ChitietMonChuongBaiModelAdmin(admin.ModelAdmin):
    list_display = ['machitiet','mamon','machuong','mabai']

@admin.register(Hocsinh)
class HocsinhModelAdmin(admin.ModelAdmin):
    list_display = ['mahs','tenhs','lophoc','email','sdt']

@admin.register(Lichsukiemtra)
class LichsukiemtraModelAdmin(admin.ModelAdmin):
    list_display = ['mals','mahs','makt','diem','thoigianlambai']

@admin.register(Lophoc)
class LophocModelAdmin(admin.ModelAdmin):
    list_display = ['malop','tenlop']

@admin.register(Monhoc)
class MonhocModelAdmin(admin.ModelAdmin):
    list_display = ['mamon','tenmon']