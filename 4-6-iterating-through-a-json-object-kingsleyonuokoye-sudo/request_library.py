import requests

BASE_URL = "https://openscriptureapi.org/api/scriptures/v1/lds/en/volume/bookofmormon/"


def get_chapter(book, chapter):
    """
    Fetch a full Book of Mormon chapter from the API.
    """
    url = BASE_URL + book.lower().replace(" ", "") + "/" + str(chapter)

    response = requests.get(url)
    response.raise_for_status()

    return response.json()


def get_chapter_summary(book, chapter):
    """
    Returns only the chapter summary.
    """
    data = get_chapter(book, chapter)
    return data["chapter"]["summary"]