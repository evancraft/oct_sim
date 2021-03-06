import os
import subprocess
import argparse
from datetime import datetime 
import threading 

# initialize date and time
now = datetime.now()

# Construct the parser to take in the inputs 
parser = argparse.ArgumentParser()
parser.add_argument("--outDir", '-o', type=str, help="output directory name", default="simResults_{}".format(now.strftime("%m%d%y_%H%M%S")))
args = parser.parse_args()

outDir = args.outDir

# Parameters constant from run to run
chamber = "large"
xCoincidenceThreshold = 3
uvCoincidenceThreshold = 3
outFilePrefix = 'outFile'

# Parameters that will change from run to run. Others are left default
nEvents = [10**3]
bkgRates = [i*(10**j) for i in range(1,10) for j in range(2,5)] 
bkgRates.sort()

# setup the output directory
if os.path.isdir(outDir) == False:
	os.system("mkdir {}".format(outDir))

#################### Begin the production of events ####################

os.system("make")

# Set up threading 

class myThread (threading.Thread):
   def __init__(self, nEvents, bkgRate, outFileName):
      threading.Thread.__init__(self)
      self.nEvents = nEvents
      self.bkgRate = bkgRate
      self.name = 'nEvents{}_bkgRate{}'.format(nEvents,bkgRate)
   def run(self):
      print "Starting " + self.name
      subprocess.call("./sim -n {} -ch {} -b {} -o {}.root -uvr -thrx {} -thruv {} -tree >> {}.log &".format(
			nEvents[nE], 
			chamber, 
			bkgRates[nB],
			outFileName,
			xCoincidenceThreshold,
			uvCoincidenceThreshold,
			outFileName), shell=True
		)
      print "Exiting " + self.name


nNEvents = len(nEvents)
nBkgRates = len(bkgRates)

threads = []
for nE in range(0,nNEvents):
	for nB in range(0,nBkgRates):
		outFileName = outDir + '/' + outFilePrefix + '_nEvents{}_bkgRate{}'.format(nEvents[nE],bkgRates[nB])
		temp = myThread(nEvents[nE],bkgRates[nB],outFileName)
		temp.start()
		threads.append(temp)
		#os.system("./sim -n {} -ch {} -b {} -o {} -uvr -thrx {} -thruv {} -tree".format(nEvents[i],bkgRate[j],outFileName))

