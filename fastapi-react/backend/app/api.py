from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import requests
import os
from groq import Groq

load_dotenv() 

# Joke
def get_joke():
    """
    Fetches a joke from the Joke API (https://sv443.net/jokeapi/v2/#try-it) and returns it as a string.

    Parameters:
    No parameters are required for this function.#+

    Returns:
    If the joke has a setup and delivery, a tuple containing the setup and delivery is returned. Otherwise, a single string containing the joke is returned.

    If an error occurs while fetching the joke, a message indicating the error is printed, and None is returned.
    """
    URL = 'https://v2.jokeapi.dev/joke/Any'
    res = requests.get(URL)
    if res.status_code == 200:
        data = res.json()
        if data.get("setup"):
            setup = data['setup']
            delivery = data['delivery']
            return setup, delivery
        else:
            joke = data['joke']
            return joke
    else:
        print("Error getting joke")


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
    API_KEY = os.getenv("GIPHY_API_KEY")
    URL = 'https://api.giphy.com/v1/gifs/search'
    params = {'q': query, 'limit': 1, 'api_key': API_KEY}
    res = requests.get(URL, params)
    if res.status_code == 200:
        data = res.json()
        first_gif = data['data'][0]
        gif_url = first_gif['images']['original']['url']
        if gif_url == None:
            pass
        else: return gif_url
    else:
        print("Error fetching GIF")
        return None


def get_important_word(joke):
    """
    This function uses the Groq API to analyze a given joke and identify the most important entity or emotion.
    The function takes a string 'joke' as input and returns the identified important word or emotion.
    Get your own API Key here: https://console.groq.com/keys

    Parameters:
    joke (str): The joke to analyze.

    Returns:
    str: The most important word or emotion identified in the joke.
    """
    client = Groq(
        api_key=os.getenv("GROQ_API_KEY"),
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You have to find the most important entity inside a joke and only output this entity. If there is no entity which is meme worthy then output an emotion. Your response will be used to find a suitable image for the joke."}, 
            {"role": "user", "content": "Life's is like my dick. The more children the harder it gets."}, 
            {"role": "assistant", "content": "children"},
            {"role": "user", "content": str(joke)}
        ],
        model="llama-3.1-8b-instant",
    )
    return chat_completion.choices[0].message.content


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000", "http://localhost:5167"],  # Add your React app's URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["root"])
async def read_root() -> dict:
    joke = str(get_joke())
    important_word = get_important_word(joke)
    gif_url = get_gif(important_word)
    return {"joke": joke, "important_word": important_word, "gif_url": gif_url}
