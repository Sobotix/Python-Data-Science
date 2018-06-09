import pages
import tkinter as tk
import visualizer

class DataMungingPage(pages.Page):
    """
    Page offering different data munging options
    """
    def __init__(self, master,parent):
       """
       Constructor for intialization of this page
       """
       pages.page.Page.__init__(self,master)
       self.parent=parent

       #Top row for Custom Variable selection
       self.varsVar=tk.StringVar(self)
       self.varsVar.trace("w",self._varsVarSelectionChanged)
       self.cBoxVars=tk.OptionMenu(self, self.varsVar, *parent.getCustomvarsString())
       self.cBoxVars.pack(side="top", expand="true")


       #Stack panels for individual rows
       self.customFrame1=tk.Frame(self)
       self.customFrame1.pack(side="top",expand="true")
       self.customFrame2=tk.Frame(self)
       self.customFrame2.pack(side="top",expand="true")
       self.customFrame3=tk.Frame(self)
       self.customFrame3.pack(side="top",expand="true")
       self.customFrame4=tk.Frame(self)
       self.customFrame4.pack(side="top",expand="true")
       self.customFrame5=tk.Frame(self)
       self.customFrame5.pack(side="top",expand="true")
       self.customFrame6=tk.Frame(self)
       self.customFrame6.pack(side="top",expand="true")
       self.customFrame7=tk.Frame(self)
       self.customFrame7.pack(side="top",expand="true")
       self.customFrame8=tk.Frame(self)
       self.customFrame8.pack(side="top",expand="true")
       self.customFrame9=tk.Frame(self)
       self.customFrame9.pack(side="top",expand="true")
       self.customFrame10=tk.Frame(self)
       self.customFrame10.pack(side="top",expand="true")

       #Buttons Images
       self.imgAddColumn=tk.PhotoImage(file="images/btnAddColumns.gif")
       self.imgFillMean=tk.PhotoImage(file="images/btnFillMissingWithMean.gif")
       self.imgFillMedian=tk.PhotoImage(file="images/btnFillMissingWithMedian.gif")
       self.imgFillMeanGrouped=tk.PhotoImage(file="images/btnFillMissingWithMeanGrouped.gif")
       self.imgFillMedianGrouped=tk.PhotoImage(file="images/btnFillMissingWithMedianGrouped.gif")
       self.imgLogTransform=tk.PhotoImage(file="images/btnLogTransform.gif")
       
       #Row: Add Columns
       self.varAddColumn1=tk.StringVar(self.customFrame1)
       self.cBoxAddColumn1=tk.OptionMenu(self.customFrame1, self.varAddColumn1, *parent.getColumns(parent.getVarValue(self.varsVar.get())))
       self.cBoxAddColumn1.pack(side="left", expand="true")
       self.varAddColumn2=tk.StringVar(self.customFrame1)
       self.cBoxAddColumn2=tk.OptionMenu(self.customFrame1, self.varAddColumn2, *parent.getColumns(parent.getVarValue(self.varsVar.get())))
       self.cBoxAddColumn2.pack(side="left", expand="true")
       self.varAddColumnOut=tk.StringVar(self.customFrame1)
       self.txtAddColumnOut=tk.Entry(self.customFrame1,textvariable=self.varAddColumnOut)
       self.txtAddColumnOut.pack(side="left")
       self.btnAddColumn=tk.Button(self.customFrame1,text="Add Column",command=self._btnAddColumnClicked, image=self.imgAddColumn)
       self.btnAddColumn.pack(side="left")

       #Row: Fill Missing With Mean 
       self.varFillMean=tk.StringVar(self.customFrame2)
       self.cBoxFillMean=tk.OptionMenu(self.customFrame2, self.varFillMean, *parent.getColumns(parent.getVarValue(self.varsVar.get())))
       self.cBoxFillMean.pack(side="left", expand="true")
       self.btnFillMean=tk.Button(self.customFrame2,text="Fill Missing With Mean",command=self._btnFillMeanClicked, image=self.imgFillMean)
       self.btnFillMean.pack(side="left")

       #Row: Fill Missing With Median
       self.varFillMedian=tk.StringVar(self.customFrame3)
       self.cBoxFillMedian=tk.OptionMenu(self.customFrame3, self.varFillMedian, *parent.getColumns(parent.getVarValue(self.varsVar.get())))
       self.cBoxFillMedian.pack(side="left", expand="true")
       self.btnFillMedian=tk.Button(self.customFrame3,text="Fill Missing With Median",command=self._btnFillMedianClicked, image=self.imgFillMedian)
       self.btnFillMedian.pack(side="left")

       #Row: Fill Missing With Mean Grouped and Fill Missing With Median Grouped
       self.varFillMeanGroup=tk.StringVar(self.customFrame4)
       self.cBoxFillMeanGroup=tk.OptionMenu(self.customFrame4, self.varFillMeanGroup, *parent.getColumns(parent.getVarValue(self.varsVar.get())))
       self.cBoxFillMeanGroup.pack(side="left", expand="true")
       columns=parent.getColumns(parent.getVarValue(self.varsVar.get()))
       self.lstFillMeanIndex=tk.Listbox(self.customFrame4, selectmode=tk.MULTIPLE,exportselection=0)
       for column in columns:
           self.lstFillMeanIndex.insert(tk.END, column)
       self.lstFillMeanIndex.pack(side="left")
       self.lstFillMeanCol=tk.Listbox(self.customFrame4, selectmode=tk.MULTIPLE,exportselection=0)
       for column in columns:
           self.lstFillMeanCol.insert(tk.END, column)
       self.lstFillMeanCol.pack(side="left")
       self.btnFillMeanGroup=tk.Button(self.customFrame4,text="Fill Missing With Mean Grouped",command=self._btnFillMeanGroupClicked, image=self.imgFillMeanGrouped)
       self.btnFillMeanGroup.pack(side="left")
       self.btnFillMedianGroup=tk.Button(self.customFrame4,text="Fill Missing With Median Grouped",command=self._btnFillMedianGroupClicked, image=self.imgFillMedianGrouped)
       self.btnFillMedianGroup.pack(side="top")

       #Row: Log Transform
       self.varLogColumn=tk.StringVar(self.customFrame5)
       self.cBoxLogColumn=tk.OptionMenu(self.customFrame5, self.varLogColumn, *parent.getColumns(parent.getVarValue(self.varsVar.get())))
       self.cBoxLogColumn.pack(side="left", expand="true")
       self.varLogColumnOut=tk.StringVar(self.customFrame5)
       self.txtLogColumnOut=tk.Entry(self.customFrame5,textvariable=self.varLogColumnOut)
       self.txtLogColumnOut.pack(side="left")
       self.btnLogColumn=tk.Button(self.customFrame5,text="Log Transform",command=self._btnLogColumnClicked, image=self.imgLogTransform)
       self.btnLogColumn.pack(side="left")

       #Impute
       #tk.Label(self.customFrame6,text="Fit Model:  ").pack(side="left")
       #self.varFitModel=tk.StringVar(self.customFrame6)
       #self.cBoxFitModel=tk.OptionMenu(self.customFrame6, self.varFitModel, *parent.getCustomvarsString())
       #self.cBoxFitModel.pack(side="left", expand="true")
       #tk.Label(self.customFrame6,text="Strategy:  ").pack(side="left")
       #self.varImputeStrategy=tk.StringVar(self.customFrame6)
       #options=['mean','median']
       #self.cBoxImputeStrategy=tk.OptionMenu(self.customFrame6, self.varImputeStrategy, *options)
       #self.cBoxImputeStrategy.pack(side="left", expand="true")
       #self.btnImpute=tk.Button(self.customFrame6,text="Impute",command=self._btnImputeClicked)
       #self.btnImpute.pack(side="left")

       #Multi Impute
       #tk.Label(self.customFrame7,text="Fit Model:  ").pack(side="left")
       #self.varMFitModel=tk.StringVar(self.customFrame7)
       #self.cBoxMFitModel=tk.OptionMenu(self.customFrame7, self.varMFitModel, *parent.getCustomvarsString())
       #self.cBoxMFitModel.pack(side="left", expand="true")
       #tk.Label(self.customFrame7,text="Imputation Order:  ").pack(side="left")
       #self.varMImputeOrder=tk.StringVar(self.customFrame7)
       #options=['ascending']
       #self.cBoxMImputeOrder=tk.OptionMenu(self.customFrame7, self.varMImputeOrder, *options)
       #self.cBoxMImputeOrder.pack(side="left", expand="true")
       #tk.Label(self.customFrame7,text="Strategy:  ").pack(side="left")
       #self.varMImputeStrategy=tk.StringVar(self.customFrame7)
       #options=['mean','median']
       #self.cBoxMImputeStrategy=tk.OptionMenu(self.customFrame7, self.varMImputeStrategy, *options)
       #self.cBoxMImputeStrategy.pack(side="left", expand="true")
       #Multi Impute Row 2
       #tk.Label(self.customFrame8,text="Burn In:  ").pack(side="left")
       #self.varBurnIn=tk.StringVar(self.customFrame8)
       #self.varBurnIn.set(10)
       #self.txtBurnIn=tk.Spinbox(self.customFrame8, from_ = 1, to = 300,textvariable=self.varBurnIn)
       #self.txtBurnIn.pack(side="left")
       #tk.Label(self.customFrame8,text="Imputations:  ").pack(side="left")
       #self.varImputations=tk.StringVar(self.customFrame8)
       #self.varImputations.set(10)
       #self.txtImputations=tk.Spinbox(self.customFrame8, from_ = 1, to = 300,textvariable=self.varImputations)
       #self.txtImputations.pack(side="left")
       #tk.Label(self.customFrame8,text="Nearest Features:  ").pack(side="left")
       #self.varNFeatures=tk.StringVar(self.customFrame8)
       #self.txtNFeatures=tk.Spinbox(self.customFrame8, from_ = 1, to = 300,textvariable=self.varNFeatures)
       #self.txtNFeatures.pack(side="left")
       #Multi Impute Row 3
       #self.btnMImpute=tk.Button(self.customFrame9,text="Multi Impute",command=self._btnMImputeClicked)
       #self.btnMImpute.pack(side="left")
       

       #Row: Output Console
       self.txtOutput=tk.Text(self.customFrame10)
       self.txtOutput.config(font=("consolas",8),bg='green',wrap="none")
       self.txtOutput.pack(side="top")
       self.sbTxtOutputY=tk.Scrollbar(self.customFrame10,command=self.txtOutput.yview)
       self.txtOutput['yscrollcommand']=self.sbTxtOutputY.set
       self.sbTxtOutputY.pack(side="left", expand=True,fill="y")
       self.sbTxtOutputX=tk.Scrollbar(self.customFrame10,command=self.txtOutput.xview)
       self.txtOutput['xscrollcommand']=self.sbTxtOutputX.set
       self.sbTxtOutputX.pack(side="top", expand=True,fill="x")

    def _btnAddColumnClicked(self):
        """
        Callback for button btnAddColumn click event
        """
        self.parent.btnAddColumnClicked(self.varsVar.get(),self.varAddColumn1.get(),self.varAddColumn2.get(),self.varAddColumnOut.get())

    def _btnFillMeanClicked(self):
        """
        Callback for button btnFillMean Click Event
        """
        self.parent.btnFillMeanClicked(self.varsVar.get(),self.varFillMean.get())

    def _btnFillMedianClicked(self):
        """
        Callback for button btnFillMedian click event
        """
        self.parent.btnFillMedianClicked(self.varsVar.get(),self.varFillMedian.get())

    def _btnFillMeanGroupClicked(self):
        """
        Callback for butoon btnFillMeanGrouped click event
        """
        self.parent.btnFillMeanGroupClicked(self.varsVar.get(),self.varFillMeanGroup.get(),map(int, self.lstFillMeanIndex.curselection()),map(int, self.lstFillMeanCol.curselection()))

    def _btnFillMedianGroupClicked(self):
        """
        Callback for button btnFillMedianGrouped click event
        """
        self.parent.btnFillMedianGroupClicked(self.varsVar.get(),self.varFillMeanGroup.get(),map(int, self.lstFillMeanIndex.curselection()),map(int, self.lstFillMeanCol.curselection()))

    def _btnLogColumnClicked(self):
        """
        Callback for button btnLogTransform click event
        """
        self.parent.btnLogColumnClicked(self.varsVar.get(),self.varLogColumn.get(),self.varLogColumnOut.get())

    def _btnImputeClicked(self):
        #self.parent.btnImputeClicked(self.varsVar.get(),self.varFitModel.get(),self.varImputeStrategy.get())
        pass

    def _btnMImputeClicked(self):
        #self.parent.btnMImputeClicked(self.varsVar.get(),self.varFitModel.get(),self.varMImputeOrder,self.varImputeStrategy.get(),self.varBurnIn.get(),self.varImputations.get(),self.varNFeatures.get())
        pass

    def show(self):
        """
        Call this method to bring this page into view
        """
        super(DataMungingPage,self).show()
        self.refresh()

    def refresh(self):
        """
        Refesh some controls
        Don't invoke this method manually
        """
        self.varsVar.set('')
        #self.varFitModel.set('')
        #self.varMFitModel.set('')
        self.cBoxVars['menu'].delete(0, 'end')
        #self.cBoxFitModel['menu'].delete(0, 'end')
        #self.cBoxMFitModel['menu'].delete(0, 'end')
        new_choices = self.parent.getCustomvarsString()
        for choice in new_choices:
            self.cBoxVars['menu'].add_command(label=choice, command=tk._setit(self.varsVar, choice))
            #self.cBoxFitModel['menu'].add_command(label=choice, command=tk._setit(self.varFitModel, choice))
            #self.cBoxMFitModel['menu'].add_command(label=choice, command=tk._setit(self.varMFitModel, choice))


    def _varsVarSelectionChanged(self,*args):
        """
        Callback for varsVarSelection selection change event
        """
        columns=self.parent.getColumns(self.parent.getVarValue(self.varsVar.get()))

        self.varAddColumn1.set('')
        self.cBoxAddColumn1['menu'].delete(0, 'end')
        self.varAddColumn2.set('')
        self.cBoxAddColumn2['menu'].delete(0, 'end')
        self.varFillMean.set('')
        self.cBoxFillMean['menu'].delete(0, 'end')
        self.varFillMeanGroup.set('')
        self.cBoxFillMeanGroup['menu'].delete(0, 'end')
        self.varFillMedian.set('')
        self.cBoxFillMedian['menu'].delete(0, 'end')
        self.varLogColumn.set('')
        self.cBoxLogColumn['menu'].delete(0, 'end')

        self.lstFillMeanCol.delete(0,tk.END)
        self.lstFillMeanIndex.delete(0,tk.END)
        if columns==None:
            return
        for column in columns:
            self.lstFillMeanCol.insert(tk.END, column)
            self.lstFillMeanIndex.insert(tk.END, column)
            self.cBoxAddColumn1['menu'].add_command(label=column, command=tk._setit(self.varAddColumn1, column))
            self.cBoxAddColumn2['menu'].add_command(label=column, command=tk._setit(self.varAddColumn2, column))
            self.cBoxFillMean['menu'].add_command(label=column, command=tk._setit(self.varFillMean, column))
            self.cBoxFillMeanGroup['menu'].add_command(label=column, command=tk._setit(self.varFillMeanGroup, column))
            self.cBoxFillMedian['menu'].add_command(label=column, command=tk._setit(self.varFillMedian, column))
            self.cBoxLogColumn['menu'].add_command(label=column, command=tk._setit(self.varLogColumn, column))

