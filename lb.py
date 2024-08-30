from bs4 import BeautifulSoup
import requests

url = 'https://letterboxd.com/JalanKotak/films/diary'
page = requests.get(url)
soup = BeautifulSoup(page.text, features="html.parser")
diary_table = soup.find('table', class_='table film-table')

# titles
diary_table_titles = diary_table.find_all('th')
plain_titles = [title.text for title in diary_table_titles]
# ['Month', 'Day', 'Film', 'Released', 'Rating', 'Like', 'Rewatch', 'Review', 'EditYou']
print(plain_titles)

#the data
def data_strip(data):
    res = []
    # Month up to Rating
    for i in range(0, 5):
        res.append(data[i].text.strip())
    
    res.append(data[7].text.strip())
    res.append(data[8].text.strip())
    return res

col_data = diary_table.find_all('tr')
for row in col_data:
    row_data = row.find_all('td')
    if (len(row_data) == 0):
        continue
    print(data_strip(row_data))