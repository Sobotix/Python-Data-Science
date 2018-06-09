import pandas
import numpy
import matplotlib
import matplotlib.pyplot
import sklearn.preprocessing

from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import KFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn import metrics
from sklearn.preprocessing import LabelEncoder
#from sklearn.impute import SimpleImputer
#from sklearn.impute import MICEImputer
from Imputation import SimpleImputer
from Imputation import MICEImputer

COLORS_LIST=['black','green','red','yellow','orange','blue','grey','darkgreen','magenta','cyan','antiquewhite','aqua','aquamarine','beige','bisque','blanchedalmond','blueviolet','brown','burlywood','cadetblue','chartreuse','chocolate','coral','cornflowerblue','cornsilk','crimson','darkblue','darkcyan','darkgoldenrod','darkgray','darkgreen','darkkhaki','darkmagenta','darkolivegreen']

def getDataFrame(path:str):
    """
    Reads and returns a csv file as a Dataframe
    """
    return pandas.read_csv(path, encoding = "ISO-8859-1")

def saveDataFrame(dataFrame:pandas.DataFrame,path:str):
    """
    Save given DataFrame to a csv file
    """
    dataFrame.to_csv(path,encoding = "ISO-8859-1")

def getTop(dataFrame:pandas.DataFrame,count:int):
    """
    Returns a sub DataFrame of top-n rocords
    """
    if dataFrame is None:
        return None
    return dataFrame.head(count)

def describe(dataFrame:pandas.DataFrame):
    """
    Describes numerical attributes of given DataFrame
    """
    if dataFrame is None:
        return None
    return dataFrame.describe()

def frequencyDistribution(dataFrame:pandas.DataFrame,column:str):
    """
    Returns frequency destribution of given column in the DataFrame
    """
    if dataFrame is None:
        return None
    dataFrame[column].value_counts()
    matplotlib.pyplot.show()
    return dataFrame[column].value_counts()

def histrogram(dataFrame:pandas.DataFrame,column:str,binsCount:int):
    """
    Display Histogram of given column with given bin value
    """
    if dataFrame is None:
        return None
    dataFrame[column].hist(bins=binsCount)
    matplotlib.pyplot.show()

def boxplot(dataFrame:pandas.DataFrame,columnName:str,byColumnName:str=None):
    """
    Displays Boxplot of given column(s)
    """
    if dataFrame is None:
        return None
    dataFrame.boxplot(column=columnName,by=byColumnName)
    matplotlib.pyplot.show()

def getPivotMean(dataFrame:pandas.DataFrame,valueColumns,indexColumns):
    """
    Return pivot mean dataframe of source dataframe
    """
    if dataFrame is None:
        return None
    return dataFrame.pivot_table(values=valueColumns,index=indexColumns,aggfunc=numpy.mean)

def getPivotMedian(dataFrame:pandas.DataFrame,valueColumns,indexColumns):
    """
    Return pivot meadian dataframe of source dataframe
    """
    if dataFrame is None:
        return None
    return dataFrame.pivot_table(values=valueColumns,index=indexColumns,aggfunc=numpy.median)

def barChart(dataFrame:pandas.DataFrame):
    """
    Display BarChart of given dataframe
    """
    if dataFrame is None:
        return None
    dataFrame.plot(kind='bar')
    matplotlib.pyplot.show()
    pass

def pieChart(dataFrame:pandas.DataFrame,column:str):
    """
    Display PieChart of given dataframe
    """
    if dataFrame is None:
        return None
    dataFrame[column].plot(kind='pie',subplots=True)
    matplotlib.pyplot.show()

def stackedBarChart(dataFrame:pandas.DataFrame,valueColumn,indexColumns):
    """
    Display Stacked-BarChart of given dataframe with given values and indexes
    """
    if dataFrame is None:
        return None
    indexList=[]
    for value in indexColumns:
        indexList.append(dataFrame[value])
    if len(indexList) <=0:
        return None
    pandas.crosstab(indexList,dataFrame[valueColumn]).plot(kind='bar',stacked=True,color=COLORS_LIST,grid=False)
    matplotlib.pyplot.show()

def addColumns(dataFrame:pandas.DataFrame,inColumn1,inColumn2,outColumn):
    """
    Add values of given columns
    """
    if dataFrame is None:
        return None
    dataFrame[outColumn]=dataFrame[inColumn1]+dataFrame[inColumn2]

def getMissingValuesCount(dataFrame:pandas.DataFrame):
    """
    Get missing values count column wise
    """
    if dataFrame is None:
        return None
    return dataFrame.apply(lambda x: sum(x.isnull()),axis=0)

def fillMissingWithMean(testData:pandas.DataFrame,trainData:pandas.DataFrame,columnName:str):
    """
    Fill missing values of given column with mean
    """
    if testData is None or trainData is None:
        return None
    testData[columnName].fillna(trainData[columnName].mean(), inplace=True)

def fillMissingWithMedian(testData:pandas.DataFrame,trainData:pandas.DataFrame,columnName:str):
    """
    Fill Missing values of given column with median
    """
    if testData is None or trainData is None:
        return None
    testData[columnName].fillna(trainData[columnName].median(), inplace=True)

def fillMissingWithMedianGrouped(trainData:pandas.DataFrame,valuesColumn,indexColumn,columnsName):
    """
    Fill missing values of given values column with median of index/columns groups
    """
    if trainData is None:
        return None
    dataFrame= trainData.pivot_table(values=valuesColumn, index=indexColumn ,columns=columnsName, aggfunc=numpy.median)
    def _getDataFrameValue(x):
        try:
            return dataFrame.loc[x[indexColumn],x[columnsName]]
        except:
            return 0
    return trainData[valuesColumn].fillna(trainData[trainData[valuesColumn].isnull()].apply(_getDataFrameValue, axis=1), inplace=True)

def fillMissingWithMeanGrouped(trainData:pandas.DataFrame,valuesColumn,indexColumn,columnsName):
    """
    Fill missing values of given values column with mean of index/columns groups
    """
    if trainData is None:
        return None
    dataFrame= trainData.pivot_table(values=valuesColumn, index=indexColumn ,columns=columnsName, aggfunc=numpy.mean)
    def _getDataFrameValue(x):
        try:
            return dataFrame.loc[x[indexColumn],x[columnsName]]
        except:
            return 0
    return trainData[valuesColumn].fillna(trainData[trainData[valuesColumn].isnull()].apply(_getDataFrameValue, axis=1), inplace=True)

def logTransform(dataFrame:pandas.DataFrame,inColumn,outColumn):
    """
    Take log of given column and save it into outColumn
    """
    dataFrame[outColumn]=numpy.log(dataFrame[inColumn])

class ClassificationResult:
    """
    Container class for storing classification result
    """
    def __init__(self,accuracy,crossValidation):
        self.accuracy=accuracy
        self.crossValidation=crossValidation

def classificationModel(model,dataFrame,predictors,outcome,nFolds:int):
    """
    Method for computing accuray and cross-validation based upon given model
    """
    if dataFrame is None:
        return None
    model.fit(dataFrame[predictors],dataFrame[outcome])
    predictions=model.predict(dataFrame[predictors])

    accuracy=metrics.accuracy_score(predictions,dataFrame[outcome])

    kf=KFold(dataFrame.shape[0],n_folds=nFolds)
    error=[]
    for train,test in kf:
        trainPredictors=(dataFrame[predictors].iloc[train,:])

        train_target=dataFrame[outcome].iloc[train]
        model.fit(trainPredictors,train_target)

        error.append(model.score(dataFrame[predictors].iloc[test,:], dataFrame[outcome].iloc[test]))

    crossValidation=numpy.mean(error)
    model.fit(dataFrame[predictors],dataFrame[outcome])

    return ClassificationResult(accuracy,crossValidation) 


def logisticRegression(dataFrame:pandas.DataFrame,predictors,outColumn,nFolds:int):
    """
    Method for computing accuray and cross-validation using logistic-regression
    """
    if dataFrame is None:
        return None
    dataFrame=_encodeLabels(dataFrame)
    model = LogisticRegression()
    return classificationModel(model, dataFrame,predictors,outColumn,nFolds)

def decisionTree(dataFrame:pandas.DataFrame,predictors,outColumn,nFolds:int):
    """
    Method for computing accuray and cross-validation using decision-tree
    """
    if dataFrame is None:
        return None
    dataFrame=_encodeLabels(dataFrame)
    model = DecisionTreeClassifier()
    return classificationModel(model, dataFrame,predictors,outColumn,nFolds)

class RandomForestResult:
    """
    Container for storing RandomForest results
    """
    def __init__(self,classificationResult,featuresImportance):
        self.classificationResult=classificationResult
        self.featuresImportance=featuresImportance

def randomForest(dataFrame:pandas.DataFrame,predictors,outColumn,nFolds:int,nEstimators:int=25,minSamplesSplit:int=25,maxDepth:int=7,maxFeatures:int=1):
    """
    Method for computing accuray and cross-validation using random-forest
    """
    if dataFrame is None:
        return None
    dataFrame=_encodeLabels(dataFrame)
    model = RandomForestClassifier(n_estimators=nEstimators, min_samples_split=minSamplesSplit, max_depth=maxDepth, max_features=maxFeatures)
    result=RandomForestResult(classificationModel(model, dataFrame,predictors,outColumn,nFolds),None)
    featuresImportance=pandas.Series(model.feature_importances_, index=predictors).sort_values(ascending=False)
    result.featuresImportance=featuresImportance
    return result

def getColumns(dataFrame:pandas.DataFrame):
    """
    Returns columns of given dataframe
    """
    if dataFrame is None:
        return None
    return list(dataFrame.columns.values)

def _encodeLabels(dataFrame):
    """
    Attribues encoding for using in classification models
    Don't invoke this method unless you know what are you doing
    """
    columns=getColumns(dataFrame)
    if columns is None or columns == None:
        return
    labelEncoder=LabelEncoder()
    newFrame=dataFrame
    for column in columns:
        newFrame[column]=labelEncoder.fit_transform(dataFrame[column])

    newFrame.dtypes
    return newFrame

def Imputation(dataFrame,fitFrame,imputeStrategy='mean'):
    #fill_NaN = SimpleImputer(missing_values=numpy.nan, strategy=imputeStrategy, axis=1)
    #imputed_DF = pandas.DataFrame(fill_NaN.fit_transform(dataFrame))
    #imputed_DF.columns = dataFrame.columns
    #imputed_DF.index = dataFrame.index
    #return imputed_DF
    dataFrame=_encodeLabels(dataFrame)
    fitFrame=_encodeLabels(fitFrame)
    imputer=SimpleImputer(missing_values='Nan',strategy=imputeStrategy)
    imputer.fit(fitFrame)
    dataFrame=imputer.transform(fitFrame)

def MultiImputation(dataFrame,fitFrame,imputationOrder='ascending',initialStrategy='mean',maxValue=None,minValue=None,nBurnIn=10,nImputations=10,nNearestFeatures=None,predctor=None,randomState=0):
    imputer=MICEImputer(imputation_order=imputationOrder, initial_strategy=initialStrategy,max_value=maxValue, min_value=minValue, missing_values='NaN', n_burn_in=nBurnIn,n_imputations=nImputations, n_nearest_features=nNearestFeatures, predictor=None,random_state=randomState, verbose=False)
    imputer.fit(fitFrame)
    dataFrame=numpy.round(imputer.transform(dataFrame))