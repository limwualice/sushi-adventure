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

    # Perform the prediction using the KMeans model
    cluster = kmeans.predict([[rating, reviews, price]])

    # Convert cluster to a scalar value
    cluster = cluster[0]

    # Filter the data frame based on the predicted cluster
    filtered_df = df[df['Cluster'] == cluster]

    # Get the top 5 sushi restaurants
    top_restaurants = filtered_df.head(5)['Name'].tolist()

    # Render the template with the top 5 sushi restaurants
    return render_template('result.html', restaurants=top_restaurants)


if __name__ == '__main__':
    app.run(port=5001)

