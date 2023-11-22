# Category and Product Assignment

This project implements a RESTful API for managing categories and products. The backend is built using Python with Flask and MySQL as the database, and the frontend is a simple HTML/CSS interface with JavaScript for dynamic functionality.

## Components

### Backend (Flask and MySQL)

1. **app.py**: Contains the main Flask application. It defines RESTful endpoints for CRUD operations on categories and products. The application uses the Flask-MySQLdb extension for MySQL connectivity.

2. **database.sql**: SQL script for creating the necessary database and tables.

3. **requirements.txt**: Lists the Python dependencies. Install them using `pip install -r requirements.txt`.

### Frontend (HTML, CSS, and JavaScript)

1. **index.html**: The main HTML file that displays the interface. It includes sections for adding categories, adding products, listing categories with child categories, listing products by category, and updating product details.

2. **style.css**: Stylesheet for formatting and styling the HTML elements.

3. **script.js**: JavaScript file for handling dynamic interactions with the backend. It includes functions for adding categories and products, fetching categories and products, and updating product details.

## Setup and Running

### Backend Setup

1. Install the required Python packages: `pip install -r requirements.txt`.

2. Set up a MySQL database. Execute the SQL script in `database.sql` to create the necessary tables.

3. Configure the MySQL connection details in `app.py`:

    ```python
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'your_password'
    app.config['MYSQL_DB'] = 'categoriesDB'
    ```

4. Run the Flask application:

    ```bash
    python app.py
    ```

### Frontend Setup

1. Open `index.html` in a web browser.

2. Interact with the provided interface to add categories, add products, view categories with child categories, view products by category, and update product details.

## API Endpoints

- `POST /category`: Add a new category.
- `POST /product`: Add a new product mapped to one or more categories.
- `GET /categories`: Get all categories with child categories.
- `GET /products/{category_id}`: Get all products by a category.
- `PUT /product/{product_id}`: Update product details.

