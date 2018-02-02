from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

master = Tk()
master.title('Editor')
master.geometry('400x380')

text = Text(master, width=400, height=380, font=('Consolas', 12), bd=2)
text.pack()


def new_file():
    ans = messagebox.askquestion(title="Save Current File", message="Would you like to save the current file ??")
    if ans is True:
        save_file()
    delete_all()


def save_file():
    path = filedialog.asksaveasfilename()
    write = open(path, 'w')
    write.write(text.get('1.0', END))
    write.close()


def icut():
    master.clipboard_clear()
    text.clipboard_append(string=text.selection_get())
    text.delete(index1=SEL_FIRST, index2=SEL_LAST)


def icopy():
    master.clipboard_clear()
    text.clipboard_append(string=text.selection_get())


def ipaste():
    text.insert(INSERT, master.clipboard_get())


def open_file():
    new_file()
    file = filedialog.askopenfile()
    text.insert(INSERT, file.read())


def close():
    new_file()
    master.quit()


def select_all():
    text.tag_add(SEL, 1.0, END)


def delete():
    text.delete(index1=SEL_FIRST, index2=SEL_LAST)


def delete_all():
    text.delete(1.0, END)


def to_caps():
    tst = text.selection_get()
    tst = tst.upper()
    text.delete(index1=SEL_FIRST, index2=SEL_LAST)
    text.insert(INSERT, tst)


menu = Menu(master)
master.config(menu=menu)
file_menu = Menu(menu)
menu.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="open", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Close", command=close)
file_menu.add_command(label="Save", command=save_file)


edit_menu = Menu(menu)
menu.add_cascade(label='Edit', menu=edit_menu)

edit_menu.add_command(label="Cut", command=icut)
edit_menu.add_separator()
edit_menu.add_command(label="Copy", command=icopy)
edit_menu.add_command(label="Paste", command=ipaste)
edit_menu.add_separator()


edit_menu.add_command(label="Select All", command=select_all)
edit_menu.add_command(label="Capitalize", command=to_caps)
# edit_menu.add_command(label="Title", command=titl)


master.mainloop()
