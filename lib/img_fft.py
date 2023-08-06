import tkinter as tk
from tkinter import filedialog
from pdf2image import convert_from_path
from PIL import Image
import img2pdf


def convert_pdf_to_png():
    # Ask user to select a PDF file
    pdf_file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    
    if pdf_file_path:
        # Convert PDF to a list of PIL images
        images = convert_from_path(pdf_file_path)

        # Save each image as a PNG file
        for i, image in enumerate(images):
            image.save(f"output_{i}.png")

        status_label.config(text="Conversion successful!")

def convert_png_to_pdf():
    # Ask user to select PNG files
    png_files_path = filedialog.askopenfilenames(filetypes=[("PNG Files", "*.png")])

    if png_files_path:
        # Create a list to store PIL images
        images = []

        # Open and append each PNG image to the list
        for png_file_path in png_files_path:
            image = Image.open(png_file_path)
            images.append(image)

        # Save the list of images as a PDF file
        with open("output.pdf", "wb") as pdf_file:
            pdf_file.write(img2pdf.convert(images))

        status_label.config(text="Conversion successful!")

# Create the main window
window = tk.Tk()
window.title("PDF to PNG Converter")
window.geometry("240x200")
# Create the buttons
pdf_to_png_button = tk.Button(window, text="Convert PDF to PNG", command=convert_pdf_to_png)
pdf_to_png_button.pack()

png_to_pdf_button = tk.Button(window, text="Convert PNG to PDF", command=convert_png_to_pdf)
png_to_pdf_button.pack()

# Create the status label
status_label = tk.Label(window, text="")
status_label.pack()

# Start the GUI event loop
window.mainloop()
