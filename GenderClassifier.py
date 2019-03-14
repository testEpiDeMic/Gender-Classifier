from sklearn import tree, svm, neighbors, naive_bayes, metrics
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

#storing the no. of Training Samples (Feature Vectors) into noTSFV
#noTSFV = sheetFV.nrows
noTS = sheetFV.nrows

#storing the dimensionality of the Training Samples into dimTS
dimTS = sheetFV.ncols

#storing the no. of Training Sample Labels into noLabels
#optional test to check if noTSFV matches with noLabels

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

#creating classifiers with the models: 1. Decision Tree 2. SVC 3. KNN 4. Naive Bayes Gaussian and storing them in a list 'listClfs'
listClfs = []
clfDT = tree.DecisionTreeClassifier()
clfSVC = svm.LinearSVC()
clfKN = neighbors.KNeighborsClassifier()
clfGNB = naive_bayes.GaussianNB()
listClfs.extend([clfDT,clfSVC,clfKN,clfGNB])

#training the classifiers
for clf in listClfs:
	clf.fit(listTSFV,listTSLabels)

#testing the classifier on 'testInput' [LIST of test Sample FVs(themselves a list): so a list of lists] and storing the predicted labels in listPredLabels (again a list of lists)
testInput = [[190,70,43],[160,53,38]]
listPredLabels = []
for clf in listClfs:
	listPredLabels.append(clf.predict(testInput))


#using the method 'sklearn.metrics.accuracy_score' to evaluate the classifier performance; normalize = True(default) => % score (remem 'T' capital in 'True') else absolute no of correct classifications
trueLabelsTestInput = ['male','female']
for predLabels in listPredLabels:
	print(metrics.accuracy_score(trueLabelsTestInput, predLabels, normalize = False))

