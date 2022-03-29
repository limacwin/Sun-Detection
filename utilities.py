import cv2

def CalculateCentroid(originalSunImage, binarySunImage, imageWidth, imageHeight):
    # print("Calculating Centroid...")
    m10 = 0
    m01 = 0
    totalWhitePixels = 0

    #Iterating over the image along horizontally and calculating image moment along X
    for row in range(imageHeight - 1):
        pixelFound = False
        count = 0
        for column in range(imageWidth - 1):
            if(binarySunImage[row,column] == 255):
                pixelFound = True
                count += 1
                totalWhitePixels += 1
        if(pixelFound):
            m10 += row * count

    #Iterating over the image along vertically and calculating image moment along Y
    for column in range(imageWidth - 1):
        pixelFound = False
        count = 0
        for row in range(imageHeight - 1):
            if(binarySunImage[row,column] == 255):
                pixelFound = True
                count += 1
        if(pixelFound):
            m01 += column * count

    #Centroid calculation
    xCentroidCoordinate = round(m10/totalWhitePixels)
    yCentroidCoordinate = round(m01/totalWhitePixels)

    # print(f"Total White Pixels: {totalWhitePixels}")
    # print(f"m10: {m10}")
    # print(f"m01: {m01}")
    # print(f"Centroid coordinate (X, Y): ({xCentroidCoordinate},{yCentroidCoordinate})")

    originalSunImage[xCentroidCoordinate, yCentroidCoordinate] = (0, 255, 0)
    # cv2.circle(originalSunImage, (yCentroidCoordinate, xCentroidCoordinate), 8, (0, 255, 0), thickness = 1)
    # cv2.imshow("Centroid", originalSunImage)
    # cv2.waitKey(0)
    
    return xCentroidCoordinate, yCentroidCoordinate

def CalulateOffset(xCentroidCoordinate, yCentroidCoordinate, originalSunImage, imageWidth, imageHeight):
    # print("Calculating offset...")
    #Calculating the centre of the frame
    xFrameCentreCoordinate = round(imageWidth/2)
    yFrameCentreCoordinate = round(imageHeight/2)

    # print(f"Frame centre coordinates: ({xFrameCentreCoordinate},{yFrameCentreCoordinate})")
    centreFrameCoordinate = (xFrameCentreCoordinate, yFrameCentreCoordinate)
    centroidCoordinate = (yCentroidCoordinate, xCentroidCoordinate)
    originalSunImage[yFrameCentreCoordinate, xFrameCentreCoordinate] = (0, 0, 0)
    # cv2.circle(originalSunImage, centreFrameCoordinate, 8, (0, 0, 0), thickness = 1)
    
    # cv2.imshow("Frame Centre", 4originalSunImage)
    # cv2.waitKey(0)

    # cv2.line(originalSunImage, centreFrameCoordinate, centroidCoordinate, (0, 0, 0), thickness = 1)
    # cv2.imshow("Offset", originalSunImage)
    # cv2.waitKey(0)

    #Calculating the offset distance
    # offset = math.sqrt(((xCentroidCoordinate - xFrameCentreCoordinate) ** 2) + ((yCentroidCoordinate - yFrameCentreCoordinate) ** 2))
    intersection = (yCentroidCoordinate, yFrameCentreCoordinate)
    # offsetY = (xFrameCentreCoordinate, yCentroidCoordinate)
    
    # cv2.line(originalSunImage, centroidCoordinate, intersection, (0, 0, 0), thickness = 1)  # Line 1
    # cv2.line(originalSunImage, intersection, centreFrameCoordinate, (0, 0, 0), thickness = 1) # Line 2
    # cv2.imshow("Offset", originalSunImage)
    # cv2.waitKey(0)
                          
    offsetX = abs(yCentroidCoordinate - xFrameCentreCoordinate)
    offsetY = abs(xCentroidCoordinate - yFrameCentreCoordinate)
    
    # print(f"OffsetX: {offsetX}")
    # print(f"OffsetY: {offsetY}")
    
    return offsetX, offsetY
    
    # offsetImage = cv2.putText(originalSunImage, f"Offset = {offset}", (xFrameCentreCoordinate + 20, yFrameCentreCoordinate + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), thickness = 1)

    # cv2.imshow("Offset Image", offsetImage)
    # cv2.waitKey(0)