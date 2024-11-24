from collections.abc import Buffer
from tkinter import *
import math,random,os
from tkinter import messagebox

class Bill_App:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color = "#074463"
        title = Label(self.root , text = "Billing Software",bd= 12,relief = GROOVE,bg=bg_color,fg= "white",font = ("times new roman",30,"bold"),pady = 2).pack(fill=X)


        self.soap = IntVar()
        self.face_cream = IntVar()
        self.face_wash = IntVar()
        self.spray = IntVar()
        self.gell = IntVar()
        self.lotion = IntVar()

        self.rice = IntVar()
        self.food_oil = IntVar()
        self.daal = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.tea_leaves = IntVar()

        self.tea = IntVar()
        self.coffee = IntVar()
        self.cold_drink = IntVar()
        self.milk = IntVar()
        self.lassi = IntVar()
        self.juice = IntVar()


        #=============Total Product price & tax Variable=========#
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drink_price=StringVar()

        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.cold_drink_tax=StringVar()

        #============Customer==========#
        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()

        F1= LabelFrame(self.root, bd=10,relief=GROOVE,text="Customer Details", font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_label= Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt = Entry(F1,width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5)

        cphone_label= Label(F1,text="Phone Number",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphone_txt = Entry(F1,width=15,textvariable=self.c_phon,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=5)

        c_bill_label= Label(F1,text="Bill Number",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
        c_bill_txt = Entry(F1,width=15,textvariable=self.search_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,padx=10,pady=5)

        bill_btn = Button(F1,text="Search",width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,pady=10,padx=15)

        F2 = LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmetics", font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=180,width=325,height=380)

        bath_lbl = Label(F2,text="Bath soap",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(F2,width=10,textvariable=self.soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        face_cream_lbl = Label(F2,text="Face Cream",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        face_cream_txt=Entry(F2,width=10,textvariable=self.face_cream,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        face_w_lbl = Label(F2,text="Face Wash",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        face_w_txt=Entry(F2,width=10,textvariable=self.face_wash,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        hair_s_lbl = Label(F2,text="Hair Shampoo",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        hair_s_txt=Entry(F2,width=10,textvariable=self.spray,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)


        hair_g_lbl = Label(F2,text="Hair Gel",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        hair_g_txt=Entry(F2,width=10,textvariable=self.gell,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        body_lbl = Label(F2,text="Body Lotion",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        body_txt=Entry(F2,width=10,textvariable=self.lotion,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        F3 = LabelFrame(self.root,bd=10,relief=GROOVE,text="Groceries", font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=325,y=180,width=325,height=380)

        rice_lbl = Label(F3,text="Rice",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        rice_txt=Entry(F3,width=10,textvariable=self.rice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        oil_cream_lbl = Label(F3,text="Food Oil",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        oil_cream_txt=Entry(F3,width=10,textvariable=self.food_oil,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        daal_lbl = Label(F3,text="Daal",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        daal_txt=Entry(F3,width=10,textvariable=self.daal,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        wheat_lbl = Label(F3,text="Wheat",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        wheat_txt=Entry(F3,width=10,textvariable=self.wheat,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        sugar_lbl = Label(F3,text="Sugar",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        sugar_txt=Entry(F3,width=10,textvariable=self.sugar,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        tea_lbl = Label(F3,text="Tea Leaves",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        tea_txt=Entry(F3,width=10,textvariable=self.tea_leaves,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        F4 = LabelFrame(self.root,bd=10,relief=GROOVE,text="Drinks", font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=644,y=180,width=325,height=380)

        tea_lbl = Label(F4,text="Tea",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        tea_txt=Entry(F4,width=10,textvariable=self.tea,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        coffee_lbl = Label(F4,text="Coffee",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        coffee_cream_txt=Entry(F4,width=10,textvariable=self.coffee,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        cold_drink_lbl = Label(F4,text="Cold Drink",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        cold_drink_txt=Entry(F4,width=10,textvariable=self.cold_drink,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        milk_lbl = Label(F4,text="Milk",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        milk_txt=Entry(F4,width=10,textvariable=self.milk,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)


        lassi_lbl = Label(F4,text="Lassi",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        lassi_txt=Entry(F4,width=10,textvariable=self.lassi,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        juice_lbl = Label(F4,text="Juice",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        juice_txt=Entry(F4,width=10,textvariable=self.juice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)


        F5 =Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=990,y=180,width=340,height=380)

        bill_title = Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scroll_y = Scrollbar(F5,orient=VERTICAL)
        self.textarea=Text(F5,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)


        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu", font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F6.place(x=0,y=560,relwidth=1,height=140)

        m1_lbl=Label(F6,text="Total Cosmetic price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_text=Entry(F6,width=18,textvariable=self.cosmetic_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=5,pady=1)

        m2_lbl=Label(F6,text="Total Grocery price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_text=Entry(F6,width=18,textvariable=self.grocery_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=5,pady=1)

        m3_lbl=Label(F6,text="Total Cold Drinks price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_text=Entry(F6,width=18,textvariable=self.cold_drink_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=5,pady=1)

        c1_lbl=Label(F6,text= "Cosmetic Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        c1_text=Entry(F6,width=18,textvariable=self.cosmetic_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=5,pady=1)

        c2_lbl=Label(F6,text="Grocery Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        c2_text=Entry(F6,width=18,textvariable=self.grocery_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=5,pady=1)

        c3_lbl=Label(F6,text="Cold Drinks Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        c3_text=Entry(F6,width=18,textvariable=self.cold_drink_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=5,pady=1)

        btn_F=Frame(F6,bd=7,relief=GROOVE,bg=bg_color)
        btn_F.place(x=750,width=580,height=105)

        total_btn=Button(btn_F,command=self.total,text="Total",bg="grey",font="arial 12 bold",bd=5,width=11,fg="black",pady=15).grid(row=0,column=0,padx=8,pady=5)
        Gbill_btn=Button(btn_F,text="Generate bill",command=self.bill_area,bg="grey",font="arial 12 bold",bd=5,width=11,fg="black",pady=15).grid(row=0,column=1,padx=5,pady=5)
        Clear_btn=Button(btn_F,text="Clear",bg="grey",font="arial 12 bold",bd=5,width=11,fg="black",pady=15).grid(row=0,column=2,padx=5,pady=5)
        Exit_btn=Button(btn_F,text="Exit",bg="grey",font="arial 12 bold",bd=5,width=11,fg="black",pady=15).grid(row=0,column=3,padx=5,pady=5)

        self.welcome_bill()

    def total(self):
        #=============Single Cosmetic product price calculate===========#
        self.c_s_p=self.soap.get()*40
        self.f_c_p=self.face_cream.get()*150
        self.f_w_p=self.face_wash.get()*240
        self.s_p=self.spray.get()*220
        self.g_p=self.gell.get()*120
        self.l_p=self.lotion.get()*200

        #=============Total of Cosmetic================#
        self.total_cosmetic_price=float(
                                    self.c_s_p+
                                    self.f_c_p+
                                    self.f_w_p+
                                    self.s_p+
                                    self.g_p+
                                    self.l_p
                                    )
        self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price))
        self.c_tax=round((self.total_cosmetic_price * 0.05), 2)
        self.cosmetic_tax.set("Rs. " + str(self.c_tax))

        #=============Single grocery product price calculate===========#
        self.r_p=self.rice.get() * 100
        self.f_o_p=self.food_oil.get() * 110
        self.d_p=self.daal.get() * 50
        self.w_p=self.wheat.get() * 300
        self.s_u_p=self.sugar.get() * 42
        self.t_p=self.tea.get() * 150

        #=============Total of grocery================#
        self.total_grocery_price = float(
                                     self.r_p +
                                     self.f_o_p+
                                     self.d_p+
                                     self.w_p +
                                     self.s_u_p +
                                     self.t_p
                                     )
        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price * 0.1), 2)
        self.grocery_tax.set("Rs. " + str(self.g_tax))

        #=============Single drink product price calculate===========#
        self.t_p_p=self.tea.get()*15
        self.c_p=self.coffee.get()*25
        self.c_d_p=self.cold_drink.get()*95
        self.m_p=self.milk.get()*29
        self.l_s_p=self.lassi.get()*40
        self.j_p=self.juice.get()*110

        #=============Total of Drink================#

        self.total_drink_price = float(
                                     self.t_p_p +
                                     self.c_p +
                                     self.c_d_p+
                                     self.m_p +
                                     self.l_s_p +
                                     self.j_p
                                     )
        self.cold_drink_price.set("Rs. "+str(self.total_drink_price))
        self.d_tax=round((self.total_drink_price * 0.05), 2)
        self.cold_drink_tax.set("Rs. " + str(self.d_tax))

        self.Total_bill=float(   self.total_cosmetic_price+
                                 self.total_grocery_price+
                                 self.total_drink_price+
                                 self.c_tax+
                                 self.g_tax+
                                 self.d_tax
                              )

    def welcome_bill(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END,"\tWelcome to Retail\n")
        self.textarea.insert(END,f"\nBill Number :  {self.bill_no.get()}")
        self.textarea.insert(END,f"\nCustomer Name : {self.c_name.get()}")
        self.textarea.insert(END,f"\nPhone Number : {self.c_phon.get()}")
        self.textarea.insert(END,f"\n=====================================")
        self.textarea.insert(END,f"\n Products\t\tQTY\t\tPrice")
        self.textarea.insert(END,f"\n=====================================")

    def bill_area(self):
        if self.c_name.get()=="" or self.c_phon.get()=="":
            messagebox.showerror("Error","Customer Details Invalid")
        elif self.cosmetic_price.get()=="Rs . 0.0" and self.grocery_price.get()=="Rs . 0.0" and self.cold_drink_price.get()=="Rs . 0.0":
            messagebox.showerror("Error", "No Product Purchased")
        else:
            self.welcome_bill()
            #======Cosmetics=======#
            if self.soap.get()!=0:
                self.textarea.insert(END, f"\n Bath Soap\t\t{self.soap.get()}\t\t{self.c_s_p}")

            if self.face_cream.get() != 0:
                self.textarea.insert(END, f"\n Face Cream\t\t{self.face_cream.get()}\t\t{self.f_c_p}")

            if self.face_wash.get() != 0:
                self.textarea.insert(END, f"\n Face Wash\t\t{self.face_wash.get()}\t\t{self.f_w_p}")

            if self.spray.get() != 0:
                self.textarea.insert(END, f"\n Spray\t\t{self.spray.get()}\t\t{self.s_p}")

            if self.gell.get() != 0:
                self.textarea.insert(END, f"\n Gell\t\t{self.gell.get()}\t\t{self.g_p}")

            if self.lotion.get() != 0:
                self.textarea.insert(END, f"\n Lotion\t\t{self.lotion.get()}\t\t{self.l_p}")


            # ======Grocery=======#
            if self.rice.get() != 0:
                self.textarea.insert(END, f"\n Rice\t\t{self.rice.get()}\t\t{self.r_p}")

            if self.food_oil.get() != 0:
                self.textarea.insert(END, f"\n Food Oil\t\t{self.food_oil.get()}\t\t{self.f_o_p}")

            if (self.daal.get() != 0):
                self.textarea.insert(END, f"\n Daal\t\t{self.daal.get()}\t\t{self.d_p}")

            if self.wheat.get() != 0:
                self.textarea.insert(END, f"\n Wheat\t\t{self.wheat.get()}\t\t{self.w_p}")

            if self.sugar.get() != 0:
                self.textarea.insert(END, f"\n Sugar\t\t{self.sugar.get()}\t\t{self.s_u_p}")

            if self.tea.get() != 0:
                self.textarea.insert(END, f"\n Tea\t\t{self.tea.get()}\t\t{self.t_p}")

            self.textarea.insert(END,f"\n-------------------------------------")

            if self.cosmetic_tax.get()!="Rs. 0.0":
                self.textarea.insert(END, f"\n Cosmetic Tax\t\t\t{self.cosmetic_tax.get()}")

            if self.grocery_tax.get()!="Rs. 0.0":
                self.textarea.insert(END, f"\n Grocery Tax\t\t\t{self.grocery_tax.get()}")

            if self.cold_drink_tax.get()!="Rs. 0.0":
                self.textarea.insert(END, f"\n Drinks Tax\t\t\t{self.cold_drink_tax.get()}")

            self.textarea.insert(END, f"\n TOTAL BILL : \t\t\t Rs. {self.Total_bill}")
            self.textarea.insert(END,f"\n-------------------------------------")

            self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the bill?")
        if op>0:
            self.bill_data = self.textarea.get('1.0',END)
            f1 = open("bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill no. : {self.bill_no.get()} saved successfully")
        else:
            return

    def find_bill(self):
        for i in os.listdir("bill/"):
            print(i)


root = Tk()
obj = Bill_App(root)
root.mainloop()
