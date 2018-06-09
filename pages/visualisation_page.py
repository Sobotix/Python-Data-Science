import pages
import tkinter as tk
import visualizer

class VisualisationPage(pages.Page):
    """
    Page offereing different visualisation options, like histogram, barchart and so on
    """
    def __init__(self, master,parent):
       """
       Constructor for intialization of this page
       """
       pages.page.Page.__init__(self,master)
       self.parent=parent

       #Custom Variable Selection Row
       self.varsVar=tk.StringVar(self)
       self.varsVar.trace("w",self._varsVarSelectionChanged)
       self.cBoxVars=tk.OptionMenu(self, self.varsVar, *parent.getCustomvarsString())
       self.cBoxVars.pack(side="top", expand="true")

       #Buttons Images
       self.imgDisplay=tk.PhotoImage(file="images/btnDisplay.gif")
       self.imgDescribe=tk.PhotoImage(file="images/btnDescribe.gif")
       self.imgBarChart=tk.PhotoImage(file="images/btnBarChart.gif")
       self.imgPierChart=tk.PhotoImage(file="images/btnPieChart.gif")
       self.imgMissingCount=tk.PhotoImage(file="images/btnMissingValuesCount.gif")
       self.imgFreqDist=tk.PhotoImage(file="images/btnFrequencyDistribution.gif")
       self.imgHistrogram=tk.PhotoImage(file="images/btnHistrogram.gif")
       self.imgBoxPlot=tk.PhotoImage(file="images/btnBoxPlot.gif")
       self.imgStackedBarChart=tk.PhotoImage(file="images/btnStackedBarChart.gif")

       #Second Linear Row Container
       self.customFrame0=tk.Frame(self)
       self.customFrame0.pack(side="top",expand="true")

       #Second Row
       self.btnDisplay=tk.Button(self.customFrame0,text="Display",command=self._btnDisplayClicked, image=self.imgDisplay)
       self.btnDisplay.pack(side="left")
       self.btnDescribe=tk.Button(self.customFrame0,text="Describe",command=self._btnDescribeClicked,image=self.imgDescribe)
       self.btnDescribe.pack(side="left")
       self.btnBarChart=tk.Button(self.customFrame0,text="Bar Chart",command=self._btnBarChartClicked,image=self.imgBarChart)
       self.btnBarChart.pack(side="left")
       self.btnMissingCount=tk.Button(self.customFrame0,text="Missing Values Count",command=self._btnMissingCountClicked,image=self.imgMissingCount)
       self.btnMissingCount.pack(side="left")

       #Container Frames
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


       #Row: Frequency Distribution and Pie Chart
       self.varFreqDistr=tk.StringVar(self.customFrame1)
       self.cBoxFreqDistr=tk.OptionMenu(self.customFrame1, self.varFreqDistr, *parent.getColumns(parent.getVarValue(self.varsVar.get())))
       self.cBoxFreqDistr.pack(side="left", expand="true")
       self.btnFreqDistr=tk.Button(self.customFrame1,text="Frequency Distribution",command=self._btnFreqDistrClicked, image=self.imgFreqDist)
       self.btnFreqDistr.pack(side="left")
       self.btnPieChart=tk.Button(self.customFrame1,text="Pie Chart",command=self._btnPieChartClicked,image=self.imgPierChart)
       self.btnPieChart.pack(side="left")

       #Row: Histrogram
       self.varHistrogram=tk.StringVar(self.customFrame2)
       self.cBoxHistrogram=tk.OptionMenu(self.customFrame2, self.varHistrogram, *parent.getColumns(parent.getVarValue(self.varsVar.get())))
       self.cBoxHistrogram.pack(side="left", expand="true")
       self.varHistrogramBin=tk.StringVar(self.customFrame2)
       self.varHistrogramBin.set(40)
       self.txtHistrogramBin=tk.Spinbox(self.customFrame2, from_ = 1, to = 1000,textvariable=self.varHistrogramBin)
       self.txtHistrogramBin.pack(side="left")
       self.btnHistrogram=tk.Button(self.customFrame2,text="Histrogram",command=self._btnHistrogramClicked,image=self.imgHistrogram)
       self.btnHistrogram.pack(side="left")

       #Row: Box Plot
       self.varBoxPlotColumn=tk.StringVar(self.customFrame3)
       self.cBoxBoxPlotColumn=tk.OptionMenu(self.customFrame3, self.varBoxPlotColumn, *parent.getColumns(parent.getVarValue(self.varsVar.get())))
       self.cBoxBoxPlotColumn.pack(side="left", expand="true")
       self.varBoxPlotByColumn=tk.StringVar(self.customFrame3)
       self.cBoxBoxPlotByColumn=tk.OptionMenu(self.customFrame3, self.varBoxPlotByColumn, *parent.getColumns(parent.getVarValue(self.varsVar.get())))
       self.cBoxBoxPlotByColumn.pack(side="left", expand="true")
       self.btnBoxPlot=tk.Button(self.customFrame3,text="Box Plot",command=self._btnBoxPlotClicked,image=self.imgBoxPlot)
       self.btnBoxPlot.pack(side="left")

       #Row: Stacked Bar Chart
       self.varSBarChartColumn=tk.StringVar(self.customFrame4)
       self.cBoxSBarChartColumn=tk.OptionMenu(self.customFrame4, self.varSBarChartColumn, *parent.getColumns(parent.getVarValue(self.varsVar.get())))
       self.cBoxSBarChartColumn.pack(side="left", expand="true")
       self.lstSBarChartIndex=tk.Listbox(self.customFrame4, selectmode=tk.MULTIPLE,exportselection=0)
       columns=parent.getColumns(parent.getVarValue(self.varsVar.get()))
       for column in columns:
           self.lstSBarChartIndex.insert(tk.END, column)
       self.lstSBarChartIndex.pack(side="left")
       self.btnSBarChart=tk.Button(self.customFrame4,text="Stacked BarChart",command=self._btnSBarChartClicked,image=self.imgStackedBarChart)
       self.btnSBarChart.pack(side="left")

       #Row: Output Console
       self.txtOutput=tk.Text(self.customFrame5)
       self.txtOutput.config(font=("consolas",8),bg='green',wrap="none")
       self.txtOutput.pack(side="top")
       self.sbTxtOutputY=tk.Scrollbar(self.customFrame5,command=self.txtOutput.yview)
       self.txtOutput['yscrollcommand']=self.sbTxtOutputY.set
       self.sbTxtOutputY.pack(side="left", expand=True,fill="y")
       self.sbTxtOutputX=tk.Scrollbar(self.customFrame5,command=self.txtOutput.xview)
       self.txtOutput['xscrollcommand']=self.sbTxtOutputX.set
       self.sbTxtOutputX.pack(side="top", expand=True,fill="x")


    def _btnDisplayClicked(self):
        """
        Callback For button btnDisplay Click event
        """
        self.txtOutput.delete(0.0,tk.END)
        result=self.parent.btnDisplayClicked(self.varsVar.get())
        self.txtOutput.insert(tk.END,str(result))
        if result is not None:
            visualizer.show(result)

    def _btnMissingCountClicked(self):
        """
        Callback for button btnMissingCount Click Event
        """
        self.txtOutput.delete(0.0,tk.END)
        result=self.parent.btnMissingCountClicked(self.varsVar.get())
        self.txtOutput.insert(tk.END,str(result))
    
    def _btnDescribeClicked(self):
        """
        Callback for button btnDescribe Click Event
        """
        self.txtOutput.delete(0.0,tk.END)
        result=self.parent.btnDescribeClicked(self.varsVar.get())
        self.txtOutput.insert(tk.END,result)
        if result is not None:
            visualizer.show(result)

    def _btnBarChartClicked(self):
        """
        Callback for button btnBarChart click event
        """
        self.parent.btnBarChartClicked(self.varsVar.get())

    def _btnPieChartClicked(self):
        """
        Callback for button btnBarChart click event
        """
        self.parent.btnPieChartClicked(self.varsVar.get(),self.varFreqDistr.get())

    def _btnFreqDistrClicked(self):
        """
        Callback for button btnFreqDistr CLick event
        """
        self.txtOutput.delete(0.0,tk.END)
        result=self.parent.btnFreqDistrClicked(self.varsVar.get(),self.varFreqDistr.get())
        self.txtOutput.insert(tk.END,result)

    def _btnHistrogramClicked(self):
        """
        Callback for button btnHistrogram click event
        """
        self.parent.btnHistrogramClicked(self.varsVar.get(),self.varHistrogram.get(),int(self.varHistrogramBin.get()))

    def _btnBoxPlotClicked(self):
        """
        Calllback for button btnBoxPlot click event
        """
        self.parent.btnBoxPlotClicked(self.varsVar.get(),self.varBoxPlotColumn.get(),self.varBoxPlotByColumn.get())

    def _btnSBarChartClicked(self):
        """
        Callback for button btnSBarchart click event
        """
        self.parent.btnSBarChartClicked(self.varsVar.get(),self.varSBarChartColumn.get(),map(int, self.lstSBarChartIndex.curselection()))

    def show(self):
        """
        Call this method to bring this page into view
        """
        super(VisualisationPage,self).show()
        self.refresh()

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


    def _varsVarSelectionChanged(self,*args):
        """
        Callback for varsVarSelection selection change event
        """
        columns=self.parent.getColumns(self.parent.getVarValue(self.varsVar.get()))

        self.varBoxPlotByColumn.set('')
        self.cBoxBoxPlotByColumn['menu'].delete(0, 'end')
        self.varBoxPlotColumn.set('')
        self.cBoxBoxPlotColumn['menu'].delete(0, 'end')
        self.varFreqDistr.set('')
        self.cBoxFreqDistr['menu'].delete(0, 'end')
        self.varHistrogram.set('')
        self.cBoxHistrogram['menu'].delete(0, 'end')
        self.varSBarChartColumn.set('')
        self.cBoxSBarChartColumn['menu'].delete(0, 'end')

        self.lstSBarChartIndex.delete(0,tk.END)
        if columns==None:
            return
        for column in columns:
            self.lstSBarChartIndex.insert(tk.END, column)
            self.cBoxBoxPlotByColumn['menu'].add_command(label=column, command=tk._setit(self.varBoxPlotByColumn, column))
            self.cBoxBoxPlotColumn['menu'].add_command(label=column, command=tk._setit(self.varBoxPlotColumn, column))
            self.cBoxFreqDistr['menu'].add_command(label=column, command=tk._setit(self.varFreqDistr, column))
            self.cBoxHistrogram['menu'].add_command(label=column, command=tk._setit(self.varHistrogram, column))
            self.cBoxSBarChartColumn['menu'].add_command(label=column, command=tk._setit(self.varSBarChartColumn, column))

