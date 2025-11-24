Project Statement: Lyrically

1. Overview of the Project

Lyrically is a Python desktop application that offers a clean, ad-free interface to fetch song lyrics for the end user. Using the Genius API, this application will let music enthusiasts easily search and display song lyrics without any troublesome web browsers or unwanted advertisements.

2. Objective

This tool's main objective is the integration of a modern GUI with a robust lyrics database. The particular objectives which need to be achieved are:

To provide an easy, user-friendly entry point for searching for music metadata.

to display large blocks of text - lyrics - in readable, scrollable format.

Handle API authentication or error states in a graceful way in a visual environment.

3. Technical Implementation

Core Technologies

Language: Python 3.x

GUI Framework: customtkinter. A modern, dark-mode wrapper around Python's standard Tkinter.

API Wrapper: lyricsgenius - Interacts with Genius.com's public API.

Environment Management: python-dotenv (For secure API key management).

Architecture

This application is based on a Class-based Object-Oriented design named LyricsApp, which inherits from customtkinter.CTk.

Initialization:

The application starts out with securely loading the GENIUS_ACCESS_TOKEN.

It tries to make a handshake with the Genius API using the function initialize_genius().

It stops opening an app if authentication fails and alerts the user by showing a message box.

User Interface :

Welcome Screen: This is a clean landing page with a primary "Find Lyrics" call-to-action.

Search Interface: Replaces the welcome screen with dynamic input fields for "Artist" and "Song Title".

Output Display This utilizes a ScrolledText widget to accommodate variable-length lyric data and is themed to the dark look.

Data Logic:

The logic of querying the API is handled by the search_lyrics function.

This class sanitizes headers, removing section headers if configured, and formats the output string.

It uses exception handling in order to capture either a network timeout or "Song not found" error and return friendly feedback to the UI.

4. Key Features

Modern Aesthetics: using customtkinter for the specific purpose of "Dark Blue" theme, with rounded corners corner_radius=20.

Asynchronous-like UX: The UI updates with status messages ("Searching for.") to keep the user informed during network requests.

Robust Error Handling: Performs checks on both empty inputs and API connectivity before performing a fetch.

5. Future Improvements

Asynchronous threading will avoid UI freezing when calling slow APIs. Recently searched songs get cached to reduce the usage of API calls. "Copy to Clipboard" functionality for the lyrics displayed.
