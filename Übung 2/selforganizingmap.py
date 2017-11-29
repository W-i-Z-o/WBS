import numpy as np

class MySOM:
    def __init__(self, datadict, label, nRows, nColumns):
        #init here
        self.datadict = datadict
        self.label = label
        self.nRows = nRows
        self.nColumns = nColumns

    def __str__(self):
        #toString()
        return "label: {0}, dimension: ({1} {2})".format(self.label, self.nRows, self.nColumns)

    def initializeNeurons(self):
        self.neurons = np.random.uniform(size=(self.nColumns, self.nRows, 244))
        
    def toPixelsArray(self, field):
        pixels = []
        for i in range(len(self.datadict[field][0])):
            features = [row[i] for row in datadict[field]]
            pixels.append(features)
        return pixels