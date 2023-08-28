import tkinter as tk
from tkinter import Label
import sys, os, glob, time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image

sys.path.append(os.path.dirname('/Users/User_Linux/OneDrive/Documents/Programs Code/Python/FT_Analysis/images'))
os.chdir('/Users/User_Linux/OneDrive/Documents/Programs Code/Python/FT_Analysis/images')
#os.chdir('/home/komputer/googledrive_Raven/FT_Analysis/images')

from data import*
from etc import*

screen_size = "1366x768"
root = tk.Tk()
root.title("Data Processing")
root.geometry(screen_size)

file_list = sorted(glob.glob('*.JPG'))

class Window:
    def __init__(self, master):
        self.master = master
        self.properties()
        self.main_window()
    
    def properties(self):
        #Frame2 position
        self.posbel_x = 0.84
        self.postry_x = 0.89

        self.pos_yinput = 0.01
        self.distance = 0.07

        #Frame3 Details
        self.fg1 = "black"
        self.green_color = "#30bd09"
        self.font1 = ('Times New Roman', 11, 'bold')
        self.font2 = ('Times New Roman', 11)

    def get_data(self):
        pass

    def loading_process(self):
        total_length = eval(screen_size[:4])  # Total length of the loading bar
        # Create a progress bar
        self.progress_bar = tk.Canvas(root, width=total_length, height=20, bg="white")
        self.progress_bar.pack(side=tk.BOTTOM)

        # Loading label
        self.loading_label = tk.Label(root, text="Processing...", font=("Arial", 12))
        self.loading_label.pack(side=tk.BOTTOM)

        #input part
        location = (self.location_entry)
        time_zone = [self.time_entry]
        date = [self.date_entry]
        ar_peak = []
        elvt = []
        c = []

        i = 0
        for file in file_list:
            i += 1
            progress = int((i / len(file_list)) * total_length)
            self.progress_bar.delete("progress")
            self.progress_bar.create_rectangle(0, 0, progress, 20, fill=self.green_color, tags="progress")
            percent = int((i / len(file_list)) * 100)
            root.title(f"Loading... {percent}% complete")
            root.update()  # Update the window
            time.sleep(0.01)
        root.title("Complete!")
        self.loading_label.destroy()

        self.x = [1,2,3,4,5]
        self.y1 = [1,2,3,4,5]
        self.y2 = [1,2,3,4,5]
        self.y3 = [1,2,3,4,5]

    def plot_data(self):
        #initial input data
        x = self.x
        y1 = self.y1 # get_all_value(img_type_input)
        y2 = self.y2
        y3 = self.y3
        
        # Create a figure and axes
        fig, ax = plt.subplots()
        
        # Plot the data
        ax.plot(x, y1, label='Data RGB')
        ax.plot(x, y2, label='Data HSV')
        ax.plot(x, y3, label='Data FT')
        
        # Set the title and labels
        ax.set_title("Grafik Perbandingan Data")
        ax.set_xlabel("Altitude")
        ax.set_ylabel("Value")
        
        # Add a legend
        ax.legend()
        
        # Create a Tkinter canvas and display the plot
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().place(x=0, y=0, relwidth=0.82, relheight=0.87)


    def data_details(self):
        data = [
            f"Total Files : {len(file_list)}",
            f"Image Size : {Image.open(file_list[0]).size}",
            f"Average Size : {len(file_list)}"
        ]

        for idx, detail in enumerate(data, start=5):
            label = Label(root, text=detail, font=self.font2, fg=self.fg1)
            label.place(relx=self.posbel_x, rely=self.pos_yinput+(self.distance*idx))

    def button_clicked(self):
        self.process_button.config(state="disable")
        self.process_button.config(bg="white")
        self.loading_process()
        if self.progress_bar is not None:
            self.progress_bar.destroy()
            self.progress_bar = None
        self.process_button.config(state="normal")
        self.process_button.config(bg=self.green_color)
        root.title("Complete")
        self.plot_data()

        self.data_details()

    def main_window(self):
        #1st frame, plot

        # Create the input fields and process button on the right
        location_label = tk.Label(root, text="Location :")
        location_label.place(relx=self.posbel_x, rely=self.pos_yinput+self.distance)
        self.location_entry = tk.Entry(root)
        self.location_entry.place(relx=self.postry_x, rely=self.pos_yinput+self.distance)

        date_label = tk.Label(root, text="Date :")
        date_label.place(relx=self.posbel_x, rely=self.pos_yinput+(self.distance*2))
        self.date_entry = tk.Entry(root)
        self.date_entry.place(relx=self.postry_x, rely=self.pos_yinput+(self.distance*2))

        time_label = tk.Label(root, text="Time :")
        time_label.place(relx=self.posbel_x, rely=self.pos_yinput+(self.distance*3))
        self.time_entry = tk.Entry(root)
        self.time_entry.place(relx=self.postry_x, rely=self.pos_yinput+(self.distance*3))

        self.process_button = tk.Button(root, text="Process", bg=self.green_color, command=self.button_clicked)
        self.process_button.place(relx=self.posbel_x, rely=self.pos_yinput+(self.distance*4), relwidth=0.143, relheight=0.05)

        #3rd frame, Details


Window(root)
root.protocol("WM_DELETE_WINDOW", root.quit)

# Start the Tkinter event loop
root.mainloop()
