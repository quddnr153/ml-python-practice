from numpy import *
from os import listdir
import operator

def classify0(inX, dataSet, labels, k):
    ''' 거리 계산 '''
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis = 1)
    distances = sqDistances ** 0.5
    sortedDistIndices = distances.argsort()

    ''' 가장 가까운 k 개의 class 계산 '''
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndices[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1

    ''' class 정렬 '''
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

def fileToMatrix(fileName):
    fileReader = open(fileName)
    numberOfLines = len(fileReader.readlines())

    ''' numpy 행렬 '''
    returnMatrix = zeros((numberOfLines, 3))
    classLabelVector = []
    fileReader = open(fileName)
    index = 0

    for line in fileReader.readlines():
        line = line.strip()
        listFromLine = line.split('\t')
        ''' float data 를 matrix 로 저장 '''
        returnMatrix[index, :] = listFromLine[0:3]
        classLabelVector.append(listFromLine[-1])
        index += 1

    return returnMatrix, classLabelVector

def normalize(dataSet):
    minValue = dataSet.min(0)
    maxValue = dataSet.max(0)
    ranges = maxValue - minValue
    normalizationDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normalizationDataSet = dataSet - tile(minValue, (m, 1))
    normalizationDataSet = normalizationDataSet / tile(ranges, (m, 1))
    return normalizationDataSet, ranges, minValue

def datingClassTest():
    hoRatio = 0.10      #hold out 10%
    datingDataMat,datingLabels = fileToMatrix('datingTestSet2.txt')       #load data setfrom file
    normMat, ranges, minVals = normalize(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m*hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],3)
        print("the classifier came back with: %d, the real answer is: %d" % (int(classifierResult), int(datingLabels[i])))
        if (classifierResult != datingLabels[i]): errorCount += 1.0
    print("the total error rate is: %f" % (errorCount/float(numTestVecs)))

def classifyPerson():
    resultList = ['not at all', 'in small doses', 'in large doses']
    percentTats = float(input("Percentage of time spent playing video games?"))
    ffMiles = float(input("Frequent flier miles earned per year?"))
    iceCream = float(input("Liters of ice cream consumed per year?"))
    datingDataMat, datingLabels = fileToMatrix('datingTestSet2.txt')
    normMat, ranges, minVals = normalize(datingDataMat)
    inArr = array([ffMiles, percentTats, iceCream])
    classifierResult = classify0((inArr - minVals) / ranges, normMat, datingLabels, 3)
    print("You will probably like this person: ", resultList[int(classifierResult) - 1])

def imageToVector(filename):
    returnVect = zeros((1,1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0, 32 * i + j] = int(lineStr[j])
    return returnVect

def handwritingClassTest():
    hwLabels = []
    trainingFileList = listdir('trainingDigits')           #load the training set
    m = len(trainingFileList)
    trainingMat = zeros((m,1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]     #take off .txt
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        trainingMat[i,:] = imageToVector('trainingDigits/%s' % fileNameStr)
    testFileList = listdir('testDigits')        #iterate through the test set
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]     #take off .txt
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = imageToVector('testDigits/%s' % fileNameStr)
        classifierResult = classify0(vectorUnderTest, trainingMat, hwLabels, 3)
        print("the classifier came back with: %d, the real answer is: %d" % (classifierResult, classNumStr))
        if (classifierResult != classNumStr): errorCount += 1.0
    print("\nthe total number of errors is: %d" % errorCount)
    print("\nthe total error rate is: %f" % (errorCount/float(mTest)))

if __name__ == '__main__':
    classifyPerson()
    handwritingClassTest()
