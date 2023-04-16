from bs4 import BeautifulSoup
import requests

def get_image_from_imdb(imdb_id):
    url = f"https://www.imdb.com/title/{imdb_id}"
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"})
    soup = BeautifulSoup(response.content, "html.parser")
    image = soup.find("img", {"class": "ipc-image"})["src"]
    return image


if __name__ == "__main__":
    pass