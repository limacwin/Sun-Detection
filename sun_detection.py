import cv2

#This function is used to display images
def DisplayImage(title, image):
    cv2.imshow(title, image)
    cv2.waitKey(0)

#This function highlights the boundary of the sun and does some computations
def HighlightBoundary(direction, originalSunImage, binarySunImage, xValue, yValue):
    while(direction < 8):
        if(direction == 0):
            if(binarySunImage[xValue + 1, yValue] == 255):
                print(f"Pixel value at({xValue + 1},{yValue}) : {binarySunImage[xValue + 1, yValue]}")
                originalSunImage[xValue + 1, yValue] = (255, 0, 0)
                xValue += 1
                return direction, xValue, yValue
                
        elif(direction == 1):
            if(binarySunImage[xValue + 1, yValue + 1] == 255):
                print(f"Pixel value at({xValue + 1},{yValue+1}) : {binarySunImage[xValue + 1, yValue +1]}")
                originalSunImage[xValue + 1, yValue + 1] = (255, 0, 0)
                xValue += 1
                yValue += 1
                return direction, xValue, yValue
                
        elif(direction == 2):
            if(binarySunImage[xValue, yValue + 1] == 255):
                print(f"Pixel value at({xValue},{yValue+1}) : {binarySunImage[xValue, yValue +1]}")
                originalSunImage[xValue, yValue + 1] = (255, 0, 0)
                yValue += 1
                return direction, xValue, yValue

        elif(direction == 3):
            if(binarySunImage[xValue - 1, yValue + 1] == 255):
                print(f"Pixel value at({xValue - 1},{yValue+1}) : {binarySunImage[xValue - 1, yValue +1]}")
                originalSunImage[xValue - 1, yValue + 1] = (255, 0, 0)
                xValue -= 1
                yValue += 1
                return direction, xValue, yValue

        elif(direction == 4):
            if(binarySunImage[xValue - 1, yValue] == 255):
                print(f"Pixel value at({xValue - 1},{yValue}) : {binarySunImage[xValue - 1, yValue]}")
                originalSunImage[xValue - 1, yValue] = (255, 0, 0)
                xValue -= 1
                return direction, xValue, yValue

        elif(direction == 5):
            if(binarySunImage[xValue - 1, yValue - 1] == 255):
                print(f"Pixel value at({xValue - 1},{yValue-1}) : {binarySunImage[xValue - 1, yValue -1]}")
                originalSunImage[xValue - 1, yValue - 1] = (255, 0, 0)
                xValue -= 1
                yValue -= 1
                return direction, xValue, yValue
                
        elif(direction == 6):
            if(binarySunImage[xValue, yValue - 1] == 255):
                print(f"Pixel value at({xValue},{yValue-1}) : {binarySunImage[xValue, yValue -1]}")
                originalSunImage[xValue, yValue - 1] = (255, 0, 0)
                yValue -= 1
                return direction, xValue, yValue
                
        elif(direction == 7):
            if(binarySunImage[xValue + 1, yValue - 1] == 255):
                print(f"Pixel value at({xValue + 1},{yValue-1}) : {binarySunImage[xValue + 1, yValue -1]}")
                originalSunImage[xValue + 1, yValue - 1] = (255, 0, 0)
                xValue += 1
                yValue -= 1
                return direction, xValue, yValue

        direction = (direction + 1) % 8
   
#This function detects the direction for computation of boundary 
def CalculateDirection(xValue, yValue, originalSunImage, binarySunImage):
    data = open("BoundaryData.txt", "w")
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
        
        print(f"Iteration {count + 1}: direction - {direction}")
        print(f"X value: {xValue}, Y value: {yValue}\n")

        data.write(f"Iteration {count+1}: direction - {direction}\n")
        data.write(f"X value: {xValue} , Y Value: {yValue}\n")

        direction, xValue, yValue = HighlightBoundary(direction, originalSunImage, binarySunImage, xValue, yValue)
        print(f"Returned direction: {direction}\n")

        data.write(f"Returned direction - {direction}\n")
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
originalSunImage = cv2.imread("images/sun_image_4.jpg")
cv2.imshow("Original Image", originalSunImage)
cv2.waitKey(0)

grayscaleSunImage = cv2.cvtColor(originalSunImage, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale Image", grayscaleSunImage)
cv2.waitKey(0)

(minIntensity, maxIntensity, minIntensityPixelLocation, maxIntensityPixelLocation) = cv2.minMaxLoc(grayscaleSunImage)
print(f"Max intensity: {maxIntensity} & Min intensity: {minIntensity}")
print(f"Max intensity Location: {maxIntensityPixelLocation} & Min intensity Location: {minIntensityPixelLocation}")
originalSunImage[minIntensityPixelLocation[1], minIntensityPixelLocation[0]] = (0, 0, 0)
originalSunImage = cv2.circle(originalSunImage, maxIntensityPixelLocation, 20, (0, 0, 0), thickness = 0)
DisplayImage("Max Intensity Pixel Point", originalSunImage)

#Gets the image width and height
imageWidth = originalSunImage.shape[1]
imageHeight = originalSunImage.shape[0]

#Iterating over the image and converting the image to binary image by thresholding
for row in range(imageHeight-1):
    for col in range(imageWidth-1):
        if (grayscaleSunImage[row, col] <= maxIntensity - 10):
            grayscaleSunImage[row, col] = 0
        else:
            grayscaleSunImage[row, col] = 255

binarySunImage = grayscaleSunImage
cv2.imwrite("D:\BE Project\Codes\Border Tracing Algorithm\BinaryThresholdImage.bmp", binarySunImage)
DisplayImage("Binary Image", binarySunImage)

maxIntensityPixelFound = False

#Iterating over the image and finding out the first pixel having pixel value 255 (in linear fashion)
for row in range(imageHeight-1):
    for col in range(imageWidth-1):
        if (binarySunImage[row, col] == 255):
            maxIntensityPixelFound = True
            print(row)
            print(col)
            xValue = row
            yValue = col
            CalculateDirection(xValue, yValue, originalSunImage, binarySunImage)
            break
    if(maxIntensityPixelFound):
        break

cv2.destroyAllWindows()