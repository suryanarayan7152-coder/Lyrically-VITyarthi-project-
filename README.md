# Lyrically-VITyarthi-project-
Lyrically........
       Hello! This is a Python application I made for immediately finding song lyrics. The Genius.com API supplies it with the needed lyrics, and it utilizes customtkinter to make the GUI modern and dark-themed.
       I made this to practice working with APIs and GUIs in Python.

Features:

Dark Mode UI: Looks much better than the standard white Tkinter windows.
Search: You can type in an Artist and a Song Name.
Lyrics Display: The lyrics are displayed within a scrollable text box.
Error Handling: Informs user if the song isn't found, or if the API is not working.

Libraries Used:

I used the following Python libraries for the project:

customtkinter (For the UI)
lyricsgenius (To talk to the Genius API)
python-dotenv - to handle the API key, though I'm still learning how to hide it properly!
tkinter (Built-in)

How to Run on Your Computer:

1. Install Python:
      Make sure you have Python installed. You can check by typing python --version in your terminal.

2. Install Dependencies:
      You need to install the external libraries I used. Open your terminal or command prompt and run this:
      " pip install customtkinter lyricsgenius python-dotenv "
 
3. Get a Genius API Token
For this to work, you are required to get your Access Token from Genius.
Go to Genius API Client Page.
Sign up/Log in and create a new API Client.
Copy the Client Access Token.
Paste it into the code where it says, GENIUS_ACCESS_TOKEN = "."

(Note: currently there is a token inside of the code, but it is better to use a .env file so that you do not share your key with everyone!)

4. Run the App:
    Run the script using Python:

Known Issues:
      Sometimes the app freezes for a second while it is searching for the song (I need to learn how to use "threading" to fix this). If the song title is  spelled wrong, it might not find it. I'd like to add the Album Art image later. 

Credits:
Genius for the lyrics database. CustomTkinter Documentation
