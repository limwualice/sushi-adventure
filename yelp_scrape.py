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
    'limit': 50  # Set a lower limit here
}

business_list = []  # Initialize an empty list to store results

# Make multiple requests with different offsets
for offset in range(0, 1000, params['limit']):
    params['offset'] = offset
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    businesses = data['businesses']

    # Extract the relevant information from the API response
    for business in businesses:
        name = business['name']
        rating = business['rating']
        review_count = business['review_count']
        price = business.get('price', 'N/A')
        location = business['location']
        business_list.append({'Name': name, 'Rating': rating, 'Reviews': review_count, 'Price': price, 'Location': location})

# Create a DataFrame from the list of dictionaries
df = pd.DataFrame(business_list)

# Save the DataFrame
df.to_csv('sushi.csv', index=False)


