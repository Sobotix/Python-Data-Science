import pages
import tkinter as tk

class AssignPage(pages.Page):
    """
    Page supporting creation/deletion/assigning of user-defined variables
    """
    def __init__(self, master,parent):
       """
       Constructor for initialization
       """
       pages.page.Page.__init__(self,master)
       self.parent=parent

       self.varsVar=tk.StringVar(self)
       self.cBoxVars=tk.OptionMenu(self, self.varsVar, *parent.getCustomvarsString())
       self.cBoxVars.pack(side="top", expand="true")

       self.customVarFrame=tk.Frame(self)
       self.customVarFrame.pack(side="top",expand="true")
       self.customFrame1=tk.Frame(self)
       self.customFrame1.pack(side="top",expand="true")
       self.customFrame2=tk.Frame(self)
       self.customFrame2.pack(side="top",expand="true")

       self.imgAssignTop=tk.PhotoImage(file="images/btnAssignTop.gif")
       self.imgAssignMean=tk.PhotoImage(file="images/btnPivotMean.gif")
       self.imgAssignMedian=tk.PhotoImage(file="images/btnPivotMedian.gif")
       self.varTopInput=tk.StringVar(self.customVarFrame)
       self.txtTopInput=tk.Spinbox(self.customVarFrame, from_ = 1, to = 300,textvariable=self.varTopInput)
       self.txtTopInput.pack(side="top")
       self.btnAssignTop=tk.Button(self.customVarFrame,text="Assign Top",command=self._btnAssignTopClicked,image=self.imgAssignTop)
       self.btnAssignTop.pack(side="top")

       columns=parent.getColumns()

       self.lstPivotMeanCol=tk.Listbox(self.customFrame1, selectmode=tk.MULTIPLE,exportselection=0)
       for column in columns:
           self.lstPivotMeanCol.insert(tk.END, column)
       self.lstPivotMeanCol.pack(side="left")
       self.lstPivotMeanIndex=tk.Listbox(self.customFrame1, selectmode=tk.MULTIPLE,exportselection=0)
       for column in columns:
           self.lstPivotMeanIndex.insert(tk.END, column)
       self.lstPivotMeanIndex.pack(side="left")
       self.btnAssignPivotMean=tk.Button(self.customFrame1,text="Assign Pivot Mean",command=self._btnAssignPivotMeanClicked,image=self.imgAssignMean)
       self.btnAssignPivotMean.pack(side="left")
       self.btnAssignPivotMedian=tk.Button(self.customFrame1,text="Assign Pivot Median",command=self._btnAssignPivotMedianClicked,image=self.imgAssignMedian)
       self.btnAssignPivotMedian.pack(side="left")

    def _btnAssignTopClicked(self):
        """
        Callback for button btnAssignTop click event
        """
        self.parent.btnAssignTopClicked(self.varsVar.get(),self.varTopInput.get())

    def _btnAssignPivotMeanClicked(self):
        """
        Callback for button btnAssignPivotMean click event
        """
        self.parent.btnAssignPivotMeanClicked(self.varsVar.get(),map(int, self.lstPivotMeanCol.curselection()),map(int, self.lstPivotMeanIndex.curselection()))

    def _btnAssignPivotMedianClicked(self):
        """
        Callback for button btnAssignPivotMedian click event
        """
        self.parent.btnAssignPivotMedianClicked(self.varsVar.get(),map(int, self.lstPivotMeanCol.curselection()),map(int, self.lstPivotMeanIndex.curselection()))

    def show(self):
        """
        Call this method to bring this page into view
        """
        super(AssignPage,self).show()
        self.refresh()

    def refresh(self):
        """
        Refesh some controls
        Don't invoke this method manually
        """
        columns=self.parent.getColumns()
        self.lstPivotMeanCol.delete(0,tk.END)
        self.lstPivotMeanIndex.delete(0, tk.END)
        for column in columns:
            self.lstPivotMeanCol.insert(tk.END, column)
            self.lstPivotMeanIndex.insert(tk.END, column)

        self.varsVar.set('')
        self.cBoxVars['menu'].delete(0, 'end')
        new_choices = self.parent.getCustomvarsString()
        for choice in new_choices:
            self.cBoxVars['menu'].add_command(label=choice, command=tk._setit(self.varsVar, choice))
