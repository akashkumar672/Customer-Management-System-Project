#Business Logic Layer
import pickle
from tkinter import *
from tkinter import messagebox
# import pymysql
cus_id_list=[]      #[10,20,30,40]
cus_name_list=[]    #["Dhruv","Abhay","Sonu","Amit"]
cus_age_list=[]     #[20,16,24,70]
cus_mob_list=[]     #[1234,2345,3456,4567]
# con=pymysql.connect(host="localhost",user="root",password="root123",database="cusdb")
# cur=con.cursor()

def addCustomer(cus_id,cus_name,cus_age,cus_mob):
    cus_id_list.append(cus_id)
    cus_name_list.append(cus_name)
    cus_age_list.append(cus_age)
    cus_mob_list.append(cus_mob)
    # cur.execute(f"insert into custb values('{cus_id}','{cus_name}','{cus_age}','{cus_mob}')")
    # con.commit()
def searchCustomer(cus_id): #cus_id=20
    i=cus_id_list.index(cus_id) #i=1
    return i
def deleteCustomer(cus_id): ##cus_id=30
    i=cus_id_list.index(cus_id) #i=2
    cus_id_list.pop(i)
    cus_name_list.pop(i)
    cus_age_list.pop(i)
    cus_mob_list.pop(i)
def modifyCustomer(cus_id,cus_name,cus_age,cus_mob):
    i=cus_id_list.index(cus_id) #i=3
    cus_name_list[i]=cus_name
    cus_age_list[i]=cus_age
    cus_mob_list[i]=cus_mob
def savetoPickle():
    f=open("D:/temp/cms.txt","wb")
    cus_list=[]
    cus_list.append(cus_id_list)
    cus_list.append(cus_name_list)
    cus_list.append(cus_age_list)
    cus_list.append(cus_mob_list)
    pickle.dump(cus_list,f)
    f.close()
def loadfromPickle():
    f=open("D:/temp/cms.txt","rb")
    cus_list=pickle.load(f)
    cus_id_list.extend(cus_list[0])
    cus_name_list.extend(cus_list[1])
    cus_age_list.extend(cus_list[2])
    cus_mob_list.extend(cus_list[3])

#Presentation Layer
def btn_AddCust_Click():
    cus_id=var_id.get()
    cus_name=var_name.get()
    cus_age=var_age.get()
    cus_mob=var_mob.get()
    addCustomer(cus_id,cus_name,cus_age,cus_mob)
    messagebox.showinfo("CMS","Customer Added Successfully")
    var_id.set("")
    var_name.set("")
    var_age.set("")
    var_mob.set("")
def btn_SearchCust_Click():
    cus_id=var_id.get()
    i=searchCustomer(cus_id)    #
    var_name.set(cus_name_list[i])
    var_age.set(cus_age_list[i])
    var_mob.set(cus_mob_list[i])
def btn_DeleteCust_Click():
    cus_id=var_id.get()
    deleteCustomer(cus_id)
    messagebox.showinfo("CMS","Customer Deleted Successfully")
def btn_ModifyCust_Click():
    cus_id = var_id.get()
    cus_name = var_name.get()
    cus_age = var_age.get()
    cus_mob = var_mob.get()
    modifyCustomer(cus_id,cus_name,cus_age,cus_mob)
    messagebox.showinfo("CMS", "Customer Modified Successfully")
def btn_DisplayAll_Click():
    root_d=Tk()
    lbl_id_h = Label(root_d, text="CUST ID", font=20, bg="Orange", width=15, height=2)
    lbl_id_h.grid(row=0, column=0)
    lbl_name_h = Label(root_d, text="CUST NAME", font=20, bg="Orange", width=15, height=2)
    lbl_name_h.grid(row=0, column=1)
    lbl_age_h = Label(root_d, text="CUST AGE", font=20, bg="Orange", width=15, height=2)
    lbl_age_h.grid(row=0, column=2)
    lbl_mob_h = Label(root_d, text="CUST MOB", font=20, bg="Orange", width=15, height=2)
    lbl_mob_h.grid(row=0, column=3)
    for i in range(len(cus_id_list)):
        lbl_id_d = Label(root_d, text=cus_id_list[i], font=20, bg="Yellow", width=15, height=2)
        lbl_id_d.grid(row=i+1, column=0)
        lbl_name_d = Label(root_d, text=cus_name_list[i], font=20, bg="Yellow", width=15, height=2)
        lbl_name_d.grid(row=i + 1, column=1)
        lbl_age_d = Label(root_d, text=cus_age_list[i], font=20, bg="Yellow", width=15, height=2)
        lbl_age_d.grid(row=i + 1, column=2)
        lbl_mob_d = Label(root_d, text=cus_mob_list[i], font=20, bg="Yellow", width=15, height=2)
        lbl_mob_d.grid(row=i + 1, column=3)

def btn_SaveAll_Click():
    savetoPickle()
    messagebox.showinfo("CMS", "Customers Data Saved Successfully")
def btn_LoadAll_Click():
    loadfromPickle()
    messagebox.showinfo("CMS", "Customers Data Retrieved Successfully")

root_main=Tk()
root_main.geometry("600x500")

lbl_id=Label(root_main,font=20,text="Cust ID:")
lbl_id.grid(row=0,column=0)
var_id=StringVar()
entry_id=Entry(root_main,font=20,textvariable=var_id)
entry_id.grid(row=0,column=1)

lbl_name=Label(root_main,font=20,text="Cust Name:")
lbl_name.grid(row=1,column=0)
var_name=StringVar()
entry_name=Entry(root_main,font=20,textvariable=var_name)
entry_name.grid(row=1,column=1)

lbl_age=Label(root_main,font=20,text="Cust Age:")
lbl_age.grid(row=2,column=0)
var_age=StringVar()
entry_age=Entry(root_main,font=20,textvariable=var_age)
entry_age.grid(row=2,column=1)

lbl_mob=Label(root_main,font=20,text="Cust Mob:")
lbl_mob.grid(row=3,column=0)
var_mob=StringVar()
entry_mob=Entry(root_main,font=20,textvariable=var_mob)
entry_mob.grid(row=3,column=1)

btn_add_cust=Button(root_main,text="Add Cust",font=20,width=15,command=btn_AddCust_Click)
btn_add_cust.grid(row=4,column=0)

btn_search_cust=Button(root_main,text="Search Cust",font=20,width=15,command=btn_SearchCust_Click)
btn_search_cust.grid(row=4,column=1)

btn_del_cust=Button(root_main,text="Delete Cust",font=20,width=15,command=btn_DeleteCust_Click)
btn_del_cust.grid(row=4,column=2)

btn_modify_cust=Button(root_main,text="Modify Cust",font=20,width=15,command=btn_ModifyCust_Click)
btn_modify_cust.grid(row=5,column=0)

btn_all_cust=Button(root_main,text="Display All",font=20,width=15,command=btn_DisplayAll_Click)
btn_all_cust.grid(row=5,column=1)

btn_save_cust=Button(root_main,text="Save All",font=20,width=15,command=btn_SaveAll_Click)
btn_save_cust.grid(row=6,column=0)

btn_load_cust=Button(root_main,text="Load All",font=20,width=15,command=btn_LoadAll_Click)
btn_load_cust.grid(row=6,column=1)


root_main.mainloop()