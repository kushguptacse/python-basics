import requests
import bs4

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
res = requests.get("https://en.wikipedia.org/wiki/Samsung_Galaxy_Watch_6", headers=headers)

soup = bs4.BeautifulSoup(res.text,"lxml")
print(soup.select("title"))  #[<title>Samsung Galaxy Watch 6 - Wikipedia</title>]
print(soup.select("title")[0].getText())  #Samsung Galaxy Watch 6 - Wikipedia

from PIL import Image

words = Image.open('word_matrix.png')

words.resize((200, 200)).save('word_matrix_resized.png')