# Secret Files
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import ImageTk, Image


class ScrolledFrame(tk.Frame): # Hada bash tdir frame fih libar hadok ta3 bach ttl3 esf7a wlla thbtha

  def __init__(self, master):
    self.frame = tk.Frame(master) # hada bach ndiro fih canvas olibar
    self.frame.grid_rowconfigure(0, weight = 1) # hada bach tdir row 0 itws3 w7do
    self.frame.grid_columnconfigure(0, weight = 1) # hada bach tdir column 0 itws3 w7do

    # canvas for inner frame
    self.canvas = tk.Canvas(self.frame) # hadi bach n7to fiha lframe eli ndiro fiha litems
    self.canvas.grid(row = 0, column = 0, sticky = 'news')

    # create right scrollbar and connect to canvas Y
    self._vertical_bar = tk.Scrollbar(self.frame, orient = 'vertical', command = self.canvas.yview) # hadi labar ta3 Y
    self._vertical_bar.grid(row = 0, column = 1, sticky = 'ns')
    self.canvas.configure(yscrollcommand = self._vertical_bar.set)
    """
    # hada emb3d nriglo 5atr mal9itoch l7l bach i5dm m3a X 5atr rah i5dm m3a Y brk
    # create bottom scrollbar and connect to canvas X
    self._horizontal_bar = tk.Scrollbar(self.frame, orient = 'horizontal', command = self.canvas.xview)
    if horizontal:
      self._horizontal_bar.grid(row = 1, column = 0, sticky = 'we')
      # self._horizontal_bar.pack(fill = "x")
    self.canvas.configure(xscrollcommand = self._horizontal_bar.set)
    """
    super().__init__(self.canvas) # hada bach t3ti eli3dadat ta3 lframe eli n7to fiha litems
    self.frameID = self.canvas.create_window((-1, -1), window = self, anchor = 'nw') # hada bach i7t lframe fi canvas

    # resize when configure changed
    self.bind("<Configure>", self.resize) # hadi event colma tbdlt 7aja fi lframe iro7 lddala resize
    self.canvas.bind("<Configure>", self.frame_size) # hadi event colma tbdlt 7aja fi canvas iro7 lddala frame_size

    # hado bach ki t7b tdiro flform, drt haka 5atr ki tstd3i
    # pack istd3i ta3 lfram eli wrtha lclass mi haka ki tstd3iha istd3i ta3 frame eli 7tit fih kolch
    self.pack = self.frame.pack
    self.grid = self.frame.grid
    self.place = self.frame.place

  def frame_size(self, event):
    # hada bach kolma itbdl el7jm ta3 canvas itbdl m3ah el7jm ta3 lframe eli n7to fih litems
    canvas_width = event.width
    self.canvas.itemconfig(self.frameID, width = canvas_width+1)

  def resize(self, event = None):# hada bach kolma kbr lframe ta3 litems irigl labar
    self.canvas.configure(scrollregion = self.canvas.bbox('all'))

class SortedFrame(ScrolledFrame):# hadi frame bach t7t fih etsawr t3tilo ch7al idir fi vol satr mn tswira hna fih 4 t9dr tbdl

  def __init__(self, master = None, nitems = 4, *args, **kw):
    super().__init__(master, *args, **kw)
    self.nitems = nitems
    self.row = 0
    self.col = 0

  def add(self, wid):
    wid.grid(row = self.row, column = self.col,
             padx = "2px 0" if self.col != self.nitems else "2px",
             pady = "2px 0")
    if self.col == self.nitems:
      self.col = 0
      self.row += 1
    else:
      self.col += 1

class Package(tk.Frame): # hadi frame bach ta3 kol wa7d liphoto wla video t9dr tbdl ana drt example nta dir kima 7bit

  def __init__(self, master = None, title = "Package", items = [], *args, **kw):
    super().__init__(master, *args, **kw)
    tk.Label(self, text = title, font = ['Tahome', 16]).pack(fill = "x")# hadi ta3 el3onwan
    frame = tk.Frame(self)
    frame.pack(fill = "x")
    tk.Button(frame, text = 'Import', command = self.import_file).pack(fill = "x", side = "left") # hada bach td5l lifichi
    tk.Button(frame, text = 'Extract').pack(fill = "x", side = "left") # hada bach t5rj lifich
    self.package_frame = SortedFrame(self) # hna n7to lframe li kolma tmdlha item irtbha W7do
    self.package_frame.pack(fill = "both")
    self.package_items = {}
    for name, image in items: # hada ila 3dk item mn 9bl hada inf3k bach t3rd bih lifich eli 3dk mn 9bl
      self.add_item(name, image)

  def add_item(self, name, image): # hada bach izid fichi t9dr tmodifi fih kima 7bit
    frame = tk.Frame(self.package_frame) # hadi frame n7t fiha kolch
    image = ImageTk.PhotoImage(Image.open(image).resize((120, 120))) # hadi etswira
    self.package_items[name] = [frame, image]
    tk.Label(frame, image = self.package_items[name][1]).pack(fill = "both") # hada bach ta3 etswira
    tk.Label(frame, text = name,wraplength = 100).pack(fill = "x") # hada ism elmilaf
    self.package_frame.add(frame) # hada bach i3rdha

  def import_file(self): # hada bach td5l elfich
    file = filedialog.askopenfilename(title = "Choose File", 
                                      filetypes = (("Images", ".PNG;.JPEG;*.JPG;*.GIF;*.BMP;"),("All files", ".")))
    if file.split(".")[-1].lower() in ["png", "jpg", "jpeg", "bmp", "gif"]:
      image = file
    else:
      image = "file.png"
    self.add_item(file.split("/")[-1], image)

class SlidersFrame(tk.Frame): # hada tmdlo frames bzaf m3a id bach ki t7b t3rd w7da tmdlo lid in7 li kant m3roda o i3rd ljdida

  def __init__(self, master = None, *args, **kw):
    super().__init__(master, *args, **kw)
    self.Frames = {} # hda bach ndir fih li frames m3a lid ta3ha
    self.showed = None # hada bach ndir fih eli rahi m3roda

  def add(self, id = None, show = False, OBJ = Package, *args, **kw):
    if not id:
      id = len(self.Frames)
    self.Frames[id] = OBJ(self, *args, **kw)
    if show:
      self.show(id)
    return self.Frames[id]

  def show(self, id):
    if self.showed:
      self.Frames[self.showed].pack_forget()
    self.Frames[id].pack(fill = "both", expand = 1)
    self.showed = id

  def remove(self, id):
    self.Frames[id].destroy()
    del(self.Frames[id])

class SideMenu(tk.Frame):# hada ta3 li buttons ta3 lakoti tmdlo ism ol photo o wash idir ki tklicki i7thom

  def __init__(self, master = None, *args, **kw):
    super().__init__(master, *args, **kw)
    self.MenuItems = {}
    self.images = {}

  def add(self, name, image, func, id = None):
    if not id:
      id = len(self.MenuItems)
    self.images[id] = ImageTk.PhotoImage(Image.open(image).resize((35, 35)))
    frame = tk.Frame(self, bg = 'white')
    tk.Label(frame, text = name, bd = 0, bg = 'white', font = 'None 10').pack(side = 'left')
    tk.Button(frame, bd = 0, bg = 'white', image = self.images[id], command = func).pack(side = 'right')
    frame.pack(fill = 'x', ipadx = '2px', ipady = '2px', padx = '2px', pady = '2px 0')
    self.MenuItems[id] = frame
    return frame

if __name__ == "__main__":
  '''root = tk.Tk()
  root.iconbitmap('imagphoto/foldricon.ico')
  root.title('Secret Files')
  root.config(background='#CDD0D4')
  fw = 800  # hajm width ta3 lforma
  fh = 600  # hajm height ta3 lforma
  x = (root.winfo_screenwidth() - fw) / 2  # hna ydi hjm licron o yn9s mno width ta3 lforma wy9smha 3la 2
  y = (root.winfo_screenheight() - fh) / 2 - 50  # hna ydi hjm licron o yn9s height ta3 lforma wy9smha 3la 2 o yn9slh 50
  root.geometry('%dx%d+%d+%d' % (fw, fh, x, y))
  root.grid_rowconfigure(0, weight = 1)
  root.grid_columnconfigure(1, weight = 1)

  side_menu = SideMenu(root) # hada ta3 li buttons
  side_menu.grid(row = 0, column = 0, sticky = "sn")

  sliders = SlidersFrame(root, bg = 'white')# hada ta3 liframes
  sliders.grid(row = 0, column = 1, sticky = "snew")

  sliders.add(id = 'Home', title = "Home", show = 1) # lframe ta3 home
  sliders.add(id = 'Photos', title = "Photos Package") # lframe ta3 photos
  sliders.add(id = 'Videos', title = "Videos Package") # lframe ta3 videos
  sliders.add(id = 'Music', title = "Music Package") # lframe ta3 music

  side_menu.add('Home', 'imagphoto/home.png', func = lambda: sliders.show('Home')) # lbutton ta3 home
  side_menu.add('Photos', 'imagphoto/photo1.png', func = lambda: sliders.show('Photos')) # lbutton ta3 photos
  side_menu.add('Videos', 'imagphoto/photo2.png', func = lambda: sliders.show('Videos')) # lbutton ta3 videos
  side_menu.add('Music', 'imagphoto/photo3.png', func = lambda: sliders.show('Music')) # lbutton ta3 music

  root.mainloop()'''