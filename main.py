import pyautogui
from PIL import Image, ImageGrab
# from numpy import asarray
import time

def hit(key):
    pyautogui.keyDown(key)
    return

# def draw():
    
# def takeScreenShot():
#     # image = ImageGrab.grab()
#     # Conver to Greyscale
#     image = ImageGrab.grab().convert('L')
#     # Show Image
#     # image.show()
#     return image

def isCollide(data):

    for i in range(250, 375):
        for j in range(300,325):
            if data[i, j] < 100:
                hit("down")
                return
            

    for i in range(250, 375):
        for j in range(400,425):
            if data[i, j] < 100:
                hit("up")
                return
    return

if __name__ == "__main__":
    print("Hey.. Dino Game to start in 3 seconds")
    time.sleep(2)
    # hit("up")
    # image = takeScreenShot()
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)

        # if isCollide(data):
        #     hit("up")
        
        
        # print(data)
        # Image as Array
        # print(asarray(image))
        
        # # Draw the rectangle for Cactus
        # for i in range(250, 375):
        #     for j in range(400,425):
        #         # data
        #         # Detect spot
        #         data[i, j] = 0

        # # Draw the rectangle for Birds
        # for i in range(250, 375):
        #     for j in range(300,325):
        #         # data
        #         # Detect spot
        #         data[i, j] = 0

        # image.show()
