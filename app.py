from flask import Flask, request, render_template, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configure MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'Local instance MySQL80'
app.config['MYSQL_PASSWORD'] = 'Whysoserious123#'
app.config['MYSQL_DB'] = 'categoriesDB'

mysql = MySQL(app)

# Define Category and Product Tables
create_categories_table = """
CREATE TABLE IF NOT EXISTS categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
)
"""

create_products_table = """
CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
)
"""

create_category_product_table = """
CREATE TABLE IF NOT EXISTS category_product (
    category_id INT,
    product_id INT,
    PRIMARY KEY (category_id, product_id),
    FOREIGN KEY (category_id) REFERENCES categories(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
)
"""

with app.app_context():
    cur = mysql.connection.cursor()
    cur.execute(create_categories_table)
    cur.execute(create_products_table)
    cur.execute(create_category_product_table)
    mysql.connection.commit()
    cur.close()


# Routes

# 1. Add a category
@app.route('/api/categories', methods=['POST'])
def add_category():
    data = request.get_json()
    name = data['name']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO categories (name) VALUES (%s)", (name,))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': 'Category added successfully'})


# 2. Add Product mapped to a category or categories.
@app.route('/api/products', methods=['POST'])
def add_product():
    data = request.get_json()
    name = data['name']
    price = data['price']
    categories = data['categories']

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO products (name, price) VALUES (%s, %s)", (name, price))
    product_id = cur.lastrowid

    # Insert into category_product table
    values = [(category, product_id) for category in categories]
    cur.executemany("INSERT INTO category_product (category_id, product_id) VALUES (%s, %s)", values)

    mysql.connection.commit()
    cur.close()
    return jsonify({'message': 'Product added successfully'})


# 3. Get all categories with all its child categories mapped to it.
@app.route('/api/categories', methods=['GET'])
def get_categories():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM categories")
    categories = cur.fetchall()

    result = []
    for category in categories:
        cur.execute("SELECT product_id FROM category_product WHERE category_id = %s", (category['id'],))
        child_categories = [item['product_id'] for item in cur.fetchall()]
        category['child_categories'] = child_categories
        result.append(category)

    cur.close()
    return jsonify(result)


# 4. Get all products by a category.
@app.route('/api/products/<int:category_id>', methods=['GET'])
def get_products_by_category(category_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT product_id FROM category_product WHERE category_id = %s", (category_id,))
    product_ids = [item['product_id'] for item in cur.fetchall()]

    if not product_ids:
        return jsonify([])

    cur.execute("SELECT * FROM products WHERE id IN %s", (tuple(product_ids),))
    products = cur.fetchall()
    cur.close()
    return jsonify(products)


# 5. Update product details (name, price, etc.)
@app.route('/api/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    name = data['name']
    price = data['price']

    cur = mysql.connection.cursor()
    cur.execute("UPDATE products SET name = %s, price = %s WHERE id = %s", (name, price, product_id))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': 'Product updated successfully'})


app = Flask(__name__, template_folder='Template')


# Frontend
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
