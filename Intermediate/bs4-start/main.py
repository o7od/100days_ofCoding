# with open('website.html') as fp:
#     soup = BeautifulSoup(fp, features='html.parser')

# # soup = BeautifulSoup("website.html", 'html.parser')
# # print(soup.title.string)

# # print(soup.prettify())
# # print(soup.p)

# # all_anchor_tags = soup.find_all(name="a")
# # for tags in all_anchor_tags:
# #     # print(tags.getText())
# #     print(tags.get("href"))

# # heading = soup.find(name="h1", id="name")
# # print(heading)

# # section_heading = soup.find(name="h3", class_="heading")
# # print(section_heading.get("class"))

# name = soup.select_one(selector="#name")
# print(name)

# headings = soup.select(selector='.heading')
# print(headings)

from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/newest")
soup = BeautifulSoup(markup=response.text, features='html.parser')

anchor_tags =soup.select("span.titleline > a")
news_titles = []
news_link = []
for tags in anchor_tags:
    news_titles.append(tags.string)
    news_link.append(tags.get('href'))


scores = soup.select("span.score")
upvotes = [int(score.string.split()[0]) for score in scores]

# print(news_titles)
# print(news_link)
max_upvotes = max(upvotes)

index_max = upvotes.index(max_upvotes)

print(news_titles[index_max])
print(news_link[index_max])
print(max_upvotes)


