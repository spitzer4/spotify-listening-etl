import json
import pandas as pd

def transform_data(json_file):
    """
    Transforms the given JSON data into a more structured format.

    Args:
        json_file (String): The JSON file name.

    Returns:
        DataFrame: A Pandas DataFrame of tracks.
    """
    
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    transformed_items = []
    
    for item in data.get('items', []):
        track = item.get('track', {})
        album = track.get('album', {})
        artists = track.get('artists', [])
        
        transformed_item = {
            'played_at': item.get('played_at'),
            'track_id': track.get('id'),
            'track_name': track.get('name'),
            'track_duration_ms': track.get('duration_ms'),
            'track_popularity': track.get('popularity'),
            'album_id': album.get('id'),
            'album_name': album.get('name'),
            'album_release_date': album.get('release_date'),
            'album_total_tracks': album.get('total_tracks'),
            'artist_ids': [artist.get('id') for artist in artists],
            'artist_names': [artist.get('name') for artist in artists],
            'context_uri': item.get('context', {}).get('uri'),
            'context_type':item.get('context', {}).get('type')
        }
        
        transformed_items.append(transformed_item)
    
    df = pd.DataFrame(transformed_items)
    return df

df = transform_data('data/raw/raw_data.json')
df.to_csv('data/transformed/listening_history.csv', index=False)