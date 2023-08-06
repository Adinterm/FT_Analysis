
import numpy as np

class get_graph:
    def __init__(self, data_array):
        self.data_ar = data_array
        
    def get_hist(self):
        array_dat = self.data_ar

        # Perform FFT
        f = np.fft.fft2(array_dat)
        fshift = np.fft.fftshift(f)

        # Calc power spectrum
        magnitude_spectrum = 20*np.log(np.abs(fshift))

        # Compute the histogram
        # plt.hist(magnitude_spectrum.flatten(), bins=256)
        hist, bins = np.histogram(magnitude_spectrum.flatten(), bins=256)
        return hist, bins
    
    def get_freq(self): #Graph

        f = np.fft.fft2(self.data_ar)
        fshift = np.fft.fftshift(f)

        # Compute the magnitude spectrum and take the absolute value
        magnitude_spectrum = 20 * np.log(np.abs(fshift))

        # Get the frequency values for rows and columns
        rows, cols = self.data_ar.shape
        freq_rows = np.fft.fftfreq(rows, d=1)
        freq_cols = np.fft.fftfreq(cols, d=1)
        freq_rows = np.fft.fftshift(freq_rows)
        freq_cols = np.fft.fftshift(freq_cols)

        # Get the positive frequency values along the rows and columns
        freq_rows_pos = freq_rows[:rows//2+1]
        freq_cols_pos = freq_cols[:cols//2+1]
        magnitude_spectrum_pos = magnitude_spectrum[:rows//2+1, :cols//2+1]

        mag_spect = magnitude_spectrum_pos.mean(axis=0)
        # Plot the magnitude of the positive frequency values along the x-axis, and the corresponding frequency values along the y-axis
        # Freq, Mag
        return freq_cols_pos, mag_spect

