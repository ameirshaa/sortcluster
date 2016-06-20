#create a database of clusters for reference

import matplotlib
import PIL
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time
from collections import Counter


clusterarray = open('cluster.txt','a')

typesofcluster = range(1,6) #how many types of clusters we have
#clusterversions = range(1,8) #here we input how many versions of each cluster type we have. 

for cluster in typesofcluster:
	#for number in clusterversions: #remember to indent properly if there are more than one versions
	print(str(cluster)+'.'+str(1)) #instead of 1 put number if...
	imgFilePath = 'clustertypes/thresholded_'+str(cluster)+'.'+str(1)+'.bmp' #save files accordingly
	ei = Image.open(imgFilePath)
	eiar = np.array(ei) #making the array
	eiar1 = str(eiar.tolist()) #saving to the text

	if cluster == 1:
		lineToWrite = 'brancher'+'::'+eiar1+'\n'
		clusterarray.write(lineToWrite)
	elif cluster == 2:
		lineToWrite = 'crossover'+'::'+eiar1+'\n'
		clusterarray.write(lineToWrite)
	elif cluster == 3:
		lineToWrite = 'looper'+'::'+eiar1+'\n'
		clusterarray.write(lineToWrite)
	elif cluster == 4:
		lineToWrite = 'slug'+'::'+eiar1+'\n'
		clusterarray.write(lineToWrite)
	elif cluster == 5:
		lineToWrite = 'straight-wiggly'+'::'+eiar1+'\n'
		clusterarray.write(lineToWrite)
	else:
		continue
		

