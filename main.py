from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename


class MyWindow(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.create_menu_bar()

        # TODO: Fill the content of the window

        self.geometry("300x200")
        self.title("")

    def create_menu_bar(self):
        menu_bar = Menu(self)

        menu_file = Menu(menu_bar, tearoff=0)
        menu_file.add_command(label="Nouveau", command=self.do_something)
        menu_file.add_command(label="Ouvrir", command=self.open_file)
        menu_file.add_command(label="Enregistrer", command=self.do_something)
        menu_file.add_separator()
        menu_file.add_command(label="Quitter", command=self.quit)
        menu_bar.add_cascade(label="Fichier", menu=menu_file)

        menu_edit = Menu(menu_bar, tearoff=0)
        menu_edit.add_command(label="Annuler", command=self.do_something)
        menu_edit.add_separator()
        menu_edit.add_command(label="Copier", command=self.do_something)
        menu_edit.add_command(label="Couper", command=self.do_something)
        menu_edit.add_command(label="Coller", command=self.do_something)
        menu_bar.add_cascade(label="Editer", menu=menu_edit)

        menu_help = Menu(menu_bar, tearoff=0)
        menu_help.add_command(label="A propos", command=self.do_about)
        menu_bar.add_cascade(label="Aide", menu=menu_help)

        self.config(menu=menu_bar)

    def open_file(self):
        file = askopenfilename(title="Choose the file to open",
                               filetypes=[("PNG image", ".png"), ("GIF image", ".gif"), ("All files", ".*")])
        print(file)

    def do_something(self):
        window1 = MyWindow()
        window1.title("New Window")
        window1.geometry("750x600")


    def do_about(self):
        messagebox.showinfo("My title", "My message")


window = MyWindow()
window.geometry("750x600")
window.mainloop()