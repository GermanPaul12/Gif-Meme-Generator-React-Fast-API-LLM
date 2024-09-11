import os
from dotenv import load_dotenv
from openai import OpenAI
from get_joke import get_joke

load_dotenv()

def get_important_word(joke):
    """
    This function uses the Zukijourney API to analyze a joke and extract the most important entity or emotion from it.
    Follow Quickl start guide to get api key: https://docs.zukijourney.com/ai
    
    Parameters:
    joke (str): The joke as a string

    Returns:
    The function returns a string containing the most important entity or emotion extracted from the joke.#+

    Usage:
    The function can be called directly to get the most important entity or emotion from a joke.

    Example:
    >>> get_important_word()
    'children'
    """
    # Follow Quickl start guide to get api key: https://docs.zukijourney.com/ai
    API_KEY = os.getenv('ZUKI_API_KEY')
    client = OpenAI(base_url="https://api.zukijourney.com/v1", api_key=API_KEY)

    response = client.chat.completions.create(
        model="caramelldansen-1", # or gpt-4o-mini, claude-3-haiku, gemini-1.5-flash, etc...
        messages=[{"role": "system", "content": "You have to find the most important entity inside a joke and only output this entity. If there is no entity which is meme worthy then output an emotion. Your response will be used to find a suitable image for the joke."}, 
                            {"role": "user", "content": "Life's is like my dick. The more children the harder it gets."}, 
                            {"role": "assistant", "content": "children"},
                            {"role": "user", "content": str(joke)}
        ])
    return response.choices[0].message.content


if __name__ == "__main__":
    joke = get_joke()
    print(get_important_word(joke))