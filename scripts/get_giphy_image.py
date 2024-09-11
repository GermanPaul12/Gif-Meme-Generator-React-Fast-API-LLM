import os
from dotenv import load_dotenv
import requests

load_dotenv() 

API_KEY = os.getenv("GIPHY_API_KEY")

def get_gif(query):
    """
    Fetches a GIF from the GIPHY API based on the provided search query.

    Args:
    query (str): The search query to find a GIF.

    Returns:
    str or None: If the request is successful, it returns the embed URL of the first GIF found. If the request fails, it returns None.

    Raises:
    None

    Usage:
    gif_url = get_gif(query)
    print(f"Gif found: {gif_url}")
    """
    URL = 'https://api.giphy.com/v1/gifs/search'
    params = {'q': query, 'limit': 1, 'api_key': API_KEY}
    res = requests.get(URL, params)
    if res.status_code == 200:
        data = res.json()
        first_gif = data['data'][0]
        embed_url = first_gif['embed_url']
        return embed_url
    else:
        print("Error fetching GIF")
        return None
    
if __name__ == '__main__':
    query = input("Enter a search term: ")
    gif_url = get_gif(query)
    print(f"Gif found: {gif_url}")