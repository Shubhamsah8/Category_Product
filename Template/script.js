// Function to update the category list in the HTML
function updateCategoryList(categories) {
  const categoryListContainer = document.getElementById('categoryList');
  categoryListContainer.innerHTML = '';

  categories.forEach(category => {
      const categoryElement = document.createElement('div');
      categoryElement.textContent = category.name;
      // Add more styling or information as needed

      categoryListContainer.appendChild(categoryElement);
  });
}

// Function to update the product list in the HTML
function updateProductList(products) {
  const productListContainer = document.getElementById('productList');
  productListContainer.innerHTML = '';

  products.forEach(product => {
      const productElement = document.createElement('div');
      productElement.textContent = `${product.name} - ${product.price}`;
      // Add more styling or information as needed

      productListContainer.appendChild(productElement);
  });
}

// Fetch categories and products on page load
window.onload = function() {
  // Example: Fetch categories and update the category list
  const mockCategories = [
      { id: 1, name: 'Electronics' },
      { id: 2, name: 'Clothing' },
      // Add more categories as needed
  ];

  updateCategoryList(mockCategories);

  // Example: Fetch products and update the product list
  const mockProducts = [
      { id: 1, name: 'Laptop', price: 999.99 },
      { id: 2, name: 'T-shirt', price: 19.99 },
      // Add more products as needed
  ];

  updateProductList(mockProducts);
}
