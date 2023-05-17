import random
import pickle
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

# Load the KMeans model
with open('kmeans.pkl', 'rb') as file:
    kmeans = pickle.load(file)

# Load the data frame
df = pd.read_csv('sushi_to_search.csv')

# Define your Flask routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input from the form
    rating = request.form.get('rating')
    reviews = request.form.get('reviews')
    price = request.form.get('price')

    # Validate the input values
    if not rating or not reviews or not price:
        if not rating:
            return "Your rating was wrong", 400
        elif not reviews:
            return "Your reviews was wrong", 400
        elif not price:
            return "Your price was wrong", 400
        else:
            return "something else", 400

    try:
        rating = float(rating)
        reviews = float(reviews)
        price = float(price)
    except ValueError:
        return "Invalid input values", 400

    # Perform the prediction using the KMeans model
    cluster = kmeans.predict([[rating, reviews, price]])

    # Convert cluster to a scalar value
    cluster = cluster[0]

    # Filter the data frame based on the predicted cluster
    filtered_df = df[df['Cluster'] == cluster]

    # Get all the sushi restaurants in the filtered cluster
    restaurants = filtered_df['Name'].tolist()

    # Randomly select 5 sushi restaurants
    random_restaurants = random.sample(restaurants, k=min(5, len(restaurants)))

    # Render the template with the random 5 sushi restaurants
    return render_template('result.html', restaurants=random_restaurants)

if __name__ == '__main__':
    app.run(port=5001)

