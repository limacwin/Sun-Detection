import cv2
import numpy as np
import utilities as util

#This function is used to display images
def DisplayImage(title, image):
    cv2.imshow(title, image)
    cv2.waitKey(0)

#This function highlights the boundary of the sun and does some computations
def HighlightBoundary(direction, originalSunImage, binarySunImage, xValue, yValue):
    while(direction < 8):
        if(direction == 0):
            if(binarySunImage[xValue, yValue + 1] == 255):
                originalSunImage[xValue, yValue + 1] = (255, 0, 0)
                yValue += 1
                return direction, xValue, yValue
                
        elif(direction == 1):
            if(binarySunImage[xValue - 1, yValue + 1] == 255):
                originalSunImage[xValue - 1, yValue + 1] = (255, 0, 0)
                xValue -= 1
                yValue += 1
                return direction, xValue, yValue
                
        elif(direction == 2):
            if(binarySunImage[xValue - 1, yValue] == 255):
                originalSunImage[xValue - 1, yValue] = (255, 0, 0)
                xValue -= 1
                return direction, xValue, yValue

        elif(direction == 3):
            if(binarySunImage[xValue - 1, yValue - 1] == 255):
                originalSunImage[xValue - 1, yValue - 1] = (255, 0, 0)
                xValue -= 1
                yValue -= 1
                return direction, xValue, yValue

        elif(direction == 4):
            if(binarySunImage[xValue, yValue - 1] == 255):
                originalSunImage[xValue, yValue - 1] = (255, 0, 0)
                yValue -= 1
                return direction, xValue, yValue

        elif(direction == 5):
            if(binarySunImage[xValue + 1, yValue - 1] == 255):
                originalSunImage[xValue + 1, yValue - 1] = (255, 0, 0)
                xValue += 1
                yValue -= 1
                return direction, xValue, yValue
                
        elif(direction == 6):
            if(binarySunImage[xValue + 1, yValue] == 255):
                originalSunImage[xValue + 1, yValue] = (255, 0, 0)
                xValue += 1
                return direction, xValue, yValue
                
        elif(direction == 7):
            if(binarySunImage[xValue + 1, yValue + 1] == 255):
                originalSunImage[xValue + 1, yValue + 1] = (255, 0, 0)
                xValue += 1
                yValue += 1
                return direction, xValue, yValue

        # print(f"direction: {direction}", end=" ")
        direction = (direction + 1) % 8
        # print(f"new_direction: {direction}")
   
#This function detects the direction for computation of boundary 
def CalculateDirection(xValue, yValue, originalSunImage, binarySunImage):
    data = open("data/boundary_data.txt", "w")
    originalSunImage[xValue, yValue] = (255, 0, 0)
    terminationXValue = -1
    terminationYValue = -1
    direction = 7
    data.write(f"Initial direction: {direction}\n\n")
    count = 0
    while True: 
        if(direction % 2 == 0):
            direction = (direction + 7) % 8
        else:
            direction = (direction + 6) % 8

        data.write(f"Iteration {count+1}: direction: {direction}\n")
        data.write(f"X value: {xValue} , Y Value: {yValue}\n")

        # print(f'function call with direction: {direction}, xval: {xValue}, yval: {yValue}')
        direction, xValue, yValue = HighlightBoundary(direction, originalSunImage, binarySunImage, xValue, yValue)
        # print(f'function return with direction: {direction}, xval: {xValue}, yval: {yValue}')
        data.write(f"Returned direction: {direction}\n\n")
        count += 1
        if(xValue == terminationXValue and yValue == terminationYValue):
            print("Boundary detected successfully")
            break

        if(count == 1):
            terminationXValue = xValue
            terminationYValue = yValue
    
    data.close()
    # DisplayImage("Boundary Detected Image", originalSunImage)

def SunDetection(pathToImage):
    #Read the input image
    print(pathToImage)
    originalSunImage = cv2.imread(pathToImage)
    #DisplayImage("Original Image", originalSunImage)

    grayscaleSunImage = cv2.cvtColor(originalSunImage, cv2.COLOR_BGR2GRAY)
    # DisplayImage("Grayscale Image", grayscaleSunImage)

    (minIntensity, maxIntensity, minIntensityPixelLocation, maxIntensityPixelLocation) = cv2.minMaxLoc(grayscaleSunImage)
    # originalSunImage = cv2.circle(originalSunImage, maxIntensityPixelLocation, 1, (0, 0, 255), thickness = 2)
    # originalSunImage[maxIntensityPixelLocation[1], maxIntensityPixelLocation[0]] = (0, 0, 255)
    # DisplayImage("Max Intensity Pixel Point", originalSunImage)

    #Gets the image width and height
    imageWidth = originalSunImage.shape[1]
    imageHeight = originalSunImage.shape[0]

    #Iterating over the image and converting it to binary by thresholding
    thresholdOffset = 10
    for row in range(imageHeight-1):
        for col in range(imageWidth-1):
            if (grayscaleSunImage[row, col] <= maxIntensity - thresholdOffset):
                grayscaleSunImage[row, col] = 0
            else:
                grayscaleSunImage[row, col] = 255

    binarySunImage = grayscaleSunImage
    # DisplayImage("Image without Erosion", binarySunImage)

    kernel = np.ones((7,7), np.uint8)
    binarySunImage = cv2.erode(binarySunImage, kernel, iterations=1)
    # DisplayImage("Eroded Image", binarySunImage)

    cv2.imwrite("images/generated/binary_threshold_image.bmp", binarySunImage)

    maxIntensityPixelFound = False

    #Iterating over the image and finding out the first pixel having pixel value 255 (in linear fashion)
    for row in range(imageHeight-1):
        for col in range(imageWidth-1):
            if (binarySunImage[row, col] == 255):
                maxIntensityPixelFound = True
                xValue = row
                yValue = col
                CalculateDirection(xValue, yValue, originalSunImage, binarySunImage)
                break 
        if(maxIntensityPixelFound):
            break
        
    xCentroidCoordinate, yCentroidCoordinate = util.CalculateCentroid(originalSunImage, binarySunImage, imageWidth, imageHeight)

    offsetX, offsetY = util.CalulateOffset(xCentroidCoordinate, yCentroidCoordinate, originalSunImage, imageWidth, imageHeight)

    cv2.destroyAllWindows()
    
    return offsetX, offsetY