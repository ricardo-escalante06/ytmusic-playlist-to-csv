from ytmusicapi import YTMusic
from ytmusicapi.auth.oauth import OAuthCredentials
import requests
from dotenv import load_dotenv
import os

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

ytmusic = YTMusic('oauth.json', oauth_credentials=OAuthCredentials(client_id=client_id, client_secret=client_secret))

# -- Playlist Code -- 

def get_Playlist(playlistID):
    return ytmusic.get_playlist(playlistID)

def print_PlaylistSongs(playlist):
    print(playlist["title"])
    for x in range(playlist["trackCount"]):
        print(playlist["tracks"][x]["title"])

def get_Playlist_Names(playlist):
    names = []
    for x in range(playlist["trackCount"]):
        # Strings
        names.append(playlist["tracks"][x]["title"])
    # print(names)
    return names

def get_Playlist_Artists(playlist):
    artists = []
    for x in range(playlist["trackCount"]):
        combined = ""
        count = 0
        for y in playlist["tracks"][x]["artists"]:
            if count == 1:
                combined += "/"
            combined += y["name"]
            count += 1
            
        # Strings
        artists.append(combined)
    # print(artists)
    return artists

def get_Playlist_Thumbnails(playlist):
    thumbnails = []
    for x in range(playlist["trackCount"]):
        songID = playlist["tracks"][x]["videoId"]
        goodThumbnail = f"https://img.youtube.com/vi/{songID}/maxresdefault.jpg"
        # Strings
        thumbnails.append(goodThumbnail)
    
    # print(thumbnails)
    return thumbnails

def get_Playlist_Albums(playlist):
    albums = []
    for x in range(playlist["trackCount"]):
        # Strings
        if playlist["tracks"][x]["album"] == None:
            albums.append("DNE")
        else:
            albums.append(playlist["tracks"][x]["album"]["name"])
            
    #print(albums)
    return albums

def get_Playlist_Links(playlist):
    links = []
    for x in range(playlist["trackCount"]):
        songID = playlist["tracks"][x]["videoId"]
        song = ytmusic.get_song(songID)
        # Strings
        links.append(song["microformat"]["microformatDataRenderer"]["urlCanonical"])

    # print(links)
    return links

def get_Playlist_Lengths(playlist):
    lengths = []
    for x in range(playlist["trackCount"]):
        # String
        lengths.append(playlist["tracks"][x]["duration"])
        
    # print(lengths)
    return lengths

def get_Playlist_Views(playlist):
    views = []
    for x in range(playlist["trackCount"]):
        songID = playlist["tracks"][x]["videoId"]
        song = ytmusic.get_song(songID)
        # Strings
        views.append(song["videoDetails"]["viewCount"])

    # print(views)
    return views

def get_Playlist_Dates(playlist):
    pfps = []
    for x in range(playlist["trackCount"]):
        songID = playlist["tracks"][x]["videoId"]
        song = ytmusic.get_song(songID)
        # Strings
        fullDate = song["microformat"]["microformatDataRenderer"]["uploadDate"]
        date = fullDate[0:fullDate.find('T')]
        pfps.append(date)

    # print (pfps)    
    return pfps

def get_Album_Year(playlist):
    views = []
    for x in range(playlist["trackCount"]):
        if playlist["tracks"][x]["album"] != None:
            albumID = playlist["tracks"][x]["album"]["id"]
            album = ytmusic.get_album(albumID)
            toReturn = album["year"]
        else:
            toReturn = "DNE"

        # Strings
        
        views.append(toReturn)

    # print (views)    
    return views

def get_Album_Thumbnails(playlist):
    thumbnails = []
    for x in range(playlist["trackCount"]):
        if playlist["tracks"][x]["album"] != None:
            albumID = playlist["tracks"][x]["album"]["id"]
            album = ytmusic.get_album(albumID)
            toReturn = album["thumbnails"][-1]["url"]
        else:
            toReturn = "DNE"

        # Strings
        thumbnails.append(toReturn)

    # print (thumbnails)    
    return thumbnails
