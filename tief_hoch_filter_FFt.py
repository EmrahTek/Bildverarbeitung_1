import numpy as np
import cv2 as cv

img = cv.imread("/home/emrahtek/Schreibtisch/CodeLab/Python_tutorial/Bildverarbeitung/Photos/cat.jpg", cv.IMREAD_GRAYSCALE).astype(np.float32)

# FFT
F = np.fft.fft2(img)
Fshift = np.fft.fftshift(F)

rows, cols = img.shape
crow, ccol = rows//2, cols//2
D0 = 40  # cutoff radius

Y, X = np.ogrid[:rows, :cols]
dist2 = (Y - crow)**2 + (X - ccol)**2

# Low-pass mask (circular)
mask_lp = dist2 <= D0**2
mask_lp = mask_lp.astype(np.float32)

# Apply low-pass
Gshift_lp = Fshift * mask_lp
G_lp = np.fft.ifftshift(Gshift_lp)
img_lp = np.fft.ifft2(G_lp).real

# High-pass mask = 1 - low-pass
mask_hp = 1.0 - mask_lp
Gshift_hp = Fshift * mask_hp
G_hp = np.fft.ifftshift(Gshift_hp)
img_hp = np.fft.ifft2(G_hp).real