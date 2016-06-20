'''
this code takes an image in the folder test_images (or a few images, depending on what you put into the for loop), thresholds 
the image/images and outputs the thresholded images into the folder test_images_thresholded. Then the code takes the thresholded
images stored in test_images_thresholded and converts them into an array of integers that represent their RGB values. 
This array of values is then compared with database.txt that we created earlier using createdatabase.py. If there is a string 
of RGB values that matches what we have in the database, the code saves that match. In the end, it counts the total number of matches 
for each value (i.e for brancher, crossover, looper, slug) and outputs it. The value with the highest match corresponds to that cluster
'''
'''
we threshold images to convert color images into black and white. this is to ensure that the computer does not get caught up in colors
but instead concentrates only on the actual pattern of those images.
'''

#you will need all these libraries
import matplotlib
import PIL
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time
from collections import Counter
from matplotlib import style
style.use("ggplot")

def threshold(image_path, output_path): #define a function for thresholding the image
    # open image
    img = Image.open(image_path)

    # get pixel map
    pm = img.load()
    balance = []

    for y in range(img.size[1]): # every row
        for x in range(img.size[0]): #every column
            pixel = pm[x,y]      # get pixel values
            avg = sum(pixel) / 3 # calculate average intensity across 3 RGB values
            balance.append(avg)  # append to list

    # determine threshold value which is basically the average of the average of the values. 
    threshold = sum(balance) / len(balance)

    # threshold filter
    for y in range(img.size[1]): # every row
        for x in range(img.size[0]): #every column
            if balance[y*img.size[0] + x] > threshold: #for the balance at that particular index, if it is more than the threshold value
                pm[x,y] = (255,255,255) #change the pixel to white
            else: #if it is less than the threshold value
                pm[x,y] = (0,0,0) #change the pixel to black

    # save image
    img.save(output_path)

#can put some for loop here to loop over all the images but you can take it away if you have only one image
for i in range(1,5):
	threshold('test_images/test_'+str(i)+'.JPG','test_images_thresholded/test_'+str(i)+'.bmp')

def whichcluster(filepath): #define a function that takes in one argument (the filepath to the image)
	matchedarray = [] #create the empty array for the matched values to go into
	loadtheoreticalvalues = open('database.txt','r').read() #opening the database we created earlier
	loadtheoreticalvalues = loadtheoreticalvalues.split('\n') #making it easier for the computer to read the data later on
	
	i = Image.open(filepath) #opening the (thresholded) image
	iar = np.array(i) #create the array for the image
	iarl = iar.tolist() #listing the pixels
	
	inquestion = str(iarl) #making the pixels into a string so as to match how we stored the data in database.txt and thus allow for easier comparison. 
	
	for eachvalue in loadtheoreticalvalues:
		if len(eachvalue) >1: #to ignore the space between the lines. 3 is completely arbitrary
			splitvalue = eachvalue.split('::')
			currenttype = splitvalue[0] #current type = brancher, slugs etc etc
			currentarray = splitvalue[1] #taking the rest of the data. if this is unclear, refer to database.txt to see how we have organised the information there
			eachpixelintheoreticalvalue = currentarray.split('],') #establishing our delimiter
			eachpixelinquestion = inquestion.split('],') #establishing our delimiter
			
			y = min(len(eachpixelintheoreticalvalue),len(eachpixelinquestion)) #taking the minimum of either string
			for x in range(y):
				if eachpixelintheoreticalvalue[x] == eachpixelinquestion[x]: #if there are values in both strings that match
					matchedarray.append(str(currenttype)) #append the type of cluster that corresponds to the matched value
			'''
			while x < len(eachpixelintheoreticalvalue):
				if eachpixelintheoreticalvalue[10] == eachpixelinquestion[10]:
					matchedarray.append(str(currenttype))
				else:
					continue
					
				'''
	
	
	#print matchedarray
	
	x = Counter(matchedarray) #counts the number of times each type of cluster has appeared in the list.
	
	print x
	
	graphX = [] #create empty lists for which we will show in a graph from later
	graphY = [] 
	
	for eachthing in x:
		print eachthing #print the 
		graphX.append(len(eachthing)) #just for the moment since the .bar function below only takes in integer values 
		print x[eachthing]
		graphY.append(x[eachthing]) #append the number of times that particular value has appeared. 
		
	fig = plt.figure() #plotting the values in a graph
	ax1 = plt.subplot2grid((4,4),(0,0), rowspan=1, colspan=4) 
	ax2 = plt.subplot2grid((4,4),(1,0), rowspan=3, colspan=4)
	
	ax1.imshow(iar) #show the original image on the top
	
	ax2.bar(graphX,graphY) #show the bar chart at the bottom
	
	plt.ylim(3800) #if the count value is less than 3800, do not show that value
	
	plt.show()
	
for i in range(1,5): #we do not need this for loop if there is only one image
	whichcluster('test_images_thresholded/test_'+str(i)+'.bmp')
	
	
