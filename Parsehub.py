import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
base_url = 'https://parsehub.com/'


# print(response.text)
for x in range(1,8):
    url = f'https://parsehub.com/sandbox/showtimes?page='
    response = requests.get(url+str(x))

    soup = bs(response.text, 'html.parser')

    urls = []
    title = []
    time = []
    for movie in soup.findAll('a','title'):
        # print(movie.string)
          urls.append(base_url + movie.get('href'))
          title.append(movie.string)
          # print(title)
          # print(urls)

    for showtime in soup.findAll('span','imax'):
        time.append(showtime.string)
        # print(showtime.string)

    raw_data = {
        'Movie_Title': title,
        'Image_Url': urls,
        'Show_Time': time
    }

dataframe = pd.DataFrame(raw_data, columns=['Movie_Title', 'Image_Url', 'Show_Time'])
dataframe.to_csv('raw_data.csv', index=False)
print(dataframe)