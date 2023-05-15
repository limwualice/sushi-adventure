import requests
import pandas as pd
from config import ACCESS_TOKEN


url = 'https://api.yelp.com/v3/businesses/search'
headers = {
    'Authorization': f'Bearer {ACCESS_TOKEN}'
}
params = {
    'term': 'sushi',
    'location': 'Los Angeles, CA',
    'categories': 'restaurants',
    'limit': 10
}

response = requests.get(url, headers=headers, params=params)
data = response.json()

# Extract the relevant information from the API response
businesses = data['businesses']

# Create a list of dictionaries with the desired data
business_list = []
for business in businesses:
    name = business['name']
    rating = business['rating']
    review_count = business['review_count']
    business_list.append({'Name': name, 'Rating': rating, 'Reviews': review_count})

# Create a DataFrame from the list of dictionaries
df = pd.DataFrame(business_list)

# Save the DataFrame
df.to_csv('sushi.csv', index=False)

