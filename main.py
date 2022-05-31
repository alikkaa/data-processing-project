import tkinter
import colorsys
from tkinter import ttk
from tkinter.filedialog import askopenfilenames, askopenfilename
from PIL import ImageTk, Image, ImageDraw 
import random



def error_tab(error_text):
    error_tab = tkinter.Tk()
    error_tab.title('Resize image')
    error_tab.geometry("400x200")
    
    Label_text_error = tkinter.Label(error_tab, 
        text=error_text, 
        font=("Helvetica", 16), 
        fg='red', 
        padx=20,
        pady=50, justify=tkinter.CENTER)

    width = Label_text_error.winfo_width()

    if width > 50:
        char_width = width / len(error_text)
        wrapped_text = '\n'.join(wrap(error_text, int(600 / char_width)))
        Label_text_error['text'] = wrapped_text

    Label_text_error.pack()

    Label_text_exit = tkinter.Label(error_tab, 
        text="(Press any key to exit)", 
        font=("Helvetica", 12))

    Label_text_exit.pack(side=tkinter.BOTTOM)

    error_tab.bind("<Key>", lambda event: error_tab.destroy())
    error_tab.mainloop()


def get_file_name(file_dir):
    dir_rotate = file_dir[::-1]
    name_rotate = dir_rotate[0:dir_rotate.find('/')]
    name = name_rotate[::-1]
    return name


def choosing_files():
    root_chouse = tkinter.Tk()
    root_chouse.withdraw()
    root_chouse.geometry("800x400")

    filenames = askopenfilenames(filetypes=[
        ("image", ".jpeg"),
        ("image", ".png"),
        ("image", ".jpg"),
        ("image", ".gif"),
    ])

    return filenames

def choosing_fil():
    root_chouse = tkinter.Tk()
    root_chouse.withdraw()
    root_chouse.geometry("800x400")

    filename = askopenfilename(filetypes=[
        ("image", ".jpeg"),
        ("image", ".png"),
        ("image", ".jpg"),
        ("image", ".gif"),
    ])

    return filename


def update_frame_tab(path, frame_tab, temp_tab):
    for widget in frame_tab.winfo_children():
        if type(widget) == tkinter.Label:
            widget.destroy()
    img = ImageTk.PhotoImage(Image.open(path))
    image_tab = tkinter.Label(frame_tab, image=img)
    image_tab.pack()
    temp_tab.destroy()
    image_tab.mainloop()


def сh_size(image, width, height, resize_tab, frame_tab):
    try:
        width=int(width)
        height=int(height)
    except:
        error_tab('Значения должны быть числом!!!')

    if width < 0:
        error_tab('Ширина не может быть меньше нуля!!!')

    elif width > 1800:
        error_tab('Ширина не может быть выше 1800!!!')

    elif height < 0:
        error_tab('Ширина не может быть меньше нуля!!!')

    elif height > 1800:
        error_tab('Ширина не может быть выше 1800!!!')

    else:
        img = Image.open(image)
        img.save('temp/save_resize.png')
        new_image = img.resize((width, height))
        new_image.save(image)
        new_image.save('temp/resize_im.png')
        update_frame_tab('temp/resize_im.png', frame_tab, resize_tab)
    return



def resize_img(image, frame_tab):
    resize_tab = tkinter.Tk()
    resize_tab.title('Resize image')
    resize_tab.geometry("400x200")
    resize_tab.configure(bg='gray50')
    

    Label_width = tkinter.Label(resize_tab, text="Выберите Ширину")
    Label_width.pack()

    message_width = tkinter.Entry(resize_tab)
    message_width.pack()
    

    Label_height = tkinter.Label(resize_tab, text="Выберите Длину")
    Label_height.pack()
    message_height = tkinter.Entry(resize_tab)
    message_height.pack()


    but_resize = tkinter.Button(resize_tab, text="Resize", width=20,
                            command=lambda: 
                            сh_size(image,
                             message_width.get(),
                             message_height.get(), 
                             resize_tab, 
                             frame_tab))

    but_rand = tkinter.Button(resize_tab, text="Resize random", width=20,
                            command=lambda: 
                            сh_size(image,
                            random.randint(0,1800),
                             random.randint(0,1800), 
                             resize_tab, 
                             frame_tab))


    but_resize.pack()
    but_rand.pack()
    resize_tab.mainloop()


def сh_degree(image, degree, rotate_tab, frame_tab):
    try:
        degree=int(degree)
    except:
        error_tab('Значение должно быть целым числом!!!')
        return

    img = Image.open(image).convert('RGBA')
    img.save('temp/save_rotate.png')
    new_image = img.rotate(degree, expand=1)

    fff = Image.new('RGBA', new_image.size, (255,)*4)
    new_image = Image.composite(new_image, fff, new_image)
    img.convert(img.mode).save('test2.bmp')


    new_image.save(image)
    new_image.save('temp/rotate_img.png')
    update_frame_tab('temp/rotate_img.png', frame_tab, rotate_tab)


def rotate_img(image, frame_tab):
    rotate_tab = tkinter.Tk()
    rotate_tab.title('Rotate image')
    rotate_tab.geometry("400x200")
    rotate_tab.configure(bg='gray50')
    

    Label_degree = tkinter.Label(rotate_tab, text="Выберите угл")
    Label_degree.pack()

    message_degree = tkinter.Entry(rotate_tab)
    message_degree.pack()
    


    but_resize = tkinter.Button(rotate_tab, text="Rotate", width=20,
                            command=lambda: 
                            сh_degree(image, 
                                message_degree.get(), 
                                rotate_tab, 
                                frame_tab))


    but_random = tkinter.Button(rotate_tab, text="Rotate random", width=20,
                            command=lambda: 
                            сh_degree(image, 
                                random.randint(0, 360), 
                                rotate_tab, 
                                frame_tab))
    but_resize.pack()
    but_random.pack()
    rotate_tab.mainloop()


def ch_color(path, R, G, B, ch_color_tab, frame_tab):
    img = Image.open(path)
    img.save('temp/save_ch_color.png')
    draw = ImageDraw.Draw(img)
    width = img.size[0]  
    height = img.size[1]
    pix = img.load()

    for x in range(width):
        for y in range(height):
            try:
                r = pix[x, y][0]

            except:
                r = 255
            try:
                g = pix[x, y][1]
            except:
                g = 255
            try:
                b = pix[x, y][2]
            except:
                b = 255
            draw.point((x, y), (r - R, g - G, b - B))

    img.save(path)
    img.save("temp/ch_color_img.png")
    update_frame_tab("temp/ch_color_img.png", frame_tab, ch_color_tab)

def set_color_index(event, index):
    index[0] = int(event)


def ch_color_img(image, frame_tab):
    ch_color_tab = tkinter.Tk()
    ch_color_tab.title('Ch color image')
    ch_color_tab.geometry("800x400")
    ch_color_tab.configure(bg='gray50')

    R, G, B = [0], [0], [0]

    scl_Red = tkinter.Scale(ch_color_tab,
            orient='horizontal',
            label='Изменение красного цвета',
            from_=-255, to=255,
            tickinterval=50,
            resolution=3,
            length=600,
            command=lambda event: set_color_index(event, R))
    scl_Red.pack()

    scl_Green = tkinter.Scale(ch_color_tab,
            orient='horizontal',
            label='Изменение зеленого цвета',
            from_=-255, to=255,
            tickinterval=50,
            resolution=3,
            length=600,
            command=lambda event: set_color_index(event, G))
    scl_Green.pack()

    scl_Blue = tkinter.Scale(ch_color_tab,
            orient='horizontal',
            label='Изменение синего цвета',
            from_=-255, to=255,
            tickinterval=50,
            resolution=3,
            length=600,
            command=lambda event: set_color_index(event, B))
    scl_Blue.pack()
    

    but_resize = tkinter.Button(ch_color_tab, text="Ch color", width=20,
                            command=lambda: 
                            ch_color(image, 
                                R[0], B[0], G[0], 
                                ch_color_tab, 
                                frame_tab))

    but_random = tkinter.Button(ch_color_tab, text="Ch color random", width=20,
                            command=lambda: 
                            ch_color(image, 
                                random.randint(-255,255),
                                random.randint(-255,255),
                                random.randint(-255,255), 
                                ch_color_tab, 
                                frame_tab))
    but_resize.pack()
    but_random.pack()
    ch_color_tab.mainloop()


class CustomNotebook(ttk.Notebook):
    """A ttk Notebook with close buttons on each tab"""

    __initialized = False

    def __init__(self, *args, **kwargs):
        if not self.__initialized:
            self.__initialize_custom_style()
            self.__inititialized = True

        kwargs["style"] = "CustomNotebook"
        ttk.Notebook.__init__(self, *args, **kwargs)

        self._active = None

        self.bind("<ButtonPress-1>", self.on_close_press, True)
        self.bind("<ButtonRelease-1>", self.on_close_release)

    def on_close_press(self, event):
        """Called when the button is pressed over the close button"""

        element = self.identify(event.x, event.y)

        if "close" in element:
            index = self.index("@%d,%d" % (event.x, event.y))
            self.state(['pressed'])
            self._active = index
            return "break"

    def on_close_release(self, event):
        """Called when the button is released"""
        if not self.instate(['pressed']):
            return

        element = self.identify(event.x, event.y)
        if "close" not in element:
            # user moved the mouse off of the close button
            return

        index = self.index("@%d,%d" % (event.x, event.y))

        if self._active == index:
            self.forget(index)
            self.event_generate("<<NotebookTabClosed>>")

        self.state(["!pressed"])
        self._active = None

    def __initialize_custom_style(self):
        style = ttk.Style()
        self.images = (
            tkinter.PhotoImage("img_close", data='''
                R0lGODlhCAAIAMIBAAAAADs7O4+Pj9nZ2Ts7Ozs7Ozs7Ozs7OyH+EUNyZWF0ZWQg
                d2l0aCBHSU1QACH5BAEKAAQALAAAAAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU
                5kEJADs=
                '''),
            tkinter.PhotoImage("img_closeactive", data='''
                R0lGODlhCAAIAMIEAAAAAP/SAP/bNNnZ2cbGxsbGxsbGxsbGxiH5BAEKAAQALAAA
                AAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU5kEJADs=
                '''),
            tkinter.PhotoImage("img_closepressed", data='''
                R0lGODlhCAAIAMIEAAAAAOUqKv9mZtnZ2Ts7Ozs7Ozs7Ozs7OyH+EUNyZWF0ZWQg
                d2l0aCBHSU1QACH5BAEKAAQALAAAAAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU
                5kEJADs=
            ''')
        )

        style.element_create("close", "image", "img_close",
                             ("active", "pressed", "!disabled", "img_closepressed"),
                             ("active", "!disabled", "img_closeactive"), border=8, sticky='')
        style.layout("CustomNotebook", [("CustomNotebook.client", {"sticky": "nswe"})])
        style.layout("CustomNotebook.Tab", [
            ("CustomNotebook.tab", {
                "sticky": "nswe",
                "children": [
                    ("CustomNotebook.padding", {
                        "side": "top",
                        "sticky": "nswe",
                        "children": [
                            ("CustomNotebook.focus", {
                                "side": "top",
                                "sticky": "nswe",
                                "children": [
                                    ("CustomNotebook.label", {"side": "left", "sticky": ''}),
                                    ("CustomNotebook.close", {"side": "left", "sticky": ''}),
                                ]
                            })
                        ]
                    })
                ]
            })
        ])



def create_bg(R, G, B, size):
   img = Image.new("RGB", size, (R, G, B))
   return img


def get_background_hh(img_list, alha, frame_bg, bg_tab):
    R = random.randint(1, 255)
    G = random.randint(1, 255)
    B = random.randint(1, 255)
    size = (800, 800)
    shift = (50, 60)
    alha = int(alha)
    img = create_bg(R, G, B, size)
    for image in img_list:
        watermark = Image.open(image).convert("RGBA")
        degree = random.randint(0, 360)
        t1 = random.randint(0, size[0]/2)
        t2 = random.randint(0, size[1]/2)
        watermark = watermark.resize((t1, t2))

        rot = watermark.rotate(degree, expand=1)
        fff = Image.new('RGBA', rot.size, (R,G,B))
        watermark = Image.composite(rot, fff, rot)
        x = random.randint(0, size[0] - watermark.size[0])
        y = random.randint(0, size[1] - watermark.size[1])
        im_rgba = watermark.copy()
        im_rgba.putalpha(alha)
        img.paste(im_rgba, (x, y),  im_rgba)

    img.save('output_bg/image_bg.png')
    update_frame_tab('output_bg/image_bg.png', frame_bg, bg_tab)


def get_background_hh_not_random(img_list, alha, frame_bg, bg_tab, img):

    try:
        alha = int(alha)
    except:
        error_tab('Значение должно быть целым числом!!!')
        return

    if alha < 0:
        error_tab('Значение должно быть пожительным!!!')
        return

    if alha > 255:
        error_tab('Значение должно быть больше чем 255!!!')
        return



    img = Image.open(img)
    size = (800, 800)
    shift = (50, 60)

    for image in img_list:
        watermark = Image.open(image)
        degree = random.randint(0, 360)
        t1 = random.randint(0, int(img.size[0]/2))
        t2 = random.randint(0, int(img.size[1]/2))

        watermark = watermark.rotate(degree).resize((t1, t2)).convert("RGBA")

        x = random.randint(0, size[0] - watermark.size[0])
        y = random.randint(0, size[1] - watermark.size[1])
        im_rgba = watermark.copy()
        im_rgba.putalpha(alha)
        img.paste(im_rgba, (x, y),  im_rgba)

    img.save('output_bg/image_bg.png')
    update_frame_tab('output_bg/image_bg.png', frame_bg, bg_tab)

def create_background(tab_control):
    img_list = choosing_files()
    bg_tab = tkinter.Tk()
    bg_tab.title('Rotate image')
    bg_tab.geometry("400x200")
    bg_tab.configure(bg='gray50')
    

    Label_alpha = tkinter.Label(bg_tab, text="Выберите коэф. прозрачности")
    Label_alpha.pack()

    message_alpha = tkinter.Entry(bg_tab)
    message_alpha.pack()    


    but_resize_r = tkinter.Button(bg_tab, text="Create image with random background", 
                            width=40,
                            command=lambda: 
                            get_background_hh(img_list, message_alpha.get(), tab_control, bg_tab))

    but_resize = tkinter.Button(bg_tab, text="Create image with choose background", 
                            width=40,
                            command=lambda: 
                            get_background_hh_not_random(img_list, message_alpha.get(), tab_control, bg_tab, choosing_fil()))

    but_resize.pack()
    but_resize_r.pack()
    
    bg_tab.mainloop()


class RunGui:
    def __init__(self):
        super().__init__()
        self.root = None
        self.images = None
        self.tab_control = None
        self.img_link_list = None
        self.init_gui()


    def init_gui(self):
        self.img_link_list = []
        self.root = tkinter.Tk()
        self.root.title('Changing_image')
        self.root.iconphoto(False, tkinter.PhotoImage(file='icon.png'))
        self.root.geometry("800x400")
        self.root.configure(bg='gray50')

        self.tab_control = CustomNotebook(width=200, height=200)


        frame_top = tkinter.Frame(master=self.root, bg="gray20")
        frame_top.pack(fill=tkinter.X, side=tkinter.TOP)


        frame_tab = tkinter.Frame(master=self.root, height=30, bg="gray30")
        frame_tab.pack(fill=tkinter.X, side=tkinter.TOP)

        but_select = tkinter.Button(frame_top, text="Select Images",
                                    command=self.select_and_show_images)
        but_select.pack(side=tkinter.LEFT)


        frame_bg = tkinter.Frame(master=self.root, bg="gray20")
        frame_bg.pack(fill=tkinter.X, side=tkinter.TOP)
        but_bg = tkinter.Button(frame_bg, text="Background",
                                    command=lambda: create_background(frame_bg))

        self.tab_control.add(frame_bg, text='background')
        but_bg.pack(side=tkinter.TOP)
        self.tab_control.pack(side="top", fill="both", expand=True)
        self.root.mainloop()


    def select_and_show_images(self):
        self.images = choosing_files()
        self.create_tab()
        self.root.mainloop()



    def create_tab(self):

        for im in range(len(self.images)):#im in self.images:
            frame_tab = tkinter.Frame(self.tab_control, bg='gray40')
            frame_left = tkinter.Frame(master=frame_tab, bg="gray10")
            frame_left.pack(fill=tkinter.Y, side=tkinter.LEFT)
            
            img = ImageTk.PhotoImage(Image.open(self.images[im]))
            self.img_link_list.append(img)
            img_label = tkinter.Label(frame_tab, image=img)
            img_label.pack()

            name = get_file_name(self.images[im])
            if len(name) > 10:
                self.tab_control.add(frame_tab, text=name[:10]+'...')
            else:
                self.tab_control.add(frame_tab, text=name)
               
            but_resize = tkinter.Button(frame_left, text="Resize", width=20,
                                        command=lambda: resize_img(self.images[im], frame_tab))
            but_resize.grid(row=2, column=1)

            but_rotate = tkinter.Button(frame_left, text="Rotate", width=20,
                                        command=lambda: rotate_img(self.images[im], frame_tab))
            but_rotate.grid(row=3, column=1)

            but_ch_color = tkinter.Button(frame_left, text="Ch color", width=20,
                                        command=lambda: ch_color_img(self.images[im], frame_tab))
            but_ch_color.grid(row=4, column=1)

            self.tab_control.update()
        self.tab_control.pack(side="top", fill="both", expand=True)
        self.tab_control.mainloop()


 
if __name__ == '__main__':
    RunGui()
