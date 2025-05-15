import requests
from bs4 import BeautifulSoup
import csv

# Step 1: Choose the URL
url = "https://www.audible.com/search?keywords=book&node=18573211011"  # Replace with the target website

# Step 2: Send an HTTP request to the URL
response = requests.get(url)

# Step 3: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")
#print(soup)

subtitle_list = []
book_name_list = []
book_href_list = []
book_narrated_by_list =[]
book_language_list = []
book_rating_list = []
book_release_date_list = []
book_length_list = []
book_author_list = []

# fetching span tag to fetch all book details
span_ele= soup.find_all('span', class_ = 'bc-text bc-size-small bc-color-secondary')
subtitle_list = [title.getText() for title in (soup.find_all('span', class_ = 'bc-text bc-size-base bc-color-secondary'))]

#
# # # Step 4: Extract desired content (example: all links)
for link in soup.find_all('a', class_= 'bc-link bc-color-link'):
    url = link.get('href')
    if url.__contains__("/pd/"):
        book_name = link.getText()
        if book_name.strip() != "":
            book_name_list.append(book_name.strip())
            book_href_list.append(url)

# fetching respective element value
for link in span_ele:
    text = link.getText()
    if text.__contains__('Narrated'):
        list = text.split(':')
        book_narrated_by_list.append(list[1].strip())
    elif text.__contains__('By'):
        list = text.split(':')
        book_author_list.append(list[1].strip())
    elif text.__contains__("Language"):
        list = text.split(':')
        book_language_list.append(list[1].strip())
    elif text.__contains__("ratings") or text.__contains__("rating"):
        list = text.split()
        book_rating_list.append(list[0])
    elif text.__contains__("Not rated yet"):
        book_rating_list.append("Not rated yet")
    elif text.__contains__("Release"):
        list = text.split()
        book_release_date_list.append(list[2])
    elif text.__contains__("Length"):
        list = text.split(':')
        book_length_list.append(list[1].strip())

# writing data in csv file
with open('scrapped.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    # Write header
    writer.writerow(['Book Name', 'URL', 'Subtitle', 'Author', 'Narrated By', 'Language', 'Rating', 'Release Date', 'Length'])
    for i in range(len(book_name_list)):
        writer.writerow([book_name_list[i], book_href_list[i], subtitle_list[i],book_author_list[i],book_narrated_by_list[i],book_language_list[i],book_rating_list[i],book_release_date_list[i],book_length_list[i]])

