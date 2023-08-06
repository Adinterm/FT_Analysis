import matplotlib.pyplot as plt

def spectrum():
    print()


def img_spectrum():
    print("test")
    plt.subplot(2, 2, 1), plt.imshow(image, cmap='gray')
    plt.title('Original Image'), plt.axis('off')

    plt.subplot(2, 2, 2), plt.imshow(log_magnitude_spectrum, cmap='gray')
    plt.title('Magnitude Spectrum'), plt.axis('off')

    plt.subplot(2, 2, 3), plt.imshow(filtered_image, cmap='gray')
    plt.title('Filtered Image'), plt.axis('off')

    plt.subplot(2, 2, 4), plt.imshow(edges_binary, cmap='gray')
    plt.title('Detected Edges'), plt.axis('off')

    plt.tight_layout()
    plt.show()

import sys

def plot_rgb():
    plt.figure(figsize=(12, 4))

    plt.subplot(131)
    plt.imshow(h_channel)
    plt.title('H Channel')

    plt.subplot(132)
    plt.imshow(s_channel, cmap='hsv')
    plt.title('S Channel')

    plt.subplot(133)
    plt.imshow(v_channel, cmap='hsv')
    plt.title('V Channel')

    plt.tight_layout()
    plt.show()

