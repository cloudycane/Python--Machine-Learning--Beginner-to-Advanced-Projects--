
from tkinter import * #Tkinter as  the GUI of our program
import PIL
from PIL import Image, ImageTk, ImageFilter, UnidentifiedImageError #Image Tkinter
import cv2 #OpenCV for image processing - as the backbone of our software
import numpy as np
from tkinter.filedialog import askopenfilename
from tkinter import messagebox



window = Tk()
window.title("Image Manipulation")

window.minsize(width=380, height=20)


load = Image.open("../flower1.jpg")
render = ImageTk.PhotoImage(load)


def gray():
    img_path = askopenfilename()
    im = Image.open(img_path)

    image = np.asarray(im)
    # loading and reading the image
    #image = img
    #convert the color to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #display the image
    cv2.imshow("Image in GrayScale",gray)
    #keep the window open until any key is pressed
    cv2.waitKey(0)
    #clears all the window buffers
    cv2.destroyAllWindows()

def hsv():
    img_path = askopenfilename()
    im = Image.open(img_path)

    image = np.asarray(im)
    #convert the color to hsv
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    cv2.imshow("Image in HSV", hsv)
    # keep the window open until any key is pressed
    cv2.waitKey(0)
    # clears all the window buffers
    cv2.destroyAllWindows()

def hls():
    img_path = askopenfilename()
    im = Image.open(img_path)

    image = np.asarray(im)
    # convert the color to hsv
    hls = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)
    cv2.imshow("Image in HLS", hls)
    # keep the window open until any key is pressed
    cv2.waitKey(0)
    # clears all the window buffers
    cv2.destroyAllWindows()

def aerochrome():
    img_path = askopenfilename()
    im = Image.open(img_path)

    image = np.asarray(im)

    img_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    hue_image = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)
    cv2.imshow("Idk", hue_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def equalizer():
    img_path = askopenfilename()
    im = Image.open(img_path)

    gray = np.asarray(im)
    grayscale = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
    gray_eq = cv2.equalizeHist(grayscale)
    hist, bins = np.histogram(gray_eq, 256, [0, 255])
    im = Image.open(img_path)
    im_color = np.asarray(im)
    hsv = cv2.cvtColor(im_color, cv2.COLOR_BGR2HSV)
    hsv[..., 2] = cv2.equalizeHist(hsv[..., 2])
    color_eq = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)


    cv2.imshow("Idk", color_eq)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def myfilter():
    img_path = askopenfilename()
    im = Image.open(img_path)
    im_array = np.asarray(im)
    color_im = cv2.cvtColor(im_array, cv2.COLOR_BGR2RGB)

    KSIZE= 11
    ALPHA = 2

    kernel = cv2.getGaussianKernel(KSIZE, 0)
    kernel = -ALPHA * kernel @ kernel.T
    kernel[KSIZE//2, KSIZE//2] += 1 + ALPHA

    filtered = cv2.filter2D(color_im, -1, kernel)

    cv2.imshow("Idk", filtered)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


button = Button(text="Grayscale", command=gray)
button.grid(column=0,row=1)
button1 = Button(text="HSV colors", command=hsv)
button1.grid(column=1,row=1)
button2 = Button(text="HLS colors", command=hls)
button2.grid(column=2,row=1)
button3 = Button(text="aerochrome", command=aerochrome)
button3.grid(column=3, row=1)
button4 = Button(text="equalizer", command=equalizer)
button4.grid(column=4, row=1)
button5 = Button(text="sharpen", command=myfilter)
button5.grid(column=5, row=1)

label = Label(text="Use the filters below to manipulate your images.", font=("Arial", 9, "bold"))
label.grid(column=2, row=0)


window.mainloop()