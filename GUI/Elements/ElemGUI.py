from tkinter import Canvas
from tkinter import Menu
import tkinter as tk

class ElemGUI(Canvas):
    elem_width = 0
    elem_height = 0
    y_connection = 0
    index = 0
    
    id1 = 0
    id2 = 0
    id3 = 0
    id4 = 0
    isSelected = False

    m:Menu

    def select(self):
        self.clear_selection()
        if(not self.isSelected):
            self.id1 = self.create_line(0, 0, self.elem_width, 0,width=3,fill="blue")
            self.id2 = self.create_line(self.elem_width, 0, self.elem_width, self.elem_height,width=3,fill="blue")
            self.id3 = self.create_line(self.elem_width, self.elem_height, 0, self.elem_height,width=3,fill="blue")
            self.id4 = self.create_line(0, self.elem_height, 0, 0,width=3,fill="blue")
            self.isSelected = True

    def do_popup(self,event): 
        self.select()
        try: 
            self.m.tk_popup(event.x_root, event.y_root) 
        finally: 
            self.m.grab_release() 

    def onclick(self,event):
            self.select()

    def clearSellection(self):
        if(self.isSelected):
            self.delete(self.id1)
            self.delete(self.id2)
            self.delete(self.id3)
            self.delete(self.id4)
            self.isSelected = False



    def init_menu(self,add_command,clear_command,clear_selection,del_elem):
        self.clear_selection = clear_selection        
        self.m = Menu(self.master,tearoff=0)
        self.m.add_command(label ="Новый элемент",command=add_command) 
        self.m.add_command(label ="Удалить", command=del_elem) 
        self.m.add_separator()
        self.m.add_command(label="Параметры")
        self.bind("<Button-3>", self.do_popup)


    def __init__(self,width,height,index,master):
        super().__init__(bg="white",width=width,height=height,bd=0, highlightthickness=0,master=master)
        self.elem_width = width
        self.elem_height = height
        self.master = master
        self.index = index
        self.bind('<Button-1>',self.onclick)


#------------------------------#
#--------Посл. элементы--------#
#------------------------------#

#Пол. Резистор

class SerRes(ElemGUI):
    def __init__(self,width,height,index,master):
        super().__init__(width=width,height=height,index=index,master=master)
        self.elem_width = width
        self.elem_height = height
        self.create_line(0, self.elem_height*0.5, self.elem_width*2/6, self.elem_height*0.5,width=3)
        self.create_line(self.elem_width*4/6, self.elem_height*0.5, self.elem_width, self.elem_height*0.5,width=3)

        self.create_line(self.elem_width*2/6, self.elem_height*0.4, self.elem_width*2/6, self.elem_height*0.6,width=3)
        self.create_line(self.elem_width*4/6, self.elem_height*0.4, self.elem_width*4/6, self.elem_height*0.6,width=3)

        self.create_line(self.elem_width*2/6, self.elem_height*0.6, self.elem_width*4/6, self.elem_height*0.6,width=3)
        self.create_line(self.elem_width*2/6, self.elem_height*0.4, self.elem_width*4/6, self.elem_height*0.4,width=3)
        self.y_connection = self.elem_height*0.5

class SerInd(ElemGUI):
    def __init__(self,width,height,index,master):
        super().__init__(width=width,height=height,index=index,master=master)
        self.elem_width = width
        self.elem_height = height
        
        #connections lines
        self.create_line(0, self.elem_height*0.5, self.elem_width*1/6, self.elem_height*0.5,width=3)
        self.create_line(self.elem_width*5/6, self.elem_height*0.5, self.elem_width, self.elem_height*0.5,width=3)

        #circs. lines
        self.create_arc(self.elem_width*1/6, self.elem_height*0.6,self.elem_width*2/6, self.elem_height*0.4,style = tk.ARC,width=3,extent = 180)
        self.create_arc(self.elem_width*2/6, self.elem_height*0.6,self.elem_width*3/6, self.elem_height*0.4,style = tk.ARC,width=3,extent = 180)
        self.create_arc(self.elem_width*3/6, self.elem_height*0.6,self.elem_width*4/6, self.elem_height*0.4,style = tk.ARC,width=3,extent = 180)
        self.create_arc(self.elem_width*4/6, self.elem_height*0.6,self.elem_width*5/6, self.elem_height*0.4,style = tk.ARC,width=3,extent = 180)
        self.y_connection = self.elem_height*0.5


class SerCap(ElemGUI):

    def __init__(self,width,height,index,master):
        super().__init__(width=width,height=height,index=index,master=master)
        self.elem_width = width
        self.elem_height = height
        self.create_line(0, self.elem_height*0.5, self.elem_width*2/5, self.elem_height*0.5,width=3)
        self.create_line(self.elem_width*3/5, self.elem_height*0.5, self.elem_width, self.elem_height*0.5,width=3)
        self.create_line(self.elem_width*2/5, self.elem_height*0.3, self.elem_width*2/5, self.elem_height*0.7,width=3)
        self.create_line(self.elem_width*3/5, self.elem_height*0.3, self.elem_width*3/5, self.elem_height*0.7,width=3)
        self.y_connection = self.elem_height*0.5


#-------------------------------#
#---------Пар. элементы---------#
#-------------------------------#

class ParRes(ElemGUI):
    def __init__(self,width,height,index,master):
        super().__init__(width=width,height=height,index=index,master=master)
        self.elem_width = width
        self.elem_height = height

        self.create_line(0, self.elem_height*1/3, self.elem_width, self.elem_height*1/3,width=3)

        self.create_line(self.elem_width*0.5, self.elem_height*1/3, self.elem_width*0.5, self.elem_height*1/3+self.elem_height*2/3*2/6,width=3)
        self.create_line(self.elem_width*0.5, self.elem_height*1/3+self.elem_height*2/3*4/6, self.elem_width*0.5, self.elem_height,width=3)


        self.create_line(self.elem_width*0.4, self.elem_height*1/3+self.elem_height*2/3*2/6, self.elem_width*0.6, self.elem_height*1/3+self.elem_height*2/3*2/6,width=3)
        self.create_line(self.elem_width*0.4, self.elem_height*1/3+self.elem_height*2/3*4/6, self.elem_width*0.6, self.elem_height*1/3+self.elem_height*2/3*4/6,width=3)

        self.create_line(self.elem_width*0.4, self.elem_height*1/3+self.elem_height*2/3*2/6, self.elem_width*0.4, self.elem_height*1/3+self.elem_height*2/3*4/6,width=3)
        self.create_line(self.elem_width*0.6, self.elem_height*1/3+self.elem_height*2/3*2/6, self.elem_width*0.6, self.elem_height*1/3+self.elem_height*2/3*4/6,width=3)       

        #Ground
        self.create_line(self.elem_width*0.3, self.elem_height-2, self.elem_width*0.7, self.elem_height-2,width=3)

        self.y_connection = self.elem_height*1/3

class ParCap(ElemGUI):
    def __init__(self,width,height,index,master):
        super().__init__(width=width,height=height,index=index,master=master)
        self.elem_width = width
        self.elem_height = height

        self.create_line(0, self.elem_height*1/3, self.elem_width, self.elem_height*1/3,width=3)

        self.create_line(self.elem_width*0.5, self.elem_height*1/3, self.elem_width*0.5, self.elem_height*1/3+self.elem_height*2/3*2/5,width=3)
        self.create_line(self.elem_width*0.5, self.elem_height*1/3+self.elem_height*2/3*3/5, self.elem_width*0.5, self.elem_height,width=3)


        self.create_line(self.elem_width*0.3, self.elem_height*1/3+self.elem_height*2/3*2/5, self.elem_width*0.7, self.elem_height*1/3+self.elem_height*2/3*2/5,width=3)
        self.create_line(self.elem_width*0.3, self.elem_height*1/3+self.elem_height*2/3*3/5, self.elem_width*0.7, self.elem_height*1/3+self.elem_height*2/3*3/5,width=3)
     

        #Ground
        self.create_line(self.elem_width*0.3, self.elem_height-2, self.elem_width*0.7, self.elem_height-2,width=3)

        self.y_connection = self.elem_height*1/3


class ParInd(ElemGUI):
    def __init__(self,width,height,index,master):
        super().__init__(width=width,height=height,index=index,master=master)
        self.elem_width = width
        self.elem_height = height

        self.create_line(0, self.elem_height*1/3, self.elem_width, self.elem_height*1/3,width=3)

        self.create_line(self.elem_width*0.5, self.elem_height*1/3, self.elem_width*0.5, self.elem_height*1/3+self.elem_height*2/3*1/6,width=3)
        self.create_line(self.elem_width*0.5, self.elem_height*1/3+self.elem_height*2/3*5/6, self.elem_width*0.5, self.elem_height,width=3)

        self.create_arc(self.elem_width*0.6-3, self.elem_height*1/3+self.elem_height*2/3*1/6+self.elem_height*2/3*4/6*0/4,self.elem_width*0.5-3, self.elem_height*1/3+self.elem_height*2/3*1/6+self.elem_height*2/3*4/6*1/4,style = tk.ARC,width=3,extent = 180,start = -90)             
        self.create_arc(self.elem_width*0.6-3, self.elem_height*1/3+self.elem_height*2/3*1/6+self.elem_height*2/3*4/6*1/4,self.elem_width*0.5-3, self.elem_height*1/3+self.elem_height*2/3*1/6+self.elem_height*2/3*4/6*2/4,style = tk.ARC,width=3,extent = 180,start = -90)             
        self.create_arc(self.elem_width*0.6-3, self.elem_height*1/3+self.elem_height*2/3*1/6+self.elem_height*2/3*4/6*2/4,self.elem_width*0.5-3, self.elem_height*1/3+self.elem_height*2/3*1/6+self.elem_height*2/3*4/6*3/4,style = tk.ARC,width=3,extent = 180,start = -90)             
        self.create_arc(self.elem_width*0.6-3, self.elem_height*1/3+self.elem_height*2/3*1/6+self.elem_height*2/3*4/6*3/4,self.elem_width*0.5-3, self.elem_height*1/3+self.elem_height*2/3*1/6+self.elem_height*2/3*4/6*4/4,style = tk.ARC,width=3,extent = 180,start = -90)             
                 
        #Ground
        self.create_line(self.elem_width*0.3, self.elem_height-2, self.elem_width*0.7, self.elem_height-2,width=3)

        self.y_connection = self.elem_height*1/3