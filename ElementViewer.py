
from tkinter import*
from GUI.Elements.ElemGUI import*
from typing import List
from NewElementWindow import*
from schematic import*

class ElementViewer(Canvas):

    elem_list:List[ElemGUI]
    schm:schematic
    m:Menu
    scale_val = 1
    offset = 10
    cell_size = 100
    
    def del_elem(self):
        ind = self.getSelectedIndex()
        self.schm.elem_list.pop(ind)
        self.RefreshViewer()
        self.clearSellection()


    def addElement(self,x:float,y:float,width:float,height:float,cs:ElemGUI):
        self.create_window(x,y,width=width,height=height,window=cs,anchor=NW)
        self.elem_list.append(cs)
        cs.init_menu(add_command=self.addCommand,clear_command=self.ClearCommand,clear_selection=self.clearSellection,del_elem=self.del_elem)

    def addSerRes(self,ind):
        cs = SerRes(width = self.cell_size,height=self.cell_size,index=ind,master=self)
        self.create_window(self.offset+ind*self.cell_size,self.offset,width=self.cell_size,height=self.cell_size,window=cs,anchor=NW)
        self.elem_list.append(cs)
        cs.init_menu(add_command=self.addCommand,clear_command=self.ClearCommand,clear_selection=self.clearSellection,del_elem=self.del_elem)

    def addSerCap(self,ind):
        cs = SerCap(width = self.cell_size,height=self.cell_size,index=ind,master=self)
        self.create_window(self.offset+ind*self.cell_size,self.offset,width=self.cell_size,height=self.cell_size,window=cs,anchor=NW)
        self.elem_list.append(cs)
        cs.init_menu(add_command=self.addCommand,clear_command=self.ClearCommand,clear_selection=self.clearSellection,del_elem=self.del_elem)

    def addSerInd(self,ind):     
        cs = SerInd(width = self.cell_size,height=self.cell_size,index=ind,master=self)
        self.create_window(self.offset+ind*self.cell_size,self.offset,width=self.cell_size,height=self.cell_size,window=cs,anchor=NW)
        self.elem_list.append(cs)
        cs.init_menu(add_command=self.addCommand,clear_command=self.ClearCommand,clear_selection=self.clearSellection,del_elem=self.del_elem)


    def addSerRes_schm(self,ind,val):
        serres = SerialResistor(val)
        self.schm.elem_list.insert(ind,serres)

    def addSerCap_schm(self,ind,val):
        sercap = SerialCapacitor(val)
        self.schm.elem_list.insert(ind,sercap)

    def addSerInd_schm(self,ind,val):
        serind = SerialInductor(val)
        self.schm.elem_list.insert(ind,serind)
    # type_dict = {"SerRes":addSerRes, "SerCap":addSerCap,"SerInd":addSerInd,"ParRes":addParRes,"ParCap":addParCap,"ParInd":addParInd}

    type_dict = {"SerRes":addSerRes, "SerCap":addSerCap,"SerInd":addSerInd}
    type_dict_schm = {"SerRes":addSerRes_schm, "SerCap":addSerCap_schm,"SerInd":addSerInd_schm}

    def addSchmElement(self,type,val):
        ind = self.getSelectedIndex()
        # self.type_dict[type](self=self,ind=ind+1)
        self.type_dict_schm[type](self=self,val=np.float32(val),ind=ind+1)
        self.RefreshViewer()



    def getSelectedIndex(self):
        for x in self.elem_list:
            if(x.isSelected):
                return x.index
        return -1

    def add_new_element(self):
        val = self.new_elem.textedit.get()
        self.addSchmElement(type=self.new_elem.type_dict[self.new_elem.combobox.current()],val=val)
        self.new_elem.destroy()


    dict_ss = {SerialResistor:"SerRes", SerialCapacitor:"SerCap", SerialInductor:"SerInd"}

    def ShowElement(self,elem:element,ind):
        self.type_dict[self.dict_ss[type(elem)]](self=self,ind=ind+1)

    def addCommand(self):
        # self.clearSellection()
        self.new_elem = NewElementWindow(master=self.master,addFunc=self.addSchmElement)
        ok_button = Button(self.new_elem,text="Ок",command=self.add_new_element)
        ok_button.pack(anchor="e",pady=5)
        self.new_elem.mainloop()


    
    def ClearCommand(self):
        self.clearSellection()

    def onclick(self,event):
        self.clearSellection()

    def do_popup(self,event): 
        try: 
            self.m.tk_popup(event.x_root, event.y_root) 
        finally: 
            self.m.grab_release() 

    def __init__(self,master,UpdateSmithChart,ax):
        super().__init__(bg="white",bd=0, highlightthickness=0)
        self.Update = UpdateSmithChart
        self.bind('<Button-1>',self.onclick)
        self.master = master
        self.ax = ax
        self.elem_list = []
        self.m = Menu(master,tearoff=0)
        self.m.add_command(label ="Новый элемент",command=self.addCommand) 
        self.bind("<Button-3>", self.do_popup) 
        self.schm = schematic(50,50)




    def RefreshViewer(self):
        for x in self.elem_list:
            x.destroy()
        self.elem_list = []  
        for x in range(0,len(self.schm.elem_list)):
            self.ShowElement(self.schm.elem_list[x],x-1)
      
        self.Update(ax=self.ax,schema = self.schm,frequency = 1e9)


    def clearSellection(self):
        for x in self.elem_list:
            x.clearSellection()
    
    
    