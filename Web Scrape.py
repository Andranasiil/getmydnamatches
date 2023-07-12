import requests
from bs4 import BeautifulSoup

# Login information
login_url = 'https://example.com/login'
username = 'your_username'
password = 'your_password'

# Create a session
session = requests.Session()

# Send a POST request to the login page with the login credentials
login_data = {
    'username': username,
    'password': password
}
response = session.post(login_url, data=login_data)

# Check if login was successful
if response.status_code == 200:
    # Logged in successfully
    # Now you can make subsequent requests and scrape the content

    # Example: Scrape a page after login
    page_url = 'https://example.com/protected_page'
    page_response = session.get(page_url)

    # Parse the HTML using Beautiful Soup
    soup = BeautifulSoup(page_response.content, 'html.parser')

    # Scraping code goes here
    # Use Beautiful Soup methods to extract the desired information from the HTML

    # Example: Extract the title of the page
    title = soup.title.string
    print(f"Page Title: {title}")
else:
    print("Login failed.")
