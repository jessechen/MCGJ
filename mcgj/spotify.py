import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

def isSpotifyTrack(url):
    return 'open.spotify.com' in url if url else False

class SpotifyClient:
    def __init__(self):
        auth_manager = SpotifyClientCredentials()
        self.spotipy = spotipy.Spotify(auth_manager=auth_manager)


    def getTrackInfo(self, url):
        track = self.spotipy.track(url)
        title = track['name']
        artist = track['artists'][0]['name']
        art_url = track['album']['images'][0]['url']
        return title, artist, art_url

    def getTrackArt(self, url):
        track = self.spotipy.track(url)
        art_url = track['album']['images'][0]['url']
        return art_url

    def getNonSpotifyArtwork(self, track):
        title = track.title if track.title else ''
        artist = track.artist if track.artist else ''
        query = title + ' ' + artist
        results = self.spotipy.search(query, type='track')
        if results['tracks']['items']:
            return results['tracks']['items'][0]['album']['images'][0]['url']
        return ''

