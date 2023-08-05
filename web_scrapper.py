import requests
from bs4 import BeautifulSoup

def scrape_news_website(url):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find all the articles on the page
            articles = soup.find_all('article')

            # Extract and print the title and URL of each article
            for article in articles:
                title = article.find('h2').text.strip()
                url = article.find('a')['href']
                print(f"Title: {title}")
                print(f"URL: {url}")
                print("---------------")

        else:
            print("Failed to retrieve data from the website.")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    news_url = 'https://www.thehindu.com/'   #scrapping from The Hindu newspaper 
    scrape_news_website(news_url)
