import random
# import pickle
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

# # Load the KMeans model
# with open('kmeans.pkl', 'rb') as file:
#     kmeans = pickle.load(file)

# Load the data frame
df = pd.read_csv('businesses_reviews.csv')

# Define your Flask routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input from the form
    stars_x = request.form.get('stars_x')
    RestaurantsTakeOut = request.form.get('RestaurantsTakeOut')
    RestaurantsDelivery = request.form.get('RestaurantsDelivery')
    BusinessAcceptsCreditCards = request.form.get('BusinessAcceptsCreditCards')
    RestaurantsPriceRange2 = request.form.get('RestaurantsPriceRange2')
    RestaurantsReservations = request.form.get('RestaurantsReservations')
    RestaurantsGoodForGroups = request.form.get('RestaurantsGoodForGroups')
    HasTV = request.form.get('HasTV')
    GoodForKids = request.form.get('GoodForKids')
    valet = request.form.get('valet')

    # Create a dictionary to store the filter conditions
    filters = {
        'stars_x': stars_x,
        'RestaurantsTakeOut': RestaurantsTakeOut,
        'RestaurantsDelivery': RestaurantsDelivery,
        'BusinessAcceptsCreditCards': BusinessAcceptsCreditCards,
        'RestaurantsPriceRange2': RestaurantsPriceRange2,
        'RestaurantsReservations': RestaurantsReservations,
        'RestaurantsGoodForGroups': RestaurantsGoodForGroups,
        'HasTV': HasTV,
        'GoodForKids': GoodForKids,
        'valet': valet
    }

    # Apply the filters to the DataFrame
    filtered_df = df.copy()  # Create a copy of the original DataFrame

    # Iterate over the filters and apply each one
    for column, value in filters.items():
        if value == "True":
            filtered_df = filtered_df[filtered_df[column] == True]
        elif value == "I don't care":
            continue  # Skip the filter for "I don't care"

    # Now you have the filtered DataFrame based on the user's input
    # You can perform further operations or return the results as needed

    return render_template('result.html', filtered_data=filtered_df)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

