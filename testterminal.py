print("PROGRAM STARTED")

import cv2
print("OpenCV imported")

cap = cv2.VideoCapture(0)
print("Camera object created")

if not cap.isOpened():
    print("❌ Camera not opened")
else:
    print("✅ Camera opened successfully")

ret, frame = cap.read()
print("Frame read result:", ret)

if ret:
    print("Frame shape:", frame.shape)
    cv2.imshow("Test Frame", frame)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()

cap.release()
print("PROGRAM ENDED")
