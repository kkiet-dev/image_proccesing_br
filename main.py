import cv2
import os
from tkinter import Tk, filedialog, messagebox

def select_image():
    """Open a file dialog to select an image."""
    Tk().withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff")]
    )
    return file_path

def process_image_to_bw(image_path):
    """Convert the selected image to black and white and save it."""
    try:
        # Read the image
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError("Could not open or find the image.")

        # Convert the image to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Save the processed image
        output_path = os.path.splitext(image_path)[0] + "_bw.jpg"
        cv2.imwrite(output_path, gray_image)

        messagebox.showinfo("Success", f"Image processed and saved at:\n{output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred:\n{e}")

if __name__ == "__main__":
    # Select an image
    image_path = select_image()

    if image_path:
        # Process the image to black and white
        process_image_to_bw(image_path)
    else:
        messagebox.showinfo("Info", "No image was selected.")