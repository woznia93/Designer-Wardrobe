import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import openai
import requests
import random

openai.api_key = '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'

class ImageLabelingApp:
    def __init__(self, root, image_folders):
        self.root = root
        self.root.title("Clothing Suggestion App")

        # Shuffle the order of folders
        self.image_folders = image_folders
        random.shuffle(self.image_folders)
        self.image_files_list = []  # List to store lists of image files from different folders
        self.current_folder_index = 0

        # Load image files from all folders and shuffle them individually
        for folder in self.image_folders:
            image_files = [f for f in os.listdir(folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
            random.shuffle(image_files)
            self.image_files_list.append(image_files)

        self.current_image_indices = [0] * len(self.image_folders)
        self.images = []  # List to store ImageTk.PhotoImage objects
        self.selected_outfits = []  # List to store outfits that the user has selected with "Yes" response

        self.label = ttk.Label(root)
        self.label.pack(padx=10, pady=10)

        button_frame_height = 50  # Adjust this value to control the height of the button frame

        self.button_yes = ttk.Button(root, text="Yes", command=self.label_yes)
        self.button_yes.pack(side=tk.LEFT, padx=5, pady=(0, button_frame_height))

        self.button_no = ttk.Button(root, text="No", command=self.label_no)
        self.button_no.pack(side=tk.RIGHT, padx=5, pady=(0, button_frame_height))

        self.load_image()

    def load_image(self):
        if all(index < len(images) for index, images in zip(self.current_image_indices, self.image_files_list)):
            images_in_folder = []
            for folder_index, current_index in enumerate(self.current_image_indices):
                folder_images = self.image_files_list[folder_index]

                if current_index < len(folder_images):
                    image_path = os.path.join(self.image_folders[folder_index], folder_images[current_index])
                    img = Image.open(image_path)
                    img = img.resize((150, 150), resample=Image.LANCZOS)  # Adjusted image size
                    images_in_folder.append(img)

            if images_in_folder:
                # Concatenate images vertically to create a composite image
                composite_img = Image.new('RGB', (150, 450))  # Adjusted composite image size
                for i, img in enumerate(images_in_folder):
                    composite_img.paste(img, (0, i * 150))

                self.images.append(composite_img)

                # Convert the composite image to Tkinter PhotoImage
                self.tk_image = ImageTk.PhotoImage(composite_img)

                # Update the label with the composite image
                self.label.config(image=self.tk_image, text=f"Images {', '.join(str(index + 1) for index in self.current_image_indices)}")
            else:
                self.label.config(image=None, text="No more outfits can be made")
                self.button_yes.config(state=tk.DISABLED)
                self.button_no.config(state=tk.DISABLED)
        else:
            self.label.config(image=None, text="No more images in any category")
            self.button_yes.config(state=tk.NORMAL)
            self.button_no.config(state=tk.NORMAL)

    def label_yes(self):
        print(f"Images {', '.join(str(index + 1) for index in self.current_image_indices)}: Yes")
        self.selected_outfits.append([
            os.path.join(self.image_folders[i], self.image_files_list[i][min(index, len(self.image_files_list[i]) - 1)])
            for i, index in enumerate(self.current_image_indices)
        ])
        self.next_image()

    def label_no(self):
        print(f"Images {', '.join(str(index + 1) for index in self.current_image_indices)}: No")
        self.next_image()

    def next_image(self):
        for i in range(len(self.current_image_indices)):
            self.current_image_indices[i] += 1

        # Check if there are more images to display in any category
        if any(index < len(images) for index, images in zip(self.current_image_indices, self.image_files_list)):
            self.load_image()
        else:
            # If all images have been displayed, generate an outfit using DALL·E based on selected outfits
            self.generate_outfit()

    def generate_outfit(self):
        if not self.selected_outfits:
            self.label.config(text="No outfits selected.")
            return

        # Flatten the list of selected outfits
        selected_items = [item for sublist in self.selected_outfits for item in sublist]

        # Use the selected items to make a request to the DALL·E API
        prompt = f"Create an outfit similar to these items on a person: {', '.join(selected_items)}"
        response = openai.Image.create(
            prompt=prompt,
            n=1  # Number of responses to generate
        )

        # Retrieve the generated image URL from the API response
        generated_image_url = response['data'][0]['url']

        # Display the generated image
        generated_img = Image.open(requests.get(generated_image_url, stream=True).raw).resize((300, 300),
                                                                                              resample=Image.LANCZOS)
        self.tk_image = ImageTk.PhotoImage(generated_img)
        self.label.config(image=self.tk_image, text="Generated Outfit")

        # Disable the "Yes" and "No" buttons
        self.button_yes.config(state=tk.DISABLED)
        self.button_no.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x550")  # Set the window size to 300x500

    # Replace 'your_image_folders' with a list of paths to folders containing your images
    app = ImageLabelingApp(root, ["C:/Users/mlgma/Desktop/shirts", "C:/Users/mlgma/Desktop/pants", "C:/Users/mlgma/Desktop/shoes"])

    root.mainloop()
