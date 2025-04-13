import pandas as pd
import ytMusicApi

playlistID = "INSERT HERE"
playlist = ytMusicApi.get_Playlist(playlistID)

songTitles = ytMusicApi.get_Playlist_Names(playlist)
songThumbnailsURL = ytMusicApi.get_Playlist_Thumbnails(playlist)
songAlbums = ytMusicApi.get_Playlist_Albums(playlist)
songLinks = ytMusicApi.get_Playlist_Links(playlist)
songLengths = ytMusicApi.get_Playlist_Lengths(playlist)
songViews = ytMusicApi.get_Playlist_Views(playlist)
songArtists = ytMusicApi.get_Playlist_Artists(playlist)
songDates = ytMusicApi.get_Playlist_Dates(playlist)

albumYears = ytMusicApi.get_Album_Year(playlist)
album_Thumbnails = ytMusicApi.get_Album_Thumbnails(playlist)

data = {
    "name": songTitles,
    "artist": songArtists,
    "thumbnailURL": songThumbnailsURL,
    "album": songAlbums,
    "link": songLinks,
    "length": songLengths,
    "views": songViews,
    "date": songDates,
    "albumYear": albumYears,
    "albumThumbnail": album_Thumbnails
}

df = pd.DataFrame(data)
df.to_csv("dataset.csv", index=False)