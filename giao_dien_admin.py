
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QDialog,QApplication, QWidget, QToolTip, QPushButton, QMessageBox) 
from PyQt5.QtGui import QIcon
import sys
from PyQt5.QtCore import QCoreApplication, Qt
import  sys
import cx_Oracle
conn = cx_Oracle.connect('DOAN3/123@//localhost:1521/xe') 
class Ui_MainWindow(QDialog):
####################################################function for tab Sinh Vien##################################################
    def closeEvent(self, event):
        reply = QMessageBox.question(
            self, "Message",
            "Are you sure you want to quit? Any unsaved work will be lost.",
            QMessageBox.Close | QMessageBox.Cancel)
        if reply == QMessageBox.Close:
            app.quit()
        else:
            pass
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()
    def display_1(self):
        self.listWidget_3.clear()
        mysearch = conn.cursor()
        search= "select * from DOAN3.SINH_VIEN"
        mysearch.execute(search)
        data = mysearch.fetchall()
        m=[]
        for x in data:
            m=x
        so_sv = len(data)
        print(data)
        i = 0
        while i < so_sv:
            stu_info=data[i]
            stu_info = list(stu_info)
            i += 1 
            if stu_info[0] == None:
                stu_info[0]='-None-'
            if stu_info[1] == None:
                stu_info[1]='-None-'
            if stu_info[2] == None:
                stu_info[2]='-None-'
            if stu_info[3] == None:
                stu_info[3]='-None-'
            if stu_info[4] == None:
                stu_info[4]='-None-'
            if stu_info[5] == None:
                stu_info[5]='-None-'
            if stu_info[6] == None:
                stu_info[6]='-None-'    
            stu_info = str(stu_info[0]+'  '+stu_info[1]+'   '+stu_info[2]+'   '+stu_info[3]+'   '+stu_info[4]+'   '+stu_info[5]+'   '+stu_info[6])
            self.listWidget_3.addItem(stu_info)
            self.listWidget_3.setCurrentRow(0)

    def search(self):
        self.listWidget_3.clear()
        id_msv=self.lineEdit.text()        
        sv_ten=self.lineEdit_2.text()        
        ngay_sinh=self.lineEdit_3.text()        
        gioi_tinh=self.lineEdit_4.text()    
        dia_chi=self.lineEdit_5.text()        
        id_lnc=self.lineEdit_6.text()        
        nganh_hoc=self.lineEdit_7.text()
        id_msv=str("%"+id_msv+"%") 
        print(id_msv)
        sv_ten=str("%"+sv_ten+"%") 
        ngay_sinh=str(ngay_sinh)
        gioi_tinh=str("%"+gioi_tinh+"%")
        dia_chi=str(dia_chi)
        id_lnc=str(id_lnc) 
        nganh_hoc=str("%"+nganh_hoc+"%")
        rows = (id_msv, sv_ten, ngay_sinh, gioi_tinh, dia_chi, id_lnc, nganh_hoc)
        
        if len(id_msv)>2:
            # conn = cx_Oracle.connect('DOAN3/123@//localhost:1521/xe') 
            mysearch = conn.cursor()
            search = "select * from DOAN3.SINH_VIEN where lower(id_msv) LIKE lower(:id_msv1)"
            mysearch.execute(search,id_msv1=id_msv)
            data = mysearch.fetchall()   
        elif len(sv_ten)>2:
            conn1 = cx_Oracle.connect('DOAN3/123@//localhost:1521/xe') 
            mysearch2 = conn1.cursor()
            search2= "select * from DOAN3.SINH_VIEN where lower(sv_ten) LIKE lower(:sv_ten1)"
            mysearch2.execute(search2,sv_ten1=sv_ten)
            data = mysearch2.fetchall()
        elif len(gioi_tinh)>2:
            conn2 = cx_Oracle.connect('DOAN3/123@//localhost:1521/xe') 
            mysearch3 = conn2.cursor()
            search3= "select * from DOAN3.SINH_VIEN where lower(gioi_tinh) LIKE lower(:gioi_tinh1)"
            mysearch3.execute(search3,gioi_tinh1=gioi_tinh)
            data = mysearch3.fetchall()
        elif len(nganh_hoc)>3:
            conn3 = cx_Oracle.connect('DOAN3/123@//localhost:1521/xe') 
            mysearch4 = conn3.cursor()
            search4= "select * from DOAN3.SINH_VIEN where lower(nganh_hoc) LIKE lower(:nganh_hoc1)"
            mysearch4.execute(search4,nganh_hoc1=nganh_hoc)
            data = mysearch4.fetchall()
        else:
            reply = QMessageBox.question(
            self, "Message",
            "Ban chua nhap, hay nhap di",
            QMessageBox.Close)
            return
        m=[]
        for x in data:
            m=x
        
        so_sv = len(data)
        
        m=list(m)
        if len(data) == 0:
            koco = 'Không có dữ liệu, hãy nhập lại.'
            self.listWidget_3.addItem(koco)
        i = 0
        while i < so_sv:
            stu_info=data[i]
            stu_info = list(stu_info)
            i += 1
            stu_info1 = []
            j = 0      
            if stu_info[0] == None:
                stu_info[0]='None'
            if stu_info[1] == None:
                stu_info[1]='None'
            if stu_info[2] == None:
                stu_info[2]='None'
            if stu_info[3] == None:
                stu_info[3]='None'
            if stu_info[4] == None:
                stu_info[4]='None'
            if stu_info[5] == None:
                stu_info[5]='None'
            if stu_info[6] == None:
                stu_info[6]='None'
            print(stu_info)
            stu_info = str(stu_info[0]+'  '+stu_info[1]+'   '+stu_info[2]+'   '+stu_info[3]+'   '+stu_info[4]+'   '+stu_info[5]+'   '+stu_info[6])
            self.listWidget_3.addItem(stu_info)
            self.listWidget_3.setCurrentRow(0)
        
    def clear1(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
        self.lineEdit_7.clear()
        self.listWidget_3.clear()
    
    def insert_row(self):
        id_msv=self.lineEdit.text()        
        sv_ten=self.lineEdit_2.text()        
        ngay_sinh=self.lineEdit_3.text()        
        gioi_tinh=self.lineEdit_4.text()    
        dia_chi=self.lineEdit_5.text()        
        id_lnc=self.lineEdit_6.text()        
        nganh_hoc=self.lineEdit_7.text()
        id_msv=str(id_msv) 
        print(id_msv)
        sv_ten=str(sv_ten) 
        ngay_sinh=str(ngay_sinh)
        gioi_tinh=str(gioi_tinh)
        dia_chi=str(dia_chi)
        id_lnc=str(id_lnc) 
        nganh_hoc=str(nganh_hoc)
        rows = (id_msv, sv_ten,ngay_sinh,gioi_tinh,dia_chi,id_lnc, nganh_hoc)
        #######check
        check_data_coincide = conn.cursor()
        check = "select * from DOAN3.SINH_VIEN where ID_MSV = :id_msv1"
        check_data_coincide.execute(check, id_msv1 = id_msv)
        data_check = check_data_coincide.fetchall()
        if len(data_check)>0:
            reply = QMessageBox.question(
            self, "Message",
            "Dữ liệu bị trùng, hãy nhập lại!",
            QMessageBox.Close)
            print(len(data_check))
            return##########
        if len(id_msv)>6 and len(sv_ten)>6 and len(id_lnc)>1:
            # conn = cx_Oracle.connect('DOAN3/123@//localhost:1521/xe') 
            myinsert = conn.cursor()
            # insert = "INSERT INTO DOAN3.SINH_VIEN (ID_MSV, SV_TEN, NGAY_SINH, GIOI_TINH, DIA_CHI, ID_LNC, NGANH_HOC) VALUES (:id_msv, :sv_ten, :ngay_sinh, :gioi_tinh, :dia_chi, :id_lnc, :nganh_hoc)"
            insert = "INSERT INTO DOAN3.SINH_VIEN (ID_MSV, SV_TEN, NGAY_SINH, GIOI_TINH,DIA_CHI, ID_LNC, NGANH_HOC) VALUES (:1,:2,:3,:4,:5,:6,:7)"
            myinsert.execute(insert,rows)
            conn.commit()
            print(myinsert)
        else:
            reply = QMessageBox.question(
            self, "Message",
            "Làm ơn nhập vào trước khi thêm!",
            QMessageBox.Close)
            return
    def delete_row (self):
        id_msv=self.lineEdit.text() 
        id_msv=str(id_msv)
        conn1 = cx_Oracle.connect('DOAN3/123@//localhost:1521/xe') 
        mydelete = conn1.cursor()
        print(id_msv)
        delete = "DELETE FROM DOAN3.SINH_VIEN WHERE ID_MSV = :id_msv1"
        mydelete.execute(delete, id_msv1 = id_msv)
        conn1.commit()
        print(mydelete)
        pass
    def update_row (self):
        id_msv=self.lineEdit.text()        
        sv_ten=self.lineEdit_2.text()        
        ngay_sinh=self.lineEdit_3.text()        
        gioi_tinh=self.lineEdit_4.text()    
        dia_chi=self.lineEdit_5.text()        
        id_lnc=self.lineEdit_6.text()        
        nganh_hoc=self.lineEdit_7.text()
        if len(id_lnc)>0:
            id_lnc=str(id_lnc)
        else:
            reply = QMessageBox.question(
            self, "Message",
            "Ban chua nhap, hay nhap di",
            QMessageBox.Cancel)
            return 
        id_msv=str("%"+id_msv+"%")
        print(id_msv)
        sv_ten=str(sv_ten) 
        ngay_sinh=str(ngay_sinh)
        gioi_tinh=str(gioi_tinh)
        dia_chi=str(dia_chi)
        id_lnc=str(id_lnc) 
        nganh_hoc=str(nganh_hoc)
        rows = (id_msv, sv_ten,ngay_sinh,gioi_tinh,dia_chi,id_lnc, nganh_hoc)
        # conn = cx_Oracle.connect('DOAN3/123@//localhost:1521/xe') 
        myupdate = conn.cursor()
        update = "UPDATE DOAN3.SINH_VIEN SET ID_LNC = :id_lnc1 WHERE lower(ID_MSV) LIKE lower(:id_msv1)"
        myupdate.execute(update, id_lnc1 = id_lnc, id_msv1 = id_msv)
        conn.commit()
        pass

###################################################function for tab Giang Vien#######################################################
    def clear2(self):
        self.lineEdit_8.clear()
        self.lineEdit_9.clear()
        self.lineEdit_10.clear()
        self.lineEdit_11.clear()
        self.lineEdit_12.clear()
        self.lineEdit_13.clear()
        self.lineEdit_14.clear()
        self.lineEdit_15.clear()
        self.lineEdit_23.clear()
    def insert_row_1(self):
        gv_ten=self.lineEdit_8.text()        ### lấy dữ liệu từ các thanh nhập
        id_gv=self.lineEdit_9.text()        
        ngay_sinh=self.lineEdit_10.text()        
        dia_chi=self.lineEdit_11.text()    
        gioi_tinh=self.lineEdit_12.text()        
        hoc_vi=self.lineEdit_13.text()        
        hoc_ham=self.lineEdit_14.text()    ###
        noi_cong_tac=self.lineEdit_15.text()    ###
        thuoc_nhom=self.lineEdit_23.text()    ###        print(id_msv)
        
        gv_ten=str(gv_ten) 
        id_gv=str(id_gv) 
        ngay_sinh=str(ngay_sinh)
        dia_chi=str(dia_chi)
        gioi_tinh=str(gioi_tinh)
        hoc_vi=str(hoc_vi)
        hoc_ham=str(hoc_ham) 
        noi_cong_tac=str(noi_cong_tac)
        thuoc_nhom=str(thuoc_nhom)
        rows = (gv_ten,id_gv,ngay_sinh,dia_chi,gioi_tinh,hoc_vi,hoc_ham,noi_cong_tac)
        ###########check data coincide
        check_data_coincide = conn.cursor()
        check = "select * from DOAN3.GIANG_VIEN where ID_GV = :id_gv1"
        check_data_coincide.execute(check, id_gv1 = id_gv)
        data_check = check_data_coincide.fetchall()
        if len(data_check)>0:
            reply = QMessageBox.question(
            self, "Message",
            "Dữ liệu bị trùng, hãy nhập lại!",
            QMessageBox.Close)
            print(len(data_check))
            return
        elif len(gv_ten)>6 and len(id_gv)>5:
            # conn = cx_Oracle.connect('DOAN3/123@//localhost:1521/xe') 
            myinsert = conn.cursor()
            # insert = "INSERT INTO DOAN3.SINH_VIEN (ID_MSV, SV_TEN, NGAY_SINH, GIOI_TINH, DIA_CHI, ID_LNC, NGANH_HOC) VALUES (:id_msv, :sv_ten, :ngay_sinh, :gioi_tinh, :dia_chi, :id_lnc, :nganh_hoc)"
            insert = "INSERT INTO DOAN3.GIANG_VIEN (GV_TEN, ID_GV, NGAY_SINH, DIA_CHI, GIOI_TINH, HOC_VI, HOC_HAM, NOI_CONG_TAC) VALUES (:1,:2,:3,:4,:5,:6,:7,:8)"
            myinsert.execute(insert,rows)
            conn.commit()
            print(myinsert)
        else:
            reply = QMessageBox.question(
            self, "Message",
            "Nhập Tên và MSGV trước khi thêm!",
            QMessageBox.Close)
            return
    def search_2(self):
        self.listWidget.clear()             ### delete data in listWidget
        gv_ten=self.lineEdit_8.text()        ### lấy dữ liệu từ các thanh nhập
        id_gv=self.lineEdit_9.text()        
        ngay_sinh=self.lineEdit_10.text()        
        dia_chi=self.lineEdit_11.text()    
        gioi_tinh=self.lineEdit_12.text()        
        hoc_vi=self.lineEdit_13.text()        
        hoc_ham=self.lineEdit_14.text()    ###
        noi_cong_tac=self.lineEdit_15.text()    ###
        thuoc_nhom=self.lineEdit_23.text()    ###

        gv_ten=str("%"+gv_ten+"%") 
        id_gv=str("%"+id_gv+"%") 
        ngay_sinh=str(ngay_sinh)
        dia_chi=str(dia_chi)
        gioi_tinh=str("%"+gioi_tinh+"%")
        hoc_vi=str(hoc_vi)
        hoc_ham=str(hoc_ham) 
        noi_cong_tac=str("%"+noi_cong_tac+"%")
        thuoc_nhom=str(thuoc_nhom)
        rows = (gv_ten, id_gv, ngay_sinh, dia_chi,gioi_tinh,hoc_vi,hoc_ham ,noi_cong_tac,thuoc_nhom)
        
        if len(gv_ten)>6:
            # conn = cx_Oracle.connect('DOAN3/123@//localhost:1521/xe') 
            mysearch = conn.cursor()
            search = "select * from DOAN3.GIANG_VIEN where lower(gv_ten) LIKE lower(:gv_ten1)"
            mysearch.execute(search,gv_ten1=gv_ten)
            data = mysearch.fetchall()   
        elif len(id_gv)>2:
            conn1 = cx_Oracle.connect('DOAN3/123@//localhost:1521/xe') 
            mysearch2 = conn1.cursor()
            search2= "select * from DOAN3.GIANG_VIEN where lower(id_gv) LIKE lower(:id_gv1)"
            mysearch2.execute(search2,id_gv1=id_gv)
            data = mysearch2.fetchall()
        elif len(gioi_tinh)>2:
            conn2 = cx_Oracle.connect('DOAN3/123@//localhost:1521/xe') 
            mysearch3 = conn2.cursor()
            search3= "select * from DOAN3.GIANG_VIEN where lower(gioi_tinh) LIKE lower(:gioi_tinh1)"
            mysearch3.execute(search3,gioi_tinh1=gioi_tinh)
            data = mysearch3.fetchall()
        elif len(hoc_vi)>3:
            conn3 = cx_Oracle.connect('DOAN3/123@//localhost:1521/xe') 
            mysearch4 = conn3.cursor()
            search4= "select * from DOAN3.GIANG_VIEN where lower(hoc_vi) LIKE lower(:hoc_vi1)"
            mysearch4.execute(search4,hoc_vi1=hoc_vi)
            data = mysearch4.fetchall()
        elif len(hoc_ham)>3:
            conn4 = cx_Oracle.connect('DOAN3/123@//localhost:1521/xe')
            mysearch5 = conn4.cursor()
            search5 = "select * from DOAN3.GIANG_VIEN where lower(hoc_ham) LIKE lower(:hoc_ham1)"
            mysearch5.execute(search5,hoc_ham1= hoc_ham)
        else:
            reply = QMessageBox.question(
            self, "Message",
            "Ban chua nhap, hay nhap di",
            QMessageBox.Close)
            return
        m=[]
        for x in data:
            m=x
        
        so_sv = len(data)
        
        m=list(m)
        if len(data) == 0:
            koco = 'Không có dữ liệu, hãy nhập lại.'
            self.listWidget.addItem(koco)
        i = 0
        while i < so_sv:
            stu_info=data[i]
            stu_info = list(stu_info)
            i += 1
            stu_info1 = []
            j = 0      
            if stu_info[0] == None:
                stu_info[0]='None'
            if stu_info[1] == None:
                stu_info[1]='None'
            if stu_info[2] == None:
                stu_info[2]='None'
            if stu_info[3] == None:
                stu_info[3]='None'
            if stu_info[4] == None:
                stu_info[4]='None'
            if stu_info[5] == None:
                stu_info[5]='None'
            if stu_info[6] == None:
                stu_info[6]='None'
            if stu_info[7] == None:
                stu_info[7] = 'None'
            print(stu_info)
            stu_info = str(stu_info[0]+'  '+stu_info[1]+'   '+stu_info[2]+'   '+stu_info[3]+'   '+stu_info[4]+'   '+stu_info[5]+'   '+stu_info[6]+'   '+stu_info[7])
            self.listWidget.addItem(stu_info)
            self.listWidget.setCurrentRow(0)
        
    def display(self):
        # conn = cx_Oracle.connect('DOAN3/123@//localhost:1521/xe') 
        self.listWidget.clear()
        mysearch = conn.cursor()
        search= "select * from DOAN3.GIANG_VIEN"
        mysearch.execute(search)
        data = mysearch.fetchall()
        m=[]
        for x in data:
            m=x
        so_gv = len(data)
        i = 0
        while i < so_gv:
            stu_info=data[i]
            stu_info = list(stu_info)
            i += 1
            stu_info1 = []
            j = 0      
            if stu_info[0] == None:
                stu_info[0]='-None-'
            if stu_info[1] == None:
                stu_info[1]='-None-'
            if stu_info[2] == None:
                stu_info[2]='-None-'
            if stu_info[3] == None:
                stu_info[3]='-None-'
            if stu_info[4] == None:
                stu_info[4]='-None-'
            if stu_info[5] == None:
                stu_info[5]='-None-'
            if stu_info[6] == None:
                stu_info[6]='-None-'
            if stu_info[7] == None:
                stu_info[7]='-None-'

            stu_info = str(stu_info[0]+'  '+stu_info[1]+'   '+stu_info[2]+'   '+stu_info[3]+'   '+stu_info[4]+'   '+stu_info[5]+'   '+stu_info[6]+'   '+stu_info[7])
            self.listWidget.addItem(stu_info)
            self.listWidget.setCurrentRow(0)
    def deleteRowGv(self):
        id_gv=self.lineEdit_9.text() 
        id_gv=str(id_gv)
        print(id_gv)
        conn_d = cx_Oracle.connect('DOAN3/123@//localhost:1521/xe') 
        mydelete = conn_d.cursor()
        delete_gv = "DELETE FROM DOAN3.GIANG_VIEN WHERE ID_GV = :id_gv1" 
        mydelete.execute(delete_gv,id_gv1 = id_gv)
        conn_d.commit()
        print(mydelete)
        pass

    def update_row_1 (self):
        gv_ten=self.lineEdit_8.text()        ### lấy dữ liệu từ các thanh nhập
        id_gv=self.lineEdit_9.text()        
        ngay_sinh=self.lineEdit_10.text()        
        dia_chi=self.lineEdit_11.text()    
        gioi_tinh=self.lineEdit_12.text()        
        hoc_vi=self.lineEdit_13.text()        
        hoc_ham=self.lineEdit_14.text()    ###
        noi_cong_tac=self.lineEdit_15.text()    ###
        thuoc_nhom=self.lineEdit_23.text()    ###

        if len(hoc_ham)>0:
            hoc_ham=str(hoc_ham)
        else:
            reply = QMessageBox.question(
            self, "Message",
            "Ban chua nhap, hay nhap di",
            QMessageBox.Cancel)
            return 
        id_gv=str("%"+id_gv+"%")
        gv_ten=str(gv_ten) 
        ngay_sinh=str(ngay_sinh)
        gioi_tinh=str(gioi_tinh)
        dia_chi=str(dia_chi)
        hoc_vi=str(hoc_vi) 
        # hoc_ham=str(hoc_ham)
        noi_cong_tac=str(noi_cong_tac)
        # rows = (id_msv, sv_ten,ngay_sinh,gioi_tinh,dia_chi,id_lnc, nganh_hoc)
        # conn = cx_Oracle.connect('DOAN3/123@//localhost:1521/xe') 
        myupdate = conn.cursor()
        update = "UPDATE DOAN3.GIANG_VIEN SET HOC_HAM = :hoc_ham1 WHERE lower(ID_GV) LIKE lower(:id_gv1)"
        myupdate.execute(update, hoc_ham1= hoc_ham, id_gv1 = id_gv)
        conn.commit()
        pass
################################################### function for tab Mon Hoc #######################################################
    def clear3(self):
        self.listWidget_2.clear()
        self.lineEdit_16.clear()
        self.lineEdit_17.clear()
        self.lineEdit_18.clear()
        self.lineEdit_19.clear()
        self.lineEdit_20.clear()
        self.lineEdit_21.clear()
        self.lineEdit_22.clear()

    def insert_row_2(self):
        ten_mh=self.lineEdit_16.text()        ### lấy dữ liệu từ các thanh nhập
        id_mh=self.lineEdit_17.text()        
        so_tin_chi=self.lineEdit_18.text()        
        tiet_lt=self.lineEdit_19.text()    
        tiet_bt=self.lineEdit_20.text()        
        tiet_thtn=self.lineEdit_21.text()        
        tiet_tu_hoc=self.lineEdit_22.text()    ###
        
        
        id_mh2=str("%"+id_mh+"%") 
        id_mh=str(id_mh)
        ten_mh=str(ten_mh) 
        so_tin_chi=str(so_tin_chi)
        tiet_lt=str(tiet_lt)
        tiet_bt=str(tiet_bt)
        tiet_thtn=str(tiet_thtn)
        tiet_tu_hoc=str(tiet_tu_hoc) 
        rows = (ten_mh,id_mh,so_tin_chi,tiet_lt,tiet_bt,tiet_thtn,tiet_tu_hoc)
        #####check
        check_data_coincide = conn.cursor()
        check = "select * from DOAN3.MONHOC where lower(ID_MH) LIKE :id_mh2"
        check_data_coincide.execute(check, id_mh2 = id_mh2)
        data_check = check_data_coincide.fetchall()
        if len(data_check)>0:
            reply = QMessageBox.question(
            self, "Message",
            "Dữ liệu bị trùng, hãy nhập lại!",
            QMessageBox.Close)
            print(len(data_check))
            return#####
        if len(id_mh)>1 and len(ten_mh)>6:
            # conn = cx_Oracle.connect('DOAN3/123@//localhost:1521/xe') 
            myinsert = conn.cursor()
            # insert = "INSERT INTO DOAN3.SINH_VIEN (ID_MSV, SV_TEN, NGAY_SINH, GIOI_TINH, DIA_CHI, ID_LNC, NGANH_HOC) VALUES (:id_msv, :sv_ten, :ngay_sinh, :gioi_tinh, :dia_chi, :id_lnc, :nganh_hoc)"
            insert = "INSERT INTO DOAN3.MONHOC (TEN_MH,ID_MH, SO_TIN_CHI, TIET_LT, TIET_BT, TIET_THTN, TIET_TU_HOC) VALUES (:1,:2,:3,:4,:5,:6,:7)"
            myinsert.execute(insert,rows)
            conn.commit()
            print(myinsert)
        else:
            reply = QMessageBox.question(
            self, "Message",
            "Làm ơn nhập vào trước khi thêm!",
            QMessageBox.Close)
            return
    def display_2(self):
        # conn = cx_Oracle.connect('DOAN3/123@//localhost:1521/xe') 
        self.listWidget_2.clear()
        mysearch = conn.cursor()
        search= "select * from DOAN3.MONHOC"
        mysearch.execute(search)
        data = mysearch.fetchall()
        m=[]
        for x in data:
            m=x
        so_gv = len(data)
        i = 0
        while i < so_gv:
            stu_info=data[i]
            stu_info = list(stu_info)
            i += 1
            stu_info1 = []
            j = 0      
            if stu_info[0] == None:
                stu_info[0]='-None-'
            if stu_info[1] == None:
                stu_info[1]='-None-'
            if stu_info[2] == None:
                stu_info[2]='-None-'
            if stu_info[3] == None:
                stu_info[3]='-None-'
            if stu_info[4] == None:
                stu_info[4]='-None-'
            if stu_info[5] == None:
                stu_info[5]='-None-'
            if stu_info[6] == None:
                stu_info[6]='-None-'

            stu_info = stu_info[0]+'  '+stu_info[1]+'   '+str(stu_info[2])+'   '+str(stu_info[3])+'   '+str(stu_info[4])+'   '+str(stu_info[5])+'   '+str(stu_info[6])
            self.listWidget_2.addItem(stu_info)
            self.listWidget_2.setCurrentRow(0)
        pass

    def search_3(self):
        self.listWidget_2.clear()             ### delete data in listWidget
        ten_mh=self.lineEdit_16.text()        ### lấy dữ liệu từ các thanh nhập
        id_mh=self.lineEdit_17.text()        
        so_tin_chi=self.lineEdit_18.text()        
        tiet_lt=self.lineEdit_19.text()    
        tiet_bt=self.lineEdit_20.text()        
        tiet_thtn=self.lineEdit_21.text()        
        tiet_tu_hoc=self.lineEdit_22.text()    ###

        ten_mh=str("%"+ten_mh+"%") 
        id_mh=str("%"+id_mh+"%") 
        so_tin_chi=str(so_tin_chi)
        tiet_lt=str(tiet_lt)
        tiet_bt=str(tiet_bt)
        tiet_thtn=str(tiet_thtn)
        tiet_tu_hoc=str(tiet_tu_hoc) 
        rows = (ten_mh, id_mh, so_tin_chi, tiet_lt,tiet_bt,tiet_thtn,tiet_tu_hoc)
        
        if len(ten_mh)>4:
            # conn = cx_Oracle.connect('DOAN3/123@//localhost:1521/xe') 
            mysearch = conn.cursor()
            search = "select * from DOAN3.MONHOC where lower(TEN_MH) LIKE lower(:ten_mh1)"
            mysearch.execute(search,ten_mh1=ten_mh)
            data = mysearch.fetchall()   
        elif len(id_mh)>4:
            conn1 = cx_Oracle.connect('DOAN3/123@//localhost:1521/xe') 
            mysearch2 = conn1.cursor()
            search2= "select * from DOAN3.MONHOC where lower(ID_MH) LIKE lower(:id_mh1)"
            mysearch2.execute(search2,id_mh1=id_mh)
            data = mysearch2.fetchall()
        elif len(so_tin_chi)>0:
            conn2 = cx_Oracle.connect('DOAN3/123@//localhost:1521/xe') 
            mysearch3 = conn2.cursor()
            search3= "select * from DOAN3.MONHOC where lower(SO_TIN_CHI) LIKE lower(:so_tin_chi1)"
            mysearch3.execute(search3,so_tin_chi1=so_tin_chi)
            data = mysearch3.fetchall()
        else:
            reply = QMessageBox.question(
            self, "Message",
            "Ban chua nhap, hay nhap di",
            QMessageBox.Close)
            return
        m=[]
        for x in data:
            m=x
        
        so_mh = len(data)
        
        m=list(m)
        if len(data) == 0:
            koco = 'Không có dữ liệu, hãy nhập lại.'
            self.listWidget_2.addItem(koco)
        i = 0
        while i < so_mh:
            stu_info=data[i]
            stu_info = list(stu_info)
            i += 1
            if stu_info[0] == None:
                stu_info[0]='None'
            if stu_info[1] == None:
                stu_info[1]='None'
            if stu_info[2] == None:
                stu_info[2]='None'
            if stu_info[3] == None:
                stu_info[3]='None'
            if stu_info[4] == None:
                stu_info[4]='None'
            if stu_info[5] == None:
                stu_info[5]='None'
            if stu_info[6] == None:
                stu_info[6]='None'
            print(stu_info)
            stu_info = stu_info[0]+'  '+stu_info[1]+'   '+str(stu_info[2])+'   '+str(stu_info[3])+'   '+str(stu_info[4])+'   '+str(stu_info[5])+'   '+str(stu_info[6])
            self.listWidget_2.addItem(stu_info)
            self.listWidget_2.setCurrentRow(0)

    def deleteRowMh(self):
        id_mh=self.lineEdit_17.text() 
        id_mh=str(id_mh)
        conn_d = cx_Oracle.connect('DOAN3/123@//localhost:1521/xe') 
        mydelete = conn_d.cursor()
        delete_mh = "DELETE FROM DOAN3.MONHOC WHERE ID_MH = :id_mh1" 
        mydelete.execute(delete_mh, id_mh1=id_mh)
        conn_d.commit()
        print(mydelete)
        pass
    def updateRowMh (self):
        ten_mh=self.lineEdit_16.text()        ### lấy dữ liệu từ các thanh nhập
        id_mh=self.lineEdit_17.text()        
        so_tin_chi=self.lineEdit_18.text()        
        tiet_lt=self.lineEdit_19.text()    
        tiet_bt=self.lineEdit_20.text()        
        tiet_thtn=self.lineEdit_21.text()        
        tiet_tu_hoc=self.lineEdit_22.text()    ###
        if len(ten_mh)>0:
            ten_mh=str(ten_mh)
        else:
            reply = QMessageBox.question(
            self, "Message",
            "Ban chua nhap, hay nhap di",
            QMessageBox.Cancel)
            return 
        # ten_mh=str(ten_mh)
        print(ten_mh)
        id_mh=str(id_mh) 
        so_tin_chi=str(so_tin_chi)
        tiet_lt=str(tiet_lt)
        tiet_bt=str(tiet_bt)
        tiet_thtn=str(tiet_thtn) 
        tiet_tu_hoc=str(tiet_tu_hoc)
        rows = (ten_mh,id_mh ,so_tin_chi,tiet_lt,tiet_bt,tiet_thtn,tiet_tu_hoc)
        # conn = cx_Oracle.connect('DOAN3/123@//localhost:1521/xe') 
        myupdate = conn.cursor()
        update = "UPDATE DOAN3.MONHOC SET TEN_MH = :ten_mh1 WHERE lower(ID_MH) LIKE lower(:id_mh1)"
        myupdate.execute(update, ten_mh1 = ten_mh, id_mh1= id_mh)
        conn.commit()
        pass

    def giaodien_admin(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(861, 655)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(400, 0))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_1)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 1, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 7, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 5, 5, 2, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 38, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 0, 6, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 2, 0, 1, 3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 2, 6, 1, 1)
        self.line = QtWidgets.QFrame(self.tab_1)
        self.line.setMinimumSize(QtCore.QSize(400, 5))
        self.line.setMaximumSize(QtCore.QSize(400, 5))
        self.line.setSizeIncrement(QtCore.QSize(0, 2))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 2, 1, 6)
        self.label_11 = QtWidgets.QLabel(self.tab_1)
        self.label_11.setMinimumSize(QtCore.QSize(450, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 0, 2, 1, 4)
        self.label_9 = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 2, 4, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(165, 28, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 0, 0, 1, 2)
        self.listWidget_3 = QtWidgets.QListWidget(self.tab_1)
        self.listWidget_3.setMinimumSize(QtCore.QSize(400, 300))
        self.listWidget_3.setObjectName("listWidget_3")
        self.gridLayout.addWidget(self.listWidget_3, 3, 4, 2, 5)
        spacerItem5 = QtWidgets.QSpacerItem(63, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 7, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(127, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 6, 8, 2, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.tab_1)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit.setMinimumSize(QtCore.QSize(300, 0))
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(2, QtWidgets.QFormLayout.FieldRole, spacerItem7)
        self.label_2 = QtWidgets.QLabel(self.tab_1)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(4, QtWidgets.QFormLayout.FieldRole, spacerItem8)
        self.label_3 = QtWidgets.QLabel(self.tab_1)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(6, QtWidgets.QFormLayout.FieldRole, spacerItem9)
        self.label_4 = QtWidgets.QLabel(self.tab_1)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(8, QtWidgets.QFormLayout.FieldRole, spacerItem10)
        self.label_5 = QtWidgets.QLabel(self.tab_1)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(10, QtWidgets.QFormLayout.FieldRole, spacerItem11)
        self.label_6 = QtWidgets.QLabel(self.tab_1)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.lineEdit_6)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(12, QtWidgets.QFormLayout.FieldRole, spacerItem12)
        self.label_7 = QtWidgets.QLabel(self.tab_1)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.lineEdit_7)
        self.gridLayout.addLayout(self.formLayout, 3, 0, 1, 4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.tab_1)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.insert_row)
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.display_1)
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.clear1)
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_1)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.delete_row)
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_1)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.search)
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_1)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.update_row)
        self.horizontalLayout_2.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_1)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.closeEvent)
        self.horizontalLayout_2.addWidget(self.pushButton_7)
        self.gridLayout.addLayout(self.horizontalLayout_2, 7, 1, 1, 7)
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem13 = QtWidgets.QSpacerItem(186, 18, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem13, 0, 0, 1, 2)
        self.label_26 = QtWidgets.QLabel(self.tab_2)
        self.label_26.setMinimumSize(QtCore.QSize(450, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.gridLayout_2.addWidget(self.label_26, 0, 2, 1, 2)
        self.line_2 = QtWidgets.QFrame(self.tab_2)
        self.line_2.setMinimumSize(QtCore.QSize(400, 5))
        self.line_2.setMaximumSize(QtCore.QSize(400, 5))
        self.line_2.setSizeIncrement(QtCore.QSize(0, 2))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 1, 2, 1, 2)
        self.label_27 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.gridLayout_2.addWidget(self.label_27, 2, 0, 1, 3)
        self.label_28 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.gridLayout_2.addWidget(self.label_28, 2, 3, 1, 2)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_8.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_8)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(2, QtWidgets.QFormLayout.FieldRole, spacerItem14)
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setObjectName("label_12")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_9)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(4, QtWidgets.QFormLayout.FieldRole, spacerItem15)
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setObjectName("label_13")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_10)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(6, QtWidgets.QFormLayout.FieldRole, spacerItem16)
        self.label_14 = QtWidgets.QLabel(self.tab_2)
        self.label_14.setObjectName("label_14")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lineEdit_11)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(8, QtWidgets.QFormLayout.FieldRole, spacerItem17)
        self.label_15 = QtWidgets.QLabel(self.tab_2)
        self.label_15.setObjectName("label_15")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.lineEdit_12)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(10, QtWidgets.QFormLayout.FieldRole, spacerItem18)
        self.label_16 = QtWidgets.QLabel(self.tab_2)
        self.label_16.setObjectName("label_16")
        self.formLayout_2.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.formLayout_2.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.lineEdit_13)
        spacerItem19 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(12, QtWidgets.QFormLayout.FieldRole, spacerItem19)
        self.label_17 = QtWidgets.QLabel(self.tab_2)
        self.label_17.setObjectName("label_17")
        self.formLayout_2.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.formLayout_2.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.lineEdit_14)
        spacerItem20 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(14, QtWidgets.QFormLayout.FieldRole, spacerItem20)
        self.label_18 = QtWidgets.QLabel(self.tab_2)
        self.label_18.setObjectName("label_18")
        self.formLayout_2.setWidget(15, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.formLayout_2.setWidget(15, QtWidgets.QFormLayout.FieldRole, self.lineEdit_15)
        self.lineEdit_23 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.formLayout_2.setWidget(17, QtWidgets.QFormLayout.FieldRole, self.lineEdit_23)
        self.label_32 = QtWidgets.QLabel(self.tab_2)
        self.label_32.setObjectName("label_32")
        self.formLayout_2.setWidget(17, QtWidgets.QFormLayout.LabelRole, self.label_32)
        spacerItem21 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(16, QtWidgets.QFormLayout.FieldRole, spacerItem21)
        self.gridLayout_2.addLayout(self.formLayout_2, 3, 0, 1, 3)
        self.listWidget = QtWidgets.QListWidget(self.tab_2)
        self.listWidget.setMinimumSize(QtCore.QSize(400, 300))
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_2.addWidget(self.listWidget, 3, 3, 1, 2)
        spacerItem22 = QtWidgets.QSpacerItem(97, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem22, 4, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.insert_row_1)
        self.horizontalLayout_3.addWidget(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(self.display)
        self.horizontalLayout_3.addWidget(self.pushButton_9)
        self.pushButton_10 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.clicked.connect(self.clear2)
        self.horizontalLayout_3.addWidget(self.pushButton_10)
        self.pushButton_11 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_11.clicked.connect(self.deleteRowGv)
        self.horizontalLayout_3.addWidget(self.pushButton_11)
        self.pushButton_12 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_12.clicked.connect(self.search_2)
        self.horizontalLayout_3.addWidget(self.pushButton_12)
        self.pushButton_13 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_13.clicked.connect(self.update_row_1)
        self.horizontalLayout_3.addWidget(self.pushButton_13)
        self.pushButton_14 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_14.setObjectName("pushButton_14")

        self.pushButton_14.clicked.connect(self.closeEvent)
        self.horizontalLayout_3.addWidget(self.pushButton_14)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 4, 1, 1, 3)
        spacerItem23 = QtWidgets.QSpacerItem(163, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem23, 4, 4, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem24 = QtWidgets.QSpacerItem(151, 38, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem24, 0, 0, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.tab_3)
        self.label_31.setMinimumSize(QtCore.QSize(450, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.gridLayout_3.addWidget(self.label_31, 0, 1, 1, 2)
        self.line_3 = QtWidgets.QFrame(self.tab_3)
        self.line_3.setMinimumSize(QtCore.QSize(400, 5))
        self.line_3.setMaximumSize(QtCore.QSize(400, 5))
        self.line_3.setSizeIncrement(QtCore.QSize(0, 2))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_3.addWidget(self.line_3, 1, 1, 1, 2)
        self.label_30 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.gridLayout_3.addWidget(self.label_30, 2, 0, 1, 2)
        self.label_29 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.gridLayout_3.addWidget(self.label_29, 2, 2, 1, 1)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_19 = QtWidgets.QLabel(self.tab_3)
        self.label_19.setObjectName("label_19")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_19)
        self.lineEdit_16 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_16.setMinimumSize(QtCore.QSize(300, 0))
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_16)
        spacerItem25 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_3.setItem(2, QtWidgets.QFormLayout.FieldRole, spacerItem25)
        self.label_20 = QtWidgets.QLabel(self.tab_3)
        self.label_20.setObjectName("label_20")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_20)
        self.lineEdit_17 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_17)
        spacerItem26 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_3.setItem(4, QtWidgets.QFormLayout.FieldRole, spacerItem26)
        self.label_21 = QtWidgets.QLabel(self.tab_3)
        self.label_21.setObjectName("label_21")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_21)
        self.lineEdit_18 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_18)
        spacerItem27 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_3.setItem(6, QtWidgets.QFormLayout.FieldRole, spacerItem27)
        self.label_22 = QtWidgets.QLabel(self.tab_3)
        self.label_22.setObjectName("label_22")
        self.formLayout_3.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_22)
        self.lineEdit_19 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.formLayout_3.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lineEdit_19)
        spacerItem28 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_3.setItem(8, QtWidgets.QFormLayout.FieldRole, spacerItem28)
        self.label_23 = QtWidgets.QLabel(self.tab_3)
        self.label_23.setObjectName("label_23")
        self.formLayout_3.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_23)
        self.lineEdit_20 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.formLayout_3.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.lineEdit_20)
        spacerItem29 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_3.setItem(10, QtWidgets.QFormLayout.FieldRole, spacerItem29)
        self.label_24 = QtWidgets.QLabel(self.tab_3)
        self.label_24.setObjectName("label_24")
        self.formLayout_3.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_24)
        self.lineEdit_21 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.formLayout_3.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.lineEdit_21)
        spacerItem30 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_3.setItem(12, QtWidgets.QFormLayout.FieldRole, spacerItem30)
        self.label_25 = QtWidgets.QLabel(self.tab_3)
        self.label_25.setObjectName("label_25")
        self.formLayout_3.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.label_25)
        self.lineEdit_22 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.formLayout_3.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.lineEdit_22)
        self.gridLayout_3.addLayout(self.formLayout_3, 3, 0, 1, 2)
        self.listWidget_2 = QtWidgets.QListWidget(self.tab_3)
        self.listWidget_2.setMinimumSize(QtCore.QSize(400, 300))
        self.listWidget_2.setObjectName("listWidget_2")
        self.gridLayout_3.addWidget(self.listWidget_2, 3, 2, 1, 2)
        spacerItem31 = QtWidgets.QSpacerItem(227, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem31, 4, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_15 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_15.clicked.connect(self.insert_row_2)
        self.horizontalLayout_4.addWidget(self.pushButton_15)
        self.pushButton_16 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_16.clicked.connect(self.display_2)
        self.horizontalLayout_4.addWidget(self.pushButton_16)
        self.pushButton_17 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_17.clicked.connect(self.clear3)
        self.horizontalLayout_4.addWidget(self.pushButton_17)
        self.pushButton_18 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_18.clicked.connect(self.deleteRowMh)
        self.horizontalLayout_4.addWidget(self.pushButton_18)
        self.pushButton_19 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_19.clicked.connect(self.search_3)
        self.horizontalLayout_4.addWidget(self.pushButton_19)
        self.pushButton_20 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_20.clicked.connect(self.updateRowMh)
        self.horizontalLayout_4.addWidget(self.pushButton_20)
        self.pushButton_21 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_21.clicked.connect(self.closeEvent)
        self.horizontalLayout_4.addWidget(self.pushButton_21)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 4, 1, 1, 2)
        spacerItem32 = QtWidgets.QSpacerItem(144, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem32, 4, 3, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 861, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Giao dien"))
        MainWindow.setWindowIcon(QIcon("icon.png"))
        self.label_10.setText(_translate("MainWindow", "Students Membership info:"))
        self.label_11.setText(_translate("MainWindow", "Bach Khoa Database Management Systems"))
        self.label_9.setText(_translate("MainWindow", "Book detail:"))
        self.label.setText(_translate("MainWindow", "MSSV:"))
        self.label_2.setText(_translate("MainWindow", "Ho va ten:"))
        self.label_3.setText(_translate("MainWindow", "Ngay sinh:"))
        self.label_4.setText(_translate("MainWindow", "Gioi tinh:"))
        self.label_5.setText(_translate("MainWindow", "Dia chi:"))
        self.label_6.setText(_translate("MainWindow", "Lop nien che:"))
        self.label_7.setText(_translate("MainWindow", "Ngành hoc:"))
        self.pushButton.setText(_translate("MainWindow", "Add new"))
        self.pushButton_2.setText(_translate("MainWindow", "Display"))
        self.pushButton_3.setText(_translate("MainWindow", "Clear"))
        self.pushButton_4.setText(_translate("MainWindow", "Delete"))
        self.pushButton_5.setText(_translate("MainWindow", "Search"))
        self.pushButton_6.setText(_translate("MainWindow", "Update"))
        self.pushButton_7.setText(_translate("MainWindow", "Exit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Sinh Vien"))
        self.label_26.setText(_translate("MainWindow", "Bach Khoa Database Management Systems"))
        self.label_27.setText(_translate("MainWindow", "Lecturers Membership info:"))
        self.label_28.setText(_translate("MainWindow", "Book detail:"))
        self.label_8.setText(_translate("MainWindow", "Ho va ten:"))
        self.label_12.setText(_translate("MainWindow", "MSGV:"))
        self.label_13.setText(_translate("MainWindow", "Ngay sinh:"))
        self.label_14.setText(_translate("MainWindow", "Địa chỉ:"))
        self.label_15.setText(_translate("MainWindow", "Giới tính:"))
        self.label_16.setText(_translate("MainWindow", "Học vị:"))
        self.label_17.setText(_translate("MainWindow", "Học hàm:"))
        self.label_18.setText(_translate("MainWindow", "Nơi công tác:"))
        self.label_32.setText(_translate("MainWindow", "Thuộc nhóm:"))
        self.pushButton_8.setText(_translate("MainWindow", "Add new"))
        self.pushButton_9.setText(_translate("MainWindow", "Display"))
        self.pushButton_10.setText(_translate("MainWindow", "Clear"))
        self.pushButton_11.setText(_translate("MainWindow", "Delete"))
        self.pushButton_12.setText(_translate("MainWindow", "Search"))
        self.pushButton_13.setText(_translate("MainWindow", "Update"))
        self.pushButton_14.setText(_translate("MainWindow", "Exit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Giang Vien"))
        self.label_31.setText(_translate("MainWindow", "Bach Khoa Database Management Systems"))
        self.label_30.setText(_translate("MainWindow", "Subjects info:"))
        self.label_29.setText(_translate("MainWindow", "Book detail:"))
        self.label_19.setText(_translate("MainWindow", "Tên môn học:"))
        self.label_20.setText(_translate("MainWindow", "Mã môn học:"))
        self.label_21.setText(_translate("MainWindow", "Số tín chỉ:"))
        self.label_22.setText(_translate("MainWindow", "Tiết lý thuyết:"))
        self.label_23.setText(_translate("MainWindow", "Tiết bài tập:"))
        self.label_24.setText(_translate("MainWindow", "Tiết thí nghiệm:"))
        self.label_25.setText(_translate("MainWindow", "Tiết tự học:"))
        self.pushButton_15.setText(_translate("MainWindow", "Add new"))
        self.pushButton_16.setText(_translate("MainWindow", "Display"))
        self.pushButton_17.setText(_translate("MainWindow", "Clear"))
        self.pushButton_18.setText(_translate("MainWindow", "Delete"))
        self.pushButton_19.setText(_translate("MainWindow", "Search"))
        self.pushButton_20.setText(_translate("MainWindow", "Update"))
        self.pushButton_21.setText(_translate("MainWindow", "Exit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Mon Hoc"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.giaodien_admin(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
