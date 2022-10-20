from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector

class Insurance:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1530x850+0+0')
        self.root.title("INSURANCE RECORD MANAGEMENT SYSTEM")


        # All veriable Declaration
        self.var_policy_no = StringVar()
        self.var_agent_id = StringVar()
        self.var_Name = StringVar()
        self.var_Primium = StringVar()
        self.var_date_of_insurance = StringVar()
        self.var_due_date = StringVar()
        self.var_address = StringVar()
        self.var_age = StringVar()
        self.var_Nominee_name = StringVar()
        self.var_Phone_no = StringVar()
        self.var_insurance_type = StringVar()
        self.var_father_name = StringVar()
        self.var_gender = StringVar()
        self.var_Paid = StringVar()


        # TItle
        lbl_title = Label(self.root, text="INSURANCE RECORD MANAGEMENT SYSTEM SOFTWERE", font=('times new roman',40,'bold'), bg='black',fg='gold')
        lbl_title.place(x=0, y=0, width=1530,height=70)

        
        # Image Frame
        img_frame = Frame(self.root, bd = 2, relief = RIDGE, bg = 'White')
        img_frame.place(x = 0, y = 70, width=1530, height=130)


        # First Image
        img1 = Image.open('images (2).jpg')
        img1 = img1.resize((540, 160), Image.ANTIALIAS)
        self.photo1 = ImageTk.PhotoImage(img1)

        self.img_1 = Label(img_frame, image = self.photo1)
        self.img_1.place(x = 0, y = 0, width = 540, height = 160)


        # second Image
        img2 = Image.open('imag2.jpg')
        img2 = img2.resize((540, 160), Image.ANTIALIAS)
        self.photo2 = ImageTk.PhotoImage(img2)

        self.img_2 = Label(img_frame, image = self.photo2)
        self.img_2.place(x = 540, y = 0, width = 540, height = 160)


        #Third Image
        img3 = Image.open('img1.jpg')
        img3 = img3.resize((540, 160), Image.ANTIALIAS)
        self.photo3 = ImageTk.PhotoImage(img3)

        self.img_3 = Label(img_frame, image = self.photo3)
        self.img_3.place(x = 1080, y = 0, width = 540, height = 160)


        # Main Frame
        main_frame = Frame(self.root, bd = 2, relief = RIDGE, bg = 'White')
        main_frame.place(x = 10, y=200, width =1500, height=560)

        # Upper Frame in main frame
        upper_frame = LabelFrame(main_frame,  text="Policy Information", font=('times new roman',12,'bold'), bg='White',fg='red')
        upper_frame.place(x = 10, y=10, width =1480, height=270)

        # Policy Number Lable
        policy_no = Label(upper_frame, text='policy No: ', font='arial 11 bold', bg='white')
        policy_no.grid(row=0, column=0, padx=5, sticky=W)

        # Polic Number Entry
        case_entry = ttk.Entry(upper_frame,textvariable=self.var_policy_no, width=22, font='arial 11 bold')
        case_entry.grid(row=0, column=1, padx=5,pady=7, sticky=W)

        # Agent Id Lable
        lbl_agent_id = Label(upper_frame, text='Agent ID: ', font='arial 11 bold', bg='white')
        lbl_agent_id.grid(row=0, column=2, padx=7, sticky=W)

        # Agent Id Entry
        txt_agent_id = ttk.Entry(upper_frame,textvariable=self.var_agent_id, width=22, font='arial 11 bold')
        txt_agent_id.grid(row=0, column=3, padx=7, sticky=W)

        # Name Lable
        lbl_Name = Label(upper_frame, text='Name: ', font='arial 11 bold', bg='white')
        lbl_Name.grid(row=1, column=0, padx=5,pady=7, sticky=W)

        # Name Entry
        txt_name = ttk.Entry(upper_frame,textvariable=self.var_Name, width=22, font='arial 11 bold')
        txt_name.grid(row=1, column=1, padx=5,pady=7, sticky=W)

        # Primium Lable
        lbl_Primium = Label(upper_frame, text='Primium: ', font='arial 11 bold', bg='white')
        lbl_Primium.grid(row=1, column=2, padx=5,pady=7, sticky=W)

        #Primium Entry
        txt_Primium = ttk.Entry(upper_frame,textvariable=self.var_Primium, width=22, font='arial 11 bold')
        txt_Primium.grid(row=1, column=3, padx=5,pady=7, sticky=W)

        # Due Date Lable
        lbl_dueDate = Label(upper_frame, text='Due Date: ', font='arial 11 bold', bg='white')
        lbl_dueDate.grid(row=2, column=0, padx=5,pady=7, sticky=W)

        # Due Date Entry
        txt_dueDate = ttk.Entry(upper_frame,textvariable=self.var_date_of_insurance, width=22, font='arial 11 bold')
        txt_dueDate.grid(row=2, column=1, padx=5,pady=7, sticky=W)

        # Insurance Date
        lbl_dateOfinsurance = Label(upper_frame, text='Date of insurance: ', font='arial 11 bold', bg='white')
        lbl_dateOfinsurance.grid(row=2, column=2, padx=5,pady=7, sticky=W)

        # Insurance Date Entry
        txt_dateOfinsurance = ttk.Entry(upper_frame,textvariable=self.var_due_date, width=22, font='arial 11 bold')
        txt_dateOfinsurance.grid(row=2, column=3, padx=5,pady=7, sticky=W)

        # Address Lable
        lbl_address = Label(upper_frame, text='Address: ', font='arial 11 bold', bg='white')
        lbl_address.grid(row=3, column=0, padx=5,pady=7, sticky=W)

        # Address Entry
        txt_address = ttk.Entry(upper_frame,textvariable=self.var_address, width=22, font='arial 11 bold')
        txt_address.grid(row=3, column=1, padx=5,pady=7, sticky=W)

        # Age Lable
        lbl_age = Label(upper_frame, text='Age: ', font='arial 11 bold', bg='white')
        lbl_age.grid(row=3, column=2, padx=5,pady=7, sticky=W)

        # Age Entry
        txt_age = ttk.Entry(upper_frame,textvariable=self.var_age, width=22, font='arial 11 bold')
        txt_age.grid(row=3, column=3, padx=5,pady=7, sticky=W)

        # Nominee Name Lable
        lbl_Nominee_name = Label(upper_frame, text='Nominee Name: ', font='arial 11 bold', bg='white')
        lbl_Nominee_name.grid(row=4, column=0, padx=5,pady=7, sticky=W)

        # Nominee Name Entry
        txt_Nominee_name = ttk.Entry(upper_frame,textvariable=self.var_Nominee_name, width=22, font='arial 11 bold')
        txt_Nominee_name.grid(row=4, column=1, padx=5,pady=7, sticky=W)

        # Phone Number Lable
        lbl_Phone_no = Label(upper_frame, text='Phone No: ', font='arial 11 bold', bg='white')
        lbl_Phone_no.grid(row=4, column=2, padx=5,pady=7, sticky=W)

        # Phone Number Entry
        txt_Phone_no = ttk.Entry(upper_frame,textvariable=self.var_Phone_no, width=22, font='arial 11 bold')
        txt_Phone_no.grid(row=4, column=3, padx=5,pady=7, sticky=W)

        # Insurance Type Lable
        lbl_insuranceType = Label(upper_frame, text='insurance Type: ', font='arial 11 bold', bg='white')
        lbl_insuranceType.grid(row=0, column=4, padx=5,pady=7, sticky=W)

        # Insurance Type Entry
        txt_insuranceType = ttk.Entry(upper_frame,textvariable=self.var_insurance_type, width=22, font='arial 11 bold')
        txt_insuranceType.grid(row=0, column=5, padx=5,pady=7, sticky=W)

        # Father Name Lable
        lbl_fatherName = Label(upper_frame, text='Father Name: ', font='arial 11 bold', bg='white')
        lbl_fatherName.grid(row=1, column=4, padx=5,pady=7, sticky=W)

        # Father Name Entry
        txt_fatherName = ttk.Entry(upper_frame,textvariable=self.var_father_name, width=22, font='arial 11 bold')
        txt_fatherName.grid(row=1, column=5, padx=5,pady=7, sticky=W)

        # Gender Lable
        lbl_gender = Label(upper_frame, text='Gender: ', font='arial 11 bold', bg='white')
        lbl_gender.grid(row=2, column=4, padx=5,pady=7, sticky=W)

        # Frame For Gender Entry
        radio_frame_gender = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
        radio_frame_gender.place(x=755, y=90, width=180, height=30)

        # Male Radiobutton
        male = Radiobutton(radio_frame_gender, text='Male',variable=self.var_gender, value='male', font='arial 9 bold')
        male.grid(row=0, column=0, pady=2, padx=10, sticky=W)

        # Female Radiobutton
        female = Radiobutton(radio_frame_gender, text='Female',variable=self.var_gender, value='female', font='arial 9 bold')
        female.grid(row=0, column=1, pady=2, padx=10, sticky=W)

        # payment status Lable
        lbl_Paid = Label(upper_frame, text='Paid: ', font='arial 11 bold', bg='white')
        lbl_Paid.grid(row=3, column=4, padx=5,pady=7, sticky=W)

        # Frame for status Entry
        radio_frame_Paid = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
        radio_frame_Paid.place(x=755, y=130, width=180, height=30)

        # Yes Radiobutton
        yes = Radiobutton(radio_frame_Paid, text='Yes',variable=self.var_Paid, value='yes', font='arial 9 bold')
        yes.grid(row=0, column=0, pady=2, padx=10, sticky=W)

        # No Radiobutton
        no = Radiobutton(radio_frame_Paid, text='No',variable=self.var_Paid, value='no', font='arial 9 bold')
        no.grid(row=0, column=1, pady=2, padx=10, sticky=W)


        # Button Frame
        Button_frame = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
        Button_frame.place(x=5, y=200, width=620, height=45)

        # Button to add record
        btn_add = Button(Button_frame,command=self.add_data, text='Record Save', font='arial 13 bold', width=14, bg='blue', fg='white')
        btn_add.grid(row=0, column=0, padx=3, pady=5)

        # Update Button
        btn_update = Button(Button_frame,command=self.update_data, text='Update', font='arial 13 bold', width=14, bg='blue', fg='white')
        btn_update.grid(row=0, column=1, padx=3, pady=5)

        # Delete Button
        btn_delete = Button(Button_frame,command=self.delete_data, text='Delete', font='arial 13 bold', width=14, bg='blue', fg='white')
        btn_delete.grid(row=0, column=2, padx=3, pady=5)

        # Clear Button to clear all entry from entry fields
        btn_clear = Button(Button_frame,command=self.clear_data, text='Clear', font='arial 13 bold', width=14, bg='blue', fg='white')
        btn_clear.grid(row=0, column=3, padx=3, pady=5)

        # Image in upper frame
        img4 = Image.open('images (3).jpg')
        img4 = img4.resize((470, 245), Image.ANTIALIAS)
        self.photo4 = ImageTk.PhotoImage(img4)

        self.img_4 = Label(upper_frame, image = self.photo4)
        self.img_4.place(x = 1000, y = 0, width = 470, height = 245)

        

        # Lower Frame
        lower_frame = LabelFrame(main_frame,  text="Policy Record", font=('times new roman',12,'bold'), bg='White',fg='red')
        lower_frame.place(x = 10, y=280, width =1480, height=270)

        # Search Frame
        search_frame = LabelFrame(lower_frame,  text="Search Policy Record", font=('times new roman',12,'bold'), bg='White',fg='red')
        search_frame.place(x = 10, y=0, width =1455, height=60)

        # Search By lable
        search_by = Label(search_frame, text='Search By: ', font='arial 11 bold', bg='red', fg='white')
        search_by.grid(row=0, column=0, padx=5,pady=2, sticky=W)

        # Combobox to Search the records 
        self.var_com_search = StringVar()
        combo_search_box = ttk.Combobox(search_frame,textvariable=self.var_com_search, font='arial 11 bold', width=18, state='readonly')
        combo_search_box['value']=('Select Option', 'policy_no', 'agent_id')
        combo_search_box.current(0)
        combo_search_box.grid(row=0, column=1, sticky=W, padx=5)

        # Search By Entry
        self.var_search = StringVar()
        search_txt = ttk.Entry(search_frame,textvariable=self.var_search, width=18, font='arial 11 bold')
        search_txt.grid(row=0, column=2, padx=5, sticky=W)

        # Search Button
        btn_search = Button(search_frame,command=self.search_data, text='search', font='arial 13 bold', width=14, bg='blue', fg='white')
        btn_search.grid(row=0, column=3, padx=5, sticky=W)

        # Show All Button
        btn_show = Button(search_frame,command=self.fetch_data, text='Show All', font='arial 13 bold', width=14, bg='blue', fg='white')
        btn_show.grid(row=0, column=4, padx=5, sticky=W)

        # Lable in Search Frame
        insuranceagency = Label(search_frame, text='LIFE INSURANCE AGENCY', font='arial 25 bold', bg='white', fg='crimson')
        insuranceagency.grid(row=0, column=5, padx=5, sticky=W)


        # table Frame in lower frame
        table_frame = Frame(lower_frame, bd=2, relief=RIDGE)
        table_frame.place(x = 0, y=70, width =1470, height=170)


        # Scroll Bar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        # Treeview for table creation
        self.insurance_table = ttk.Treeview(table_frame, column=('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.config(command=self.insurance_table.xview)
        scroll_y.config(command=self.insurance_table.yview)

        # Fields name in table
        self.insurance_table.heading('1', text='Policy No')
        self.insurance_table.heading('2', text='Agent ID')
        self.insurance_table.heading('3', text='Name')
        self.insurance_table.heading('4', text='Primium')
        self.insurance_table.heading('5', text='Due Date')
        self.insurance_table.heading('6', text='Date of Insurance')
        self.insurance_table.heading('7', text='Address')
        self.insurance_table.heading('8', text='Age')
        self.insurance_table.heading('9', text='Nominee Name')
        self.insurance_table.heading('10', text='Phone No')
        self.insurance_table.heading('11', text='insurance Type')
        self.insurance_table.heading('12', text='Father Name')
        self.insurance_table.heading('13', text='Gender')
        self.insurance_table.heading('14', text='Paid')

        self.insurance_table['show']='headings'

        self.insurance_table.column('1', width=100)
        self.insurance_table.column('2', width=100)
        self.insurance_table.column('3', width=100)
        self.insurance_table.column('4', width=100)
        self.insurance_table.column('5', width=100)
        self.insurance_table.column('6', width=100)
        self.insurance_table.column('7', width=100)
        self.insurance_table.column('8', width=100)
        self.insurance_table.column('9', width=100)
        self.insurance_table.column('10', width=100)
        self.insurance_table.column('11', width=100)
        self.insurance_table.column('12', width=100)
        self.insurance_table.column('13', width=100)
        self.insurance_table.column('14', width=100)

        self.insurance_table.pack(fill=BOTH, expand=1)

        self.insurance_table.bind("<ButtonRelease>", self.get_cursor)

        self.fetch_data()


    # Function to add record in database
    def add_data(self):
        if self.var_policy_no.get() == "":
            messagebox.showerror('Error','All Fields are required')
        else:
            try:
                conn = mysql.connector.connect(host='localhost', user='root', password = 'Shivangi@123', database='management')
                my_cursor = conn.cursor()
                my_cursor.execute('insert into insurance values (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)', (self.var_policy_no.get(),
                                                                                                                    self.var_agent_id.get(),
                                                                                                                    self.var_Name.get(),
                                                                                                                    self.var_Primium.get(),
                                                                                                                    self.var_date_of_insurance.get(),
                                                                                                                    self.var_due_date.get(),
                                                                                                                    self.var_address.get(),
                                                                                                                    self.var_age.get(),
                                                                                                                    self.var_Nominee_name.get(),
                                                                                                                    self.var_Phone_no.get(),
                                                                                                                    self.var_insurance_type.get(),
                                                                                                                    self.var_father_name.get(),
                                                                                                                    self.var_gender.get(),
                                                                                                                    self.var_Paid.get()))
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()                      
                messagebox.showinfo('Success', 'Policy record has been added')
            
            except Exception as es:
                messagebox.showerror('Error', f'Due to {str(es)}')
    
    
    # Function to retrieve all information from the database
    def fetch_data(self):
        conn = mysql.connector.connect(host='localhost', user='root', password = 'Shivangi@123', database='management')
        my_cursor = conn.cursor()
        my_cursor.execute('select * from insurance')
        data = my_cursor.fetchall()
        if len(data) != 0:
            self.insurance_table.delete(*self.insurance_table.get_children())
            for i in data:
                self.insurance_table.insert('', END, values=i)
            conn.commit()
        conn.close()


    def get_cursor(self, event=""):
        cursor_row = self.insurance_table.focus()
        content = self.insurance_table.item(cursor_row)
        data = content['values']
        self.var_policy_no.set(data[0])
        self.var_agent_id.set(data[1])
        self.var_Name.set(data[2])
        self.var_Primium.set(data[3])
        self.var_date_of_insurance.set(data[4])
        self.var_due_date.set(data[5])
        self.var_address.set(data[6])
        self.var_age.set(data[7])
        self.var_Nominee_name.set(data[8])
        self.var_Phone_no.set(data[9])
        self.var_insurance_type.set(data[10])
        self.var_father_name.set(data[11])
        self.var_gender.set(data[12])
        self.var_Paid.set(data[13])


    # Function to update some record
    def update_data(self):
        if self.var_policy_no.get() == "":
            messagebox.showerror('Error','All Fields are required')
        else:
            try:
                update = messagebox.askyesno('Update', 'Are you sure you want to update this Policy record')
                if update >0:
                    conn = mysql.connector.connect(host='localhost', user='root', password = 'Shivangi@123', database='management')
                    my_cursor = conn.cursor()
                    my_cursor.execute('update insurance set agent_id=%s, name=%s, Primium=%s, date_of_insurance=%s, due_date=%s, address=%s, age=%s, Nominee_name=%s, Phone_no=%s, insuranceType=%s, FatherName=%s, gender=%s, Paid=%s where policy_no=%s',(self.var_agent_id.get(),
                                                                                                                                                                                                                                                                self.var_Name.get(),
                                                                                                                                                                                                                                                                self.var_Primium.get(),
                                                                                                                                                                                                                                                                self.var_date_of_insurance.get(),
                                                                                                                                                                                                                                                                self.var_due_date.get(),
                                                                                                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                                                                                                self.var_age.get(),
                                                                                                                                                                                                                                                                self.var_Nominee_name.get(),
                                                                                                                                                                                                                                                                self.var_Phone_no.get(),
                                                                                                                                                                                                                                                                self.var_insurance_type.get(),
                                                                                                                                                                                                                                                                self.var_father_name.get(),
                                                                                                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                                                                                                self.var_Paid.get(),
                                                                                                                                                                                                                                                                self.var_policy_no.get()))
                
                else:
                    if not update:
                        return 
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('Success', 'Policy record has been successfully updated')

            except Exception as es:
                messagebox.showerror('Error', f'Due to {str(es)}')

    # Function to dalete data from database
    def delete_data(self):
        if self.var_policy_no.get() == "":
            messagebox.showerror('Error','All Fields are required')
        else:
            try:
                delete = messagebox.askyesno('Delete', 'Are you sure you want to delete this Policy record')
                if delete >0:
                    conn = mysql.connector.connect(host='localhost', user='root', password = 'Shivangi@123', database='management')
                    my_cursor = conn.cursor()
                    sql = 'delete from insurance where policy_no=%s'
                    Value = (self.var_policy_no.get(),)
                    my_cursor.execute(sql,Value)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('Success', 'Policy record has been successfully deleted')

            except Exception as es:
                messagebox.showerror('Error', f'Due to {str(es)}')


    # Function to clear data from the entry fields
    def clear_data(self):
        self.var_policy_no.set("")
        self.var_agent_id.set("")
        self.var_Name.set("")
        self.var_Primium.set("")
        self.var_date_of_insurance.set("")
        self.var_due_date.set("")
        self.var_address.set("")
        self.var_age.set("")
        self.var_Nominee_name.set("")
        self.var_Phone_no.set("")
        self.var_insurance_type.set("")
        self.var_father_name.set("")
        self.var_gender.set("")
        self.var_Paid.set("")


    # Function to search data
    def search_data(self):
        if self.var_com_search.get() == "":
            messagebox.showerror('Error','All Fields are required')
        else:
            try:
                conn = mysql.connector.connect(host='localhost', user='root', password = 'Shivangi@123', database='management')
                my_cursor = conn.cursor()
                my_cursor.execute('select * from insurance where ' +str(self.var_com_search.get())+" like '%"+str(self.var_search.get()+"%'"))
                rows = my_cursor.fetchall()
                if len(rows) != 0:
                    self.insurance_table.delete(*self.insurance_table.get_children())
                    for i in rows:
                        self.insurance_table.insert('', END, values=i)
                conn.commit()
                conn.close()

            except Exception as es:
                messagebox.showerror('Error', f'Due to {str(es)}')



if __name__ == "__main__":
    root = Tk()
    obj = Insurance(root)
    root.mainloop()
