import cv2
import numpy as np
from math import sqrt, log10

img = cv2.imread("testimage.png", 0)
ref = cv2.equalizeHist(img)

# Twilight Factor
mean = np.mean(img)
std = np.std(img)
twilight = sqrt(mean * std)

# SNR
signal = np.mean(img)
noise = np.std(img)
snr = 20 * log10(signal / noise) if noise != 0 else 0

# PSNR
mse = np.mean((img - ref) ** 2)
psnr = 10 * log10((255 ** 2) / mse) if mse != 0 else 0

# Relative Brightness
brightness = np.mean(img) / 255

print("\n--- Low Light Image Metrics (YOLOv3 Input) ---")
print(f"Twilight Factor     : {twilight:.2f}")
print(f"SNR (dB)            : {snr:.2f}")
print(f"PSNR (dB)           : {psnr:.2f}")
print(f"Relative Brightness : {brightness:.2f}")
