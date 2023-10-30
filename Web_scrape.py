import requests
from bs4 import BeautifulSoup
import sqlite3

# Connect to the database
conn = sqlite3.connect('database.sqlite3')
c = conn.cursor()

# Create the database table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS scraped_data (
    title TEXT,
    content TEXT
)''')

# Get the web page content
url = 'https://example.com/'
response = requests.get(url)

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the data from the web page
for article in soup.find_all('article'):
    title = article.find('h1').text
    content = article.find('p').text

    # Store the data in the database
    c.execute('''INSERT INTO scraped_data (title, content) VALUES (?, ?)''', (title, content))

# Commit the changes to the database
conn.commit()

# Close the database connection
conn.close()
