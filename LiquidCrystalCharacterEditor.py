import cv2
import numpy as np
import math
import Grider

yoffset = 7
xoffset = 10

def createImage(ccAmount = 1):

    data = Grider.findTwoNumbers(ccAmount)
    createdSquares = 0
    maxSquares = (data[0] * data[1]) + data[2]

    se_height = data[0]
    se_width = data[1]
    #if(math.sqrt(ccAmount).is_integer()):
    #   se_height = int(math.sqrt(ccAmount))
    #   se_width = int(math.sqrt(ccAmount))
    #else:
    #   se_width = ccAmount
    #   se_height = 1

    px_height = 10 * se_height
    px_width = 7 * se_width
    blank_image = np.zeros((px_height,px_width,3), np.uint8)
    blank_image[0:px_height,0:px_width] = (25,25,25)
    color_image = blank_image
    for x in range(0,se_width):
        for y in range(0,se_height):
            if(createdSquares < maxSquares):
                createdSquares+=1
                color_image[x*xoffset,y*yoffset] = (255,0,0) #blue
                color_image[x*xoffset,y*yoffset+6] = (0,0,255) #red
                color_image[x*xoffset+9,y*yoffset] = (0,255,0) #green
                color_image[x*xoffset+9,y*yoffset+6] = (0,255,255) #yellow
                color_image[x*xoffset+1:x*xoffset+9,y*yoffset+1:y*yoffset+6] = (40,40,40) #whtie

    print("\nCreated template which contains",ccAmount,"characters")

    cv2.imwrite('Output.png',color_image)
    return color_image

def createCharArray(name = "Input.png"):
    if(name.strip() == ""):
        name = "Input.png"
    img = cv2.imread(name)
    while(img == None):
        print("No such file exists in this folder.")
        name = input("Please enter a new file name, or type exit to quit: ")
        if(name == "exit"):
            break
        else:
            img = cv2.imread(name)

    dimensions = img.shape
    width = dimensions[1]
    height = dimensions[0]

    yellow = "[  0 255 255]"
    red = "[  0   0 255]"
    green = "[  0 255   0]"
    blue = "[255   0   0]"

    rectangles = []
    
    for y in range(0,height):
        for x in range(0,width):
            currPx = str(img[y,x]).strip()
            #print("X-Y",x,y)
            
            if(currPx == blue): #top left


                topLeft = [x,y]
                topRight = [0,0]
                bottomLeft = [0,0]
                bottomRight = [0,0]
                
                for i in range(x,width):
                    if(str(img[y,i]).strip() == red):
                        topRight = [i,y]
                        break
                for i in range(y,height):
                    if(str(img[i,x]).strip() == green):
                        bottomLeft = [x,i]
                        break
                bottomRight = [topRight[0],bottomLeft[1]]

                rectangle = [[topLeft[0]+1,topLeft[1]+1],[topRight[0]-1,topRight[1]+1],[bottomLeft[0]+1,bottomLeft[1]-1],[bottomRight[0]-1,bottomRight[1]-1]]
                rectangles += [rectangle]
    
    textFile = open(name.replace(".png","")+".txt","w+")

    for rect in rectangles:
        rectWidth = abs(int(rect[0][0]) - int(rect[1][0]))+1
        rectHeight = abs(int(rect[0][1]) - int(rect[2][1]))+1

        print("RWidth",rectWidth,"RHeight",rectHeight)
        rectx=rect[0][0]
        recty=rect[0][1]

        currTextRect = "byte char"+str(rectangles.index(rect))+"["+str(rectHeight)+"] = {"

        for y in range(recty,recty+rectHeight):
            currLine = "B"
            for x in range(rectx,rectx+rectWidth):
                if(str(img[y,x]).strip() == '[0 0 0]'):
                    currLine+=str(1)
                else:
                    currLine+=str(0)
            currTextRect += currLine + ","
        currTextRect += "}"
        print(currTextRect)
        print("============")
        textFile.write(currTextRect+"\n")
                    

    #print("Size",width,height)


while True:
    selected = int(input('\nSelect : 1 - Help ; 2 - Create Template ; 3 - Create Character Array ; 4 - Close ALCCC >> '))
    if(selected == 1):
        print('\nStep One.')
        print('========.')
        print('To create custom characters using ALCCC, you must first create a template.')
        print('Press 2 to create a template, and specify the number of characters.')
        print('The template will be exported under the name "Output.png", open it in your favorite photo editing software (if you dont have one - https://www.piskelapp.com/).')
        print('Draw your desired characters in the brighter parts of the image.')
        print('Save the new image and place it in the same folder as "Output.png" (this is your input file).')
        print('\nStep Two.')
        print('========.')
        print('Press 3 to create the Character Array, specify the name of the input file.')
        print('ALCCC will create a text file named the same as the input file, this is your character array.')
        print('All thats left is to copy it into your project!.\n')
    elif(selected == 2):
        createImage(int(input('\nHow many characters would you like to create? ')))
    elif(selected == 3):
        createCharArray(input('\nPleaze specify the name of the input image (default is Input.png)'))
    elif(selected == 4):
        print('\n\nClosing ALCCC\n\n')
        break