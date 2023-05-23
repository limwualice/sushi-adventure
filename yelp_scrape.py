import requests
import pandas as pd
from config import ACCESS_TOKEN
import ast



def get_reviews(business_id, limit):
    url = f'https://api.yelp.com/v3/businesses/{business_id}/reviews'
    headers = {
        'Authorization': f'Bearer {ACCESS_TOKEN}'
    }
    params = {
        'limit': limit  # Set the limit to 21 reviews per request
    }
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    reviews = data['reviews']
    return reviews

search_url = 'https://api.yelp.com/v3/businesses/search'
search_params = {
    'term': 'sushi',
    'location': 'Los Angeles, CA',
    'categories': 'restaurants',
    'limit': 50  # Set a lower limit here
}
headers = {
    'Authorization': f'Bearer {ACCESS_TOKEN}'
}

business_list = []  # Initialize an empty list to store results

# Make multiple requests with different offsets
for offset in range(0, 10, search_params['limit']):
    
    search_params['offset'] = offset
    search_response = requests.get(search_url, headers=headers, params=search_params)
    search_data = search_response.json()
    businesses = search_data['businesses']

    # Extract the relevant information from the API response
    for business in businesses:
        name = business['name']
        rating = business['rating']
        review_count = business['review_count']
        price = business.get('price', 'N/A')
        location = business['location']

    # Fetch the reviews for the current business
        business_id = business['id']
        reviews = get_reviews(business_id, 100)
        review_texts = [review['text'] for review in reviews]


        business_list.append({
            'Name': name,
            'Rating': rating,
            'Reviews': review_count,
            'Price': price,
            'Location': location,
            'ReviewsData': review_texts
        })

# Create a DataFrame from the list of dictionaries
df = pd.DataFrame(business_list)

# Save the DataFrame
df.to_csv('sushi_reviews.csv', index=False)
