
import numpy as np
from PIL import Image

class get_rgb:
    def __init__(self,image):
        self.image = np.array(Image.open(image))
        
    def get_r(self):
        r_channel = self.image[:,:,0]
        return r_channel
    
    def get_g(self):
        g_channel = self.image[:,:,1]
        return g_channel
    
    def get_b(self):
        b_channel = self.image[:,:,2]
        return b_channel

class get_hsv:
    def __init__(self, image):
        img = Image.open(image)
        hsv_image = img.convert('HSV')
        self.image = np.array(hsv_image)
        
    def get_h(self):
        h_channel = self.image[:,:,0]
        return h_channel
    
    def get_s(self):
        s_channel = self.image[:,:,1]
        return s_channel
    
    def get_v(self):
        v_channel = self.image[:,:,2]
        return v_channel




