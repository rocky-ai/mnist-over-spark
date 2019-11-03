from pyspark.mllib.regression import LabeledPoint
from numpy import array
from pyspark.mllib.util import MLUtils
from pyspark.mllib.tree import RandomForest, RandomForestModel

# Boilerplate Spark stuff:

conf = SparkConf().setMaster().setAppName()
sc = SparkContext(conf = conf)


rawData = sc.textFile()
testData = sc.textFile()

header = rawData.first()
rawData = rawData.filter(lambda x:x != header)

def parsePoint(line):
    values = '''write here your own code'''
    return LabeledPoint('''write here on ypur own thinking''')


import time
start_time = time.time()


model = RandomForest.trainClassifier(parsedData, numClasses=10,
                                     categoricalFeaturesInfo={},
                                     impurity='gini', maxDepth=20, maxBins=32,numTrees=20)





#testdata

header = testData.first()
testData = testData.filter(lambda x:x != header)


TestData = testData.map(parsePoint)
predictions = model.predict(TestData.map(lambda x: x.features))

labelsAndPredictions = TestData.map(lambda lp: lp.label).zip(predictions)
testErr = labelsAndPredictions.filter(
    lambda lp: lp[0] != lp[1]).count() / float(TestData.count())
print('Test Error = ' + str(testErr))






print("\n")
print("\n")
print("\n")
print('Test Error = ' + str(testErr))
print("\n")
print("\n")
print("\n")
print("--- %s seconds ---" % (time.time() - start_time))
print("\n")
print("\n")
print("\n")



