import cv2
import numpy as np
import math

# ================= CAMERA SAFE OPEN ================= #

def open_camera():
    backends = [
        cv2.CAP_DSHOW,
        cv2.CAP_ANY,
        0
    ]
    for backend in backends:
        try:
            cap = cv2.VideoCapture(0, backend)
            if cap.isOpened():
                return cap
        except:
            pass
    return None

cap = open_camera()
if cap is None:
    print("❌ Camera could not be opened")
    exit()

# ================= METRICS ================= #

def relative_brightness(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return np.mean(gray)

def snr(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    mean = np.mean(gray)
    std = np.std(gray)
    return mean / (std + 1e-6)

def psnr(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    mse = np.mean((gray - np.mean(gray)) ** 2)
    if mse == 0:
        return 100
    return 20 * math.log10(255.0 / math.sqrt(mse))

def twilight_factor(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return np.mean(gray) * np.std(gray)

# ================= LOAD YOLOv3 ================= #

net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

with open("coco.names") as f:
    classes = f.read().strip().split("\n")

# ================= LIVE LOOP ================= #

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Frame not captured")
        break

    h, w = frame.shape[:2]

    blob = cv2.dnn.blobFromImage(frame, 1/255, (416,416), swapRB=True, crop=False)
    net.setInput(blob)
    outputs = net.forward(output_layers)

    for output in outputs:
        for det in output:
            scores = det[5:]
            class_id = np.argmax(scores)
            conf = scores[class_id]

            if conf > 0.5:
                cx, cy, bw, bh = det[0:4]
                x = int((cx - bw/2) * w)
                y = int((cy - bh/2) * h)
                bw = int(bw * w)
                bh = int(bh * h)

                cv2.rectangle(frame, (x,y), (x+bw, y+bh), (0,255,0), 2)
                cv2.putText(frame, classes[class_id], (x,y-5),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)

    rb = relative_brightness(frame)
    snr_val = snr(frame)
    psnr_val = psnr(frame)
    tf = twilight_factor(frame)

    cv2.putText(frame, f"Brightness: {rb:.2f}", (10,20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)
    cv2.putText(frame, f"SNR: {snr_val:.2f}", (10,40),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)
    cv2.putText(frame, f"PSNR: {psnr_val:.2f}", (10,60),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)
    cv2.putText(frame, f"Twilight Factor: {tf:.2f}", (10,80),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)

    cv2.imshow("YOLOv3 Live Low-Light Metrics", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
