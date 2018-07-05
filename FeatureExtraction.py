####################### IMPORTING LIABRARIES ##################################
import pandas as pd
import cv2
import numpy as np

############################ FUNCTIONS ########################################
def rgb2gray(rgb):

    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b

    return gray
############################# DATASET CREATION ################################
def DatasetForTesting(pathstr):
    print("Module Name : "+__name__)
    dataset = []
    imageno=0
    while imageno<1:
        #READING RGB IMAGE
        imageno = imageno+1;
        #pathstr = "F:\Recovery After Formatting\Thesis\Main\Python Code Thesis\Starting 1\Data2/image"+str(imageno)+".png"
        img = cv2.imread(pathstr,cv2.IMREAD_COLOR)
        #RGB TO GREY SCALE IMAGE
        grayimg = rgb2gray(img)    
        #THRESHOLDING AND GRAYSCALE TO BINARY IMAGE
        ret,thresh1 = cv2.threshold(grayimg,127,255,cv2.THRESH_BINARY)
        binimg = cv2.threshold(grayimg, ret, 255, cv2.THRESH_BINARY)[1]
        
        binimg2 = binimg
        
        for i in range(0,20):
            for j in range(0,20):
                if binimg[i][j] == 255:
                    binimg2[i][j] = 1
        print(binimg2)
        #CONVERTING 2D to 1D AND ADDING TO DATASET
        datasetRow=[]
        for i in range(0,20):
            for j in range(0,20):
                datasetRow.append(binimg2[i][j])
        dataset.append(datasetRow)
    ##################### WRITING DATA TO CSV FILE ################################
    df = pd.DataFrame(dataset)
    df.to_csv("test1gui.csv")