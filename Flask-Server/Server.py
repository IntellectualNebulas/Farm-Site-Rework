from flask import Flask, jsonify
import csv
from pathlib import Path

app = Flask(__name__)
FILE_PATH = "Flask-Server/MenuItems.csv"

# Members API Route
@app.route("/menu")
def Menu():

        Foodname = []
        FoodPrice = []
        Drinks = []
        DrinkPrice = []

        with open(FILE_PATH, mode='r') as file:
            reader = csv.DictReader(file)

            # Empty lists to store column values

            # Iterating over each row
            for row in reader:
                Foodname.append(row['ItemName'])
                FoodPrice.append(row['FoodPrice'])
                Drinks.append(row['Drinks'])
                DrinkPrice.append(row['DrinkPrice'])

        return jsonify({
        "Foodname": Foodname,
        "FoodPrice": FoodPrice,
        "Drinks": Drinks,
        "DrinkPrice": DrinkPrice
        })

if __name__ == "__main__":
    app.run(debug=True)