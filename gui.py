import tkinter as tk
import pages
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfile
from tkinter.messagebox import showerror
import core
import visualizer

class CustomVar:
    """
    Container for storing name/value pairs
    Used for storing user-defined variables
    """
    def __init__(self,name,value):
        self.name=name
        self.value=value

#GUI Component
class Window(tk.Frame):
    """
    GUI Window that is shown to the user
    """
    #Constructor
    def __init__(self,master):
        """
        Constructor for initialization
        """
        #Initialization
        tk.Frame.__init__(self,master)
        self.master=master
        self.master.title("#Python Data Science")
        self.pack(side="top", fill="both", expand=True)
        master.geometry("550x550")
        master.resizable(1,1)
        master.config(background="blue")
        self.config(background="black")

        self.navFrame = tk.Frame(self)
        self.containerFrame = tk.Frame(self)
        self.navFrame.pack(side="left", fill="y", expand=False)
        self.containerFrame.pack(side="left", fill="both", expand=True)
        self.navFrame.config(background="orange")
        self.containerFrame.config(background="red")
        

        self.imgHome=tk.PhotoImage(file="images/btnHome.gif")
        self.imgAssign=tk.PhotoImage(file="images/btnAssign.gif")
        self.imgPrediction=tk.PhotoImage(file="images/btnPrediction.gif")
        self.imgDataMunging=tk.PhotoImage(file="images/btnDataMunging.gif")
        self.imgVisualization=tk.PhotoImage(file="images/btnVisualization.gif")
        self.btnHome=tk.Button(self.navFrame, text="Home", command=self.btnHomeClicked, image=self.imgHome)
        self.btnHome.pack(side="top")
        self.btnAssign=tk.Button(self.navFrame, text="Assign", command=self.btnAssignClicked,image=self.imgAssign)
        self.btnAssign.pack(side="top")
        self.btnVisualisation=tk.Button(self.navFrame, text="Visualisation", command=self.btnVisualisationClicked,image=self.imgVisualization)
        self.btnVisualisation.pack(side="top")
        self.btnDataMunging=tk.Button(self.navFrame, text="Data Munging", command=self.btnDataMungingClicked,image=self.imgDataMunging)
        self.btnDataMunging.pack(side="top")
        self.btnPrediction=tk.Button(self.navFrame, text="Prediction", command=self.btnPredictionClicked,image=self.imgPrediction)
        self.btnPrediction.pack(side="top")

        self.dataFrame=core.getDataFrame("train_dataset.csv")
        self.customVars=[CustomVar("var1",self.dataFrame)]


        self.homePage=pages.HomePage(self,self)
        self.homePage.place(in_=self.containerFrame,x=0,y=0,relwidth=1,relheight=1)
        self.assignPage=pages.AssignPage(self,self)
        self.assignPage.place(in_=self.containerFrame,x=0,y=0,relwidth=1,relheight=1)
        self.visualisationPage=pages.VisualisationPage(self,self)
        self.visualisationPage.place(in_=self.containerFrame,x=0,y=0,relwidth=1,relheight=1)
        self.predictionPage=pages.PredictionPage(self,self)
        self.predictionPage.place(in_=self.containerFrame,x=0,y=0,relwidth=1,relheight=1)
        self.dataMungingPage=pages.DataMungingPage(self,self)
        self.dataMungingPage.place(in_=self.containerFrame,x=0,y=0,relwidth=1,relheight=1)

        self.homePage.show()

    def btnHomeClicked(self):
        self.homePage.show()
        pass

    def btnAssignClicked(self):
        self.assignPage.show()
        pass

    def btnVisualisationClicked(self):
        self.visualisationPage.show()

    def btnPredictionClicked(self):
        self.predictionPage.show()

    def btnDataMungingClicked(self):
        self.dataMungingPage.show()
    
    def btnLoadClicked(self):
        filePath = askopenfilename(title='Load Dataset',filetypes = [('Dataset', '.csv')])
        if filePath:
            try:
                self.dataFrame=core.getDataFrame(filePath)
            except:
                print("Error: Could not read dataset")

    def btnSaveClicked(self, varStr):
        var=self.getVarValue(varStr)
        if var is None:
            return
        file = asksaveasfile(title='Save Dataset',filetypes = [('Dataset', '.csv')])
        if file:
            try:
                core.saveDataFrame(var,file.name+'.csv')
            except:
                print("Error: Could not save dataset")

    def getCustomvarsString(self):
        varsList=[]
        for value in self.customVars:
            varsList.append(value.name)
        return varsList
    
    def btnAddVarClicked(self, name):
        self.customVars.append(CustomVar(name,self.dataFrame))
    
    def btnDeleteVarClicked(self,name):
        index=0
        while(index<len(self.customVars)):
            if self.customVars[index].name==name:
                del self.customVars[index]
                index=index-1
            index=index+1

    def getColumns(self,dataFrame=None):
        if dataFrame is None:
            return core.getColumns(self.dataFrame)
        return core.getColumns(dataFrame)

    def getVarValue(self,varStr):
        for value in self.customVars:
            if value.name==varStr:
                return value.value
        return None

    def btnAssignTopClicked(self,varStr,count):
        for value in self.customVars:
            if value.name==varStr:
                value.value=core.getTop(self.dataFrame,int(count))
                
    def btnAssignPivotMeanClicked(self,varStr,columns,indexes):
        columnsList=[]
        indexesList=[]
        columnsNames=self.getColumns()
        for value in columns:
            columnsList.append(columnsNames[value])
        for value in indexes:
            indexesList.append(columnsNames[value])
        for value in self.customVars:
            if value.name==varStr:
                value.value=core.getPivotMean(self.dataFrame,columnsList,indexesList)

    def btnAssignPivotMedianClicked(self,varStr,columns,indexes):
        columnsList=[]
        indexesList=[]
        columnsNames=self.getColumns()
        for value in columns:
            columnsList.append(columnsNames[value])
        for value in indexes:
            indexesList.append(columnsNames[value])
        for value in self.customVars:
            if value.name==varStr:
                value.value=core.getPivotMedian(self.dataFrame,columnsList,indexesList)

    def btnDisplayClicked(self,varStr):
        return (self.getVarValue(varStr))

    def btnMissingCountClicked(self,varStr):
        return (core.getMissingValuesCount(self.getVarValue(varStr)))
    
    def btnDescribeClicked(self,varStr):
        return core.describe(self.getVarValue(varStr))

    def btnBarChartClicked(self,varStr):
        core.barChart(self.getVarValue(varStr))

    def btnPieChartClicked(self,varStr,column):
        core.pieChart(self.getVarValue(varStr),column)

    def btnFreqDistrClicked(self,varStr,column):
        return core.frequencyDistribution(self.getVarValue(varStr),column)

    def btnHistrogramClicked(self,varStr,column,bin):
        core.histrogram(self.getVarValue(varStr),column,bin)

    def btnBoxPlotClicked(self,varStr,column,byColumn):
        core.boxplot(self.getVarValue(varStr),column,byColumn)

    def btnSBarChartClicked(self,varStr,column,indexes):
        lstIndex=[]
        columnsList=self.getColumns(self.getVarValue(varStr))
        for index in indexes:
            lstIndex.append(columnsList[index])
        core.stackedBarChart(self.getVarValue(varStr),column,lstIndex)

    def btnAddColumnClicked(self,varStr,column1,column2,columnOut):
        core.addColumns(self.getVarValue(varStr),column1,column2,columnOut)

    def btnFillMeanClicked(self,varStr,column):
        core.fillMissingWithMean(self.getVarValue(varStr),self.getVarValue(varStr),column)

    def btnFillMedianClicked(self,varStr,column):
        core.fillMissingWithMedian(self.getVarValue(varStr),self.getVarValue(varStr),column)

    def btnFillMeanGroupClicked(self,varStr,valueColumn,indexes,columns):
        lstIndex=[]
        columnsList=self.getColumns(self.getVarValue(varStr))
        for index in indexes:
            lstIndex.append(columnsList[index])
        lstColumn=[]
        for column in columns:
            lstColumn.append(columnsList[column])
        core.fillMissingWithMeanGrouped(self.getVarValue(varStr),valueColumn,lstIndex,lstColumn)

    def btnFillMedianGroupClicked(self,varStr,valueColumn,indexes,columns):
        lstIndex=[]
        columnsList=self.getColumns(self.getVarValue(varStr))
        for index in indexes:
            lstIndex.append(columnsList[index])
        lstColumn=[]
        for column in columns:
            lstColumn.append(columnsList[column])
        core.fillMissingWithMedianGrouped(self.getVarValue(varStr),valueColumn,lstIndex,lstColumn)

    def btnLogColumnClicked(self,varStr,columnIn,columnOut):
        core.logTransform(self.getVarValue(varStr),columnIn,columnOut)

    def btnLogisticRegressionClicked(self,varStr,predictors,outColumn,nFolds):
        lstPredictors=[]
        columnsList=self.getColumns(self.getVarValue(varStr))
        for predictor in predictors:
            lstPredictors.append(columnsList[predictor])
        return core.logisticRegression(self.getVarValue(varStr),lstPredictors,outColumn,nFolds)

    def btnDecisionTreeClicked(self,varStr,predictors,outColumn,nFolds):
        lstPredictors=[]
        columnsList=self.getColumns(self.getVarValue(varStr))
        for predictor in predictors:
            lstPredictors.append(columnsList[predictor])
        return core.decisionTree(self.getVarValue(varStr),lstPredictors,outColumn,nFolds)

    def btnRandomForestClicked(self,varStr,predictors,outColumn,nFolds,nEstimators,minSamplesSplit,maxDepth,maxFeatures):
        lstPredictors=[]
        columnsList=self.getColumns(self.getVarValue(varStr))
        for predictor in predictors:
            lstPredictors.append(columnsList[predictor])
        return core.randomForest(self.getVarValue(varStr),lstPredictors,outColumn,nFolds,nEstimators,minSamplesSplit,maxDepth,maxFeatures)

    def btnImputeClicked(self,strVar,strFit,strategy):
        if strategy is None:
            strategy='mean'
        core.Imputation(self.getVarValue(strVar),self.getVarValue(strFit),strategy)

    def btnMImputeClicked(self,strVar,strFit,order,strategy,burnIn,imputations,nFeatures):
        if burnIn is None:
            burnIn=10
        if imputations is None:
            imputations=10
        core.MultiImputation(self.getVarValue(strVar),self.getVarValue(strFit),nBurnIn=burnIn,nNearestFeatures=nFeatures,nImputations=imputations)


def init():
    """
    Intialize Graphical User Interface and start's application loop
    Don't invoke this method more then once
    """
    #Entry point for this program
    root=tk.Tk()
    Window(root)
    root.iconbitmap('images/icon.ico')
    root.mainloop()