from flask import Flask, jsonify
import csv
from pathlib import Path

app = Flask(__name__)
FILE_PATHMENU = "Flask-Server/MenuItems.csv"
FILE_PATHSHOP = "Flask-Server/ShopProducts.csv"

# Menu API Route
@app.route("/menu")
def Menu():

        Foodname = []
        FoodPrice = []
        Drinks = []
        DrinkPrice = []

        with open(FILE_PATHMENU, mode='r') as file:
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

# Shop API Route
@app.route("/shop")
def Shop():

        ShopItem = []
        ShopPrice = []

        with open(FILE_PATHSHOP, mode='r') as file:
            reader = csv.DictReader(file)

            # Empty lists to store column values

            # Iterating over each row
            for row in reader:
                ShopItem.append(row['ShopItem'])
                ShopPrice.append(row['ShopPrice'])

        return jsonify({
        "ShopItem": ShopItem,
        "ShopPrice": ShopPrice,
        })


if __name__ == "__main__":
    app.run(debug=True)