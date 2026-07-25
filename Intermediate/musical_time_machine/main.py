from bs4 import BeautifulSoup
import requests
from pprint import pprint
from ytmusicapi import YTMusic
import os


if not os.path.exists("browser.json"):
    print("browser.json not found")
    print("You need to authenticate with youtube music first")
    print("Run one of these commands in your terminal from this project folder:\n")
    print("  Mac:     pbpaste | ytmusicapi browser")
    print("  Windows: ytmusicapi browser\n")
    print("Copy the request headers from Firefox first.")
    print("This will create browser.json.")
    exit()


date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

####### Scraping Website for 100 musics from a particular time #######
top_100_music_url = f"https://appbrewery.github.io/bakeboard-hot-100/{date}"
response = requests.get(top_100_music_url)


soup = BeautifulSoup(markup=response.text, features="html.parser")
songs = soup.find_all(name="h3", class_="chart-entry__title")
song_names = [song.getText().strip() for song in songs]

###### Authenticating with Youtube Music ######
ytmusic = YTMusic("browser.json")
print(song_names)

# Creating a playlist
playlist_name = f"{date} Billboard 100"
playlist_id = ytmusic.create_playlist(
            playlist_name,
            f"Top songs from {date}",
            privacy_status="PRIVATE",
)

print(f"Created a playlist:  {playlist_name}")

# Searching for a song and getting their ids
for song in song_names:
    try:
        result = ytmusic.search(song, filter="songs", limit=1)
        ytmusic.add_playlist_items(playlist_id, [result[0]["videoId"]])
        print(f"Added {song}")
    except Exception as e:
        print(f"Skipped {song} | Error occured {e}")
