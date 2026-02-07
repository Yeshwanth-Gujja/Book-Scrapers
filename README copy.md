# Book Data Scraper

A Python web scraping project that collects book information from an e-commerce website and stores it in a structured CSV file.

## Features
- Scrapes 50 pages (1000 books total)
- Extracts book title, price, rating, and availability
- Handles pagination automatically
- Implements rate limiting for ethical scraping
- Includes error handling for failed requests
- Saves extracted data to CSV format

## Technologies Used
- Python 3
- Requests
- BeautifulSoup4

## How to Run
1. Clone this repository
2. Install dependencies:
pip install -r requirements.txt
3. Run the scraper:
python book_scraper.py
4. Check the output in `books.csv`

## Sample Output

| Title | Price | Rating | Availability |
|------|-------|--------|--------------|
| A Light in the Attic | £51.77 | Three | In stock |

## Author
Your Name
