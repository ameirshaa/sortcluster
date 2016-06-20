import PIL
from PIL import Image

def threshold(image_path, output_path):
    # open image
    img = Image.open(image_path)

    # get pixel map
    pm = img.load()
    balance = []

    for y in range(img.size[1]): # every row
        for x in range(img.size[0]): #every column
            pixel = pm[x,y]      # get pixel values
            avg = sum(pixel) / 3 # calculate average intensity
            balance.append(avg)  # append to list

    # determine threshold
    threshold = sum(balance) / len(balance)

    # threshold filter
    for y in range(img.size[1]): # every row
        for x in range(img.size[0]): #every column
            if balance[y*img.size[0] + x] > threshold:
                pm[x,y] = (255,255,255)
            else:
                pm[x,y] = (0,0,0)

    # save image
    img.save(output_path)

#can put some for loop here to loop over all the images

threshold('test.png','clustertypes/thresholded_test.bmp')
        

