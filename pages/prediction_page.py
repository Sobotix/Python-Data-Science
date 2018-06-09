import pages
import tkinter as tk
import visualizer

class PredictionPage(pages.Page):
    """
    Page offereing different predictions options
    """
    def __init__(self, master,parent):
       """
       Constructor for intialization of this page
       """
       pages.page.Page.__init__(self,master)
       self.parent=parent

       #Top Row
       self.varsVar=tk.StringVar(self)
       self.varsVar.trace("w",self._varsVarSelectionChanged)
       self.cBoxVars=tk.OptionMenu(self, self.varsVar, *parent.getCustomvarsString())
       self.cBoxVars.pack(side="top", expand="true")


       #Stack panels for each row
       self.customFrame1=tk.Frame(self)
       self.customFrame1.pack(side="top",expand="true")
       self.customFrame4=tk.Frame(self)
       self.customFrame4.pack(side="top",expand="true")
       self.customFrame2=tk.Frame(self)
       self.customFrame2.pack(side="top",expand="true")
       self.customFrame5=tk.Frame(self)
       self.customFrame5.pack(side="top",expand="true")
       self.customFrame6=tk.Frame(self)
       self.customFrame6.pack(side="top",expand="true")
       self.customFrame3=tk.Frame(self)
       self.customFrame3.pack(side="top",expand="true")

       #Buttons Images
       self.imgLogisticRegression=tk.PhotoImage(file="images/btnLogisticRegression.gif")
       self.imgDecisionTree=tk.PhotoImage(file="images/btnDecisionTree.gif")
       self.imgRandomForest=tk.PhotoImage(file="images/btnRandomForest.gif")

       
       #Row: Logistic Regression And Decision Tree
       columns=parent.getColumns(parent.getVarValue(self.varsVar.get()))
       self.lstPredictors=tk.Listbox(self.customFrame1, selectmode=tk.MULTIPLE,exportselection=0)
       for column in columns:
           self.lstPredictors.insert(tk.END, column)
       self.lstPredictors.pack(side="left")
       self.varOutCoulmn=tk.StringVar(self.customFrame1)
       self.cBoxOutCoulmn=tk.OptionMenu(self.customFrame1, self.varOutCoulmn, *parent.getColumns(parent.getVarValue(self.varsVar.get())))
       self.cBoxOutCoulmn.pack(side="left", expand="true")
       self.varNFolds=tk.StringVar(self.customFrame1)
       self.varNFolds.set(4)
       self.txtNFolds=tk.Spinbox(self.customFrame1, from_ = 1, to = 100,textvariable=self.varNFolds)
       self.txtNFolds.pack(side="left")
       self.btnLogisticRegression=tk.Button(self.customFrame1,text="Logistic Regression",command=self._btnLogisticRegressionClicked, image=self.imgLogisticRegression)
       self.btnLogisticRegression.pack(side="left")
       self.btnDecisionTree=tk.Button(self.customFrame1,text="Decision Tree",command=self._btnDecisionTreeClicked, image=self.imgDecisionTree)
       self.btnDecisionTree.pack(side="left")

       
       #Row: Random Forest
       tk.Label(self.customFrame2,text="Estimators: ").pack(side="left")
       self.varNEstimators=tk.StringVar(self.customFrame2)
       self.varNEstimators.set(25)
       self.txtNEstimators=tk.Spinbox(self.customFrame2, from_ = 1, to = 200,textvariable=self.varNEstimators)
       self.txtNEstimators.pack(side="left")
       tk.Label(self.customFrame2,text="Min Samples Split: ").pack(side="left")
       self.varMinSamplesSplit=tk.StringVar(self.customFrame2)
       self.varMinSamplesSplit.set(25)
       self.txtMinSamplesSplit=tk.Spinbox(self.customFrame2, from_ = 1, to = 200,textvariable=self.varMinSamplesSplit)
       self.txtMinSamplesSplit.pack(side="left")
       tk.Label(self.customFrame5,text="Max Depth: ").pack(side="left")
       self.varMaxDepth=tk.StringVar(self.customFrame5)
       self.varMaxDepth.set(7)
       self.txtMaxDepth=tk.Spinbox(self.customFrame5, from_ = 1, to = 200,textvariable=self.varMaxDepth)
       self.txtMaxDepth.pack(side="left")
       tk.Label(self.customFrame5,text="Max Features: ").pack(side="left")
       self.varMaxFeatures=tk.StringVar(self.customFrame5)
       self.varMaxFeatures.set(1)
       self.txtMaxFeatures=tk.Spinbox(self.customFrame5, from_ = 1, to = 50,textvariable=self.varMaxFeatures)
       self.txtMaxFeatures.pack(side="left")
       self.btnRandomForest=tk.Button(self.customFrame6,text="Random Forest",command=self._btnRandomForestClicked, image=self.imgRandomForest)
       self.btnRandomForest.pack(side="left")

       #Row: Output Console
       self.txtOutput=tk.Text(self.customFrame3)
       self.txtOutput.config(font=("consolas",8),bg='green',wrap="none")
       self.txtOutput.pack(side="top")
       self.sbTxtOutputY=tk.Scrollbar(self.customFrame3,command=self.txtOutput.yview)
       self.txtOutput['yscrollcommand']=self.sbTxtOutputY.set
       self.sbTxtOutputY.pack(side="left", expand=True,fill="y")
       self.sbTxtOutputX=tk.Scrollbar(self.customFrame3,command=self.txtOutput.xview)
       self.txtOutput['xscrollcommand']=self.sbTxtOutputX.set
       self.sbTxtOutputX.pack(side="top", expand=True,fill="x")

    def _btnLogisticRegressionClicked(self):
        """
        Callback for Button btnLogisticRegression Click event
        """
        result = self.parent.btnLogisticRegressionClicked(self.varsVar.get(),map(int, self.lstPredictors.curselection()),self.varOutCoulmn.get(),int(self.varNFolds.get()))
        self.txtOutput.delete(0.0,tk.END)
        self.txtOutput.insert(tk.END,"Accuracy : %s\n" % "{0:.3%}".format(result.accuracy))
        self.txtOutput.insert(tk.END,"Cross-Validation : %s\n" % "{0:.3%}".format(result.crossValidation))

    def _btnDecisionTreeClicked(self):
        """
        Callback for Button btnDecisionTree Click event
        """
        result= self.parent.btnLogisticRegressionClicked(self.varsVar.get(),map(int, self.lstPredictors.curselection()),self.varOutCoulmn.get(),int(self.varNFolds.get()))
        self.txtOutput.delete(0.0,tk.END)
        self.txtOutput.insert(tk.END,"Accuracy : %s\n" % "{0:.3%}".format(result.accuracy))
        self.txtOutput.insert(tk.END,"Cross-Validation : %s\n" % "{0:.3%}".format(result.crossValidation))

    def _btnRandomForestClicked(self):
        """
        Callback for Button btnRandomForest Click event
        """
        result=self.parent.btnRandomForestClicked(self.varsVar.get(),map(int, self.lstPredictors.curselection()),self.varOutCoulmn.get(),int(self.varNFolds.get()),int(self.varNEstimators.get()),int(self.varMinSamplesSplit.get()),int(self.varMaxDepth.get()),int(self.varMaxFeatures.get()))
        self.txtOutput.delete(0.0,tk.END)
        self.txtOutput.insert(tk.END,"Accuracy : %s\n" % "{0:.3%}".format(result.classificationResult.accuracy))
        self.txtOutput.insert(tk.END,"Cross-Validation : %s\n" % "{0:.3%}".format(result.classificationResult.crossValidation))
        self.txtOutput.insert(tk.END,"Features Importance:\n")
        self.txtOutput.insert(tk.END,result.featuresImportance)

    def show(self):
        """
        Call this method to bring this page into view
        """
        super(PredictionPage,self).show()
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

        self.varOutCoulmn.set('')
        self.cBoxOutCoulmn['menu'].delete(0, 'end')

        self.lstPredictors.delete(0,tk.END)
        if columns==None:
            return
        for column in columns:
            self.lstPredictors.insert(tk.END, column)
            self.cBoxOutCoulmn['menu'].add_command(label=column, command=tk._setit(self.varOutCoulmn, column))

