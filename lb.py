from bs4 import BeautifulSoup
import requests
import re

base = 'https://letterboxd.com'

#the data
def data_strip(data):
    res = []
    # Month up to Rating
    for i in range(0, 5):
        res.append(data[i].text.strip())
    
    if len(data) > 7 and 'Read the review' in data[7].text:
        link = data[7].find('a', href=True)
        if link:
            res.append(get_review(link['href']))
        else:
            res.append('No review')
    else:
        res.append('No review')

    return res

def get_review(link):
    review_link = base + link
    review_page = requests.get(review_link)
    review_soup = BeautifulSoup(review_page.text, features="html.parser")
    # print(review_soup)
    review_body = review_soup.find(class_=re.compile('review body-text'))
    content = review_body.find('p')
    return content.text

def main():
    url = base + '/JalanKotak/films/diary/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, features="html.parser")
    diary_table = soup.find('table', class_='table film-table')

    # titles
    diary_table_titles = diary_table.find_all('th')
    plain_titles = [title.text for title in diary_table_titles]
    # ['Month', 'Day', 'Film', 'Released', 'Rating', 'Like', 'Rewatch', 'Review', 'EditYou']
    print(plain_titles)

    col_data = diary_table.find_all('tr')
    for row in col_data:
        row_data = row.find_all('td')
        if (len(row_data) == 0):
            continue
        print(data_strip(row_data))

if __name__ == '__main__':
    main()