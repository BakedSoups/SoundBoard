import os
import tkinter as tk
from tkinter import ttk, filedialog
import pygame

class SoundboardApp:
    def __init__(self, master):
        self.master = master
        self.master.geometry("250x275")
        self.master.title("Soundboard")

        self.selected_folder = None  # Initialize selected_folder attribute

        self.queue = []

        # Pygame mixer initialization
        pygame.mixer.init()

        # Select folder button
        ttk.Button(self.master, text="Select Folder", command=self.select_folder).pack(pady=10)

        # Create buttons for each MP3 file in the folder
        for filename in self.get_mp3_files():
            ttk.Button(self.master, text=filename, command=lambda f=filename: self.play(f)).pack(pady=15)

    def play(self, filename):
        full_path = os.path.join(self.selected_folder, filename)
        try:
            pygame.mixer.music.load(full_path)
            pygame.mixer.music.play()
        except pygame.error as e:
            print("Pygame Error:", e)

    def select_folder(self):
        self.selected_folder = filedialog.askdirectory()
        self.update_buttons()

    def get_mp3_files(self):
        if hasattr(self, 'selected_folder') and self.selected_folder:
            mp3_files = [f for f in os.listdir(self.selected_folder) if f.endswith(".mp3") or f.endswith(".m4a")]
            return mp3_files
        else:
            return []

    def update_buttons(self):
        # Clear existing buttons
        for widget in self.master.winfo_children():
            widget.destroy()

        # Select folder button
        ttk.Button(self.master, text="Select Folder", command=self.select_folder).pack(pady=10)

        # Create buttons for each MP3 file in the folder
        for filename in self.get_mp3_files():
            ttk.Button(self.master, text=filename, command=lambda f=filename: self.play(f)).pack(pady=5)

        ttk.Button(self.master, text="Stop", command=self.stop).pack(pady=10)
        ttk.Button()

    def stop(self):
        pygame.mixer.music.stop()

if __name__ == "__main__":
    root = tk.Tk()
    app = SoundboardApp(root)
    root.mainloop()
