import tkinter as tk
from tkinter import filedialog, Text
from PIL import ImageTk, Image
import platform
import subprocess
import os
from PyPDF2 import PdfFileReader
import webbrowser
import win32print
import win32api
class ScrolledFrame(tk.Frame):
    def __init__(self, master):
        self.frame = tk.Frame(master)
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

        self.canvas = tk.Canvas(self.frame)
        self.canvas.grid(row=0, column=0, sticky='news')

        self._vertical_bar = tk.Scrollbar(self.frame, orient='vertical', command=self.canvas.yview)
        self._vertical_bar.grid(row=0, column=1, sticky='ns')
        self.canvas.configure(yscrollcommand=self._vertical_bar.set)

        super().__init__(self.canvas)
        self.frameID = self.canvas.create_window((-1, -3), window=self, anchor='nw')

        self.bind("<Configure>", self.resize)
        self.canvas.bind("<Configure>", self.frame_size)

        self.pack = self.frame.pack
        self.grid = self.frame.grid
        self.place = self.frame.place

    def frame_size(self, event):
        canvas_width = event.width
        self.canvas.itemconfig(self.frameID, width=canvas_width + 1)
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def resize(self, event=None):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        self.canvas.config(width=event.width, height=event.height)


class SortedFrame(ScrolledFrame):
    def __init__(self, master=None, nitems=4, *args, **kw):
        super().__init__(master, *args, **kw)
        self.nitems = nitems
        self.row = 0
        self.col = 0

    def add(self, wid):
        wid.grid(row=self.row, column=self.col,
                 padx="2px 0" if self.col != self.nitems else "2px",
                 pady="2px 0")
        if self.col == self.nitems:
            self.col = 0
            self.row += 1
        else:
            self.col += 1


class Package(tk.Frame):
    def __init__(self, master=None, title="Package", items=[], *args, **kw):
        super().__init__(master, *args, **kw)
        tk.Label(self, text=title, font=['Tahome', 16]).pack(fill="x")
        frame = tk.Frame(self)
        frame.pack(fill="x")
        self.import_button = tk.Button(frame, text='Import', command=self.import_file, width=10, bg='#4CAF50', fg='white', bd=0)
        self.import_button.pack(fill="x", side="left", padx=(10, 5))
        self.extract_button = tk.Button(frame, text='Extract',width=10, bg='#2196F3', fg='white', bd=0,)
        self.extract_button.pack(fill="x", side="left")
        self.package_frame = SortedFrame(self)
        self.package_frame.pack(fill="both")
        self.package_items = {}
        for name, file_path in items:
            self.add_item(name, file_path)



    def add_item(self, name, file_path):
        frame = tk.Frame(self.package_frame)
        
        # Check file extension to determine icon and action
        file_extension = file_path.split(".")[-1].lower()
        if file_extension in ["png", "jpg", "jpeg", "bmp", "gif"]:
            # For image files, display thumbnail
            image = ImageTk.PhotoImage(Image.open(file_path).resize((120, 120)))
            label = tk.Label(frame, image=image)
            label.image = image  # Keep a reference to prevent garbage collection
            label.pack(fill="both")
            self.package_items[name] = [frame, image]
            label.bind("<Button-1>", lambda event, path=file_path: self.show_image(path))
            label.bind("<Button-3>", lambda event, name=name: self.show_context_menu(event, name))  # Bind right-click event
        elif file_extension == "mp3":
            # For MP3 files, display music icon and play music
            music_icon = ImageTk.PhotoImage(Image.open("imagetof/music_icon.png").resize((120, 120)))
            label = tk.Label(frame, image=music_icon)
            label.image = music_icon  # Keep a reference to prevent garbage collection
            label.pack(fill="both")
            self.package_items[name] = [frame, music_icon]
            label.bind("<Button-1>", lambda event, path=file_path: self.play_music(path))
            label.bind("<Button-3>", lambda event, name=name: self.show_context_menu(event, name))  # Bind right-click event
        elif file_extension == "mp4":
            # For MP4 files, display video icon and open video
            video_icon = ImageTk.PhotoImage(Image.open("imagetof/video_icon.png").resize((120, 120)))
            label = tk.Label(frame, image=video_icon)
            label.image = video_icon  # Keep a reference to prevent garbage collection
            label.pack(fill="both")
            self.package_items[name] = [frame, video_icon]
            label.bind("<Button-1>", lambda event, path=file_path: self.open_video(path))
            label.bind("<Button-3>", lambda event, name=name: self.show_context_menu(event, name))  # Bind right-click event
        elif file_extension == "pdf":
            # For PDF files, display PDF icon and open in default PDF viewer
            pdf_icon = ImageTk.PhotoImage(Image.open("imagetof/pdf_icon.png").resize((120, 120)))
            label = tk.Label(frame, image=pdf_icon)
            label.image = pdf_icon  # Keep a reference to prevent garbage collection
            label.pack(fill="both")
            self.package_items[name] = [frame, pdf_icon]
            label.bind("<Button-1>", lambda event, path=file_path: self.open_pdf(path))
            label.bind("<Button-3>", lambda event, name=name: self.show_context_menu(event, name))  # Bind right-click event
        elif file_extension == "txt":
            # For TXT files, display text icon and open in default text editor
            txt_icon = ImageTk.PhotoImage(Image.open("imagetof/txt_icon.png").resize((120, 120)))
            label = tk.Label(frame, image=txt_icon)
            label.image = txt_icon  # Keep a reference to prevent garbage collection
            label.pack(fill="both")
            self.package_items[name] = [frame, txt_icon]
            label.bind("<Button-1>", lambda event, path=file_path: self.open_text(path))
            label.bind("<Button-3>", lambda event, name=name: self.show_context_menu(event, name))  # Bind right-click event
        elif file_extension in ["doc", "docx"]:
            # For Word files, display Word icon and open in default Word viewer
            word_icon = ImageTk.PhotoImage(Image.open("imagetof/word_icon.png").resize((120, 120)))
            label = tk.Label(frame, image=word_icon)
            label.image = word_icon  # Keep a reference to prevent garbage collection
            label.pack(fill="both")
            self.package_items[name] = [frame, word_icon]
            label.bind("<Button-1>", lambda event, path=file_path: self.open_word(path))
            label.bind("<Button-3>", lambda event, name=name: self.show_context_menu(event, name))  # Bind right-click event
        elif file_extension in ["ppt", "pptx"]:
            # For PowerPoint files, display PowerPoint icon and open in default PowerPoint viewer
            powerpoint_icon = ImageTk.PhotoImage(Image.open("imagetof/powerpoint_icon.png").resize((120, 120)))
            label = tk.Label(frame, image=powerpoint_icon)
            label.image = powerpoint_icon  # Keep a reference to prevent garbage collection
            label.pack(fill="both")
            self.package_items[name] = [frame, powerpoint_icon]
            label.bind("<Button-1>", lambda event, path=file_path: self.open_powerpoint(path))
            label.bind("<Button-3>", lambda event, name=name: self.show_context_menu(event, name))  # Bind right-click event
        elif file_extension in ["xls", "xlsx"]:
            # For Excel files, display Excel icon and open in default Excel viewer
            excel_icon = ImageTk.PhotoImage(Image.open("imagetof/excel_icon.png").resize((120, 120)))
            label = tk.Label(frame, image=excel_icon)
            label.image = excel_icon  # Keep a reference to prevent garbage collection
            label.pack(fill="both")
            self.package_items[name] = [frame, excel_icon]
            label.bind("<Button-1>", lambda event, path=file_path: self.open_excel(path))
            label.bind("<Button-3>", lambda event, name=name: self.show_context_menu(event, name))  # Bind right-click event
        else:
            # For other file types, display a default icon
            default_icon = ImageTk.PhotoImage(Image.open("default_icon.png").resize((120, 120)))
            tk.Label(frame, image=default_icon).pack(fill="both")
            self.package_items[name] = [frame, default_icon]

        tk.Label(frame, text=name, wraplength=100).pack(fill="x")
        self.package_frame.add(frame)

    def import_file(self):
        file = filedialog.askopenfilename(
            title="Choose File",
            filetypes=(
                ("Images", ".PNG;.JPEG;*.JPG;*.GIF;*.BMP;"),
                ("MP3 files", "*.mp3"),
                ("MP4 files", "*.mp4"),
                ("PDF files", "*.pdf"),
                ("Text files", "*.txt"),
                ("Word files", "*.doc;*.docx"),
                ("PowerPoint files", "*.ppt;*.pptx"),
                ("Excel files", "*.xls;*.xlsx"),
                ("All files", "*.*")
            )
        )
        if file:
            filename = os.path.basename(file)
            if filename not in self.package_items:
                self.add_item(filename, file)

    def show_image(self, file_path):
        # Create a new window to display the image
        image_window = tk.Toplevel(self)
        image_window.title("Image Viewer")

        # Load and display the image
        image = Image.open(file_path)
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(image_window, image=photo)
        label.image = photo  # Keep a reference to prevent garbage collection
        label.pack()

    def play_music(self, file_path):
        # Launch the default music player to play the selected music file
        webbrowser.open(file_path)

    def open_video(self, file_path):
        if platform.system() == "Darwin":  # macOS
            subprocess.call(["open", file_path])
        elif platform.system() == "Windows":  # Windows
            subprocess.call(["start", file_path], shell=True)
        else:  # Linux
            subprocess.call(["xdg-open", file_path])

    def open_pdf(self, file_path):
        # Open PDF file in default PDF viewer
        if platform.system() == "Darwin":  # macOS
            subprocess.call(["open", file_path])
        elif platform.system() == "Windows":  # Windows
            os.startfile(file_path)
        else:  # Linux
            subprocess.call(["xdg-open", file_path])

    def open_text(self, file_path):
        # Open text file in default text editor
        if platform.system() == "Darwin":  # macOS
            subprocess.call(["open", file_path])
        elif platform.system() == "Windows":  # Windows
            os.startfile(file_path)
        else:  # Linux
            subprocess.call(["xdg-open", file_path])

    def open_word(self, file_path):
        # Open Word file in default Word viewer
        if platform.system() == "Darwin":  # macOS
            subprocess.call(["open", file_path])
        elif platform.system() == "Windows":  # Windows
            os.startfile(file_path)
        else:  # Linux
            subprocess.call(["xdg-open", file_path])

    def open_powerpoint(self, file_path):
        # Open PowerPoint file in default PowerPoint viewer
        if platform.system() == "Darwin":  # macOS
            subprocess.call(["open", file_path])
        elif platform.system() == "Windows":  # Windows
            os.startfile(file_path)
        else:  # Linux
            subprocess.call(["xdg-open", file_path])

    def open_excel(self, file_path):
        # Open Excel file in default Excel viewer
        if platform.system() == "Darwin":  # macOS
            subprocess.call(["open", file_path])
        elif platform.system() == "Windows":  # Windows
            os.startfile(file_path)
        else:  # Linux
            subprocess.call(["xdg-open", file_path])

    def show_context_menu(self, event, name):
        # Create a context menu for right-clicking on the item
        context_menu = tk.Menu(self, tearoff=0)
        context_menu.add_command(label="Delete", command=lambda: self.delete_item(name))
        context_menu.add_command(label="Print", command=lambda: self.print_item(name))  # Add print option
        context_menu.post(event.x_root, event.y_root)

    def delete_item(self, name):
        # Delete the item from the package
        item_frame, item_image = self.package_items[name]
        item_frame.destroy()
        del self.package_items[name]

    def print_item(self, name):
        # Get the default printer
        printer_name = win32print.GetDefaultPrinter()

        # Create a printer handle
        printer_handle = win32print.OpenPrinter(printer_name)

        try:
            # Start a print job
            job_info = win32print.GetPrinter(printer_handle, 2)
            job_id = win32print.StartDocPrinter(printer_handle, 1, ("Item Printing", None, None))

            try:
                # Start a new page
                win32print.StartPagePrinter(printer_handle)

                # Print the item name
                win32print.WritePrinter(printer_handle, str.encode("Item: " + name))

                # End the page
                win32print.EndPagePrinter(printer_handle)

            finally:
                # End the print job
                win32print.EndDocPrinter(printer_handle)

        finally:
            # Close the printer handle
            win32print.ClosePrinter(printer_handle)


class SlidersFrame(tk.Frame):
    def __init__(self, master=None, *args, **kw):
        super().__init__(master, *args, **kw)
        self.Frames = {}
        self.showed = None

    def add(self, id=None, show=False, OBJ=Package, *args, **kw):
        if not id:
            id = len(self.Frames)
        self.Frames[id] = OBJ(self, *args, **kw)
        if show:
            self.show(id)
        return self.Frames[id]

    def show(self, id):
        if self.showed:
            self.Frames[self.showed].pack_forget()
        self.Frames[id].pack(fill="both", expand=1)
        self.showed = id

    def remove(self, id):
        self.Frames[id].destroy()
        del (self.Frames[id])

class SideMenu(tk.Frame):
    def __init__(self, master=None, *args, **kw):
        super().__init__(master, *args, **kw)
        self.MenuItems = {}
        self.images = {}

    def add(self, name, image, func, id=None):
        if not id:
            id = len(self.MenuItems)
        self.images[id] = ImageTk.PhotoImage(Image.open(image).resize((35, 35)))
        frame = tk.Frame(self, bg='white')
        
        button_frame = tk.Frame(frame, bg='white', highlightthickness=0)
        button_frame.pack(side='right', padx=(0, 5))

        button = tk.Button(button_frame, bd=0, bg='#F0F0F0', image=self.images[id], command=func)
        button.pack(side='left', padx=(5, 0))
        
        label_frame = tk.Frame(frame, bg='white', highlightthickness=0)
        label_frame.pack(side='left')

        tk.Label(label_frame, text=name, bd=0, bg='white', font='None 10').pack(side='left')
        
        frame.pack(fill='x', ipadx='2px', ipady='2px', padx='2px', pady='2px 0')
        self.MenuItems[id] = frame
        return frame

if __name__ == "__main__":
    root = tk.Tk()
    root.iconbitmap('imagphoto/foldricon.ico')
    root.title('Secret Files')
    root.config(background='#CDD0D4')
    # root.state('zoomed')  # Maximize the window
    root.geometry('780x420')
    root.resizable(False, False)  # Disable window resizing

    side_menu = SideMenu(root)
    side_menu.pack(side='left', fill='y')

    sliders = SlidersFrame(root, bg='white')
    sliders.pack(side='right', fill='both', expand=True)

    sliders.add(id='Home', title="Home", show=True)
    sliders.add(id='Photos', title="Photos Package")
    sliders.add(id='Videos', title="Videos Package")
    sliders.add(id='Music', title="Music Package")
    sliders.add(id='Pdf', title="Pdf File Package")
    sliders.add(id='Text', title="Text Files Package")
    sliders.add(id='Word', title="Word Package")
    sliders.add(id='Excel', title="Excel File Package")
    sliders.add(id='Powerpoint', title="Powerpoint Files Package")
    

    side_menu.add('Home', 'imagphoto/home.png', func=lambda: sliders.show('Home'))
    side_menu.add('Photos', 'imagphoto/photo1.png', func=lambda: sliders.show('Photos'))
    side_menu.add('Videos', 'imagphoto/photo2.png', func=lambda: sliders.show('Videos'))
    side_menu.add('Music', 'imagphoto/photo3.png', func=lambda: sliders.show('Music'))
    side_menu.add('Pdf', 'imagphoto/pdffile.png', func=lambda: sliders.show('Pdf'))
    side_menu.add('Text', 'imagphoto/txtfile.png', func=lambda: sliders.show('Text'))
    side_menu.add('Word', 'imagphoto/word.png', func=lambda: sliders.show('Word'))
    side_menu.add('Excel', 'imagphoto/excel.png', func=lambda: sliders.show('Excel'))
    side_menu.add('Powerpoint', 'imagphoto/powerpoint.png', func=lambda: sliders.show('Powerpoint'))
    


    root.mainloop()
