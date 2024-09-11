import requests

def get_joke():
    """
    Fetches a joke from the Joke API and returns it as a string.#+

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

if __name__ == '__main__':
    print(get_joke())