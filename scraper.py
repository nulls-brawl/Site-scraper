import requests
from bs4 import BeautifulSoup
import csv

def scrape_nullbrawl():
    # URL of the website to scrape
    url = "https://nullbrawl.org"
    
    # Send a GET request to the website
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract relevant information
        title = soup.title.string if soup.title else "No title found"
        
        # Find all paragraph elements
        paragraphs = soup.find_all('p')
        
        # Extract links
        links = [a['href'] for a in soup.find_all('a', href=True)]
        
        # Save the extracted data to a CSV file
        with open('nullbrawl_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Title', 'Paragraphs', 'Links'])
            writer.writerow([title, len(paragraphs), len(links)])
        
        print(f"Title: {title}")
        print(f"Number of paragraphs: {len(paragraphs)}")
        print(f"Number of links: {len(links)}")
        print("Data saved to nullbrawl_data.csv")
    else:
        print(f"Failed to retrieve the website. Status code: {response.status_code}")

if __name__ == "__main__":
    scrape_nullbrawl()
