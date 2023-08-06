import math, glob, os
from PIL import Image
import metadata, altitude
from PIL.ExifTags import TAGS
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
import numpy as np


class get_data:
    def __init__(self, ):
        files = sorted(glob.glob('*.JPG'))

        #fft image
    def fft_img(imgpath): 
        imr = plt.imread(imgpath)
        fft_img = np.fft.fftshift(np.fft.fft2(rgb2gray(imr)))
        return np.array(fft_img)

        #highest value from an array
    def get_peak(array):
        peak_ar = np.array(array)
        axis = peak_ar.shape[1]
        axis2 = int(axis/2)
        axisy = peak_ar[:,axis2]
        ir_1 = [0]
        for i in range(0,len(axisy)):
            if ir_1 < axisy[i]:
                ir_1 = axisy[i]
        return ir_1

        #get time from image metadata
    def get_time(img):
        metadata.get_time(img)

    def sunpos(when, location, refraction):
        altitude.sunpos(when, location, refraction)

    def into_range(x, range_min, range_max):
        shiftedx = x - range_min
        delta = range_max - range_min
        return (((shiftedx % delta) + delta) % delta) + range_min

    def center_rc(img,rc):    #use (image array, [0 = row, 1 = column])
        peak_ar = np.array(img)
        edge = peak.shape[rc]
        edge2 = edge/2
        if rc == 0:
            peak_rc = peak_ar[edge2,:]
        if rc == 1:
            peak_rc = peak_ar[:,edge2]
        ir_1 = [0]
        for i in range(0,len(peak_rc)):
            if ir_1 < peak_rc[i]:
                ir_1 = peak_rc[i]
        return ir_1

    def get_peak_rc(img,rc):    #use (image array, [0 = row, 1 = column])
        peak_ar = np.array(img)
        edge = rc
        if rc == 0:
            peak_rc = peak_ar[edge2,:]
        if rc == 1:
            peak_rc = peak_ar[:,edge2]
        ir_1 = [0]
        for i in range(0,len(peak_rc)):
            if ir_1 < peak_rc[i]:
                ir_1 = peak_rc[i]
        return ir_1

    def get_peak_rc(img, rc, rc2):
        peak_ar = np.array(img)
        if rc == 0:
            peak_rc = peak_ar[rc2,:]
        if rc == 1:
            peak_rc = peak_ar[:,rc2]
        ir_1 = [0]
        for i in range(0, len(peak_rc)):
            if ir_1 < peak_rc[i]:
                ir_1 = peak_rc[i]
        return ir_1

    def get_peak_rc(img):
        for i in range(0, len(img.shape[0])):
            get_row = peak_rc(img,0,i)
        print("Length row = {}".format(len(img.shape[0])))
        
        for i in range(0, len(img.shape[1])):
            get_column = peak_rc(img,1,i)
        print("Length column = {}".format(len(img.shape[1])))
        return get_row, get_column

import sys
sys.exit()

if __name__ == "__main__":
    location = (-6.832327, 107.618571)
    time_zone = [7]
    date = [2018, 4, 24]
    ar_peak = []
    elvt = []
    c = []

for i in range(0,len(files)):
    fft_image = fft_img(files[i])
    peak = get_peak(fft_image)
    ar_peak = ar_peak+[peak]
    #time
    gt_time = get_time(files[i])
    gt_time = gt_time[11:19]
    gt_time = gt_time.split(":")
    tm = [int(x) for x in gt_time]
    tm_lst = date + tm + time_zone
    when = tuple(tm_lst)
    #elevation
    sunp = sunpos(when, location, True)
    elvt = elvt + [sunp[1]]
