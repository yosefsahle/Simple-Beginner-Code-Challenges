from tkinter import *
from tkinter import filedialog
from tkinter import font

root = Tk()
root.title('YOSEF SAHLE')
root.geometry("400x400")

my_frame = Frame(root)
my_frame.pack(pady=10)

text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

my_text = Text(my_frame, width=40, height=10, font=("Helvetica", 16),
               selectbackground="black", yscrollcommand=text_scroll.set, undo=True,)
my_text.pack()

text_scroll.config(command=my_text.yview)

my_label = Label(
    root, text="YOSEF SAHLE @ SOLOLEARN\n undo redo Functionality", font=("Cursive", 10))
my_label.pack()

undo_button = Button(root, text="Undo", command=my_text.edit_undo)
undo_button.pack(pady=5)

redo_button = Button(root, text="Redo", command=my_text.edit_redo)
redo_button.pack(pady=5)

root.mainloop()
