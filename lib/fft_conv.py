import numpy as np
import cv2

class get_fft:
    def __init__(self, img_data, val=0):
        self.img_data = img_data
        self.val = val

    def fft_img(self):
        # Apply the FFT
        fft = np.fft.fft2(self.img_data)
        fft_shift = np.fft.fftshift(fft)
        return fft_shift
    
    def fft_spectrum(self):
        # Analyze the Spectrum
        magnitude_spectrum = np.abs(self.fft_img())
        log_magnitude_spectrum = np.log1p(magnitude_spectrum)  # Apply logarithm for better visualization
        return magnitude_spectrum, log_magnitude_spectrum
    
    def fft_mask(self):
        # Detect Object Edges
        # Create a high-pass filter mask
        rows, cols = self.img_data.shape
        center_row, center_col = rows // 2, cols // 2
        mask = np.ones((rows, cols), np.uint8)
        mask[center_row-rows//self.val:center_row+rows//self.val, center_col-cols//self.val:center_col+cols//self.val] = 0  # Customize filter size
        return mask
    
    def fft_filter(self):
        filtered_spectrum = self.fft_img() * self.fft_mask()
        filtered_image = np.fft.ifft2(np.fft.ifftshift(filtered_spectrum)).real

        # Statistical Analysis
        gradient_x = cv2.Sobel(filtered_image, cv2.CV_64F, 1, 0, ksize=3)
        gradient_y = cv2.Sobel(filtered_image, cv2.CV_64F, 0, 1, ksize=3)
        gradient_magnitude = np.sqrt(gradient_x**2 + gradient_y**2)

        # Thresholding to obtain binary image
        threshold = 100  # Adjust the threshold value as needed
        edges_binary = np.uint8(gradient_magnitude > threshold) * 255
        return filtered_image, gradient_magnitude, edges_binary
    

