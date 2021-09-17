
import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import sqlite3

root = Tk()
root.geometry('500x610')
root.title('POLICE CRIME REPORTING SYSTEM')
root.configure(bg="black")
root.iconbitmap('D:\.phy programme\pythonProject\CRS.ico')

conn = sqlite3.connect('CRIMECASESRECORD.db')
cur = conn.cursor()

'''cur.execute("CREATE TABLE R1 (station_name text,type_of_crime text,day_of_crime text,date_of_crime text,t_from text,t_to text,address_of_crime text,place_of_occurence text)")
cur.execute("CREATE TABLE R2 (complainant_name text,unique_id integer,nationality text,mobile integer,date_of_birth text,gender text,occupation text,address_of_complainant text,place_of_complainant tex)")
cur.execute("CREATE TABLE R3 (accused_name text,loss_particulars text,total_value integer)")'''

conn.commit()
conn.close

def opencr1():
    cr1=Toplevel(root)
    cr1.geometry('680x400')
    cr1.title('Details Of Offence')
    cr1.configure(bg="grey")
    cr1.iconbitmap('D:\.phy programme\pythonProject\CRS.ico')


    Options = ["Kidnapping", "Theft", "Sexual Assault", "Murder", "White Collar Crime", "False Pretences", "Any Other"]
    Days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    def onclick1():
        cr1.destroy()

    def onclick2():
        conn = sqlite3.connect('CRIMECASESRECORD.db')
        cur = conn.cursor()
        cur.execute("INSERT INTO R1 VALUES (:ps_name,:crime,:day,:date,:t_from,:t_to,:add,:place)",
                   {

                    'ps_name': name.get(),
                    'crime' : op.get(),
                    'day' : day.get(),
                    'date' : date.get(),
                    't_from' : tfrom.get(),
                    't_to' : tto.get(),
                    'add': ad.get(),
                    'place' : dis.get()
                   })

        conn.commit()
        conn.close()

        name.set(" ")
        date.set(" ")
        tto.set(" ")
        tfrom.set(" ")
        ad.set(" ")
        dis.set(" ")
        op.set(" ")
        day.set(" ")

        cr1.destroy()
        messagebox.showinfo("Save", "Details are Saved")



    global op,day,date,tto,tfrom,name,ad1,dis
    op = StringVar(root)
    op.set("Select")
    day = StringVar(root)
    date = StringVar(root)
    date.set("DD/MM/YYYY")
    tto = StringVar(root)
    tto.set("to")
    tfrom = StringVar(root)
    tfrom.set("from(hh:mm)")
    name = StringVar(root)
    ad = StringVar(root)
    dis = StringVar(root)
    dis.set("district,state,pincode")

    Label(cr1, text="INFORMED P.S", font=("Bold Arial  ", 16), bg="grey").grid(row=3, column=0, pady=10, padx=10)
    Label(cr1, text="CRIME", font=("Bold Arial  ", 16), bg="grey").grid(row=4, column=0, pady=10, padx=10)
    Label(cr1, text="DAY & DATE ", font=("Arial ", 16), bg="grey").grid(row=6, column=0, padx=10,
                                                                                         pady=10)
    Label(cr1, text="TIME ", font=("Bold Arial  ", 16), bg="grey").grid(row=7, column=0, pady=10, padx=10)
    Label(cr1, text="TIME ", font=("Bold Arial  ", 16), bg="grey").grid(row=7, column=0, pady=10, padx=10)
    Label(cr1, text="PLACE", font=("Bold Arial  ", 16), bg="grey").grid(row=8, column=0, pady=10,
                                                                                       padx=10)

    Entry(cr1, textvariable=name, font=("Courier New", 16), bg="pink", width=32).grid(row=3, column=1,columnspan=2, pady=10,
                                                                                       padx=10)
    Entry(cr1, textvariable=date, font=("Courier New", 16), bg="pink", width=15).grid(row=6, column=2, pady=10,
                                                                                       padx=10)
    Entry(cr1, textvariable=tfrom, font=("Courier New", 16), bg="pink", width=15).grid(row=7, column=1, pady=10,
                                                                                        padx=10)
    Entry(cr1, textvariable=tto, font=("Courier New", 16), bg="pink", width=15).grid(row=7, column=2, pady=10, padx=10)
    Entry(cr1, textvariable=ad, font=("Courier New", 16), bg="pink", width=32).grid(row=8, column=1,columnspan=2, pady=10, padx=10)
    Entry(cr1, textvariable=dis, font=("Courier New", 16), bg="pink", width=32).grid(row=9, column=1,columnspan=2, pady=10, padx=10)

    op1 = OptionMenu(cr1, op, *Options)
    op1.grid(row=4, column=1,columnspan=2, padx=10, pady=10)
    op1.config(font="Courier", bg="pink", width=31, height=1)
    op2 = OptionMenu(cr1, day, *Days)
    op2.grid(row=6, column=1, padx=10, pady=10)
    op2.config(font="Courier", bg="pink", width=13, height=1)


    Button(cr1, text="<-BACK", font=("Copperplate Gothic Bold", 11), borderwidth=8, relief=GROOVE, width="16", height="1",
           bg="#ff66ff", command=onclick1).grid(row=11, column=1, pady=10, padx=10)
    Button(cr1, text="SUBMIT->", font=("Copperplate Gothic Bold", 11), borderwidth=8, relief=GROOVE, width="16", height="1",
           bg="green", command=onclick2).grid(row=11, column=2, pady=10, padx=10)

def opencr2():
    cr2=Toplevel(root)
    cr2.geometry('730x440')
    cr2.title('Complainant/ Informant')
    cr2.configure(bg="grey")
    cr2.iconbitmap('D:\.phy programme\pythonProject\CRS.ico')

    Gender=["MALE","FEMALE","OTHER"]

    def onclick3():
        cr2.destroy()

    def onclick4():
        conn = sqlite3.connect('CRIMECASESRECORD.db')
        cur = conn.cursor()
        cur.execute("INSERT INTO R2 VALUES (:c_name,:id,:nat,:mob,:dob,:gen,:occ,:add1,:place1)",
                   {
                    'c_name' : cname.get(),
                    'id' : idn.get(),
                    'nat' : nat.get(),
                    'mob' : mob.get(),
                    'dob' : date1.get(),
                    'gen' : gn.get(),
                    'occ' : occup.get(),
                    'add1' : add1.get(),
                    'place1' : dis1.get()
                   })

        conn.commit()
        conn.close()

        cname.set(" ")
        idn.set(" ")
        nat.set(" ")
        mob.set(" ")
        date1.set(" ")
        occup.set(" ")
        add1.set(" ")
        dis1.set(" ")
        gn.set("")

        cr2.destroy()
        messagebox.showinfo("Save", "Details are Saved")


    global cname,idn,nat,mob,date1,gn,occup,add1,dis1
    gn = StringVar(root)
    gn.set(" Gender ")
    i = IntVar()
    cname = StringVar(root)
    idn = StringVar(root)
    add1 = StringVar(root)
    date1 = StringVar(root)
    nat = StringVar(root)
    nat.set("INDIAN")
    mob = StringVar(root)
    mob.set("+91 ")
    occup = StringVar(root)
    dis1 = StringVar(root)


    Label(cr2, text="NAME", font=("Bold Arial  ", 16), bg="grey").grid(row=3, column=0, pady=10, padx=10)
    Label(cr2, text="IDENTITY", font=("Bold Arial  ", 16), bg="grey").grid(row=4, column=0, pady=10,padx=10)
    Label(cr2, text="CONTACT NUMBER", font=("Bold Arial  ", 16), bg="grey").grid(row=5, column=0, pady=10, padx=10)
    Label(cr2, text="DATE OF BIRTH", font=("Bold Arial  ", 16), bg="grey").grid(row=6, column=0, pady=10, padx=10)
    Label(cr2, text="OCCUPATION", font=("Bold Arial  ", 16), bg="grey").grid(row=7, column=0, pady=10, padx=10)
    Label(cr2, text="ADDRESS", font=("Bold Arial  ", 16), bg="grey").grid(row=8, column=0, pady=10, padx=10)

    Entry(cr2, textvariable=cname, font=("Courier New", 16), bg="pink", width=34).grid(row=3, column=1,columnspan=2, pady=10,
                                                                                       padx=10)
    Entry(cr2, textvariable=idn, font=("Courier New", 16), bg="pink", width=16).grid(row=4, column=1, pady=10,
                                                                                        padx=8)
    Entry(cr2, textvariable=nat, font=("Courier New", 16), bg="pink", width=16).grid(row=4, column=2, pady=10,
                                                                                       padx=8)
    Entry(cr2, textvariable=mob, font=("Courier New", 16), bg="pink", width=34).grid(row=5, column=1,columnspan=2, pady=10, padx=10)
    Entry(cr2, textvariable=date1, font=("Courier New", 16), bg="pink", width=16).grid(row=6, column=1, pady=10,
                                                                                       padx=10)
    Entry(cr2, textvariable=occup, font=("Courier New", 16), bg="pink", width=34).grid(row=7, column=1,columnspan=2, pady=10,
                                                                                        padx=10)

    Entry(cr2, textvariable=add1, font=("Courier New", 16), bg="pink", width=34).grid(row=8, column=1,columnspan=2, pady=10, padx=10)
    Entry(cr2, textvariable=dis1, font=("Courier New", 16), bg="pink", width=34).grid(row=9, column=1,columnspan=2, pady=10,padx=10)

    op = OptionMenu(cr2, gn, *Gender)
    op.config(font="Courier", bg="pink", width=14, height=1)
    op.grid(row=6, column=2, padx=8, pady=10)

    Button(cr2, text="<-BACK", font=("Copperplate Gothic Bold", 11), borderwidth=8, relief=GROOVE, width="16", height="1",
           bg="#ff66ff", command=onclick3).grid(row=12, column=1, pady=10, padx=10)
    Button(cr2, text="SUBMIT->", font=("Copperplate Gothic Bold", 11), borderwidth=8, relief=GROOVE, width="16", height="1",
           bg="green", command=onclick4).grid(row=12, column=2, pady=10, padx=10)
def opencr3():
    cr3=Toplevel(root)
    cr3.geometry('810x230')
    cr3.title('Loss of Life and Property')
    cr3.configure(bg="grey")
    cr3.iconbitmap('D:\.phy programme\pythonProject\CRS.ico')

    def onclick5():
        cr3.destroy()

    def onclick6():
        conn = sqlite3.connect('CRIMECASESRECORD.db')
        cur = conn.cursor()
        cur.execute("INSERT INTO R3 VALUES (:acc_name,:loss,:val)",
                   {
                       'acc_name': enter1.get(),
                       'loss': enter2.get(),
                       'val' : enter3.get(),
                   })

        conn.commit()
        conn.close()

        enter1.set(" ")
        enter2.set(" ")
        enter3.set(" ")

        cr3.destroy()
        messagebox.showinfo("showinfo", "Details are Saved")





    global enter1,enter2,enter3
    enter1 = StringVar(root)
    enter1.set("(If Known)")
    enter2 = StringVar(root)
    enter3 = StringVar(root)


    Label(cr3, text="ACCUSED DETAILS", font=("Bold Arial  ", 16), bg="grey").grid(row=3, column=0, pady=10, padx=10)
    Label(cr3, text="LOSS PARTICULARS", font=("Bold Arial  ", 16), bg="grey").grid(row=4, column=0, pady=10,
                                                                                              padx=10)
    Label(cr3, text="TOTAL LOSS VALUE", font=("Bold Arial  ", 16), bg="grey").grid(row=5, column=0,
                                                                                                 pady=10, padx=10)

    Entry(cr3, textvariable=enter1, font=("Courier New", 16), bg="pink", width=40).grid(row=3, column=1,columnspan=2, pady=10,
                                                                                         padx=10)
    Entry(cr3, textvariable=enter2, font=("Courier New", 16), bg="pink", width=40).grid(row=4, column=1,columnspan=2, pady=10,
                                                                                         padx=10)
    Entry(cr3, textvariable=enter3, font=("Courier New", 16), bg="pink", width=40).grid(row=5, column=1,columnspan=2, pady=10,
                                                                                         padx=10)


    Button(cr3, text="<-BACK", font=("Copperplate Gothic Bold", 12), borderwidth=8, relief=GROOVE, width="16", height="1",
           bg="#ff66ff", command=onclick5).grid(row=6, column=1, pady=10, padx=10)
    Button(cr3, text="SUBMIT->", font=("Copperplate Gothic Bold", 12), borderwidth=7, relief=GROOVE, width="16", height="1",
           bg="green", command=onclick6).grid(row=6, column=2, pady=10, padx=10)

def onclick3():
    cr4 = Toplevel(root)
    cr4.geometry('496x775')
    cr4.title('Details')
    cr4.configure(bg="dark grey")
    cr4.iconbitmap('D:\.phy programme\pythonProject\CRS.ico')

    print_str1 = " "
    print_str2 = " "
    print_str3 = " "

    def onclick7():
        cr4.destroy()
        messagebox.showinfo("showinfo", "Case is Registered")


    conn = sqlite3.connect('CRIMECASESRECORD.db')
    cur = conn.cursor()


    cur.execute("SELECT *, oid FROM R1")
    records1=cur.fetchall()
    count1=len(records1)

    for record1 in records1[count1-1]:
         print_str1 += str(record1) + "\n"

    cur.execute("SELECT *, oid FROM R2")
    records2=cur.fetchall()
    count2=len(records2)

    for record2 in records2[count2-1]:
        print_str2 += str(record2) + "\n"

    cur.execute("SELECT *, oid FROM R3")
    records3=cur.fetchall()
    count3=len(records3)

    for record3 in records3[count3-1]:
        print_str3 += str(record3) + "\n"

    conn.commit()
    conn.close()

    Label(cr4, text="         OFFENCE DETAILS       ", font=("COOPER BLACK", 18), fg="black",bg="light grey").grid(row=0, column=0)
    Label(cr4, text=" COMPLAINANT/INFORMANT DETAILS", font=("COOPER BLACK", 18), fg="black",bg="light grey").grid(row=2, column=0)
    Label(cr4, text="    LOSS PARTICULAR DETAILS    ", font=("COOPER BLACK", 18), fg="black",bg="light grey").grid(row=4, column=0)
    Label(cr4, text=print_str1, font=("Bookman Old Style", 15), bg="dark grey",fg="black").grid(row=1, column=0)
    Label(cr4, text=print_str2, font=("Bookman Old Style", 15), bg="dark grey",fg="black").grid(row=3, column=0)
    Label(cr4, text=print_str3, font=("Bookman Old Style", 15), bg="dark grey",fg="black").grid(row=5, column=0)
    Button(cr4, text="O K ", font=("Copperplate Gothic Bold", 13), borderwidth=8, relief=GROOVE, width="16", height="1",bg="light green", command=onclick7).grid(row=6, column=0, pady=10, padx=10)



def onclick4():
    MsgBox = tkinter.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application')
    if MsgBox == 'yes':
       root.destroy()




Label(root, text="File Report!", font=("Arial Rounded MT Bold", 50), bg="black", fg="white").place(x=60, y=19)

Button(root,text="Offence Details", font=("Berlin Sans FB",15),borderwidth=10,relief=RIDGE, width="30",height="1",bg="#cc6600",command=opencr1).place(x=70, y=150)
Button(root,text="Complainant / Informant", font=("Berlin Sans FB",15),borderwidth=10,relief=RIDGE, width="30",height="1",bg="#cc6600",command=opencr2).place(x=70, y=240)
Button(root,text="Loss of Life and Property", font=("Berlin Sans FB",15),borderwidth=10,relief=RIDGE, width="30",height="1",bg="#cc6600",command=opencr3).place(x=70, y=330)
Button(root,text="Register ", font=("Berlin Sans FB",15),borderwidth=10,relief=RIDGE, width="30",height="1",bg="#cc6600",command=onclick3).place(x=70, y=420)
Button(root,text="EXIT", font=("Berlin Sans FB",15),borderwidth=10,relief=RIDGE, width="30",height="1",bg="#cc6600",command=onclick4).place(x=70, y=510)
root.mainloop()
