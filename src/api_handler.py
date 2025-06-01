from dotenv import load_dotenv
import requests
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")
URL = f"http://www.omdbapi.com/?apikey={API_KEY}&"


def get_by_title(s_title: str, s_year: str = None, s_type: str = "movie", s_plot: str = "short"):

    if not s_title:
        raise ValueError("Title not given")

    REQUEST_URL = URL + f"t={s_title}&type={s_type}&plot={s_plot}"

    if s_year:
        REQUEST_URL += f"&y={s_year}"

    try:
        response = requests.get(REQUEST_URL)

        if response.status_code == 200:
            posts = response.json()
            return posts
        else:
            return f"Error: {response.status_code}"

    except requests.exceptions.RequestException as e:
        return f"Error: {e}"


def get_by_id(s_id: str, s_year: str = None, s_type: str = "movie", s_plot: str = "short"):

    if not s_id:
        raise ValueError("IMDB Id not given")

    REQUEST_URL = URL + f"i={s_id}&type={s_type}&plot={s_plot}"

    if s_year:
        REQUEST_URL += f"&y={s_year}"

    try:
        response = requests.get(REQUEST_URL)

        if response.status_code == 200:
            posts = response.json()
            return posts
        else:
            return f"Error: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"


def search_by_name(s_title, s_type: str = "movie", s_year: str = None, s_page: str = "1"):

    if not s_title:
        raise ValueError("Search term not given")

    REQUEST_URL = URL + f"s={s_title}&type={s_type}&page={s_page}"

    if s_year:
        REQUEST_URL += f"&y={s_year}"

    try:
        response.requests.get(REQUEST_URL)

        if response.status_code == 200:
            posts = response.json()
            return posts

        else:
            return f"Error: {response.status_code}"

    except requests.exceptions.RequestException as e:
        return f"Error: {e}"


if __name__ == "__main__":
    main()
