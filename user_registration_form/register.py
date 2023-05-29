from tkinter import *
from tkinter import Tk,ttk,Label
from tkinter import messagebox
import re
import mysql.connector
import pyttsx3


class Register():
    def __init__(self,root):
        self.root=root
        self.root.title("Register Page")
        self.root.geometry('1600x790+0+0')
        
        #text-to-speech
        self.engine=pyttsx3.init()
        self.voices=self.engine.getProperty("voices")
        self.engine.setProperty("voice",self.voices[1].id)



        #variable
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.country_var=StringVar()
        self.contact_var=StringVar()
        self.gender_var=StringVar()
        self.id_var=StringVar()
        self.id_no_var=StringVar()
        self.password=StringVar()
        self.confirm_pass=StringVar()
        self.check_var=StringVar()


        #title frame
        title_frame=Frame(self.root,bd=1,relief=RIDGE)
        title_frame.place(x=450,y=28,width=550,height=82)

        
        #title_Label
        title_lbl=Label(title_frame,text='USER REGISTER FORM',font=('times new roman',30,'bold'),fg='darkblue')
        title_lbl.place(x=10,y=10)
        
        #information frame
        main_frame=Frame(self.root,bd=1,relief=RIDGE)
        main_frame.place(x=450,y=110,width=550,height=620)
        

        #username
        user_name=Label(main_frame,text='Username:',font=('times new roman',16,'bold'))
        user_name.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        user_entry=ttk.Entry(main_frame,textvariable=self.name_var,font=('times new roman',15,'bold'),width=25)
        user_entry.grid(row=0,column=1,padx=10,pady=10,sticky=W)
        
        #callback and validation
        validate_name=self.root.register(self.checkname)
        user_entry.config(validate='key',validatecommand=(validate_name,'%P'))


        
        #email
        email_lbl=Label(main_frame,text='Email:',font=('times new roman',16,'bold'))
        email_lbl.grid(row=1,column=0,padx=10,pady=10,sticky=W)
        
        
        txt_email=ttk.Entry(main_frame,textvariable=self.email_var,font=('times new roman',15),width=25)
        txt_email.grid(row=1,column=1,padx=10,pady=10,sticky=W)
        

        #contact
        
        contactno=Label(main_frame,text='Contact No:',font=('times new roman',16,'bold'))
        contactno.grid(row=2,column=0,padx=10,pady=10,sticky=W)
        
        
        entry_contact=ttk.Entry(main_frame,textvariabl=self.contact_var,font=('times new roman',15),width=25)
        entry_contact.grid(row=2,column=1,padx=10,pady=10,sticky=W)

        
        #callback and validation
        validate_contact=self.root.register(self.checkcontact)
        entry_contact.config(validate='key',validatecommand=(validate_contact,'%P'))

        #gender
        gender_lbl=Label(main_frame,text='Select Gender:',font=('times new roman',16,'bold'))
        gender_lbl.grid(row=3,column=0,padx=10,pady=10,sticky=W)
        
        #gender_frame
        gender_frame=Frame(main_frame,bd=2,relief=RIDGE)
        gender_frame.place(x=200,y=160,width=280,height=35)

        radio_male=Radiobutton(gender_frame,variable=self.gender_var,value='Male',text='Male',font=('times new roman',15))
        radio_male.grid(row=0,column=0,padx=10,pady=0,sticky=W)
        self.gender_var.set('Male')
        
        radio_female=Radiobutton(gender_frame,variable=self.gender_var,value='Female',text='Female',font=('times new roman',15))
        radio_female.grid(row=0,column=1,padx=10,pady=0,sticky=W)
        

        #country
        
        select_country=Label(main_frame,text='Select Country:',font=('times new roman',16,'bold'))
        select_country.grid(row=4,column=0,padx=10,pady=10,sticky=W)

        list=['India','UK','Japan','Nepal','USA']
        droplist=OptionMenu(main_frame,self.country_var,*list)
        droplist.config(width=21,font=('times new roman',15),bg='white')
        self.country_var.set('Select Country')
        droplist.grid(row=4,column=1,padx=10,pady=10,sticky=W)

        #id
        id_type=Label(main_frame,text='Select Id type:',font=('times new roman',16,'bold'))
        id_type.grid(row=5,column=0,padx=10,pady=10,sticky=W)
        
        self.combo_id_type=ttk.Combobox(main_frame,textvariable=self.id_var,font=('times new roman',15),justify='center',state='readonly',width=23)
        self.combo_id_type['values']=("select your id","Adhar card","Passport","Driving License","Pan card")
        self.combo_id_type.grid(row=5,column=1,padx=10,pady=10,sticky=W)
        self.combo_id_type.current(0)

        #id number
        
        id_no=Label(main_frame,text='ID No:',font=('times new roman',16,'bold'))
        id_no.grid(row=6,column=0,padx=10,pady=10,sticky=W)
        
        
        entry_id_no=ttk.Entry(main_frame,textvariable=self.id_no_var,font=('times new roman',15),width=25)
        entry_id_no.grid(row=6,column=1,padx=10,pady=10,sticky=W)

        #password
        s_password=Label(main_frame,text='Password:',font=('times new roman',16,'bold'))
        s_password.grid(row=7,column=0,padx=10,pady=10,sticky=W)
        
        
        entry_pass=ttk.Entry(main_frame,textvariable=self.password,font=('times new roman',15),width=25)
        entry_pass.grid(row=7,column=1,padx=10,pady=10,sticky=W)

        #confirm password
        
        c_password=Label(main_frame,text=' Confirm Password:',font=('times new roman',16,'bold'))
        c_password.grid(row=8,column=0,padx=10,pady=10,sticky=W)
        
        
        entry_confirm=ttk.Entry(main_frame,textvariable=self.confirm_pass,font=('times new roman',15),width=25)
        entry_confirm.grid(row=8,column=1,padx=10,pady=10,sticky=W)


        #check frame
        check_frame=Frame(main_frame)
        check_frame.place(x=130,y=460,width=400,height=70)

        check_btn=Checkbutton(check_frame,variable=self.check_var,text="Agree our terms and condition",font=('times new roman',16),onvalue=1,offvalue=0)
        check_btn.grid(row=0,column=0,padx=10,sticky=W)

        self.check_lbl=Label(check_frame,text="",font=('times new roman',16),fg='red')
        self.check_lbl.grid(row=1,column=0,padx=10,sticky=W)

         #button frame
        btn_frame=Frame(main_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=30,y=530,width=480,height=70)

        save_data=Button(btn_frame,text='Save',command=self.validation,font=('times new roman',16,'bold'),width=12,cursor='hand2')
        save_data.grid(row=0,column=0,padx=1,sticky=W)

        
        verify_data=Button(btn_frame,command=self.verify_data,text='Verify',font=('times new roman',16,'bold'),width=12,cursor='hand2')
        verify_data.grid(row=0,column=1,padx=1,sticky=W)

        
        clear_data=Button(btn_frame,command=self.clear_data,text='Clear',font=('times new roman',16,'bold'),width=12,cursor='hand2')
        clear_data.grid(row=0,column=2,padx=1,sticky=W)
        
        
        
#call back function
    def checkname(self,name):
       if name.isalnum():
         return True
       if name=="":
         return True
       else:
         messagebox.showerror('Invalid','Not Allowed'+name[-1])

#contct function
    def checkcontact(self,contact):
      if contact.isdigit():
        return True
      if len(str(contact))==0:
        return True
      else:
        messagebox.showerror("Invalid","Invalid Entry")
        return False   

#passwrd function   
    def checkpassword(self,password):
        if len(password)<=21:
            if re.match("^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])", password):
             return True
            else:
              messagebox.showinfo("invalid","Enter valid password(Example:kIshan@123)")
              return False
        else:
            messagebox.showinfo("invalid","Length exceed")
            return False

    

#email function
    def checkemail(self,email):
       if len(email)>7:
          if re.match("^([a-zA-Z0-9_\-\.]+)@[a-zA-Z0-9_\-\.]+\.[a-zA-Z0]{2,5}$", email):
             return True
          else:
             messagebox.showwarning("Alert","invalid email enter valid user email(example:xyz@gmail.com)")
             return False
       else:
          messagebox.showinfo("Invalid","Email length is to small")
#validation
    def validation(self):
       x=y=0
       if self.name_var.get()=="":
          self.engine.say("please enter your name")
          self.engine.runAndWait()
          messagebox.showerror("Error","please enter your name",parent=self.root)
       elif self.email_var.get()=="":
          self.engine.say("please enter your emailid")
          self.engine.runAndWait()
          messagebox.showerror("Error","please enter your emailid",parent=self.root)
       elif self.contact_var.get()=="" or len(self.contact_var.get())!=10:
          self.engine.say("please enter your contact valid")
          self.engine.runAndWait()
          messagebox.showerror("Error","please enter your contact valid",parent=self.root)  
       elif self.gender_var.get()=="":
          self.engine.say("please enter your gender")
          self.engine.runAndWait()
          messagebox.showerror("Error","please enter your gender",parent=self.root)
       elif self.country_var.get()=="" or self.country_var.get()=="select your country":
          self.engine.say("please enter your country")
          self.engine.runAndWait()
          messagebox.showerror("Error","please enter your country",parent=self.root)
       elif self.password.get()=="":
          self.engine.say("please enter your password correct")
          self.engine.runAndWait()
          messagebox.showerror("Error","please enter your password correct",parent=self.root)
       elif self.id_var.get()=="select your id":
          self.engine.say("please enter your id valid")
          self.engine.runAndWait()
          messagebox.showerror("Error","please enter your id valid",parent=self.root)
       elif len(self.id_no_var.get())!=14:
          self.engine.say("please enter your id number valid")
          self.engine.runAndWait()
          messagebox.showerror("Error","please enter your id number valid",parent=self.root)
       elif self.confirm_pass.get()=="":
          self.engine.say("please enter your password correctly")
          self.engine.runAndWait()
          messagebox.showerror("Error","please enter your password correctly",parent=self.root)
       elif self.password.get()!=self.confirm_pass.get():
          self.engine.say("Password and confirm password must be same")
          self.engine.runAndWait()
          messagebox.showerror("Error","Password and confirm password must be same",parent=self.root)
       elif self.email_var.get()!=None and self.password.get()!=None:
          x=self.checkemail(self.email_var.get())
          y=self.checkpassword(self.password.get())
       
       
          if(x==True) and (y==True):
           if self.check_var.get()==0:
            self.engine.say("Agree our terms and condition")
            self.engine.runAndWait()
            self.check_lbl.config(text="Agree our terms and condition",fg='red')
           else:
             self.check_lbl.config(text="Checked",fg="green")
             
             
           try:
                conn=mysql.connector.connect(host='localhost',username='root',password='manager',database='mydata')
                my_cursur=conn.cursor()
                my_cursur.execute('insert into register values(%s,%s,%s,%s,%s,%s,%s,%s)',(self.name_var.get(),self.email_var.get(),self.contact_var.get(),self.gender_var.get(),self.country_var.get(),self.id_var.get(),self.id_no_var.get(),self.password.get()))
                conn.commit()
                conn.close()
                messagebox.showinfo("Successfully",f"your registration is done your username:{self.name_var.get()} and your password:{self.password.get()}")
           except Exception as es:
                messagebox.showerror('Error',f'Due to:{str(es)}',parent=self.root)
                
    def verify_data(self):
       data=f'Name:{self.name_var.get()}\nEmail:{self.email_var.get()}\ncontact:{self.contact_var.get()}\nGender:{self.gender_var.get()}\ncountry:{self.country_var.get()}\npassword:{self.password.get()}\nID:{self.id_var.get()}\nID_No:{self.id_no_var.get()}'
       messagebox.showinfo("Details",data)
      
    
    def clear_data(self):
       
        self.name_var.set('')
        self.email_var.set('')
        self.country_var.set('select your country')
        self.contact_var.set('')
        self.gender_var.set('Male')
        self.id_var.set('select your Id')
        self.id_no_var.set('')
        self.password.set('')
        self.confirm_pass.set('')
        self.check_var.set(0)


              
                             




      

if __name__=="__main__":
    root=Tk()
    obj=Register(root)
    root.mainloop()

