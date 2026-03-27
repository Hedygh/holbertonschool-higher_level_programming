from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_products_from_json():
    with open('products.json', 'r', encoding='utf-8') as file:
        return json.load(file)

def read_products_from_csv():
    with open('products.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        products = []

        for row in reader:
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            })

        return products

def read_products_from_sql():
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()

        conn.close()

        return [dict(row) for row in rows]
    except sqlite3.Error:
        return None

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error='Wrong source')

    if source == 'json':
        products_list = read_products_from_json()
    elif source == 'csv':
        products_list = read_products_from_csv()
    else:
        products_list = read_products_from_sql()
        if products_list is None:
            return render_template('product_display.html', error='Database error')

    if product_id is not None:
        products_list = [
            product for product in products_list
            if str(product.get('id')) == str(product_id)
        ]

        if not products_list:
            return render_template('product_display.html', error='Product not found')

    return render_template('product_display.html', products=products_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)