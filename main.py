from roboflow import Roboflow
import tkinter as tk
from tkinter import filedialog, ttk
from PIL import Image, ImageTk
import os
import json


class VarroaDetectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Varroa Detector")

        # Roboflow initialization
        rf = Roboflow(api_key="BON0iyZLT9NILB2g5muV")
        self.project = rf.workspace().project("varroa-detector-znvpp")
        self.model = self.project.version(1).model

        # Variables
        self.current_image_path = None
        self.dataset_path = "dataset"

        # Interface
        self.create_widgets()
        self.load_dataset_images()

    def create_widgets(self):
        # Image list
        self.listbox_frame = ttk.Frame(self.root)
        self.listbox_frame.pack(side=tk.LEFT, padx=10, pady=10)

        self.listbox_label = ttk.Label(self.listbox_frame, text="Available Images:")
        self.listbox_label.pack()

        self.listbox = tk.Listbox(self.listbox_frame, width=40, height=20)
        self.listbox.pack()
        self.listbox.bind('<<ListboxSelect>>', self.on_select_image)

        # Preview and results
        self.preview_frame = ttk.Frame(self.root)
        self.preview_frame.pack(side=tk.LEFT, padx=10, pady=10)

        self.preview_label = ttk.Label(self.preview_frame, text="Preview:")
        self.preview_label.pack()

        self.image_label = ttk.Label(self.preview_frame)
        self.image_label.pack()

        self.analyze_button = ttk.Button(self.preview_frame, text="Analyze", command=self.analyze_image)
        self.analyze_button.pack(pady=10)

        self.result_label = ttk.Label(self.preview_frame, text="")
        self.result_label.pack()

    def load_dataset_images(self):
        if os.path.exists(self.dataset_path):
            image_files = [f for f in os.listdir(self.dataset_path) if f.endswith(('.jpg', '.jpeg', '.png'))]
            for image_file in image_files:
                self.listbox.insert(tk.END, image_file)

    def on_select_image(self, event):
        if self.listbox.curselection():
            filename = self.listbox.get(self.listbox.curselection())
            self.current_image_path = os.path.join(self.dataset_path, filename)
            self.show_preview()

    def show_preview(self):
        # Display image preview
        image = Image.open(self.current_image_path)
        # Resize image for preview
        image.thumbnail((300, 300))
        photo = ImageTk.PhotoImage(image)
        self.image_label.configure(image=photo)
        self.image_label.image = photo

    def analyze_image(self):
        if self.current_image_path:
            # Prediction
            prediction = self.model.predict(self.current_image_path, confidence=20, overlap=25)

            # Get number of detections
            predictions_json = prediction.json()
            num_detections = len(predictions_json['predictions'])

            # Save image with predictions
            output_path = "prediction.jpg"
            prediction.save(output_path)

            # Display result with number of detections
            result_text = f"Analysis completed!\nNumber of varroa detected: {num_detections}\nResults saved in: {output_path}"
            self.result_label.configure(text=result_text)

            # Wait a bit for the file to be properly saved
            self.root.after(500, lambda: self.show_result(output_path, num_detections))

    def show_result(self, output_path, num_detections):
        try:
            result_image = Image.open(output_path)
            # Create new window for result
            result_window = tk.Toplevel(self.root)
            result_window.title(f"Detection Result - {num_detections} varroa(s) detected")

            # Create frame to contain image and information
            main_frame = ttk.Frame(result_window)
            main_frame.pack(padx=10, pady=10)

            # Display detection information
            info_label = ttk.Label(
                main_frame,
                text=f"Total number of varroa detected: {num_detections}",
                font=("Arial", 12, "bold")
            )
            info_label.pack(pady=(0, 10))

            # Resize if image is too large
            max_size = (800, 800)
            result_image.thumbnail(max_size, Image.LANCZOS)

            # Convert to PhotoImage
            photo = ImageTk.PhotoImage(result_image)

            # Create label to display image
            label = ttk.Label(main_frame, image=photo)
            label.image = photo  # Keep a reference!
            label.pack()

        except Exception as e:
            print(f"Error displaying result: {e}")


# Launch application
if __name__ == "__main__":
    root = tk.Tk()
    app = VarroaDetectorApp(root)
    root.mainloop()