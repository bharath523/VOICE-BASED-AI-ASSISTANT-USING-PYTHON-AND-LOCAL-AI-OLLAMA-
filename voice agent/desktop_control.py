import os
import webbrowser
import urllib.parse


def open_app(command):
    command = command.lower()

    # ===============================
    # BASIC DESKTOP APPS
    # ===============================
    if "open chrome" in command:
        os.system("start chrome")
        return "Opening Chrome"

    if "open notepad" in command:
        os.system("start notepad")
        return "Opening Notepad"

    if "open calculator" in command:
        os.system("start calc")
        return "Opening Calculator"

    if "open file explorer" in command or "open explorer" in command:
        os.system("start explorer")
        return "Opening File Explorer"

    if "open vscode" in command or "open vs code" in command:
        os.system("code")
        return "Opening Visual Studio Code"

    if "open settings" in command:
        os.system("start ms-settings:")
        return "Opening Settings"


    # ===============================
    # WEBSITES
    # ===============================
    if "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube"

    if "open google" in command:
        webbrowser.open("https://www.google.com")
        return "Opening Google"

    if "open gmail" in command:
        webbrowser.open("https://mail.google.com")
        return "Opening Gmail"

    if "open spotify" in command:
        webbrowser.open("https://open.spotify.com")
        return "Opening Spotify"


    # ===============================
    # SEARCH
    # ===============================
    if "search youtube for" in command:
        query = command.split("search youtube for")[-1].strip()
        url = "https://www.youtube.com/results?search_query=" + urllib.parse.quote(query)
        webbrowser.open(url)
        return f"Searching YouTube for {query}"

    if "search google for" in command:
        query = command.split("search google for")[-1].strip()
        url = "https://www.google.com/search?q=" + urllib.parse.quote(query)
        webbrowser.open(url)
        return f"Searching Google for {query}"


    # ===============================
    # MUSIC / VIDEO
    # ===============================
    if "play music on youtube" in command:
        webbrowser.open("https://www.youtube.com/results?search_query=music")
        return "Playing music on YouTube"

    if "play song" in command:
        query = command.replace("play song", "").strip()
        url = "https://www.youtube.com/results?search_query=" + urllib.parse.quote(query)
        webbrowser.open(url)
        return f"Playing {query} on YouTube"


    # ===============================
    # SYSTEM CONTROL (SAFE)
    # ===============================
    if "lock system" in command:
        os.system("rundll32.exe user32.dll,LockWorkStation")
        return "Locking system"

    if "restart system" in command:
        os.system("shutdown /r /t 5")
        return "Restarting system"

    if "shutdown system" in command:
        os.system("shutdown /s /t 5")
        return "Shutting down system"


    # ===============================
    # SCREENSHOT
    # ===============================
    if "take screenshot" in command:
        os.system("snippingtool")
        return "Opening Snipping Tool"


    return None
