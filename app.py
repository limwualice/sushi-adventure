import random
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

# Load the data frame
df = pd.read_csv('cleaned_business_reviews.csv')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input from the form
    state=request.form.get('state')
    city=request.form.get('city')
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
    RestaurantsAttire = request.form.get('RestaurantsAttire')
    validated = request.form.get("validated")
    garage = request.form.get("garage")
    lot = request.form.get("lot")
    Alcohol = request.form.get("Alcohol")

    # Create a dictionary to store the filter conditions
    filters = {}
    column_interests = {}

    if state != "I don't care":
        filters['state'] = state
        column_interests['state'] = True
    else:
        column_interests['city'] = False

    if city != "":
        filters['city'] = city
        column_interests['city'] = True
    else:
        column_interests['city'] = False

    if stars_x != "I don't care":
        filters['stars_x'] = float(stars_x)
        column_interests['stars_x'] = True
    else:
        column_interests['stars_x'] = False

    if RestaurantsTakeOut != "I don't care":
        filters['RestaurantsTakeOut'] = RestaurantsTakeOut
        column_interests['RestaurantsTakeOut'] = True
    else:
        column_interests['RestaurantsTakeOut'] = False

    if RestaurantsDelivery != "I don't care":
        filters['RestaurantsDelivery'] = RestaurantsDelivery
        column_interests['RestaurantsDelivery'] = True
    else:
        column_interests['RestaurantsDelivery'] = False

    if BusinessAcceptsCreditCards != "I don't care":
        filters['BusinessAcceptsCreditCards'] = BusinessAcceptsCreditCards
        column_interests['BusinessAcceptsCreditCards'] = True
    else:
        column_interests['BusinessAcceptsCreditCards'] = False

    if RestaurantsPriceRange2 != "I don't care":
        filters['RestaurantsPriceRange2'] = float(RestaurantsPriceRange2)
        column_interests['RestaurantsPriceRange2'] = True
    else:
        column_interests['RestaurantsPriceRange2'] = False

    if RestaurantsGoodForGroups != "I don't care":
        filters['RestaurantsGoodForGroups'] = RestaurantsGoodForGroups
        column_interests['RestaurantsGoodForGroups'] = True
    else:
        column_interests['RestaurantsGoodForGroups'] = False

    if RestaurantsReservations != "I don't care":
        filters['RestaurantsReservations'] = RestaurantsReservations
        column_interests['RestaurantsReservations'] = True
    else:
        column_interests['RestaurantsReservations'] = False

    if HasTV != "I don't care":
        filters['HasTV'] = HasTV
        column_interests['HasTV'] = True
    else:
        column_interests['HasTV'] = False

    if GoodForKids != "I don't care":
        filters['GoodForKids'] = GoodForKids
        column_interests['GoodForKids'] = True
    else:
        column_interests['GoodForKids'] = False

    if valet != "I don't care":
        filters['valet'] = valet
        column_interests['valet'] = True
    else:
        column_interests['valet'] = False

    if RestaurantsAttire != "I don't care":
        filters['RestaurantsAttire'] = RestaurantsAttire
        column_interests['RestaurantsAttire'] = True
    else:
        column_interests['RestaurantsAttire'] = False

    if validated != "I don't care":
        filters['validated'] = validated
        column_interests['validated'] = True
    else:
        column_interests['validated'] = False

    if garage != "I don't care":
        filters['garage'] = garage
        column_interests['garage'] = True
    else:
        column_interests['garage'] = False

    if lot != "I don't care":
        filters['lot'] = lot
        column_interests['lot'] = True
    else:
        column_interests['lot'] = False

    if Alcohol != "I don't care":
        filters['Alcohol'] = Alcohol
        column_interests['Alcohol'] = True
    else:
        column_interests['Alcohol'] = False

    # Apply the filters to the DataFrame
    filtered_df = df.copy()

    for column, value in filters.items():
        if value == "I don't care":
            continue
        else:
            filtered_df = filtered_df[filtered_df[column] == value]

    # Get the unique restaurant names
    restaurants = filtered_df[['city','state','name','stars_x','RestaurantsTakeOut', 'RestaurantsDelivery','BusinessAcceptsCreditCards','RestaurantsPriceRange2',
                               'RestaurantsReservations', 'RestaurantsGoodForGroups','HasTV', 'GoodForKids', 'valet','RestaurantsAttire', 'validated',
                               'garage', 'lot', 'Alcohol'
    ]]

    return render_template('result.html', restaurants=restaurants, column_interests=column_interests)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
