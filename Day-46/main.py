import requests 
from bs4 import BeautifulSoup 
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import dotenv
import os 

dotenv.load_dotenv()

CLIENT_ID = os.getenv("spotify_clientid")
SECRET = os.getenv("spotify_secret")

# date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

# base_url = "https://www.billboard.com/charts/hot-100/"



# response = requests.get(base_url + date)
# website_contents = response.text

# soup = BeautifulSoup(website_contents,"html.parser")


# song_tags = soup.select(selector="li ul li h3")

# song_names = [song.getText().strip() for song in song_tags]

# print(song_names)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username="Avinaash A" 
    )
)

user_id = sp.current_user()["id"]
print(user_id)

