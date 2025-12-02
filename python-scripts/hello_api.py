import requests

def get_weather(city):
    url = f"https://wttr.in/{city}?format=3"
    response = requests.get(url)
    return response.text

if __name__ == "__main__":
    print(get_weather("Houston"))
