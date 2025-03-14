This is a personal python library including assorted general utilities i've standardised for my own reuse.

It currently includes the following modules:

fileHandling - Assorted functions to streamline reading and writing data with CSV, txt, and fig.png
	createFolder(directory, folderName)
	getData(filePath, fileName)
	saveCSV(filepath, filename, dataFrame)
	saveTxT(filepath, filename, text)
	saveFigure(directory, fileName, fig)

inputOutput - Assorted functions streamlining IO functions
	IObool(text, default=True, ynDict = {"y":True, "n":False})
	IOint(text, default=1)
	IOfloat(text, default=0)
	IOsaveTxT(text, fileName)
	IOsaveCSV(data, fileName)
	IOsaveFig(fig, fileName)

progress - Progress class; implements a basic timer object
	class progress
		__init__(self, startIt, totalIt)
		cls(self)
		increment(self, increment=1)
		display(self, title="", percentDisplay=True, rounding=2)
		timeElapsed(self)

misc - Miscelaneous utilities
	strLinesConcatenate(strList, current="")


Given it's current file location, it should be imported as:

import os
curDir = os.getcwd()
os.chdir("/Users/nayandusoruth/Desktop/Y2Physics/GeneralUtilities")
import misc
os.chdir(curDir)