import customtkinter
import lyricsgenius as Genius
import os
from dotenv import load_dotenv
from tkinter import messagebox, scrolledtext
import tkinter as tk

load_dotenv()

GENIUS_ACCESS_TOKEN="MOIKMxj_NAvQHmChKRQjcCqeIoc1k9SzAzu27FEUb-nJVwQ98KS85MSdHF4KBpka"
genius_handler = None

def initialize_genius() -> bool:
    global genius_handler

    if not GENIUS_ACCESS_TOKEN:
        return False

    try:
        handler = Genius.Genius(GENIUS_ACCESS_TOKEN, verbose=False, timeout=15)
        handler.remove_section_headers = True
        genius_handler = handler
        return True
    except Exception as err:
        messagebox.showerror(
            "Initialization Error",
            f"Failed to initialize Genius API:\n{err}"
        )
        return False
def search_lyrics(artist: str, title: str) -> str:
    if genius_handler is None:
        return "Genius API is not initialized."

    try:
        song = genius_handler.search_song(title, artist)
        if song:
            header = f"Lyrics for: {song.title} by {song.artist}\n" + "-" * 60 + "\n"
            return header + song.lyrics
        return f"No lyrics found for '{title}' by {artist}."
    except Exception as err:
        return f"Error retrieving lyrics: {err}"

class LyricsApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        self.title("Lyrically")
        self.geometry("700x650")

        self.main_area = customtkinter.CTkFrame(self, corner_radius=20, fg_color="black")
        self.main_area.pack(padx=20, pady=20, fill="both", expand=True)

        self.artist_entry = None
        self.title_entry = None
        self.lyrics_box = None

        self.load_welcome_screen()

    def load_welcome_screen(self):
        button = customtkinter.CTkButton(
            master=self.main_area,
            text="Find Lyrics",
            width=200,
            height=50,
            fg_color="#080838",
            hover_color="white",
            command=self.open_search_ui
        )
        button.pack(expand=True)

    def open_search_ui(self):
        for widget in self.main_area.winfo_children():
            widget.destroy()

        input_frame = customtkinter.CTkFrame(self.main_area)
        input_frame.pack(pady=10)

        customtkinter.CTkLabel(input_frame, text="Artist:").pack(side="left", padx=5)
        self.artist_entry = customtkinter.CTkEntry(input_frame, width=150)
        self.artist_entry.pack(side="left", padx=10)

        customtkinter.CTkLabel(input_frame, text="Song:").pack(side="left", padx=5)
        self.title_entry = customtkinter.CTkEntry(input_frame, width=150)
        self.title_entry.pack(side="left", padx=10)

        customtkinter.CTkButton(
            input_frame,
            text="Search",
            width=100,
            fg_color="#080838",
            hover_color="white",
            command=self.run_search,
        ).pack(side="left", padx=25)

        self.lyrics_box = scrolledtext.ScrolledText(
            self.main_area,
            wrap="word",
            bg="#242424",
            fg="white",
            font=("Arial", 11),
            state="disabled"
        )
        self.lyrics_box.pack(fill="both", expand=True, padx=10, pady=10)

        self.update_text("Enter an artist name and song title to begin.")

    def update_text(self, text: str):
        self.lyrics_box.configure(state="normal")
        self.lyrics_box.delete("1.0", tk.END)
        self.lyrics_box.insert(tk.END, text)
        self.lyrics_box.configure(state="disabled")

    def run_search(self):
        artist = self.artist_entry.get().strip()
        title = self.title_entry.get().strip()

        if not artist or not title:
            messagebox.showwarning("Input Required", "Please fill in both fields.")
            return

        self.update_text(f"Searching for '{title}' by {artist}...")
        self.update()

        lyrics = search_lyrics(artist, title)
        self.update_text(lyrics)


if __name__ == "__main__":
    if initialize_genius():
        app = LyricsApp()
        app.mainloop()
    else:
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Startup Error", "Invalid or missing Genius API token.")
        root.destroy()
