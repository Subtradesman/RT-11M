

from GUI.Elements.SerCap  import*
from tkinter import*
from tkinter.ttk import*

class NewElementWindow(Toplevel):

    def show_ser_res(self):
        self.elem = SerRes(100,100,0,self)
        self.elem.pack(side="top")

    def show_ser_cap(self):
        self.elem = SerCap(100,100,0,self) 
        self.elem.pack(side="top")
    
    def show_ser_ind(self):
        self.elem = SerInd(100,100,0,self) 
        self.elem.pack(side="top")

    def show_par_res(self):
        self.elem = ParRes(100,100,0,self) 
        self.elem.pack(side="top")
    def show_par_cap(self):
        self.elem = ParCap(100,100,0,self) 
        self.elem.pack(side="top")
    def show_par_ind(self):
        self.elem = ParInd(100,100,0,self) 
        self.elem.pack(side="top")


    func_opt ={0:show_ser_cap,
               1:show_ser_res,
               2:show_ser_ind,
               3:show_par_cap,
               4:show_par_res,
               5:show_par_ind}

    def comb_change(self,event):
        self.elem.forget()
        self.func_opt[self.combobox.current()](self=self)

    type_dict = {1:"SerRes", 0:"SerCap",2:"SerInd"}



    def __init__(self,master,addFunc):
        super().__init__(master=master)
        self.geometry("200x200")
        self.title("New element")
        self.resizable(False, False)

        self.addFunc = addFunc

        elements = ["Посл. Конденсатор","Посл. Резистор","Посл. Индуктивность","Пар. Конденсатор","Пар. Резистор","Пар. Индуктивность"]
        self.combobox = Combobox(self,values=elements,state="readonly")
        self.combobox.set(elements[0])
        self.combobox.bind('<<ComboboxSelected>>', self.comb_change) 
        self.combobox.pack()

        label = Label(self, text="Параметр:")
        label.pack()

        self.textedit = Entry(self)
        self.textedit.pack()

        # ok_button = Button(self,text="Ок")
        # ok_button.pack(anchor="e",pady=5)

        self.elem = SerCap(100,100,0,self)
        self.elem.pack()

        self.grab_set()
        
