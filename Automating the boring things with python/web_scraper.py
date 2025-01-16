from bs4 import BeautifulSoup
import requests

webpage = requests.get("https://books.toscrape.com")
soup = BeautifulSoup(webpage.text, "lxml")

directory = soup.find("ol", class_="row")
book_items = directory.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
with open("books.html", "a") as file:
    for book_item in book_items:
        title = book_item.h3.a["title"]
        rating = book_item.p["class"][1]
        price = book_item.find(class_="price_color").get_text("£")[1:]
        link = book_item.a["href"]
        file.write(f"Title: {title}\n")
        if rating == "One":
            file.write(f"Rating: {rating} star\n")
        else:
            file.write(f"Rating: {rating} stars\n")
        file.write(f"Price: {price} pounds\n")
        file.write(f"Link: books.toscrape.com/{link}\n")
        file.write("\n")
