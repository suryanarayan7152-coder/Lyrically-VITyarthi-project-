# Lyrically-VITyarthi-project-
Hello! This is a Python application I have created to immediately find song lyrics, and it gets the needed lyrics with the Genius.com API. The GUI is designed using customtkinter so that it will be modern and dark themed. I did this because I wanted to practice how to work with APIs and GUIs in Python.

1.Features:

Dark Mode UI: Looks much better than the default white Tkinter windows. Search: The user can type in an Artist and a Song Name. Lyrics Display: The lyrics are displayed inside of a scrollable text box. Error Handling: Informs user if the song isn't found, or if the API is not working.

2.Libraries Used:

The following Python libraries were used for the project:
customtkinter - for the UI
lyricsgenius - to speak with the Genius API
python-dotenv - handling of the API key, though I am still learning how to properly hide it! tkinter - built in

3.How to Run on Your Computer:

Setting Up Python: First and foremost, ensure that Python is installed. You could check this in your terminal by typing python --version.
Install Dependencies: These are the external libraries I utilized, and you will need to install them. Fire up your terminal or command prompt and execute this: " pip install customtkinter lyricsgenius python-dotenv "
Get a Genius API Token To make this work you have to first get your Access Token from Genius. Go to Genius API Client Page. Sign up / Log in and create a new API client. Copy the Client Access Token. Paste it into the code where it says, GENIUS_ACCESS_TOKEN = "."

{Note: Currently there is a token inside of the code, but it is better to use a .env file so that you do not share your key with everybody!}

4.Run the App: 
Use Python to run this script.
Known Issues: The app freezes for a second every now and then when it's searching for the song. I need to learn how to use "threading" to resolve this. If the title of the song is misspelled, it may not find it. I would like to add an Album Art image later. 

5.Credits: 
Genius for the lyrics database,
CustomTkinter Documentation
