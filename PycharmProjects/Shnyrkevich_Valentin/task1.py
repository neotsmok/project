import os
import sys
import numpy as np


fileOrPath = sys.argv[1]

if os.path.isfile(fileOrPath):
    with open(fileOrPath, 'r', encoding='utf-8') as inputFile:
        inputVar = np.asarray(inputFile.read().splitlines(), dtype='int')

percentile90 = np.percentile(inputVar, 90)
mediana = np.percentile(inputVar, 50)
max = max(inputVar)
min = min(inputVar)
middle = sum(inputVar)/len(inputVar)

print('{0:.2f}'.format(percentile90) + "\n" + 
    '{0:.2f}'.format(mediana) + "\n" + 
    '{0:.2f}'.format(max) + "\n" + 
    '{0:.2f}'.format(min) + "\n" + 
    '{0:.2f}'.format(middle) + "\n"
    )
