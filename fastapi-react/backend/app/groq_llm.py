import os
from dotenv import load_dotenv
from groq import Groq
from get_joke import get_joke

load_dotenv()
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

if __name__ == "__main__":
    joke = get_joke()
    print(f"Important word: {get_important_word(joke)}")
    print(f"Joke: {joke}")