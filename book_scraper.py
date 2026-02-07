import requests
from bs4 import BeautifulSoup
import csv
import time

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"

def scrape_books():
    books = []

    for page in range(1, 51):
        url = BASE_URL.format(page)
        print(f"Scraping page {page}...")

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Error fetching page {page}: {e}")
            continue

        soup = BeautifulSoup(response.text, "html.parser")
        book_items = soup.select("article.product_pod")

        for book in book_items:
            try:
                title = book.h3.a["title"]
                price = book.select_one(".price_color").text.strip()
                availability = book.select_one(".availability").text.strip()

                rating_class = book.p["class"]
                rating = rating_class[1] if len(rating_class) > 1 else "Not rated"

                books.append([title, price, rating, availability])
            except Exception as e:
                print(f"Error parsing book: {e}")
                continue

        time.sleep(1)  # rate limiting

    return books

def save_to_csv(books):
    with open("books.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Price", "Rating", "Availability"])
        writer.writerows(books)

    print(f"Saved {len(books)} books to books.csv")

if __name__ == "__main__":
    books_data = scrape_books()
    save_to_csv(books_data)