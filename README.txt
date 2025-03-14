This is a personal python library including assorted general utilities i've standardised for my own reuse.

It currently includes the following modules:
fileHandling - Assorted functions to streamline reading and writing data with CSV, txt, and fig.png
inputOutput  - Assorted functions streamlining IO functions
progress     - Progress class; implements a basic timer object
misc         - Miscelaneous utilities


Given it's current file location, it should be imported as:

import os
curDir = os.getcwd()
os.chdir("/Users/nayandusoruth/Desktop/Y2Physics/GeneralUtilities")
import misc
os.chdir(curDir)