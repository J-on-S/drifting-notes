import requests

def spotify_oembed(spotify_url: str):
    r = requests.get(
        "https://open.spotify.com/oembed",
        params={"url": spotify_url},
        timeout=10
    )
    r.raise_for_status()
    return r.json()