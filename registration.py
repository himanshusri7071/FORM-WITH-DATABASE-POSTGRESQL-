import tkinter as tk
from tkinter import ttk
from csv import DictWriter
import os
win=tk.Tk()
win.title('CHECK')
"""menubar=tk.Menu(win)
menubar.add_command(label='save')
win.configure(menu=menubar)"""

nb=ttk.Notebook(win)
page1=ttk.Frame(nb)
page2=ttk.Frame(nb)
page3=ttk.Frame(nb)
page4=ttk.Frame(nb)
page5=ttk.Frame(nb)
nb.add(page1,text='HOME')
nb.add(page2,text='HELP')
nb.add(page3,text='about')
nb.add(page4,text='info')
nb.add(page5,text='apply')
nb.grid(row='0',column='0')
nb.grid(row='0',column='0')
nb.grid(row='0',column='0')
nb.grid(row='0',column='0')
nb.grid(row='0',column='0')
#nb.pack(expand=True,fill='both')


#labelframe
label=ttk.LabelFrame(page1,text="Please enter the details")
label.grid(row=1,column=0,padx=300)

#details
name=ttk.Label(label,text="Enter your name :")
name.grid(row=0,column=0,sticky=tk.W,padx=12,pady=12)

age=ttk.Label(label,text="Enter your age:")
age.grid(row=1,column=0,sticky=tk.W,padx=12,pady=12)

gender=ttk.Label(label,text="Enter your gender :")
gender.grid(row=2,column=0,sticky=tk.W,padx=12,pady=12)

adhar=ttk.Label(label,text="Enter your adhar card number :")
adhar.grid(row=4,column=0,sticky=tk.W,padx=12,pady=12)

mobile=ttk.Label(label,text="mobile number:")
mobile.grid(row=3,column=0,sticky=tk.W,padx=12,pady=12)

type_Label=ttk.Label(label,text="user type:")
type_Label.grid(row=5,column=0,sticky=tk.W,padx=12,pady=12)

option_Label=ttk.Label(label,text="option:")
option_Label.grid(row=6,column=0,sticky=tk.W,padx=12,pady=12)
#box
namev=tk.StringVar()
namee=ttk.Entry(label,width=16,textvariable=namev)
namee.grid(row=0,column=1,padx=12,pady=12)
namee.focus()

agev=tk.StringVar()
agee=ttk.Entry(label,width=16,textvariable=agev)
agee.grid(row=1,column=1,padx=12,pady=12)

genderv=tk.StringVar()
gendere=ttk.Combobox(label,width=16,textvariable=genderv,state='readonly')
gendere['values']=('male','female','other')
gendere.grid(row=2,column=1,padx=12,pady=12)
gendere.current(0)

mobilev=tk.StringVar()
mobilee=ttk.Entry(label,width=16,textvariable=mobilev)
mobilee.grid(row=3,column=1,padx=12,pady=12)


adharvv=tk.StringVar()
adhare=ttk.Entry(label,width=16,textvariable=adharvv)
adhare.grid(row=4,column=1,padx=12,pady=12)

#
#optionv=tk.StringVar()
#optione=ttk.Entry(label,width=16,textvariable=optionv)
#optione.grid(row=5,column=1,padx=12,pady=12)

#radiobutton
nation=tk.StringVar()
radiobuttn1=ttk.Radiobutton(label,text='INDIAN',value='indian',variable=nation)
radiobuttn1.grid(row=6,column=0)

radiobuttn2=ttk.Radiobutton(label,text='non indian',value='non indian',variable=nation)
radiobuttn2.grid(row=6,column=1)
 
#checkbutton
checkbtnv=tk.IntVar()
checkbtn=ttk.Checkbutton(label,text='i declare that information are correct',variable=checkbtnv)
checkbtn.grid(row=7,columnspan=3)

optionv=tk.StringVar()
optionc=ttk.Combobox(label,width=14,textvariable=optionv,state='readonly')
optionc['values']=('new user','regular user','older user')
optionc.current(0)
optionc.grid(row=5,column=1,pady=12,padx=12)



#newpage
new=ttk.Label(page2,text="Enter your help :")
new.grid(row=0,column=1,padx=8,pady=4)
new=ttk.Label(page3,text="Enter your about :")
new.grid(row=0,column=1,padx=8,pady=4)
new=ttk.Label(page4,text="Enter your info :")
new.grid(row=0,column=1,padx=8,pady=4)
new=ttk.Label(page5,text="Enter your apply :")
new.grid(row=0,column=1,padx=8,pady=4)

#def action
"""def action():
    username=namev.get()
    userage=agev.get()
    usergender=genderv.get()
    usernation=nation.get()
    usermobile=mobilev.get()
    useroption=optionv.ge()
    useradhar=adharvv.get()
    userdeclare=checkbtnv.get()
    if userdeclare==0:
        userdeclaration='no'
    else:
           userdeclaration='yes'
    
    with open('file7.txt','a') as f:
        f.write(f'{username},{userage},{usergender},{usernation},{userdeclaration},{usermobile},{useradhar}{useroption}\n')
    namee.delete(0,tk.END) 
    agee.delete(0,tk.END)    
    gendere.delete(0,tk.END) 
    
    namee.configure(foreground='Blue')
    agee.configure(foreground='Blue')
    gendere.configure(foreground='Blue')
    submit.configure(foreground='Blue')"""
#wite to csv file
def action():
    username=namev.get()
    userage=agev.get()
    usergender=genderv.get()
    usernation=nation.get()
    userdeclare=checkbtnv.get()
    useradhar=adharvv.get()
    usermobile=mobilev.get()
    useroption=optionv.get()
    
    
    if userdeclare==0:
        userdeclaration='no'
    else:
           userdeclaration='yes' 


    with open('file8.csv','a') as f:
        dict_writer=DictWriter(f,fieldnames=['usernamee','useragee','usergendere','usernatione','userdeclaratione','useradhare','usermobilee','useroptione'])
        if os.stat('file8.csv').st_size==0:
            
           dict_writer.writeheader()
        dict_writer.writerow({
                'usernamee':username,
                'useragee':userage,
                'usergendere':usergender,
                'usernatione':usernation,
                'userdeclaratione':userdeclaration,
                'useradhare':useradhar,
                'usermobilee':usermobile,
                'useroptione':useroption
                })
    
    namee.delete(0,tk.END) 
    agee.delete(0,tk.END)    
    gendere.delete(0,tk.END) 
    namee.configure(foreground='Blue')
    agee.configure(foreground='Blue')
    gendere.configure(foreground='Blue')
    submit.configure(foreground='Blue')
    
    
    
    
#submitbutton
submit=tk.Button(label,text='submit',command=action)
submit.grid(row=12,column=0)

win.mainloop()