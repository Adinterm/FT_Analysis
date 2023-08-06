import sys, os, glob
from data import *
from lib import *
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

sys.path.append(os.path.dirname('/Users/User_Linux/OneDrive/Documents/Programs Code/Python/FT_Analysis/images'))
os.chdir('/Users/User_Linux/OneDrive/Documents/Programs Code/Python/FT_Analysis/images')
import sys, os, glob
from data import *
from data import metadata, altitude
from lib import *
from lib import img, fft_conv
import images
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
os.chdir('/home/komputer/googledrive_Raven/FT_Analysis/images')
# sys.path.append(os.path.dirname('/Users/User_Linux/OneDrive/Documents/Programs Code/Python/FT_Analysis/images'))
# os.chdir('/Users/User_Linux/OneDrive/Documents/Programs Code/Python/FT_Analysis/images')

image_type = 'image.get_r()'#, get_hsv_val()
image_type2 = 'image.get_h()'
file_list = sorted(glob.glob('*.JPG'))

def get_r_data():
    output = []
    for i in file_list:
        image = img.get_rgb(i)
        image_out = image.get_r()
        sum_val = np.sum(image_out)
        output.append(sum_val)
    return output


#get black and white value from fft
def get_two_value(): 
    output = []
    for i in file_list:
        image = img.get_rgb(i)
        input_img_dat = image.get_r() #eval(img_input)
        fft_img = fft_conv.get_fft(input_img_dat, val=100)
        magnitude_spectrum, log_magnitude_spectrum = fft_img.fft_spectrum()
        filtered_image, gradient_magnitude, edge_binary = fft_img.fft_filter()
        sum_val = np.sum(edge_binary)
        output.append(sum_val)
    return output

# the value of black and white of hsv image
def get_all_value():
    output = []
    for i in file_list: 
        image = img.get_hsv(i)
        input_img_dat = image.get_h() #eval(img_input)
        fft_img = fft_conv.get_fft(input_img_dat , val=100)
        magnitude_spectrum, log_magnitude_spectrum = fft_img.fft_spectrum()
        filtered_image, gradient_magnitude, edge_binary = fft_img.fft_filter()
        sum_val = np.sum(log_magnitude_spectrum )
        output.append(sum_val)
    return output

# print(file_list)
# plt.plot(get_all_value(image_type2))
# plt.show()

if __name__ == "__main__":
    location = (-6.832327, 107.618571)
    time_zone = [7]
    date = [2018, 4, 24]
    ar_peak = []
    elvt = []
    c = []
    
    for i in file_list:
        # fft_image = fft_img(i)
        # peak = get_peak(fft_image)
        # ar_peak = ar_peak+[peak]
        #time
        gt_time = metadata.get_time(i)
        gt_time = gt_time[11:19]
        gt_time = gt_time.split(":")
        tm = [int(x) for x in gt_time]
        tm_lst = date + tm + time_zone
        when = tuple(tm_lst)
        #elevation
        sunp = altitude.sunpos(when, location, True)
        elvt = elvt + [sunp[1]]


    def plot_data():
        x = elvt
        #y1 = [] #get_r_data()
        y2 = get_two_value()
        y3 = get_all_value()
        # Plotting the data
        #plt.plot(x, y1, label='Data 1')
        plt.plot(x, y2, label='Data 2')
        plt.plot(x, y3, label='Data 3')

        # Adding labels and title to the plot
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.title('Plotting Three Data Sets')

        # Adding a legend
        plt.legend()

        # Display the plot
        plt.show()

    plot_data()

print("Done!")