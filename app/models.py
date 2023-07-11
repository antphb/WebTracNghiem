# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Bai(models.Model):
    mabai = models.TextField(db_column='MaBai', primary_key=True)  # Field name made lowercase.
    tenbai = models.TextField(db_column='TenBai', blank=True, null=True)  # Field name made lowercase.
    machuong = models.ForeignKey('Chuong', models.DO_NOTHING, db_column='MaChuong')  # Field name made lowercase.

    class Meta:
        # set id = false
        managed = False
        db_table = 'Bai'


class Baikiemtra(models.Model):
    makt = models.TextField(db_column='MaKT', primary_key=True)  # Field name made lowercase.
    tenkt = models.TextField(db_column='TenKT', blank=True, null=True)  # Field name made lowercase.
    monkt = models.TextField(db_column='MonKT', blank=True, null=True)  # Field name made lowercase.
    ngaylambai= models.TextField(db_column='NgayLamBai', blank=True, null=True)  # Field name made lowercase.
    giolambai= models.TextField(db_column='GioLamBai', blank=True, null=True)  # Field name made lowercase.
    thoigian = models.TextField(db_column='ThoiGian', blank=True, null=True)  # Field name made lowercase.
    socauhoi = models.IntegerField(db_column='SoCauHoi', blank=True, null=True)  # Field name made lowercase.
    trangthai = models.BooleanField(db_column='TrangThai', blank=True, null=True)  # Field name made lowercase.
    lopkt = models.TextField(db_column='LopKT', blank=True, null=True)  # Field name made lowercase.
    solanthi= models.IntegerField(db_column='SoLanThi', blank=True, null=True)  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name msade lowercase.
    matkhaubkt = models.TextField(db_column='MatKhauBKT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BaiKiemTra'


class Cauhoi(models.Model):
    macauhoi = models.TextField(db_column='MaCauHoi', primary_key=True)  # Field name made lowercase.
    noidung = models.TextField(db_column='NoiDung', blank=True, null=True)  # Field name made lowercase.
    dapana = models.TextField(db_column='DapAnA', blank=True, null=True)  # Field name made lowercase.
    dapanb = models.TextField(db_column='DapAnB', blank=True, null=True)  # Field name made lowercase.
    dapanc = models.TextField(db_column='DapAnC', blank=True, null=True)  # Field name made lowercase.
    dapand = models.TextField(db_column='DapAnD', blank=True, null=True)  # Field name made lowercase.
    dapandung = models.TextField(db_column='DapAnDung', blank=True, null=True)  # Field name made lowercase.
    mucdo = models.TextField(db_column='MucDo', blank=True, null=True)  # Field name made lowercase.
    machitiet = models.ForeignKey('ChitietMonChuongBai', models.DO_NOTHING, db_column='MaChiTiet')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CauHoi'


class Cauhoikiemtra(models.Model):
    machkt = models.TextField(db_column='MaCHKT', primary_key=True)  # Field name made lowercase.
    cauhoi_macauhoi = models.ForeignKey(Cauhoi, models.DO_NOTHING, db_column='CauHoi_MaCauHoi')  # Field name made lowercase.
    makt = models.ForeignKey(Baikiemtra, models.DO_NOTHING, db_column='MaKT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CauHoiKiemTra'


class Chitiedapancauhoi(models.Model):
    malsch = models.TextField(db_column='MaLSCH', primary_key=True)  # Field name made lowercase.
    machkt = models.ForeignKey(Cauhoikiemtra, models.DO_NOTHING, db_column='MaCHKT')  # Field name made lowercase.
    mals = models.ForeignKey('Lichsukiemtra', models.DO_NOTHING, db_column='MaLS')  # Field name made lowercase.
    dapantraloi = models.TextField(db_column='DapAnTraLoi', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ChiTieDapAnCauHoi'


class Chitietmonhoc(models.Model):
    malop = models.ForeignKey('Lophoc', models.DO_NOTHING, db_column='MaLop')  # Field name made lowercase.
    mamon = models.ForeignKey('Monhoc', models.DO_NOTHING, db_column='MaMon')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ChiTietMonHoc'


class ChitietMonChuongBai(models.Model):
    machitiet = models.TextField(db_column='MaChiTiet', primary_key=True)  # Field name made lowercase.
    mamon = models.ForeignKey('Monhoc', models.DO_NOTHING, db_column='MaMon', blank=True, null=True)  # Field name made lowercase.
    machuong = models.ForeignKey('Chuong', models.DO_NOTHING, db_column='MaChuong', blank=True, null=True)  # Field name made lowercase.
    mabai = models.ForeignKey(Bai, models.DO_NOTHING, db_column='MaBai', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ChiTiet_Mon_Chuong_Bai'


class Chuong(models.Model):
    machuong = models.TextField(db_column='MaChuong', primary_key=True)  # Field name made lowercase.
    tenchuong = models.TextField(db_column='TenChuong')  # Field name made lowercase.
    mamon = models.ForeignKey('Monhoc', models.DO_NOTHING, db_column='MaMon')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Chuong'


class Hocsinh(models.Model):
    mahs = models.TextField(db_column='MaHS', primary_key=True)  # Field name made lowercase.
    tenhs = models.TextField(db_column='TenHS', blank=True, null=True)  # Field name made lowercase.
    lophoc = models.ForeignKey('Lophoc', models.DO_NOTHING, db_column='LopHoc', blank=True, null=True)  # Field name made lowercase.
    email = models.TextField(db_column='Email', blank=True, null=True)  # Field name made lowercase.
    sdt = models.TextField(db_column='Sdt', blank=True, null=True)  # Field name made lowercase.
    matkhau= models.TextField(db_column='Matkhau', blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'HocSinh'


class Lichsukiemtra(models.Model):
    mals = models.TextField(db_column='MaLS', primary_key=True)  # Field name made lowercase.
    mahs = models.ForeignKey(Hocsinh, models.DO_NOTHING, db_column='MaHS')  # Field name made lowercase.
    makt = models.ForeignKey(Baikiemtra, models.DO_NOTHING, db_column='MaKT')  # Field name made lowercase.
    diem = models.TextField(db_column='Diem', blank=True, null=True)  # Field name made lowercase.
    thoigianlambai = models.TextField(db_column='ThoiGianLamBai', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LichSuKiemTra'


class Lophoc(models.Model):
    malop = models.TextField(db_column='MaLop', primary_key=True)  # Field name made lowercase.
    tenlop = models.TextField(db_column='TenLop', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LopHoc'


class Monhoc(models.Model):
    mamon = models.TextField(db_column='MaMon', primary_key=True)  # Field name made lowercase.
    tenmon = models.TextField(db_column='TenMon', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MonHoc'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
