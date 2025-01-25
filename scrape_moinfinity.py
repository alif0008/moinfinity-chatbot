import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = "https://moinfinitydigital.com/"

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract all text content from <p> (paragraph) tags
    content = ""
    for paragraph in soup.find_all("p"):
        content += paragraph.get_text() + "\n"

    # Save the scraped content to a file
    with open("moinfinity_content.txt", "w", encoding="utf-8") as file:
        file.write(content)

    print("Website content saved to 'moinfinity_content.txt'")
else:
    print(f"Failed to access the website. HTTP Status Code: {response.status_code}")
