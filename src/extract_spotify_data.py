import spotipy
import spotipy.util as util
import json
import types
import os
import dotenv

def current_user_recently_played(self, limit=50):
    return self._get('me/player/recently-played', limit=limit)

dotenv.load_dotenv()

token = util.prompt_for_user_token(
        username="kaleighspitz",
        scope="user-read-recently-played user-read-private user-top-read user-read-currently-playing",
        client_id = os.getenv('SPOTIPY_CLIENT_ID'),
		client_secret = os.getenv('SPOTIPY_CLIENT_SECRET'),
        redirect_uri='http://127.0.0.1:8080/')

spotify = spotipy.Spotify(auth=token)
spotify.current_user_recently_played = types.MethodType(current_user_recently_played, spotify)

tracks = spotify.current_user_recently_played(limit=50)
out_file = open("data/raw/raw_data.json","w")
out_file.write(json.dumps(tracks, sort_keys=True, indent=4))
out_file.close()

print(json.dumps(tracks, sort_keys=True, indent=4))