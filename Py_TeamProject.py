"""
===============================================================================
ENGR 133 Fa 2020

Assignment Information
	Assignment:     Python Team Project
	Team ID:        LC4-07 
	
Contributors:   Tommy Wygal, twygal@purdue.edu
                Maya Havens, mnhavens@purdue 
                Elizabeth Gauthier, gauthiee@purdue 
                Claire Huang, huan1536@purdue 
                
	My contributor(s) helped me:	
	[X] understand the assignment expectations without
		telling me how they will approach it.
	[X]] understand different ways to think about a solution
		without helping me plan my solution.
	[X] think through the meaning of a specific error or
		bug present in my code without looking at my code.
	Note that if you helped somebody else with their code, you
	have to list that person as a contributor here as well.
===============================================================================
"""


#import the needed libraries; NumPy and matplotlib
import numpy as np
import matplotlib.pyplot as plt

#==============================================================================

#ERROR CHECKING CODE
def errorCheck(pic):
    while True:
        try:
            pic = plt.imread(pic) #Input the name of the image file
            break
        except FileNotFoundError: #Make sure the file name is valid, if not then ask again
            print('Error: Incorrect File Name')
            pic = input("Input name of file:  ") #ask the user for a correct input file name
    return pic #returns the image file name
    
#==============================================================================

#EDGE ENHANCEMENT CODE
def thresholding(img):

    length = img.shape[0] #sets length to the length of the image
    width = img.shape[1] #sets width to the width of the image
    
    enhanced = np.zeros_like(img) #creates an array filled with zeros the size of the image
    threshold = 0.3 #sets a threshold value for black or white ourput pixel on image
    for row in range(1,length): #reads through each row of the image
            for column in range(1, width): #reads through each column of the image
                if img[row][column] < threshold: #can flip < or >, depending on if you want primary black or white
                    enhanced[row][column] = 0 #blacker
                else:
                    enhanced[row][column] = 1 #whiter
    plt.imsave("threshold.png",enhanced, cmap="Greys_r") #This will save the file that was made as threshold.png to be used later
    return(enhanced) #returns the matrix of the threshold picture
            
#==============================================================================

#GRAYSCALE CODE
def getGray(image):
	gimage=(image.shape[0],image.shape[1]) #This takes in the length and width of the image. This does not take in the channels as we are wanting to convert this to grey scale, wich only uses 1 channel.
	gmatrix=np.zeros(gimage) #This makes a matrix of zeros that is the same length and width of the original image
	for i in range(image.shape[0]): #This nested for loop goes through the length and the width of the image and puts the values into the matrix of zeros that was made earlier.
		for j in range(image.shape[1]):
			gmatrix[i,j]=0.2126*image[i,j,0]+0.7152*image[i,j,1]+0.0722*image[i,j,2] #This uses the BT.709 standard that Dr.Delp talks about in his lecture image[i,j,0] is red, [i,j,1] is green, [i,j,2] is blue. All 3 of these channels are transfered to one channel to become grey scale and is outputed in the gray image matrix. 
	plt.imsave("grey.png",gmatrix, cmap="Greys_r") #This will save the file that was made as grey.png to be used later
	return(gmatrix) #returns the matrix of the grayscale picture

#==============================================================================

#NOISE SMOOTHING CODE
def smooooth(gimage): 
	gmatrix=getGray(image) 
	smoothmatrix=np.zeros_like(gimage) #sets a matrix of zeros the size of the input image
	for i in range(1,image.shape[0]-1): #reads through each row of the image
		for j in range(1,image.shape[1]-1): #reads through each column of the image
			smoothmatrix[i,j]=(gmatrix[i-1,j+1]/9)+(gmatrix[i-1,j]/9)+(gmatrix[i-1,j-1]/9)+(gmatrix[i,j+1]/9)+(gmatrix[i,j]/9)+(gmatrix[i,j-1]/9)+(gmatrix[i+1,j+1]/9)+(gmatrix[i+1,j]/9)+(gmatrix[i+1,j-1]/9)#averages the values of the 3x3 pixels and puts the value in the middle pixel
	plt.imsave("smooth.png",smoothmatrix,cmap="Greys_r") #Saves the smoothed image as smooth.png 
	return(smoothmatrix) #returns the matrix of the smoothed picture
  
#==============================================================================

#EDGE ENHANCEMENT CODE
def enhancement(img):
    horFilter = [[-1, 0, 1], #creates the horizontal filter for edge enhancement
              [-2, 0, 2],
              [-1, 0, 1]]

    vertFilter = [[-1, -2, -1], #creates the vertical filter for edge enhancement
              [0, 0, 0],
              [1, 2, 1]]

    length = img.shape[0] #sets length to the length of the image
    width = img.shape[1] #sets width to the width of the image

    vertEdges = np.zeros_like(img) #sets a matrix of zeros the same size as the input image
    horEdges = np.zeros_like(img) #sets a matrix of zeros the same size as the input image
    for row in range(1,length - 1): #reads through each row of the image
        for column in range(1, width - 1): #reads through each column of the image
            box = img[row - 1: row + 2, column - 1: column + 2] #sets a box of 3x3 pixels in the image
            change1 = vertFilter * box #multiplies the vertical filter times the 3x3 in the image
            change2 = horFilter * box #multiplies the horizontal filter times the 3x3 in the image            
            boxValue1 = change1.sum()  #adds each of the 3x3 pixel products
            boxValue2 = change2.sum() #adds each of the 3x3 pixel products           
            vertEdges[row][column] = boxValue1 #sets the product of the 3x3 pixels to the middle pixel in the 3x3
            horEdges[row][column] = boxValue2 #sets the product of the 3x3 pixels to the middle pixel in the 3x3
            
    combined = np.zeros_like(img) #sets a matrix of zeros the same size as the input image
    combined = np.sqrt((vertEdges ** 2) + (horEdges ** 2)) #dot product of the vertical and horizontal edges
    plt.imsave('edgeEnhancement.png',combined, cmap = 'Greys_r') #Saves the enhanced image as edgeEnhancement.png 
    return(combined) #returns the matrix of the edge enhanced picture
    
#==============================================================================

#Main Code
image=errorCheck(input("Input name of .png file:  ")) #Checks to see if the input file works. 
length=len(image.shape)
if length==3: #Checks to see if the image is already grayscale or if it is in color
	gimage=getGray(image)#converts a color image to grayscale with the UDF
else:
	gimage=image #if the inputted image is already grey, it will assign gimage to image
#even better, the result looks feasible and is proper
smooth=smooooth(gimage)#smooths the image with a UDF
edgeFixes = enhancement(smooth)#enhances the image with a UDF
picture = thresholding(edgeFixes)#detects edges with a UDF
plt.imshow(image) #This displays the original image
plt.show() #Plt.show() makes it so the image is printed out in the window no matter what comes after it
plt.imshow(gimage,cmap="Greys_r") #This displays the grey scale image.ima
plt.show()
plt.imshow(smooth,cmap="Greys_r") #This displays the smoothed grey scale image
plt.show()
plt.imshow(edgeFixes, cmap='Greys_r') #This displays the edge enhanced image
plt.show()
plt.imshow(picture,cmap="Greys_r") #This displays the thresd image
plt.show()

'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''