import cv2
import numpy as np

#This function is used to display images
def DisplayImage(title, image):
    cv2.imshow(title, image)
    cv2.waitKey(0)

#This function highlights the boundary of the sun and does some computations
def HighlightBoundary(direction, originalSunImage, binarySunImage, xValue, yValue):
    while(direction < 8):
        if(direction == 0):
            if(binarySunImage[xValue + 1, yValue] == 255):
                originalSunImage[xValue + 1, yValue] = (255, 0, 0)
                xValue += 1
                return direction, xValue, yValue
                
        elif(direction == 1):
            if(binarySunImage[xValue + 1, yValue + 1] == 255):
                originalSunImage[xValue + 1, yValue + 1] = (255, 0, 0)
                xValue += 1
                yValue += 1
                return direction, xValue, yValue
                
        elif(direction == 2):
            if(binarySunImage[xValue, yValue + 1] == 255):
                originalSunImage[xValue, yValue + 1] = (255, 0, 0)
                yValue += 1
                return direction, xValue, yValue

        elif(direction == 3):
            if(binarySunImage[xValue - 1, yValue + 1] == 255):
                originalSunImage[xValue - 1, yValue + 1] = (255, 0, 0)
                xValue -= 1
                yValue += 1
                return direction, xValue, yValue

        elif(direction == 4):
            if(binarySunImage[xValue - 1, yValue] == 255):
                originalSunImage[xValue - 1, yValue] = (255, 0, 0)
                xValue -= 1
                return direction, xValue, yValue

        elif(direction == 5):
            if(binarySunImage[xValue - 1, yValue - 1] == 255):
                originalSunImage[xValue - 1, yValue - 1] = (255, 0, 0)
                xValue -= 1
                yValue -= 1
                return direction, xValue, yValue
                
        elif(direction == 6):
            if(binarySunImage[xValue, yValue - 1] == 255):
                originalSunImage[xValue, yValue - 1] = (255, 0, 0)
                yValue -= 1
                return direction, xValue, yValue
                
        elif(direction == 7):
            if(binarySunImage[xValue + 1, yValue - 1] == 255):
                originalSunImage[xValue + 1, yValue - 1] = (255, 0, 0)
                xValue += 1
                yValue -= 1
                return direction, xValue, yValue

        direction = (direction + 1) % 8
   
#This function detects the direction for computation of boundary 
def CalculateDirection(xValue, yValue, originalSunImage, binarySunImage):
    data = open("Boundary_Data.txt", "w")
    originalSunImage[xValue, yValue] = (255, 0, 0)
    terminationXValue = -1
    terminationYValue = -1
    direction = 7
    count = 0
    while True: 
        if(direction % 2 == 0):
            direction = (direction + 7) % 8
        else:
            direction = (direction + 6) % 8

        data.write(f"Iteration {count+1}: direction: {direction}\n")
        data.write(f"X value: {xValue} , Y Value: {yValue}\n")

        direction, xValue, yValue = HighlightBoundary(direction, originalSunImage, binarySunImage, xValue, yValue)

        data.write(f"Returned direction: {direction}\n")
        count += 1
        if(xValue == terminationXValue and yValue == terminationYValue):
            print("Boundary detected successfully")
            break

        if(count == 1):
            terminationXValue = xValue
            terminationYValue = yValue
    
    data.close()
    DisplayImage("Boundary Detected Image", originalSunImage)

#Read the input image
originalSunImage = cv2.imread("images/sun_image_1_.jpg")
DisplayImage("Original Image", originalSunImage)

grayscaleSunImage = cv2.cvtColor(originalSunImage, cv2.COLOR_BGR2GRAY)
DisplayImage("Grayscale Image", grayscaleSunImage)

(minIntensity, maxIntensity, minIntensityPixelLocation, maxIntensityPixelLocation) = cv2.minMaxLoc(grayscaleSunImage)
originalSunImage = cv2.circle(originalSunImage, maxIntensityPixelLocation, 1, (0, 0, 255), thickness = 2)
DisplayImage("Max Intensity Pixel Point", originalSunImage)

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
DisplayImage("Image without Erosion", binarySunImage)

kernel = np.ones((7,7), np.uint8);
binarySunImage = cv2.erode(binarySunImage, kernel, iterations=1)
DisplayImage("Eroded Image", binarySunImage)

cv2.imwrite("Binary_Threshold_Image.bmp", binarySunImage)

# moments = cv2.moments(binarySunImage)

# cX = int(moments["m10"] / moments["m00"])
# cY = int(moments["m01"] / moments["m00"])

# cv2.circle(binarySunImage, (cX, cY), 5, (0), -1)

# DisplayImage("Centroid Image", binarySunImage)

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

cv2.destroyAllWindows()