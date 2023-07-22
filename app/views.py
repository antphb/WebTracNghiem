import datetime
import statistics
from django.shortcuts import redirect, render
from django.views import View
from .models import *
import math
import ast
from django.http import HttpResponseRedirect
import random
import string
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import datetime



# Create your views here.
def generate_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))

time_test={
    '15P': '15:00',
    '30P': '30:00',
    '45P': '45:00',
    '60P': '60:00',
    '90P': '90:00',
    '120P': '120:00',
    '150P': '150:00',
    '180P': '180:00',
}

def get_user_class(request):
    try:
        user=request.user.username
        lophoc= Hocsinh.objects.get(mahs=request.user).lophoc.malop
    except:
        user=request
        lophoc=Hocsinh.objects.get(mahs=request).lophoc.malop
    return user,lophoc



def base(request):
    return render(request,'app/base.html')

class home(View):
    def get(self,request):
        if request.user.is_superuser:
            soluongCauhoi= Cauhoi.objects.count()
            soluongLopHoc= Lophoc.objects.count()
            soLuongBaiKt= Baikiemtra.objects.count()
        
            return render(request,'app/home.html',locals())
        else:
            
            user=request.user.username
            lophoc= Hocsinh.objects.get(mahs=request.user).lophoc.malop
            url= f'/DanhSachCauHoiHocSinh/{lophoc}={user}'
            return redirect(url)

def MakeTest(nb,th,vd,vdc,ds_cauhoi,socauhoi):
    ds_cauhoi_nhanbiet= ds_cauhoi.filter(mucdo='Nhận biết')
    ds_cauhoi_thonghieu= ds_cauhoi.filter(mucdo='Thông hiểu')
    ds_cauhoi_vandung= ds_cauhoi.filter(mucdo='Vận dụng')
    ds_cauhoi_vandungcao= ds_cauhoi.filter(mucdo='Vận dụng cao')
    pctNB= socauhoi*float(nb)/100
    pctTH= socauhoi*float(th)/100
    pctVD= socauhoi*float(vd)/100
    pctVDC = socauhoi*float(vdc)/100
    list_cauhoi_nhanbiet=random.sample(list(ds_cauhoi_nhanbiet),k=math.floor(pctNB))
    list_cauhoi_thonghieu=random.sample(list(ds_cauhoi_thonghieu),k=math.floor(pctTH))
    list_cauhoi_vandung=random.sample(list(ds_cauhoi_vandung),k=math.floor(pctVD))
    list_cauhoi_vandungcao=random.sample(list(ds_cauhoi_vandungcao),k=math.ceil(pctVDC))
    list_cauhoi= list_cauhoi_nhanbiet+list_cauhoi_thonghieu+list_cauhoi_vandung+list_cauhoi_vandungcao
    if len(list_cauhoi)<socauhoi:
        list_cauhoi_vandungcao_new=random.sample(list(ds_cauhoi_vandungcao),k=socauhoi-len(list_cauhoi))
        list_cauhoi= list_cauhoi_nhanbiet+list_cauhoi_thonghieu+list_cauhoi_vandung+list_cauhoi_vandungcao+list_cauhoi_vandungcao_new
    
    # print(len(list_cauhoi))
    return list_cauhoi

class listTest(View):
    def get(self,request):
        List_bai_kiem_tra= Baikiemtra.objects.all()
        checkma_de_thi= True
        maDeThi_add=''
        while checkma_de_thi:
            maDeThi_add= generate_random_string(8)
            if Baikiemtra.objects.filter(makt=maDeThi_add).count()==0:
                checkma_de_thi= False
        dsmon= Monhoc.objects.all()
        dsthoigian=time_test.values() 
        dslh= Lophoc.objects.all()
        dschuong= Chuong.objects.all()
        # print(dsmon)
        return render(request,'app/ListTest.html',locals())
    def post(self,request):
        made= request.POST['made']
        tende= request.POST['tende']
        mamonKT= request.POST['mamonKT']
        malopKT= request.POST['malopKT']
        ngaylam= request.POST['ngaylam']
        giolam= request.POST['giolam']
        thoigianlam= request.POST['thoigianlam']
        socauhoi= request.POST['socauhoi']
        solanthi= request.POST['solanthi']
        ghichu= request.POST['ghichu']
        noidungKT=request.POST['noidungKT']
        pct_NB=float(request.POST['pct_Nhanbiet'])
        pct_TH=float(request.POST['pct_Thonghieu'])
        pct_VD=float(request.POST['pct_Vandung'])
        pct_VDC=float(request.POST['pct_Vandungcao'])
        list_noidungKT= noidungKT.split('-')
        save_bai_kiem_tra= Baikiemtra(
            makt= made,
            tenkt= tende,
            monkt=Monhoc.objects.get(mamon=mamonKT).tenmon,
            ngaylambai= ngaylam,
            giolambai= giolam,
            thoigian= thoigianlam,
            socauhoi= int(socauhoi),
            trangthai= False,
            lopkt= Lophoc.objects.get(malop=malopKT).tenlop,
            solanthi= int(solanthi),
            ghichu= ghichu,
            matkhaubkt= generate_random_string(8),
        )
        save_bai_kiem_tra.save()
        ds_cauhoi= Cauhoi.objects.select_related('machitiet__machitiet').values(
            'machitiet__mabai','macauhoi','noidung','dapana','dapanb','dapanc','dapand','dapandung','mucdo','machitiet'
        ).filter(machitiet__mabai__in=list_noidungKT)
        
        list_cauhoi_Test= MakeTest(pct_NB,pct_TH,pct_VD,pct_VDC,ds_cauhoi,int(socauhoi))

        for i in list_cauhoi_Test:
            machkt = generate_random_string(8)
            maCHTN= Cauhoi.objects.get(macauhoi=i['macauhoi'])
            madeKT= Baikiemtra.objects.get(makt=made)
            taoCauhoiKT= Cauhoikiemtra(
                machkt= machkt,
                cauhoi_macauhoi= maCHTN,
                makt= madeKT,
            )
            taoCauhoiKT.save()
        return redirect(request.META.get('HTTP_REFERER'))

class delete_test(View):
    def get(self,request,makt):
        cauhikt= Cauhoikiemtra.objects.filter(makt=makt)
        # print(cauhikt)
        for i in cauhikt:
            # print(Chitiedapancauhoi.objects.filter(machkt=i.machkt))
            if Chitiedapancauhoi.objects.filter(machkt=i.machkt).count()>0:
                Chitiedapancauhoi.objects.filter(machkt=i.machkt).delete()
        Cauhoikiemtra.objects.filter(makt=makt).delete()
        Lichsukiemtra.objects.filter(makt=makt).delete()
        Baikiemtra.objects.get(makt=makt).delete()
        return redirect(request.META.get('HTTP_REFERER'))

class changeTrangThai(View):
    def get(self,request,makt,trangthai):
        baikiemtra= Baikiemtra.objects.get(makt=makt)
        if trangthai=='True':
            baikiemtra.trangthai= False
            baikiemtra.save()
        else:
            baikiemtra.trangthai= True
            baikiemtra.save()

        return redirect(request.META.get('HTTP_REFERER'))


class API_getChuong_getBai_byMon(APIView):
    def get(self,request,mamon,lop):
        chuong_lop= lop[:2]
        # print(chuong_lop)
        chuong= Chuong.objects.filter(mamon=mamon,machuong__startswith=chuong_lop)

        json_chuong_bai={}
        for i in range(len(chuong)):
            json_chuong_bai[chuong[i].machuong]={
                'tenchuong': f"Chương {i+1}: {chuong[i].tenchuong}",
                'baihoc':{}
            }
            json_bai={}
            bai=Bai.objects.filter(machuong=chuong[i].machuong)
            for j in bai:
                split_chuong= j.mabai.split('_')
                baiso= split_chuong[2].replace('B','')
                json_bai[j.mabai]=f"Bài {baiso}: {j.tenbai}"
            json_bai= dict(sorted(json_bai.items(),key=lambda x: x[0]))
            json_chuong_bai[chuong[i].machuong]['baihoc']=json_bai
        # json_chuong_bai = dict(sorted(json_chuong_bai.items(),key=lambda x: x[0]))
        return Response(json_chuong_bai)

class API_getBai_byChuong(APIView):
    def get(self,request,machuong):
        bai= Bai.objects.filter(machuong=machuong)
        json_bai={}
        for i in range(len(bai)):
            json_bai[bai[i].mabai]=f"Bài {i+1}: {bai[i].tenbai}"
        # sort lại mã bài 
        json_bai= dict(sorted(json_bai.items(),key=lambda x: x[0]))
        return Response(json_bai)

class listQuesion(View):
    def get(self,request):
        listCauhoi= Cauhoi.objects.select_related('machitiet__mamon','machitiet__machuong','machitiet__mabai').values(
            'machitiet__mamon__tenmon',
            'machitiet__machuong__tenchuong',
            'machitiet__mabai__tenbai',
            'macauhoi','noidung','dapana','dapanb','dapanc','dapand','dapandung','mucdo'
        )
        return render(request,'app/ListQuesion.html',locals())

class listGroupClass(View):
    def get(self,request):
        list_group_class= Lophoc.objects.all()
        ba_socuoi= generate_random_string(3)
        return render(request,'app/ListGroupClass.html',locals())

class addNewStudent(View):
    def post(self,request):
        mhs= request.POST['mhs']
        hoten= request.POST['hoten']
        lophoc= request.POST['lophoc']
        email= request.POST['email']
        sdt= request.POST['sdt']
        hocsinh= Hocsinh(mahs=mhs,tenhs=hoten,lophoc=Lophoc.objects.get(malop=lophoc),email=email,sdt=sdt,matkhau='1111')
        hocsinh.save()
        name_split= hoten.rsplit(' ',1)
        first_name= name_split[1]
        last_name= name_split[0]
        user= User.objects.create_user(username=mhs,password='1111',email=email,first_name=first_name,last_name=last_name,is_staff=False)
        user.save()
        return redirect(request.META.get('HTTP_REFERER')) 

class deleteStudent(View):
    def get(self,request,mhs):
        if Lichsukiemtra.objects.filter(mahs=mhs).count()>0:
            for i in Lichsukiemtra.objects.filter(mahs=mhs):
                for j in Chitiedapancauhoi.objects.filter(mals=i.mals):
                    j.delete()
        Lichsukiemtra.objects.filter(mahs=mhs).delete()
        Hocsinh.objects.get(mahs=mhs).delete()
        User.objects.get(username=mhs).delete()
        return redirect(request.META.get('HTTP_REFERER'))

class listStudent(View):
    def get(self,request,malh):
        list_student= Hocsinh.objects.filter(lophoc=Lophoc.objects.get(malop=malh).malop)
        # print(list_student)
        return render(request,'app/ListStudent.html',locals())

class listScoreStudent(View):
    def get(self,request,makt,mhs):
        # print(makt,mhs)
        if mhs=='all':
            lich_su_kiem_tra= Lichsukiemtra.objects.filter(makt=makt)
        else:
            lich_su_kiem_tra= Lichsukiemtra.objects.filter(makt=makt,mahs=mhs)
        # print(lich_su_kiem_tra)
        return render(request,'app/ListScoreStudent.html',locals())

class listStudentQuesion(View):
    def get(self,request,mlh,mhs):
        today= datetime.date.today()
        gioToday= datetime.datetime.now().time().strftime("%H:%M")
        username,classname=get_user_class(request)
        List_bai_kiem_tra= Baikiemtra.objects.filter(lopkt=mlh)
        l_or_n=[]
        
        soluongbaithi=len(List_bai_kiem_tra)
        for bkt in List_bai_kiem_tra:
            test_ngaylambai=bkt.ngaylambai
            test_giolambai=bkt.giolambai
            test_solanthi=bkt.solanthi==1
            test_thoigiankiemtra=bkt.thoigian.split(':')[0]

            test_thoigianlambai = check_SoLanThi(test_giolambai,test_thoigiankiemtra,test_solanthi)
            # print(test_solanthi)

            if str(today) == test_ngaylambai and test_giolambai<=gioToday<=test_thoigianlambai:
                bkt.trangthai= True
                bkt.save()
            else:
                bkt.trangthai= False
                bkt.save()
            # print(bkt.trangthai)
            List_bai_kiem_tra_test = Lichsukiemtra.objects.filter(mahs=mhs,makt=bkt.makt)
            l_or_n.append(List_bai_kiem_tra_test.count() >= bkt.solanthi)
        baikt_zip= zip(List_bai_kiem_tra,l_or_n)
        return render(request,'app/ListStudentQuesion.html',locals())

class resultTest(View):
    def get(self,request,makt,malskt,mhs):
        if not request.user.is_superuser:
            username,classname=get_user_class(request)
        else:
            username,classname= get_user_class(mhs)
        temp_makt=makt
        temp_malskt=malskt
        lskt_diem_time= Lichsukiemtra.objects.select_related(
            'makt__makt','mahs__mahs').values(
                'mals','mahs__tenhs','mahs__lophoc','mahs__email','mahs__sdt','diem','thoigianlambai'
            ).filter(makt_id=makt,mahs_id=mhs,mals=malskt)
        # print(lskt_diem_time)
        # thông tin trả lời câu hỏi
        lich_su_kiem_tra= Lichsukiemtra.objects.select_related(
            'mahs__mahs','mals__mals','machkt__machkt','cauhoi_macauhoi__macauhoi'
        ).values(
            'chitiedapancauhoi__machkt__cauhoi_macauhoi',
            'chitiedapancauhoi__dapantraloi',
            'chitiedapancauhoi__machkt__cauhoi_macauhoi__dapandung',
            'chitiedapancauhoi__machkt__cauhoi_macauhoi__mucdo',
            'chitiedapancauhoi__machkt__cauhoi_macauhoi__machitiet__mamon__tenmon',
            'chitiedapancauhoi__machkt__cauhoi_macauhoi__machitiet__machuong__tenchuong',
            'chitiedapancauhoi__machkt__cauhoi_macauhoi__machitiet__mabai__tenbai',
        ).filter(makt_id=makt,mahs_id=mhs,mals=malskt)
        # print(lich_su_kiem_tra)
        soluongCauhoi= len(lich_su_kiem_tra)
        socauDung=0
        mucdo={
            'Nhận biết': [],
            'Thông hiểu': [],
            'Vận dụng': [],
            'Vận dụng cao': [],
        }
        for i in lich_su_kiem_tra:
            if i['chitiedapancauhoi__dapantraloi'] == i['chitiedapancauhoi__machkt__cauhoi_macauhoi__dapandung']:
                socauDung+=1
            else:
                mucdo[i['chitiedapancauhoi__machkt__cauhoi_macauhoi__mucdo']].append(i)
        new_mucdo={}
        chitietcausai=[]
        for key,value in mucdo.items():
            if len(value) > 0:
                new_mucdo[key]=value
                chitietcausai.extend(value)
        new_chitietcausai=[]
        for i in chitietcausai:
            split_ma= i['chitiedapancauhoi__machkt__cauhoi_macauhoi'].split('_')
            lop="Lớp "+split_ma[2]
            chuong=split_ma[3].replace('C','Chương ')+': '+i['chitiedapancauhoi__machkt__cauhoi_macauhoi__machitiet__machuong__tenchuong']
            bai=split_ma[4].replace('B','Bài ')+': '+i['chitiedapancauhoi__machkt__cauhoi_macauhoi__machitiet__mabai__tenbai']

            mucdo_c= i['chitiedapancauhoi__machkt__cauhoi_macauhoi__mucdo']
            
            nchitiet={
                'lop':lop,
                'chuong':chuong,
                'bai':bai,
                'mucdo':mucdo_c,
            }
            new_chitietcausai.append(nchitiet)
        new_chitietBaiHoc=[]
        for i in new_chitietcausai:
            xyz=[]
            for j in new_chitietcausai:
                if j['chuong']==i['chuong'] and j['mucdo']==i['mucdo']:
                    xyz.append(j['bai'])
            if xyz not in [i['bai'] for i in new_chitietBaiHoc]:
                chitietBaiHoc={
                    'lop':i['lop'],
                    'chuong':i['chuong'],
                    'bai':xyz,
                    'mucdo':i['mucdo'],
                }
                new_chitietBaiHoc.append(chitietBaiHoc)
        new_chitietBaiHoc_V2=[]
        for i in new_chitietBaiHoc:
            bai_tung_chuong=[]
            for j in i['bai']:
                if j not in bai_tung_chuong:
                    bai_tung_chuong.append(j)
            new_chitietBaiHoc_V2.append({
                'lop':i['lop'],
                'chuong':i['chuong'],
                'bai':bai_tung_chuong,
                'mucdo':i['mucdo'],
            })
        return render(request,'app/ResultTest.html',locals())


def check_SoLanThi(test_giolambai,test_thoigiankiemtra,is1Lan):
    if is1Lan == True:
        if int(test_thoigiankiemtra) < 60:
            test_thoigianlambaiKT= datetime.timedelta(minutes=int(test_thoigiankiemtra)) + datetime.datetime.strptime(test_giolambai, "%H:%M")
        else:
            hour= int(test_thoigiankiemtra)//60
            minute= int(test_thoigiankiemtra)%60
            test_thoigianlambaiKT= datetime.timedelta(hours=hour,minutes=minute) + datetime.datetime.strptime(test_giolambai, "%H:%M")
        test_thoigianlambaiKT= test_thoigianlambaiKT.strftime("%H:%M")
        return test_thoigianlambaiKT
    else:
        if int(test_thoigiankiemtra) < 60:
            test_thoigianlambaiKT= datetime.timedelta(minutes=int(test_thoigiankiemtra)) + datetime.datetime.now()
        else:
            hour= int(test_thoigiankiemtra)//60
            minute= int(test_thoigiankiemtra)%60
            test_thoigianlambaiKT= datetime.timedelta(hours=hour,minutes=minute) + datetime.datetime.now()
        test_thoigianlambaiKT= test_thoigianlambaiKT.strftime("%H:%M")
        return test_thoigianlambaiKT

class listStudentLamBai(View):
    def get(self,request,makt):
        username,classname=get_user_class(request)
        list_cauhoiKiemTra=Cauhoikiemtra.objects.select_related('cauhoi_macauhoi__macauhoi','makt__makt').values(
            'cauhoi_macauhoi__macauhoi','makt__makt','makt__tenkt','makt__thoigian','makt__giolambai','makt__solanthi',
            'cauhoi_macauhoi__noidung','cauhoi_macauhoi__dapana','cauhoi_macauhoi__dapanb','cauhoi_macauhoi__dapanc','cauhoi_macauhoi__dapand','cauhoi_macauhoi__dapandung','cauhoi_macauhoi__mucdo'
        ).filter(makt__makt=makt).order_by('?')
        # print(list_cauhoiKiemTra[0])           
        # print(list_cauhoiKiemTra)
        test_giolambai=list_cauhoiKiemTra[0]['makt__giolambai']
        test_thoigiankiemtra=list_cauhoiKiemTra[0]['makt__thoigian'].split(':')[0]
        test_soLanthi=list_cauhoiKiemTra[0]['makt__solanthi']==1
        test_thoigianlambaiKT=check_SoLanThi(test_giolambai,test_thoigiankiemtra,test_soLanthi)

        socauhoi= [i for i in range(len(list_cauhoiKiemTra))]
        soCot=[i for i in range(4)]
        soHang=[i for i in range(math.ceil(len(list_cauhoiKiemTra)/len(soCot)))]
        socauhoi_list=zip(socauhoi,list_cauhoiKiemTra)
        malskt=generate_random_string(8)
        return render(request,'app/ListStudentLamBai.html',locals())
    
    def post(self,request,makt):
        score=0
        ma_de_thi= makt
        ma_hs= request.POST['maHS']
        thoi_gian_kiem_tra=request.POST['time_kiem_tra']
        thoi_gian_lam_bai=request.POST['time_student_done']
        dap_an_tra_loi=request.POST['dap_an_tra_loi']
        ma_lskt= request.POST['ma_lskt']

        list_cauhoiKiemTra=Cauhoikiemtra.objects.select_related('cauhoi_macauhoi__macauhoi','makt__makt').values(
            'machkt',
            'cauhoi_macauhoi__macauhoi',
            'cauhoi_macauhoi__dapandung'
        ).filter(makt__makt=makt)

        soLgCauHoi= len(list_cauhoiKiemTra)
        scoreOne= 10/soLgCauHoi

        dap_an_tra_loi_LSKT={}
        dap_an_tra_loi_json=ast.literal_eval(dap_an_tra_loi)
        for i in list_cauhoiKiemTra:
            key=i['cauhoi_macauhoi__macauhoi']
            dap_an_dung=i['cauhoi_macauhoi__dapandung']
            try:
                dap_an_tra_loi_LSKT[key]=dap_an_tra_loi_json[key]
                if dap_an_tra_loi_json[key]==dap_an_dung:
                    score+=scoreOne
            except:
                dap_an_tra_loi_LSKT[key]=''

        thoigian_lam_bai_pro=int(thoi_gian_kiem_tra)-int(thoi_gian_lam_bai)/60

        hocsinh= Hocsinh.objects.get(mahs=ma_hs)
        bai_kiem_tra=Baikiemtra.objects.get(makt=ma_de_thi)
        check_lskt= Lichsukiemtra.objects.filter(mahs=ma_hs,makt=ma_de_thi)
        solanthi = bai_kiem_tra.solanthi
        if len(check_lskt)<=solanthi:
            lich_su_kiem_tra= Lichsukiemtra(ma_lskt,ma_hs,ma_de_thi,round(score,2),thoigian_lam_bai_pro)
            lich_su_kiem_tra.save()
            for i in list_cauhoiKiemTra:
                maLSCH= generate_random_string(8)
                chi_tiet_dapan_cauhoi=Chitiedapancauhoi(maLSCH,i['machkt'],ma_lskt,dap_an_tra_loi_LSKT[i['cauhoi_macauhoi__macauhoi']])
                chi_tiet_dapan_cauhoi.save()
        return redirect(request.META.get('HTTP_REFERER')) 
    
class detailResultTest(View):
    def get(self,request,makt,malskt,mhs):
        if not request.user.is_superuser:
            username,classname=get_user_class(request)
        makt_de_thi= makt
        lich_su_kiem_tra= Lichsukiemtra.objects.select_related(
            'mahs__mahs','mals__mals','machkt__machkt','cauhoi_macauhoi__macauhoi'
        ).values(
            'mals',
            'chitiedapancauhoi__machkt__cauhoi_macauhoi',
            'chitiedapancauhoi__dapantraloi',
            'chitiedapancauhoi__machkt__cauhoi_macauhoi__noidung',
            'chitiedapancauhoi__machkt__cauhoi_macauhoi__dapana',
            'chitiedapancauhoi__machkt__cauhoi_macauhoi__dapanb',
            'chitiedapancauhoi__machkt__cauhoi_macauhoi__dapanc',
            'chitiedapancauhoi__machkt__cauhoi_macauhoi__dapand',
            'chitiedapancauhoi__machkt__cauhoi_macauhoi__dapandung',
            'chitiedapancauhoi__machkt__cauhoi_macauhoi__mucdo',
        ).filter(makt_id=makt,mahs_id=mhs,mals=malskt)

        # print(lich_su_kiem_tra)
        socauhoi= [i for i in range(len(lich_su_kiem_tra))]
        soCot=[i for i in range(4)]
        soHang=[i for i in range(math.ceil(len(lich_su_kiem_tra)/len(soCot)))]
        socauhoi_list=zip(socauhoi,lich_su_kiem_tra)
        compare_dapan=[i['chitiedapancauhoi__dapantraloi']==i['chitiedapancauhoi__machkt__cauhoi_macauhoi__dapandung'] for i in lich_su_kiem_tra]
        # print(compare_dapan)
        # print(lich_su_kiem_tra[0])
        return render(request,'app/DetailResultTest.html',locals())

class detailTest(View):
    def get(self,request,makt):
        makt_de_thi= makt
        list_cauhoiKiemTra=Cauhoikiemtra.objects.select_related('cauhoi_macauhoi__macauhoi','makt__makt').values(
            'cauhoi_macauhoi__macauhoi','makt__makt','makt__tenkt','makt__thoigian','makt__giolambai','makt__solanthi',
            'cauhoi_macauhoi__noidung','cauhoi_macauhoi__dapana','cauhoi_macauhoi__dapanb','cauhoi_macauhoi__dapanc','cauhoi_macauhoi__dapand','cauhoi_macauhoi__dapandung','cauhoi_macauhoi__mucdo'
        ).filter(makt__makt=makt)

        # print(lich_su_kiem_tra)
        socauhoi= [i for i in range(len(list_cauhoiKiemTra))]
        soCot=[i for i in range(4)]
        soHang=[i for i in range(math.ceil(len(list_cauhoiKiemTra)/len(soCot)))]
        socauhoi_list=zip(socauhoi,list_cauhoiKiemTra)
        compare_dapan=[True]*len(list_cauhoiKiemTra)

        return render(request,'app/DetailTest.html',locals())

class printTestPDF(View):
    def get(self,request,makt):
        list_cauhoiKiemTra=Cauhoikiemtra.objects.select_related('cauhoi_macauhoi__macauhoi','makt__makt').values(
            'cauhoi_macauhoi__macauhoi','makt__makt','makt__tenkt','makt__lopkt','makt__thoigian','makt__giolambai','makt__solanthi',
            'cauhoi_macauhoi__noidung','cauhoi_macauhoi__dapana','cauhoi_macauhoi__dapanb','cauhoi_macauhoi__dapanc','cauhoi_macauhoi__dapand','cauhoi_macauhoi__dapandung','cauhoi_macauhoi__mucdo'
        ).filter(makt__makt=makt).order_by('?')
        # print(list_cauhoiKiemTra[0])           
        # print(list_cauhoiKiemTra)
        test_thoigiankiemtra=list_cauhoiKiemTra[0]['makt__thoigian'].split(':')[0]
        lopkiemtra=list_cauhoiKiemTra[0]['makt__lopkt']
        tende=list_cauhoiKiemTra[0]['makt__tenkt']
        socauhoi= [i for i in range(len(list_cauhoiKiemTra))]
        soCot=[i for i in range(10)]
        soHang=[i for i in range(math.ceil(len(list_cauhoiKiemTra)/len(soCot)))]
        # print(list_cauhoiKiemTra[0])
        dapandung=[]
        for i in list_cauhoiKiemTra:
            if i['cauhoi_macauhoi__dapana'] == i['cauhoi_macauhoi__dapandung']:
                dapandung.append('A')
            elif i['cauhoi_macauhoi__dapanb'] == i['cauhoi_macauhoi__dapandung']:
                dapandung.append('B')
            elif i['cauhoi_macauhoi__dapanc'] == i['cauhoi_macauhoi__dapandung']:
                dapandung.append('C')
            elif i['cauhoi_macauhoi__dapand'] == i['cauhoi_macauhoi__dapandung']:
                dapandung.append('D')
            else:
                dapandung.append('A')
        # print(dapandung)
        socauhoi_list=zip(socauhoi,list_cauhoiKiemTra)
        madethikiemtra=generate_random_string(3)
        return render(request,'app/PrintTest.html',locals())

class StatisticResultTest(View):
    def get(self,request):
        return render(request,'app/StatisticResultTest.html',locals())

class API_Get_Score(APIView):
    def get(self,request,makt):
        list_lskt= Lichsukiemtra.objects.filter(makt=makt)
        list_score= {}
        list_score['mahs']= []
        list_score['tenhs']= []
        list_score['diemhs']= []
        list_score['diemTB']= 0
        list_score['diemTrungVi']= 0
        list_score['range']= 0
        list_score['top5DiemCao']=[]
        list_score['top5DiemThap']=[]
        if len(list_lskt)!=0:
            list_score['diemTB']= round(sum([float(i.diem) for i in list_lskt])/len(list_lskt),2)
            list_score['diemTrungVi']= round(statistics.median([float(i.diem) for i in list_lskt]),2)
            list_score['range']= "-".join([str(min([float(i.diem) for i in list_lskt])),str(max([float(i.diem) for i in list_lskt]))])
            list_diem_hoten= [[i.diem,i.mahs.tenhs] for i in list_lskt]
            list_diem_hoten.sort(key=lambda x: x[0],reverse=True)
            list_score['top5DiemCao']=list_diem_hoten[:5]
            list_score['top5DiemThap']=(list_diem_hoten[-5:])
            list_score['top5DiemThap'].reverse()
            for i in list_lskt:
                list_score['mahs'].append(i.mahs.mahs)
                list_score['tenhs'].append(i.mahs.tenhs)
                list_score['diemhs'].append(i.diem)
        
        return Response(list_score)

class API_Get_Question_True_False(APIView):
    def get(self,request,makt):
        baikiemtra= Baikiemtra.objects.select_related(
            'makt__makt','cauhoi_macauhoi__macauhoi'
        ).values(
            'cauhoikiemtra__cauhoi_macauhoi','cauhoikiemtra__cauhoi_macauhoi__noidung',
        ).filter(makt=makt)
        # print(baikiemtra)
        Cau_i_Cauhoi= [f"Câu {i+1}" for i in range(len(baikiemtra))]
        maCauhoi= [i['cauhoikiemtra__cauhoi_macauhoi'] for i in baikiemtra]
        noidungCauhoi= [i['cauhoikiemtra__cauhoi_macauhoi__noidung'] for i in baikiemtra]
        dict_dapandungtungcau= {i['cauhoikiemtra__cauhoi_macauhoi']:0 for i in baikiemtra}
        # print(dict_dapandungtungcau)
        dict_dapansaitungcau= {i['cauhoikiemtra__cauhoi_macauhoi']:0 for i in baikiemtra}
        dict_cauhoi= {
            'cau':Cau_i_Cauhoi,
            'maCauHoi':maCauhoi,
            'noiDungCauHoi':noidungCauhoi,
            'dapandungtungcau':dict_dapandungtungcau,
            'dapansaitungcau':dict_dapansaitungcau,
        }
        lich_su_kiem_tra= Lichsukiemtra.objects.select_related(
            'mahs__mahs','mals__mals','machkt__machkt','cauhoi_macauhoi__macauhoi'
        ).values(
            'chitiedapancauhoi__machkt__cauhoi_macauhoi',
            'chitiedapancauhoi__dapantraloi',
            'chitiedapancauhoi__machkt__cauhoi_macauhoi__dapandung',
        ).filter(makt_id=makt)

        for i in lich_su_kiem_tra:
            if i['chitiedapancauhoi__dapantraloi']==i['chitiedapancauhoi__machkt__cauhoi_macauhoi__dapandung']:
                dict_cauhoi['dapandungtungcau'][i['chitiedapancauhoi__machkt__cauhoi_macauhoi']]+=1
            else:
                dict_cauhoi['dapansaitungcau'][i['chitiedapancauhoi__machkt__cauhoi_macauhoi']]+=1
        return Response(dict_cauhoi)

class API_Get_Lop_BaiKT(APIView):
    def get(self,request):
        baiKT= Baikiemtra.objects.all()
        return Response(baiKT.values('makt','tenkt','lopkt'))

def logout_user(request):
    logout(request)
    return redirect('login')
