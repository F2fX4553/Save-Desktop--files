from tkinter import ttk
from tkinter import messagebox
def kolch(pos):
    pos.update()
    fw = pos.winfo_width()
    fh = pos.winfo_height()
    sw = pos.winfo_screenwidth()
    sh = pos.winfo_screenheight()
    x = (sw - fw) / 2-180
    y = (sh - fh) / 2- 150
    pos.geometry('%dx%d+%d+%d' % (fw, fh, x, y))


def bgall(pos,bg):
    pos.update()
    clt = pos.winfo_children()
    pos.config(bg=bg)
    for c in clt:
        ci = c.winfo_class()
        if ci == 'Label' or ci == 'Button' or ci == 'Entry':
            c['bg'] = bg

        if ci == 'TLabel' or ci == 'TButton':
            my = ttk.Style()
            my.configure('TLabel',background = bg)
            my.configure('TButton',background = bg)
            my.configure('TEntry ', background=bg)

def fontall(pos,font):
    pos.update()
    clt = pos.winfo_children()
    for c in clt:
        ci = c.winfo_class()
        if ci == 'Label' or ci == 'Button' or ci == 'Entry' or ci == 'TEntry':
            c['font']= font
        if ci == 'TLabel' or ci == 'TButton':
            my = ttk.Style()
            my.configure('TLabel',font = font)
            my.configure('TButton', font = font)


def fgall(pos,fg):
    pos.update()
    clt = pos.winfo_children()
    for c in clt:
        ci = c.winfo_class()
        if ci == 'Label' or ci == 'Button' or ci == 'Entry':
            c['fg'] = fg
        if ci == 'TLabel' or ci == 'TButton' or ci == 'TEntry':
            my = ttk.Style()
            my.configure('TLabel',foreground = fg)
            my.configure('TButton', foreground = fg)
            my.configure('TEntry',foreground = fg)


def mesbox(text):
    messagebox.showinfo('',text)


def mesyesno(text):
    return messagebox.askyesno('',text)