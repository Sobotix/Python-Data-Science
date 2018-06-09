import pages
import tkinter as tk

class HomePage(pages.Page):
    """
    Page offering functionalities like loading different datasets into different pages
    """
    def __init__(self, master,parent):
       """
       Constructor for intialization of this page
       """
       pages.page.Page.__init__(self,master)
       self.parent=parent
       self.imgLoad=tk.PhotoImage(file="images/btnLoad.gif")
       self.imgAdd=tk.PhotoImage(file="images/btnAddVariable.gif")
       self.imgDelete=tk.PhotoImage(file="images/btnDeleteVariable.gif")
       self.imgSave=tk.PhotoImage(file="images/btnSaveVariable.gif")
       btnLoad=tk.Button(self, text="Load Dataset", command=self._btnLoadClicked,image=self.imgLoad)
       btnLoad.pack(side="top", expand=True)

       self.customVarFrame=tk.Frame(self)
       self.customVarFrame.pack(side="top",expand="true")
       #elf.customVarFrame.grid(column=0,row=0 )
       #elf.customVarFrame.columnconfigure(0, weight = 1)
       #self.customVarFrame.rowconfigure(0, weight = 1)
       #self.customVarFrame.pack(pady = 100, padx = 100)
       self.customVarFrame2=tk.Frame(self)
       self.customVarFrame2.pack(side="top",expand="true")

       self.varInputVar=tk.StringVar(self.customVarFrame)
       self.txtVarInput=tk.Entry(self.customVarFrame,textvariable=self.varInputVar)
       self.txtVarInput.pack(side="top")
       self.btnAddVar=tk.Button(self.customVarFrame,text="Add Variable",command=self._btnAddVarClicked,image=self.imgAdd)
       self.btnAddVar.pack(side="top")

       self.varsVar=tk.StringVar(self.customVarFrame2)
       self.cBoxVars=tk.OptionMenu(self.customVarFrame2, self.varsVar, *parent.getCustomvarsString())
       self.cBoxVars.config(fg='white',bg='black')
       self.cBoxVars.pack(side="top")
       self.btnDeleteVar=tk.Button(self.customVarFrame2,text="Delete Variable",command=self._btnDeleteVarClicked,image=self.imgDelete)
       self.btnDeleteVar.pack(side="top")

       self.btnSave=tk.Button(self, text="Save Variable", command=self._btnSaveClicked,image=self.imgSave)
       self.btnSave.pack(side="top", expand=True)

    def _btnLoadClicked(self):
        """
        Callback for button btnLoad Click event
        """
        self.parent.btnLoadClicked()
        pass

    def _btnSaveClicked(self):
        """
        Callback for button btnSave Click event
        """
        self.parent.btnSaveClicked(self.varsVar.get())
        pass
    
    def _btnAddVarClicked(self):
        """
        Callback for button btnAddVar click event
        """
        if self.varInputVar.get()=="" or self.varInputVar.get()==None:
            return
        else:
            self.parent.btnAddVarClicked(self.varInputVar.get())
            self.varsVar.set('')
            self.cBoxVars['menu'].delete(0, 'end')

            new_choices = self.parent.getCustomvarsString()
            for choice in new_choices:
                self.cBoxVars['menu'].add_command(label=choice, command=tk._setit(self.varsVar, choice))

    def _btnDeleteVarClicked(self):
        """
        Callback for button btnDeleteVarClick event
        """
        if self.varsVar.get()=="" or self.varsVar.get()==None:
            return
        else:
            self.parent.btnDeleteVarClicked(self.varsVar.get())
            self.varsVar.set('')
            self.cBoxVars['menu'].delete(0, 'end')
            new_choices = self.parent.getCustomvarsString()
            for choice in new_choices:
                self.cBoxVars['menu'].add_command(label=choice, command=tk._setit(self.varsVar, choice))

    def show(self):
        """
        Call this method to bring this page into view
        """
        self.refresh()
        super(HomePage,self).show()

    def refresh(self):
        """
        Refesh some controls
        Don't invoke this method manually
        """
        self.varsVar.set('')
        self.cBoxVars['menu'].delete(0, 'end')
        new_choices = self.parent.getCustomvarsString()
        for choice in new_choices:
            self.cBoxVars['menu'].add_command(label=choice, command=tk._setit(self.varsVar, choice))