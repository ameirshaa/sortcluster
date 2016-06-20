import matplotlib
import PIL
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time
from collections import Counter
from matplotlib import style
style.use("ggplot")


def whichcluster(filepath):
	matchedarray = []
	loadtheoreticalvalues = open('cluster.txt','r').read()
	loadtheoreticalvalues = loadtheoreticalvalues.split('\n')
	
	i = Image.open(filepath)
	iar = np.array(i) #create the array for the image
	iarl = iar.tolist() #listing the pixels
	
	inquestion = str(iarl)
	
	for eachvalue in loadtheoreticalvalues:
		if len(eachvalue) >1: #to ignore the space between the lines. 3 is completely arbitrary
			splitvalue = eachvalue.split('::')
			currenttype = splitvalue[0] #current type = brancher, slugs etc etc
			currentarray = splitvalue[1]
			eachpixelintheoreticalvalue = currentarray.split('],')
			eachpixelinquestion = inquestion.split('],')
			
			y = min(len(eachpixelintheoreticalvalue),len(eachpixelinquestion))
			for x in range(y):
				if eachpixelintheoreticalvalue[x] == eachpixelinquestion[x]:
					matchedarray.append(str(currenttype))
			'''
			while x < len(eachpixelintheoreticalvalue):
				if eachpixelintheoreticalvalue[10] == eachpixelinquestion[10]:
					matchedarray.append(str(currenttype))
				else:
					continue
					
				'''
	
	
	#print matchedarray
	
	x = Counter(matchedarray)
	
	print x
	
	graphX = []
	graphY = []
	
	for eachthing in x:
		print eachthing
		graphX.append(len(eachthing)) #just for the moment since the .bar function below only takes in integer values
		print x[eachthing]
		graphY.append(x[eachthing])
		
	fig = plt.figure()
	ax1 = plt.subplot2grid((4,4),(0,0), rowspan=1, colspan=4)
	ax2 = plt.subplot2grid((4,4),(1,0), rowspan=3, colspan=4)
	
	ax1.imshow(iar)
	
	ax2.bar(graphX,graphY)
	
	plt.ylim(3800)
	
	plt.show()
	

whichcluster('test.bmp')
	
	
