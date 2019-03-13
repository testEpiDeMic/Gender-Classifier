from sklearn import tree
from sklearn.metrics import accuracy_score
import xlrd

#storing the location of the Excel Workbook containing the Training Samples
ipWBLoc = ("TrainingSamples.xlsx")

#opening the said input Excel Workbook
ipWB = xlrd.open_workbook(ipWBLoc)

#opening the sheet containing the Feature Vectors into 'sheetFV'
sheetNameFV = "FeatureVectors"
sheetFV = ipWB.sheet_by_name(sheetNameFV)
#opening the sheet containing the Labels into 'sheetLabels'
sheetNameLabels = "Labels"
sheetLabels = ipWB.sheet_by_name(sheetNameLabels)

#storing the no. of Training Samples into noTSFV
#noTSFV = sheetFV.nrows
noTS = sheetFV.nrows

#storing the dimensionality of the Training Samples into dimTS
dimTS = sheetFV.ncols

#storing the no. of Training Sample Labels into noLabels
#optional test to check if noTS matches with noLabels

#creating a list of Training Sample Feature Vectors
listTSFV = []
for TSCounter in range(noTS):
	TSFV = []
	for dimCounter in range(dimTS):
		TSFV.append(sheetFV.cell_value(TSCounter,dimCounter))
	listTSFV.append(TSFV)

#creating a list of Training Sample Labels (assumming they are in the first column of the worksheet)
listTSLabels = []
for TSCounter in range(noTS):
	listTSLabels.append(sheetLabels.cell_value(TSCounter,0))

#creating a classifier 'clf' with the Descision Tree model
clf = tree.DecisionTreeClassifier()

#training the classifier with the Decision Tree model
clf.fit(listTSFV,listTSLabels)

#testing the classifier on 'testInput' (LIST of test Sample FVs: so a list of lists) and printing the output
testInput = [[190,70,43]]
predLabels = clf.predict(testInput)

#using the method 'sklearn.metrics.accuracy_score' to evaluate the classifier performance
trueLabelsTestInput = ['male']
print(accuracy_score(labelsTestInput, clf.predict(testInput), normalize = False))

