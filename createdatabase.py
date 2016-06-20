'''
this code takes the predetermined 'perfect' images that represent various cluster patterns, 
converts them into an array of strings with numbers representing their RGB values
and outputs that array into database.txt creating a database for later reference

'''
#you do not need any of this to run this script
import matplotlib
import PIL
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time
from collections import Counter



clusterarray = open('database.txt','a') #opens a file database.txt, does not matter if you have created it yet

typesofcluster = range(1,5) #how many types of clusters we have
#clusterversions = range(1,8) #here we input how many versions of each cluster type we have. 

for cluster in typesofcluster:
	#for number in clusterversions: #remember to indent properly if there are more than one versions
	print(str(cluster)+'.'+str(1)) #instead of 1 put number if...
	imgFilePath = 'clustertypes_thresholded/'+str(cluster)+'.'+str(1)+'.bmp' #where we have saved the predetermined perfect images #save files accordingly
	ei = Image.open(imgFilePath) #opening the image
	eiar = np.array(ei) #making the array
	eiar1 = str(eiar.tolist()) #saving to database.txt
	'''
earlier we had set cluster to be in range(5). in order to convert the integers into strings we 
understand, (i.e. the actual names of the various clusters) we apply this if statement that 
matches each number to the various clusters we had saved as images earlier.
'''

	if cluster == 1: 
		print 'we are now printing the brancher'
		lineToWrite = 'brancher'+'::'+eiar1+'\n'   
		clusterarray.write(lineToWrite)
	elif cluster == 2:
		print 'we are now printing the crossover'
		lineToWrite = 'crossover'+'::'+eiar1+'\n'
		clusterarray.write(lineToWrite)
	elif cluster == 3:
		print 'we are now printing the looper'
		lineToWrite = 'looper'+'::'+eiar1+'\n'
		clusterarray.write(lineToWrite)
	elif cluster == 4:
		print 'we are now printing the slug'
		lineToWrite = 'slug'+'::'+eiar1+'\n'
		clusterarray.write(lineToWrite)
	#elif cluster == 5:
		#lineToWrite = 'straight-wiggly'+'::'+eiar1+'\n'
		#clusterarray.write(lineToWrite)
	else:
		continue
		

