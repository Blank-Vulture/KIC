#!/bin/bash

# addressエンドポイント
echo "Requesting address endpoint..."
curl -s "https://fakerapi.it/api/v2/address?_quantity=1&_locale=en_US" -o "address_response.json"
echo "Saved response to address_response.json"

# booksエンドポイント
echo "Requesting books endpoint..."
curl -s "https://fakerapi.it/api/v2/books?_quantity=1&_locale=en_US" -o "books_response.json"
echo "Saved response to books_response.json"

# companiesエンドポイント
echo "Requesting companies endpoint..."
curl -s "https://fakerapi.it/api/v2/companies?_quantity=1&_locale=en_US" -o "companies_response.json"
echo "Saved response to companies_response.json"

# creditCardsエンドポイント
echo "Requesting creditCards endpoint..."
curl -s "https://fakerapi.it/api/v2/creditCards?_quantity=1&_locale=en_US" -o "creditCards_response.json"
echo "Saved response to creditCards_response.json"

# imagesエンドポイント
echo "Requesting images endpoint..."
curl -s "https://fakerapi.it/api/v2/images?_quantity=1&_type=any&_height=300&_width=400&_locale=en_US" -o "images_response.json"
echo "Saved response to images_response.json"

# personsエンドポイント（現在の日時を取得）
current_date=$(date +%Y-%m-%d)
echo "Requesting persons endpoint..."
curl -s "https://fakerapi.it/api/v2/persons?_quantity=1&_locale=en_US&_birthday_end=${current_date}" -o "persons_response.json"
echo "Saved response to persons_response.json"

# placesエンドポイント
echo "Requesting places endpoint..."
curl -s "https://fakerapi.it/api/v2/places?_quantity=1&_locale=en_US" -o "places_response.json"
echo "Saved response to places_response.json"

# productsエンドポイント
echo "Requesting products endpoint..."
curl -s "https://fakerapi.it/api/v2/products?_quantity=1&_locale=en_US&_taxes=12&_categories_type=uuid&_price_min=20.50&_price_max=10320.99" -o "products_response.json"
echo "Saved response to products_response.json"

# textsエンドポイント
echo "Requesting texts endpoint..."
curl -s "https://fakerapi.it/api/v2/texts?_quantity=1&_characters=500&_locale=en_US" -o "texts_response.json"
echo "Saved response to texts_response.json"

# usersエンドポイント
echo "Requesting users endpoint..."
curl -s "https://fakerapi.it/api/v2/users?_quantity=1&_gender=male&_locale=en_US" -o "users_response.json"
echo "Saved response to users_response.json"

echo "All responses have been saved."