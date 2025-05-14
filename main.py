import requests
from bs4 import BeautifulSoup

# Step 1: Choose the URL
url = "https://www.audible.com/search?keywords=book&node=18573211011"  # Replace with the target website

# Step 2: Send an HTTP request to the URL
response = requests.get(url)

# Step 3: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")
#print(soup)

span_ele= soup.find_all('span', class_ = 'bc-text bc-size-small bc-color-secondary')
span_subtitle = soup.find_all('span', class_ = 'bc-text bc-size-base bc-color-secondary');


#print(span_subtitle)
# anchor_tag =
# print(anchor_tag)
#
# # # Step 4: Extract desired content (example: all links)
for link in soup.find_all('a', class_= 'bc-link bc-color-link'):
    url = link.get('href')
    if url.__contains__("/pd/"):
        book_name = link.getText()
        if book_name.strip() != "":
            print(book_name.strip())
            print(url)
            print("--------------------")



# for link in span_subtitle:
#     text = link.getText()
#     print(text)


# for link in span_subtitle:
#     text = link.getText()
#     print(text)


# for link in span_ele:
#     text = link.getText()
#     if text.__contains__('Narrated'):
#         list = text.split(':')
#         print(f"{list[1].strip()}")
#     elif text.__contains__("Language"):
#         lan = text.split(':')
#         print(f"{lan[1].strip()}")
#     elif text.__contains__("ratings"):
#         rating = text.split()
#         print(f"{rating[0]}")
#     elif text.__contains__("Release"):
#         release = text.split()
#         print(f"{release[2]}")
#     elif text.__contains__("Length"):
#         length = text.split(':')
#         print(f"{length[1].strip()}")
#     print("------")