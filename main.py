# ************************************
# Python Text Editor
# ************************************
import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *


def change_color():
    color = colorchooser.askcolor()
    text_area.config(fg=str(color[1]))


def change_font(*args):
    text_area.config(font=(font_name.get(), size_box.get()))


def new_file():
    window.title("Untitled")
    text_area.delete(1.0, END)


def open_file():
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

    try:

        try:
            window.title(os.path.basename(file))
            text_area.delete(1.0, END)

            file = open(file, "r")

            text_area.insert(1.0, file.read())

        except Exception:
            print("couldn't read file")

        finally:
            file.close()

    except AttributeError:

        window.title("Text Editor")
        print(AttributeError)


def save_file():
    file = filedialog.asksaveasfilename(initialfile='unititled.txt',
                                        defaultextension=".txt",
                                        filetypes=[("All Files", "*.*"),
                                                   ("Text Documents", "*.txt")])

    try:

        try:
            window.title(os.path.basename(file))
            file = open(file, "w")

            file.write(text_area.get(1.0, END))

        except Exception:
            print("couldn't save file")

        finally:
            file.close()

    except AttributeError:

        window.title("Text Editor")
        print(AttributeError)


def cut():
    text_area.event_generate("<<Cut>>")


def copy():
    text_area.event_generate("<<Copy>>")


def paste():
    text_area.event_generate("<<Paste>>")


def about():
    showinfo("About this program", "Text Editor v0.1")


def quit():
    window.destroy()


def set_size():
    try:
        if 0 <= int(size_box.get()) <= 100:
            text_area.config(font=(font_name.get(), size_box.get()))
        else:
            showinfo(title="Not Valid", message="Enter valid number between 0 and 100")
    except ValueError:
        showinfo(title="Not Valid", message="Enter valid number between 0 and 100")


window = Tk()
window.title("Text Editor")

file = None

window_width = 500
window_height = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width - window_width) / 2)
y = int((screen_height - window_height) / 2)

# window.geometry("500x500+550+200")
window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y, ))

font_name = StringVar(window)
font_name.set("Arial")

font_size = StringVar(window)
font_size.set("25")

text_area = Text(window, font=(font_name.get(), font_size.get()))

scroll_bar = Scrollbar(text_area,
                       command=text_area.yview)  # command=text_area.yview enables scroll to be clicked by mouse
window.grid_rowconfigure(0, weight=1)  # Creating row for grid in window
window.grid_columnconfigure(0, weight=1)  # Creating column for grid in window

text_area.grid(sticky=W + E + N + S)
scroll_bar.pack(side=RIGHT, fill=Y)
text_area.config(
    yscrollcommand=scroll_bar.set)  # Set the yscrollcommand property of the scrollable widget so it links to the
# scrollbar.
# text_area['yscrollcommand']= scroll_bar.set

frame = Frame(window)
frame.grid(row=1, column=0)

color_button = Button(frame, text="color", command=change_color)
color_button.grid(row=0, column=0)

font_size_change = OptionMenu(frame, font_name, *font.families(), command=change_font)
font_size_change.grid(row=0, column=1)

size_box = Spinbox(frame, from_=1, to=100, textvariable=font_size, command=change_font, )
size_box.grid(row=0, column=2)

set_button = Button(frame, text="Set", command=set_size)
set_button.grid(row=0, column=3)

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
edit_menu = Menu(menu_bar, tearoff=0)
about_menu = Menu(menu_bar, tearoff=0)

menu_bar.add_cascade(label='File', menu=file_menu)
menu_bar.add_cascade(label='Edit', menu=edit_menu)
menu_bar.add_cascade(label='About', menu=about_menu)

file_menu.add_command(label='New', command=new_file)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_file)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=quit)

edit_menu.add_command(label='Cut', command=cut)
edit_menu.add_command(label='Copy', command=copy)
edit_menu.add_command(label='Paste', command=paste)

about_menu.add_command(label='Help', command=about)

window.mainloop()
