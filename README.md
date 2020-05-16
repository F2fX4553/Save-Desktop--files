from tkinter import * # istd3a kolch min tkinter
from tkinter import ttk # istd3a ttk mn tkinter
from tkinter import messagebox # istd3a messagebox min tkinter
import re
import datetime

root = Tk() # forma
root.title('0.0.1   SIBNA') # title ta3 lforma
root.iconbitmap('image\icon.ico.ico')
fnt = 'Times 16 ' # font ta3 lable
fntent = 'Helvetica 14' # font ta3 entry
fntbot = 'Times 14' # font ta3 lbutton
bg = '#CDD0D4' # background ta3 forma
bgtxtent = '#7A1B7A' # color text li da5le entry
pattgmail = '[a-zA-Z0-9]+@[a-zA-Z]+\.(com|fr|outlook|net)' # regolar ta3 gmaile
pattphone = '[0-9].{9}' # rigolar ta3 phone
pattmotpass = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!?@#$%^&+=])" # hada lmotpass
pattname = '[A-Z]' # hada name 1
pattlname = '[A-Z]' # hada name 2
pattaddres = '[A-Z]' # hda address
fordata = '#402B9C'

pad = 10
padxx = 10
root.config(background = bg) # color ta3 forma
fw = 1100 # hajm width ta3 lforma
fh = 400 # hajm height ta3 lforma
x = (root.winfo_screenwidth() - fw) / 2 # hna ydi hjm licron o yn9s mno width ta3 lforma wy9smha 3la 2
y = (root.winfo_screenheight() - fh) /2 - 50 # hna ydi hjm licron o yn9s height ta3 lforma wy9smha 3la 2 o yn9slh 50
root.geometry('%dx%d+%d+%d' % (fw,fh,x,y)) # han jm3t kolch
#root.resizable(False,False)

# hada lable li flforma
Label(root,text = 'Secret Files',font = 'impact 30',background = '#FEFFFF',foreground = '#4C7DD2',width = 100,height = 0).pack()
farme = Frame(root,bg = bg)
# hna std3itha o pady m3ntha yb3dhom b 10 px mtlan :)
farme.pack(pady = pad,padx = padxx)

# lable 1
lblfirstname = ttk.Label(farme,text = 'Enter Yor First Name ',background = bg,font = fnt)
#lable 2
lbllastname = ttk.Label(farme,text ='Enter Yor Last Name ',background = bg,font = fnt)
#lable 3
lblgmaile2 = ttk.Label(farme,text = ' Enter Yor Gmaile ',background = bg,font = fnt)
#lable 4
lbladdress = ttk.Label(farme,text = ' Enter Yor Address ',background = bg,font = fnt)
#lable 5
lblphone = ttk.Label(farme,text = '   Enter Yor Number Phone ',background = bg,font = fnt)
#lable 6
lblpassword1 = ttk.Label(farme,text ='Enter Yor Password ',background = bg,font = fnt)
#lable 7
lblpassword2 = ttk.Label(farme,text ='Enter Yor Password ',background = bg,font = fnt)
# lable 8
now = datetime.datetime.now()
datat = ttk.Label(farme,text = now.strftime('%I : %M  : %S'),background = bg,foreground = fordata,font = fnt)
# lable 9
chiks = ttk.Style()
chiks.configure('TButton',background = 'blue')
v = BooleanVar()
chik = ttk.Checkbutton(root,text = 'Agree to the terms of use',variable = v)
chik.place(x = 590,y = 290)
###########################################################
sventfirstname = StringVar()
sventlastname = StringVar()
sventsgmaile1 = StringVar()
sventgmaile2 = StringVar()
sventaddress = StringVar()
sventphone = StringVar()
sventpassword1 = StringVar()
sventpassword2 = StringVar()


# entry 1
entfirstname = ttk.Entry(farme,foreground = bgtxtent,font = fntent,width = 23,textvariable = sventfirstname)
#entry 2
entlastname = ttk.Entry(farme,foreground = bgtxtent,font = fntent,width = 23,textvariable = sventlastname)
#entry 3
entgmaile2 = ttk.Entry(farme,foreground = bgtxtent,font = fntent,width = 23,textvariable = sventgmaile2)
#entry 4
entaddress = ttk.Entry(farme,foreground = bgtxtent,font = fntent,width = 23,textvariable = sventaddress)
#entry 5
entphone = ttk.Entry(farme,foreground = bgtxtent,font = fntent,width = 23,textvariable = sventphone)
#entry 6
entpassword1 = ttk.Entry(farme,foreground = bgtxtent,font = fntent,width = 23,textvariable = sventpassword1)
#entry 7
entpassword2 = ttk.Entry(farme,foreground = bgtxtent,font = fntent,width = 23,textvariable = sventpassword2)

datat.grid(row = 0,column = 0,pady = 20,padx = 10)
############################################################
lblfirstname.grid(row = 1,column = 0,pady = pad,padx = padxx)   #
entfirstname.grid(row = 1,column = 1,pady = pad,padx = padxx)   #
############################################################
lbllastname.grid(row = 1,column = 2,pady = pad,padx = padxx)  #
entlastname.grid(row = 1,column = 3,pady = pad,padx = padxx)  #
############################################################
lblgmaile2.grid(row = 2,column = 0,pady = pad,padx = padxx)    #
entgmaile2.grid(row = 2,column = 1,pady = pad,padx = padxx)    #
############################################################
lbladdress.grid(row = 2,column = 2,pady = pad,padx = padxx)    #
entaddress.grid(row = 2,column = 3,pady = pad,padx = padxx)    # hado ga3 bach nstf lable o entry
############################################################
lblphone.grid(row = 5,column = 0,pady = pad,padx = padxx)      #
entphone.grid(row = 5,column = 1,pady = pad,padx = padxx)      #
############################################################
lblpassword1.grid(row = 5,column = 2,pady = pad,padx = padxx)  #
entpassword1.grid(row = 5,column = 3,pady = pad,padx = padxx)  #
############################################################
lblpassword2.grid(row = 7,column = 0,pady = pad,padx = padxx)  #
entpassword2.grid(row = 7,column = 1,pady = pad,padx = padxx)  #
############################################################

def tst():
    patt1 =  pattname # hadi ta3 name lwale ######## #
    fnam = re.match(patt1, entfirstname.get())

    patt2 = pattlname  # hadi ta3 name tow ######## #
    lnam = re.match(patt2, entlastname.get())

    patt3 = pattgmail # hadi ta3 gmaile ######## #
    g = re.match(patt3, entgmaile2.get())                                     #
    ##########################################################################

    patt4 = pattaddres  # hadi ta3 address ######## #
    addr = re.match(patt4, entaddress.get())

    patt5 = pattphone # hdi ta3 phone ##########
    ph = re.match(patt5,entphone.get())
    #############################################################################

    patt6 = pattmotpass # hadi ta3 motpass 1########
    pas = re.match(patt6,entpassword1.get())

    #############################################################################
    patt7 = pattmotpass #hadi ta3 motpass 2 ##########
    pas2 = re.match(patt7,entpassword2.get())

    if entfirstname.get().strip() == '':
        messagebox.showinfo('','Fill out the first name ! ')
        entfirstname.focus()

    elif fnam == None:
        messagebox.showinfo('','He writes an uppercase with lowercase letters')
        entfirstname.focus()

    elif entlastname.get().strip() == '':
        messagebox.showinfo('','Fill out the second name !')
        entlastname.focus()
    elif lnam == None:
        messagebox.showinfo('','He writes an uppercase with lowercase letters')
        entlastname.focus()


    elif entgmaile2.get().strip() == '':
        messagebox.showinfo('','Dictate the gmaile !')
        entgmaile2.focus()

    elif g  == None:
        messagebox.showinfo('','The e-mail is wrong ')
        entgmaile2.focus()

    elif entaddress.get().strip() == '':
        messagebox.showinfo('','Dictate the address !')
        entaddress.focus()
    elif addr == None:
        messagebox.showinfo('','Dictate the address')
        entaddress.focus()

    elif entphone.get().strip() == '':
        messagebox.showinfo('','Dictate the number phone !')
        entphone.focus()

    elif ph == None:
        messagebox.showinfo('','Wrong number ')
        entphone.focus()

    elif entpassword1.get().strip() == '':
        messagebox.showinfo('','Dictate the first password !')
        entpassword1.focus()

    elif pas == None:
        messagebox.showinfo('', 'Uppercase and lowercase letters with symbol')
        entpassword1.focus()

    elif entpassword2.get().strip() == '':
        messagebox.showinfo('','Dictate the last password !')
        entpassword2.focus()

    elif pas2 == None:
        messagebox.showinfo('','Uppercase and lowercase letters with symbol')
        entpassword2.focus()

    elif entpassword1.get() != entpassword2.get():
        messagebox.showinfo('','The password does not match !')
    elif v.get() == False:
        messagebox.showinfo('','Knowing to consent')


    else:
        filename = entfirstname.get() + '.txt'
        f = open(filename,'w+')
        f.write('first name : ' + entfirstname.get() + '\n')
        f.write('last name : ' + entlastname.get() + '\n')
        f.write('gmaile : ' + entgmaile2.get() + '\n')
        f.write('address : ' + entaddress.get() + '\n')
        f.write('number phone : '+ entphone.get() + '\n')
        f.write('first password : '+ entpassword1.get() + '\n')
        f.write('last password : '+ entpassword2.get())
        f.close()
        messagebox.showinfo('','The file  : '+ entfirstname.get() + '  was created' )
        sventfirstname.set('')
        sventlastname.set('')
        sventgmaile2.set('')
        sventaddress.set('')
        sventphone.set('')
        sventpassword1.set('')
        sventpassword2.set('')
        entfirstname.focus()

botons = ttk.Style()
botons.configure('TButton',bg = 'red',font = fntbot)
botclic = ttk.Button(root,text = 'CLIC HER' ,command = tst)
botext = ttk.Button(root,text = 'Exit',command = root.destroy)
botclic.place(x= 250,y = 350)
botext.place(x = 100,y = 350)
clt = root.winfo_children()
for c in clt:
    print(type(c))
root.mainloop()
