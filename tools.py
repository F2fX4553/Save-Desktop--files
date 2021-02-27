from tkinter import *
from mess import *
from ossama import *
from tkinter import ttk
from tkinter import messagebox  # istd3a messagebox min tkinter
import re
import datetime

##########################################################################
fnt = 'Times 16 ' # font ta3 lable
fntent = 'Helvetica 14' # font ta3 entry
fntbot = 'Times 8' # font ta3 lbutton
bg = '#CDD0D4' # background ta3 forma
bgtxtent = '#7A1B7A' # color text li da5le entry
##########################################################################
poss = Tk()
kolch(poss)
poss.title('Secret Files')
poss.geometry('639x369')
poss.iconbitmap('imagetof/foldricon.ico')

canvas = Canvas(poss,width = 639, height =357,bg = 'black')
canvas.pack()
phot = PhotoImage(file = 'imagetof\imageform1.png')
canvas.create_image(0,0,image = phot,anchor = NW)


pgbar = ttk.Progressbar(poss, length=640, orient=HORIZONTAL, maximum=100, value=10)
pgbar.start(100)
poss.after(9000 ,lambda: poss.destroy())
pgbar.place(x=1, y=360)
poss.overrideredirect(1) #Remove border
poss.resizable(False,False)

poss.mainloop()




###########################################################################

def forma3():

    root = Toplevel()  # forma
    root.title('0.0.1   SIBNA')  # title ta3 lforma
    root.iconbitmap('imagetof/foldricon.ico')
    fnt = 'Times 16 '  # font ta3 lable
    fntent = 'Helvetica 14'  # font ta3 entry
    fntbot = 'Times 10'  # font ta3 lbutton
    bg = '#CDD0D4'  # background ta3 forma
    bgtxtent = '#7A1B7A'  # color text li da5le entry
    pattgmail = '[a-zA-Z0-9]+@[a-zA-Z]+\.(com|fr|outlook|net)'  # regolar ta3 gmaile
    pattphone = '[0-9].{9}'  # rigolar ta3 phone
    pattmotpass = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!?@#$%^&+=])"  # hada lmotpass
    pattname = '[A-Z]'  # hada name 1
    pattlname = '[A-Z]'  # hada name 2
    pattaddres = '[A-Z]'  # hda address
    fordata = '#402B9C'

    pad = 10
    padxx = 10
    root.config(background=bg)  # color ta3 forma
    fw = 1100  # hajm width ta3 lforma
    fh = 400  # hajm height ta3 lforma
    x = (root.winfo_screenwidth() - fw) / 2  # hna ydi hjm licron o yn9s mno width ta3 lforma wy9smha 3la 2
    y = (root.winfo_screenheight() - fh) / 2 - 50  # hna ydi hjm licron o yn9s height ta3 lforma wy9smha 3la 2 o yn9slh 50
    root.geometry('%dx%d+%d+%d' % (fw, fh, x, y))  # han jm3t kolch
    root.resizable(False,False)

    # hada lable li flforma
    Label(root, text='Secret Files', font='impact 30', background='#FEFFFF', foreground='#4C7DD2', width=100,height=0).pack()
    farme = Frame(root, bg=bg)
    # hna std3itha o pady m3ntha yb3dhom b 10 px mtlan :)
    farme.pack(pady=pad, padx=padxx)

    # lable 1
    lblfirstname = ttk.Label(farme, text='Enter Yor First Name ', background=bg, font=fnt)
    # lable 2
    lbllastname = ttk.Label(farme, text='Enter Yor Last Name ', background=bg, font=fnt)
    # lable 3
    lblgmaile2 = ttk.Label(farme, text=' Enter Yor Gmaile ', background=bg, font=fnt)
    # lable 4
    lbladdress = ttk.Label(farme, text=' Enter Yor Address ', background=bg, font=fnt)
    # lable 5
    lblphone = ttk.Label(farme, text='   Enter Yor Number Phone ', background=bg, font=fnt)
    # lable 6
    lblpassword1 = ttk.Label(farme, text='Enter Yor Password ', background=bg, font=fnt )
    # lable 7
    lblpassword2 = ttk.Label(farme, text='Enter Yor Password ', background=bg, font=fnt )
    # lable 8
    now = datetime.datetime.now()
    datat = ttk.Label(farme, text=now.strftime('%I : %M  : %S'), background=bg, foreground=fordata, font=fnt)
    # lable 9
    chiks = ttk.Style()
    chiks.configure('TButton', background='blue')
    v = BooleanVar()
    chik = ttk.Checkbutton(root, text='Agree to the terms of use', variable=v)
    chik.bind('<Return>',lambda my : tst())
    chik.place(x=590, y=290)
    ###########################################################
    sventfirstname = StringVar()
    sventlastname = StringVar()
#    sventsgmaile1 = StringVar()
    sventgmaile2 = StringVar()
    sventaddress = StringVar()
    sventphone = StringVar()
    sventpassword1 = StringVar()
    sventpassword2 = StringVar()

    # entry 1
    entfirstname = ttk.Entry(farme, foreground=bgtxtent, font=fntent, width=23, textvariable=sventfirstname)
    entfirstname.bind('<Return>',lambda my : tst())
    # entry 2
    entlastname = ttk.Entry(farme, foreground=bgtxtent, font=fntent, width=23, textvariable=sventlastname)
    entlastname.bind('<Return>',lambda my : tst())
    # entry 3
    entgmaile2 = ttk.Entry(farme, foreground=bgtxtent, font=fntent, width=23, textvariable=sventgmaile2)
    entgmaile2.bind('<Return>',lambda my : tst())
    # entry 4
    entaddress = ttk.Entry(farme, foreground=bgtxtent, font=fntent, width=23, textvariable=sventaddress)
    entaddress.bind('<Return>',lambda my : tst())
    # entry 5
    entphone = ttk.Entry(farme, foreground=bgtxtent, font=fntent, width=23, textvariable=sventphone)
    entphone.bind('<Return>',lambda my : tst())
    # entry 6
    entpassword1 = ttk.Entry(farme, foreground=bgtxtent, font=fntent, width=23, textvariable=sventpassword1, show='*')
    entpassword1.bind('<Return>',lambda my : tst())
    # entry 7
    entpassword2 = ttk.Entry(farme, foreground=bgtxtent, font=fntent, width=23, textvariable=sventpassword2 ,  show='*')
    entpassword2.bind('<Return>',lambda my : tst())

    datat.grid(row=0, column=0, pady=20, padx=10)
    ############################################################
    lblfirstname.grid(row=1, column=0, pady=pad, padx=padxx)  #
    entfirstname.grid(row=1, column=1, pady=pad, padx=padxx)  #
    ############################################################
    lbllastname.grid(row=1, column=2, pady=pad, padx=padxx)  #
    entlastname.grid(row=1, column=3, pady=pad, padx=padxx)  #
    ############################################################
    lblgmaile2.place(x = -5,y = 125)
    entgmaile2.grid(row=2, column=1, pady=pad, padx=padxx)  #
    ############################################################
    lbladdress.place(x = 495,y = 125)
    entaddress.grid(row=2, column=3, pady=pad, padx=padxx)  # hado ga3 bach nstf lable o entry
    ############################################################
    lblphone.place(x = -15,y = 175)  #
    entphone.grid(row=5, column=1, pady=pad, padx=padxx)  #
    ############################################################
    lblpassword1.place(x = 495,y = 175)
    entpassword1.grid(row=5, column=3, pady=pad, padx=padxx)  #
    ############################################################
    lblpassword2.place(x = -2,y = 220)
    entpassword2.grid(row=7, column=1, pady=pad, padx=padxx)  #

    ############################################################

    def tst():
        patt1 = pattname  # hadi ta3 name lwale ######## #
        fnam = re.match(patt1, entfirstname.get())

        patt2 = pattlname  # hadi ta3 name tow ######## #
        lnam = re.match(patt2, entlastname.get())

        patt3 = pattgmail  # hadi ta3 gmaile ######## #
        g = re.match(patt3, entgmaile2.get())  #
        ##########################################################################

        patt4 = pattaddres  # hadi ta3 address ######## #
        addr = re.match(patt4, entaddress.get())

        patt5 = pattphone  # hdi ta3 phone ##########
        ph = re.match(patt5, entphone.get())
        #############################################################################

        patt6 = pattmotpass  # hadi ta3 motpass 1########
        pas = re.match(patt6, entpassword1.get())

        #############################################################################
        patt7 = pattmotpass  # hadi ta3 motpass 2 ##########
        pas2 = re.match(patt7, entpassword2.get())

        if entfirstname.get().strip() == '':
            messagebox.showinfo('', 'Fill out the first name ! ')
            entfirstname.focus()

        elif fnam == None:
            messagebox.showinfo('', 'He writes an uppercase with lowercase letters')
            entfirstname.focus()

        elif entlastname.get().strip() == '':
            messagebox.showinfo('', 'Fill out the second name !')
            entlastname.focus()
        elif lnam == None:
            messagebox.showinfo('', 'He writes an uppercase with lowercase letters')
            entlastname.focus()


        elif entgmaile2.get().strip() == '':
            messagebox.showinfo('', 'Dictate the gmaile !')
            entgmaile2.focus()

        elif g == None:
            messagebox.showinfo('', 'The e-mail is wrong ')
            entgmaile2.focus()

        elif entaddress.get().strip() == '':
            messagebox.showinfo('', 'Dictate the address !')
            entaddress.focus()
        elif addr == None:
            messagebox.showinfo('', 'Dictate the address')
            entaddress.focus()

        elif entphone.get().strip() == '':
            messagebox.showinfo('', 'Dictate the number phone !')
            entphone.focus()

        elif ph == None:
            messagebox.showinfo('', 'Wrong number ')
            entphone.focus()

        elif entpassword1.get().strip() == '':
            messagebox.showinfo('', 'Dictate the first password !')
            entpassword1.focus()

        elif pas == None:
            messagebox.showinfo('', 'Uppercase and lowercase letters with symbol')
            entpassword1.focus()

        elif entpassword2.get().strip() == '':
            messagebox.showinfo('', 'Dictate the last password !')
            entpassword2.focus()

        elif pas2 == None:
            messagebox.showinfo('', 'Uppercase and lowercase letters with symbol')
            entpassword2.focus()

        elif entpassword1.get() != entpassword2.get():
            messagebox.showinfo('', 'The password does not match !')
        elif v.get() == False:
            messagebox.showinfo('', 'Knowing to consent')


        else:

            mesbox('welcom')
            pos.destroy()
            forma0()

    botons = ttk.Style()
    botons.configure('TButton', bg='red', font=fntbot)
    botclic = ttk.Button(root, text='CLIC HER', command=tst)
    botext = ttk.Button(root, text='Exit', command=root.destroy)
    botclic.place(x=250, y=350)
    botext.place(x=100, y=350)
    clt = root.winfo_children()
    for c in clt:
        print(type(c))
    root.grab_set()
########################################################################################################################

def forma0():
    ton = tk.Tk()
    ton.iconbitmap('imagphoto/foldricon.ico')
    ton.title('Secret Files')
    ton.config(background='#CDD0D4')
    fw = 800  # hajm width ta3 lforma
    fh = 600  # hajm height ta3 lforma
    x = (ton.winfo_screenwidth() - fw) / 2  # hna ydi hjm licron o yn9s mno width ta3 lforma wy9smha 3la 2
    y = (ton.winfo_screenheight() - fh) / 2 - 50  # hna ydi hjm licron o yn9s height ta3 lforma wy9smha 3la 2 o yn9slh 50
    ton.geometry('%dx%d+%d+%d' % (fw, fh, x, y))
    ton.grid_rowconfigure(0, weight=1)
    ton.grid_columnconfigure(1, weight=1)

    side_menu = SideMenu(ton)  # hada ta3 li buttons
    side_menu.grid(row=0, column=0, sticky="sn")

    sliders = SlidersFrame(ton, bg='white')  # hada ta3 liframes
    sliders.grid(row=0, column=1, sticky="snew")

    sliders.add(id='Home', title="Home", show=1)  # lframe ta3 home
    sliders.add(id='Photos', title="Photos Package")  # lframe ta3 photos
    sliders.add(id='Videos', title="Videos Package")  # lframe ta3 videos
    sliders.add(id='Music', title="Music Package")  # lframe ta3 music

    side_menu.add('Home', 'imagphoto/home.png', func=lambda: sliders.show('Home'))  # lbutton ta3 home
    side_menu.add('Photos', 'imagphoto/photo1.png', func=lambda: sliders.show('Photos'))  # lbutton ta3 photos
    side_menu.add('Videos', 'imagphoto/photo2.png', func=lambda: sliders.show('Videos'))  # lbutton ta3 videos
    side_menu.add('Music', 'imagphoto/photo3.png', func=lambda: sliders.show('Music'))  # lbutton ta3 music

    ton.mainloop()






def forma4():
    mino = Toplevel()
    mino.title('Secret Files')
    mino.geometry('600x400')
    mino.config(background='#CDD0D4')
    mino.iconbitmap('imagetof/foldricon.ico')
    pattgmail = '[a-zA-Z0-9]+@[a-zA-Z]+\.(com|fr|outlook|net)'
    pattmotpass = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!?@#$%^&+=])"

    Label(mino, text='Secret Files', font='impact 30', background='#FEFFFF', foreground='#4C7DD2', width=100,
          height=0).pack()

    lableforma2 = ttk.Label(mino, text='Enter Your Gmaile', background='#CDD0D4', foreground='black', font=fnt)
    lableforma2mo = ttk.Label(mino, text='Enter Your Password', background='#CDD0D4', foreground='black', font=fnt)
    entforma2 = ttk.Entry(mino, background='#CDD0D4', foreground='#7A1B7A', font=fnt, width=22)
    entforma2.bind('<Return>', lambda my: test2())
    entforma2mo = ttk.Entry(mino, background='#CDD0D4', foreground='#7A1B7A', font=fnt, width=22, show='*')
    entforma2mo.bind('<Return>', lambda my: test2())
    lableforma2.place(x=175, y=125)
    entforma2.place(x=175, y=150)
    lableforma2mo.place(x=175, y=225)
    entforma2mo.place(x=175, y=250)
    def test2():
        patt1 = pattgmail  # hadi ta3 gmaile ######## #
        minos = re.match(patt1, entforma2.get())  #

        patt2 = pattmotpass  # hadi ta3 motpass 1########
        minoss= re.match(patt2, entforma2mo.get())

        if entforma2.get().strip() == '':
            messagebox.showinfo('', 'Dictate the gmaile !')
            entforma2.focus()
        elif minos == None:
            messagebox.showinfo('', 'The e-mail is wrong ')
            entforma2.focus()
        elif entforma2mo.get().strip() == '':
            messagebox.showinfo('', 'Dictate the last password !')
            entforma2mo.focus()

        elif minoss == None:
            messagebox.showinfo('', 'Uppercase and lowercase letters with symbol')
            entforma2mo.focus()

        else:
            mesbox('welcom')
            pos.destroy()
            forma0()








    botonsforma = ttk.Style()
    botonsforma.configure('TButton', font='Times 10', background='blue', widht=100, foreground='black')
    botonforma2 = ttk.Button(mino, text='Enter', command= test2)
    botonforma2ext = ttk.Button(mino, text='Exit', command=mino.destroy)
    botonforma2.place(x=50, y=350)
    botonforma2ext.place(x=140, y=350)
    mino.resizable(False, False)
    mino.grab_set()

#############################################################################################################################
pos = Tk()

kolch(pos)
pos.geometry('639x400')
pos.title('Secret Files')

pos.iconbitmap('imagetof/foldricon.ico')
Label(pos, text='Welcome to Secret Files', font='impact 30', background='#FEFFFF', foreground='#4C7DD2', width=100,
      height=0).pack()

pos.resizable(False, False)
canvas2 = Canvas(pos, width=639, height=357, background='black')
canvas2.pack()
mktabs = PhotoImage(file='imagetof\coorona.png')
canvas2.create_image(0, 0, image=mktabs, anchor=NW)
def con():
    pass
botonsforma1 = ttk.Style()
botonsforma1.configure('TButton', font='Times 10', background='yellow', widht=100, foreground='blue')
btontsjile = ttk.Button(pos, text='Login', command=forma4)
btonttsjiledo5ol = ttk.Button(pos, text='Join Unsplash', width=18, command=forma3)
btontsjile.place(x=30, y=90)
btonttsjiledo5ol.place(x=120, y=90)

pos.mainloop()


