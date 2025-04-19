import spotipy 
from spotipy.oauth2 import SpotifyOAuth
from top_100 import Top_100
from dotenv import load_dotenv
import os

art = r"""
      ___  ____  ____  ___  ___  _______  _______     ______  ___  ___  
     |"  |("  _||_ " ||"  \/"  |/"     "||   _  "\   /    " \|"  \/"  | 
     ||  ||   (  ) : | \   \  /(: ______)(. |_)  :) // ____  \\   \  /  
     |:  |(:  |  | . )  \\  \/  \/    |  |:     \/ /  /    ) :)\\  \/   
  ___|  /  \\ \__/ //   /\.  \  // ___)_ (|  _  \\(: (____/ // /\.  \   
 /  :|_/ ) /\\ __ //\  /  \   \(:      "||: |_)  :)\        / /  \   \  
(_______/ (__________)|___/\___|\_______)(_______/  \"_____/ |___/\___| 
                                                                        
  -Spotify Playlist Generator-    """
  
load_dotenv(override=True)
CLIENT_ID = os.getenv("CLIENT_ID")
SECRET = os.getenv("SECRET")
USERNAME = os.getenv("USERNAME")

#------------------------------------FUNCTIONS----------------------------------  
# SPOTIFY CLIENT  ----------
def SpotifyClient(client_id,secret,username):
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope="playlist-modify-private",
            redirect_uri="http://localhost:9000/callback",
            client_id= client_id,
            client_secret= secret, 
            show_dialog= True,
            cache_path="/token.txt",
            username= username,
        )
    )
    return  sp 

# FUNCTION - SEARCH ON SPOTIFY THE TRACKS ----------
def sp_track_finder(top_100:list):
    spotify_uri_list = [] 
    prct = 0 
    for song in top_100:
        spotify_result = sp.search(q=f"track:{song} year:{year}", type="track")
        prct += 1
        try:
            if spotify_result["tracks"]["items"][0]["name"] == song: 
                spotify_uri_list.append(spotify_result["tracks"]["items"][0]["uri"])
        except IndexError:
            print(f"{song} -  Not found")
        print(f"{prct} %")
    return spotify_uri_list

# FUNCTION - CREATE A PLAYLIST ON SPOTIFY ----------

def playlist_creator(user_id,date,year,track_list):
    playlist_name = f"{date} Billboard 100"
    new_playlist = sp.user_playlist_create(user= user_id,name= playlist_name,public= False,collaborative= False,description= f"Best song of the year {year}")
    playlist_id = new_playlist["id"]
    sp.playlist_add_items(playlist_id=playlist_id,items=track_list)
    print("Job done")

#--------------------------------------MAIN------------------------------------                                                                                                     
sp = SpotifyClient(CLIENT_ID,SECRET,USERNAME)
print(f"{art}\n")
date = input("Choose the Year you want to travel to. Type the date in this format YYYY-MM-DD:  ")
year = date[0:4]
selection = Top_100(date).selection
user_id = sp.current_user()["id"]
spotify_track_list = sp_track_finder(selection)
playlist_creator(user_id,date,year,spotify_track_list)
