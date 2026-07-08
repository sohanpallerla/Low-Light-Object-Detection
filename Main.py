import numpy as np
import cv2 as cv
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from ObjectDetection import detectObject, displayImage
from gtts import gTTS
from playsound import playsound
from threading import Thread

global class_labels
global cnn_model
global cnn_layer_names
playcount = 0

# GUI related functions
def selectImage():
    filename = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
    if filename:
        detectFromImage(filename)

def selectVideo():
    filename = filedialog.askopenfilename(title="Select a Video", filetypes=[("Video Files", "*.mp4;*.avi;*.mov")])
    if filename:
        detectFromVideo(filename)

def startDetectionFromVideo():
    detectFromVideo()

def deleteDirectory():
    filelist = [ f for f in os.listdir('play') if f.endswith(".mp3") ]
    for f in filelist:
        os.remove(os.path.join('play', f))

def speak(data, playcount):
    class PlayThread(Thread):
        def __init__(self, data, playcount):
            Thread.__init__(self)
            self.data = data
            self.playcount = playcount
        def run(self):
            t1 = gTTS(text=self.data, lang='en', slow=False)
            t1.save("play/"+str(self.playcount)+".mp3")
            playsound("play/"+str(self.playcount)+".mp3")

    newthread = PlayThread(data, playcount)
    newthread.start()

import cv2 as cv
from tkinter import messagebox

def loadLibraries():
    global class_labels
    global cnn_model
    global cnn_layer_names
    try:
        # Correct path to labels file
        class_labels = open('model/yolov3-labels').read().strip().split('\n')

        # Correct absolute path to YOLOv3 config and weights
        cnn_model = cv.dnn.readNetFromDarknet('model/yolov3.cfg', 
                                              'model/yolov3.weights')
        # Dataset paths
        COCO_PATH = "datasets/coco_samples/"
        EXDARK_PATH = "datasets/exdark/"

        # Flag to choose dataset
        USE_EXDARK = True   # change to False for normal images
        def enhance_low_light(image):
           hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
           h, s, v = cv.split(hsv)
           v = cv.equalizeHist(v)
           final = cv.merge((h, s, v))
           return cv.cvtColor(final, cv.COLOR_HSV2BGR)



        cnn_layer_names = cnn_model.getLayerNames()
        cnn_layer_names = cnn_model.getUnconnectedOutLayersNames()

        messagebox.showinfo("Info", "Libraries Loaded Successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Error loading libraries: {str(e)}")

def detectFromImage(imagename):
    label_colors = np.random.randint(0, 255, size=(len(class_labels), 3), dtype='uint8')
    try:
        image = cv.imread(imagename)
        if image is None:
            raise Exception("Invalid image path or file not found")
        
        image_height, image_width = image.shape[:2]
        
        image, _, _, _, _ = detectObject(cnn_model, cnn_layer_names, image_height, image_width, image, label_colors, class_labels)
        displayImage(image)
    
    except Exception as e:
        messagebox.showerror("Error", f"Error processing image: {str(e)}")


def detectFromVideo(video_source=0):
    global playcount
    label_colors = np.random.randint(0, 255, size=(len(class_labels), 3), dtype='uint8')
    try:
        video = cv.VideoCapture(video_source)
        frame_height, frame_width = None, None
    except:
        raise 'Unable to load video'
    finally:
        while True:
            frame_grabbed, frames = video.read()
            if not frame_grabbed:
                break
            if frame_width is None or frame_height is None:
                frame_height, frame_width = frames.shape[:2]
            frames, cls, _, _, _, _ = detectObject(cnn_model, cnn_layer_names, frame_height, frame_width, frames, label_colors, class_labels)
            data = ""
            if len(cls) > 0:
                for i in range(len(cls)):
                    data += cls[i] + ","
            cv.imshow("Detected Objects", frames)
            if len(cls) > 0:
                speak("Detected Objects = " + data, playcount)
                playcount += 1
            if cv.waitKey(5) & 0xFF == ord('q'):
                break

# GUI Setup
root = tk.Tk()
root.title("Object Detection GUI")
root.geometry("400x300")

load_button = tk.Button(root, text="Load YOLO Model", command=loadLibraries)
load_button.pack(pady=10)


video_live_button = tk.Button(root, text="Start Live Video Detection", command=startDetectionFromVideo)
video_live_button.pack(pady=10)

quit_button = tk.Button(root, text="Quit", command=root.quit)
quit_button.pack(pady=10)

root.mainloop()
