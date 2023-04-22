import tkinter as tk
from tkinter import filedialog
import facebook

class FacebookPostApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Facebook Post App")

        # Create page id entry
        self.page_id_label = tk.Label(self, text="Page ID:")
        self.page_id_entry = tk.Entry(self)
        self.page_id_label.grid(row=0, column=0)
        self.page_id_entry.grid(row=0, column=1)

        # Create access token entry
        self.token_label = tk.Label(self, text="Access Token:")
        self.token_entry = tk.Entry(self)
        self.token_label.grid(row=1, column=0)
        self.token_entry.grid(row=1, column=1)

        # Create post message entry
        self.post_label = tk.Label(self, text="Post Message:")
        self.post_entry = tk.Entry(self)
        self.post_label.grid(row=2, column=0)
        self.post_entry.grid(row=2, column=1)

        # Create browse button for image selection
        self.browse_button = tk.Button(self, text="Browse", command=self.browse_files)
        self.browse_button.grid(row=3, column=0)

        # Create post button
        self.post_button = tk.Button(self, text="Post", command=self.post_to_facebook)
        self.post_button.grid(row=3, column=1)

        # Function to browse and select image files
    def browse_files(self):
        self.image_files = filedialog.askopenfilenames(initialdir="/", title="Select Image Files", filetypes=(("jpeg files", "*.jpg"), ("png files", "*.png"), ("all files", "*.*")))
        print("Selected image files:", self.image_files)

    # Function to post message and images to Facebook
    def post_to_facebook(self):
        # Get page id, access token, and post message
        page_id = self.page_id_entry.get()
        access_token = self.token_entry.get()
        message = self.post_entry.get()

        # Create a Facebook object with your access token
        graph = facebook.GraphAPI(access_token=access_token, version='3.0')

        # Upload image files
        for image_file in self.image_files:
            with open(image_file, 'rb') as image:
                graph.put_photo(image=image.read(), album_path=f"{page_id}/photos", message=message)

        print('Post successful!')

if __name__ == "__main__":
    app = FacebookPostApp()
    app.mainloop()
