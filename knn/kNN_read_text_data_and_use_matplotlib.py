from numpy import *
from numpy import array
import operator
import matplotlib
import matplotlib.pyplot as plt

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

if __name__ == '__main__':
    datingDataMatrix, datingLabels = fileToMatrix('datingTestSet2.txt')
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(datingDataMatrix[:, 1], datingDataMatrix[:, 2], 15.0 * array(datingLabels, int), 15.0 * array(datingLabels, int))
    plt.show()
