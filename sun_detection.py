import cv2
import numpy as np

def display_image(title, img):
    cv2.imshow(title, img)
    cv2.waitKey(0)

    # if(direction == 0 and binary_sun[xValue + 1, yValue] == 255):
    #     sun_image[xValue + 1, yValue] = (255, 0, 0)
    #     newDirection = 0
    #     return newDirection
    # elif(direction == 1 and binary_sun[xValue + 1, yValue + 1] == 255):
    #     sun_image[xValue + 1, yValue + 1] = (255, 0, 0)
    #     newDirection = 1
    #     return newDirection
    # elif(direction == 2 and binary_sun[xValue, yValue + 1] == 255):
    #     sun_image[xValue, yValue + 1] = (255, 0, 0)
    #     newDirection = 2
    #     return newDirection
    # elif(direction == 3 and binary_sun[xValue - 1, yValue + 1] == 255):
    #     sun_image[xValue + 1, yValue + 1] = (255, 0, 0)
    #     newDirection = 3
    #     return newDirection
    # elif(direction == 4 and binary_sun[xValue - 1, yValue] == 255):
    #     sun_image[xValue + 1, yValue + 1] = (255, 0, 0)
    #     newDirection = 4
    #     return newDirection
    # elif(direction == 5 and binary_sun[xValue - 1, yValue - 1] == 255):
    #     sun_image[xValue + 1, yValue + 1] = (255, 0, 0)
    #     newDirection = 5
    #     return newDirection
    # elif(direction == 6 and binary_sun[xValue, yValue - 1] == 255):
    #     sun_image[xValue + 1, yValue + 1] = (255, 0, 0)
    #     newDirection = 6
    #     return newDirection
    # elif(direction == 7 and binary_sun[xValue + 1, yValue - 1] == 255):
    #     sun_image[xValue + 1, yValue + 1] = (255, 0, 0)
    #     newDirection = 7
    #     return newDirection
    # else:
    #     return 7
def HighlightBoundary(direction,sun_image, binary_sun, xValue, yValue):
    print("i got called")
    while(direction < 8):
        print(direction)
        if(direction == 0):
            if(binary_sun[xValue + 1, yValue] == 255):
                print(f"Pixel value at({xValue + 1},{yValue}) : {binary_sun[xValue + 1, yValue]}")
                sun_image[xValue + 1, yValue] = (255, 0, 0)
                xValue += 1
                return 0
            else:
                direction = (direction + 1) % 8
                continue

        if(direction == 1):
            if(binary_sun[xValue + 1, yValue + 1] == 255):
                print(f"Pixel value at({xValue + 1},{yValue+1}) : {binary_sun[xValue + 1, yValue +1]}")
                sun_image[xValue + 1, yValue + 1] = (255, 0, 0)
                xValue += 1
                yValue += 1
                return 1
            else:
                direction = (direction + 1) % 8
                continue

        if(direction == 2):
            if(binary_sun[xValue, yValue + 1] == 255):
                print(f"Pixel value at({xValue},{yValue+1}) : {binary_sun[xValue, yValue +1]}")
                sun_image[xValue, yValue + 1] = (255, 0, 0)
                yValue += 1
                return 2
            else:
                direction = (direction + 1) % 8
                continue

        if(direction == 3):
            if(binary_sun[xValue - 1, yValue + 1] == 255):
                print(f"Pixel value at({xValue - 1},{yValue+1}) : {binary_sun[xValue - 1, yValue +1]}")
                sun_image[xValue - 1, yValue + 1] = (255, 0, 0)
                xValue -= 1
                yValue += 1
                return 3
            else:
                direction = (direction + 1) % 8
                continue

        if(direction == 4):
            if(binary_sun[xValue - 1, yValue] == 255):
                print(f"Pixel value at({xValue - 1},{yValue}) : {binary_sun[xValue - 1, yValue]}")
                sun_image[xValue - 1, yValue] = (255, 0, 0)
                xValue -= 1
                return 4
            else:
                direction = (direction + 1) % 8
                continue

        if(direction == 5):
            if(binary_sun[xValue - 1, yValue - 1] == 255):
                print(f"Pixel value at({xValue - 1},{yValue-1}) : {binary_sun[xValue - 1, yValue -1]}")
                sun_image[xValue - 1, yValue - 1] = (255, 0, 0)
                xValue -= 1
                yValue -= 1
                return 5
            else:
                direction = (direction + 1) % 8
                continue

        if(direction == 6):
            if(binary_sun[xValue, yValue - 1] == 255):
                print(f"Pixel value at({xValue},{yValue-1}) : {binary_sun[xValue, yValue -1]}")
                sun_image[xValue, yValue - 1] = (255, 0, 0)
                yValue -= 1
                return 6
            else:
                direction = (direction + 1) % 8
                continue

        if(direction == 7):
            if(binary_sun[xValue + 1, yValue - 1] == 255):
                print(f"Pixel value at({xValue + 1},{yValue-1}) : {binary_sun[xValue + 1, yValue -1]}")
                sun_image[xValue + 1, yValue - 1] = (255, 0, 0)
                xValue += 1
                yValue -= 1
                return 7
            else:
                direction = (direction + 1) % 8
                continue
   
def DetectBoundary(xValue, yValue, sun_image, binary_sun):
    sun_image[xValue, yValue] = (255, 0, 0)
    originalXPos = xValue
    originalYPos = yValue
    direction = 7
    count = 0
    while True: 
        if(direction % 2 == 0):
            direction = (direction + 7) % 8
        else:
            direction = (direction + 6) % 8
        
        print(f"before first iteration : {direction}")
        direction = HighlightBoundary(direction, sun_image, binary_sun, xValue, yValue)
        #print(direction.type()) #testing
        print(f"returned direction: {direction}")
        count = count + 1
        if(count == 5):
            break
    
    display_image("Boundary", sun_image)

        

sun_image = cv2.imread("images/sun_image_3.jpg")
cv2.imshow("Original Image", sun_image)
cv2.waitKey(0)

grayscale_sun = cv2.cvtColor(sun_image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale sun image", grayscale_sun)
cv2.waitKey(0)

(min_intensity, max_intensity, min_loc, max_loc) = cv2.minMaxLoc(grayscale_sun)
print(f"Max intensity: {max_intensity} & Min intensity: {min_intensity}")
print(f"Max intensity Location: {max_loc} & Min intensity Location: {min_loc}")
sun_image[min_loc[1], min_loc[0]] = (0, 0, 0)
sun_image = cv2.circle(sun_image, max_loc, 20, (0, 0, 0), thickness = 0)
display_image("Max Intensity", sun_image)

width = sun_image.shape[1]
height = sun_image.shape[0]

for row in range(height-1):
    for col in range(width-1):
        if (grayscale_sun[row, col] <= max_intensity - 10):
            grayscale_sun[row, col] = 0
        else:
            grayscale_sun[row, col] = 255

binary_sun = grayscale_sun
cv2.imwrite("D:\BE Project\Codes\Border Tracing Algorithm\BinaryThresholdImage.bmp", binary_sun)
display_image("Binary Image", binary_sun)

for row in range(height-1):
    for col in range(width-1):
        if (binary_sun[row, col] == 255):
            break
    if (binary_sun[row, col] == 255):
        print(row)
        print(col)
        xValue = row
        yValue = col
        DetectBoundary(xValue, yValue, sun_image, binary_sun)
        #print(f"Binary value at ({row},{col}) : {binary_sun[row-5,col-5]}")
        break

cv2.destroyAllWindows()
