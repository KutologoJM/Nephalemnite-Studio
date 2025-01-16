import requests

# Define the base URL of the API
base_url = "https://example.com/api"

# Make a GET request to retrieve information
response = requests.get(f"{base_url}/books")

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    books_data = response.json()
    # Process the data
    for book in books_data:
        print(f"Title: {book['title']}, Author: {book['author']}")
else:
    print("Error:", response.status_code)
