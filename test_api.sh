#!/bin/bash

# Test Case 1: Create a normal hero
echo "Test Case 1: Creating a normal hero"
curl -X POST "http://localhost:8000/heroes/" \
-H "Content-Type: application/json" \
-d '{
    "name": "Spider-Man",
    "age": 25,
    "secret_name": "Peter Parker"
}'
echo -e "\n"

# Test Case 2: Create a hero without age (optional field)
echo "Test Case 2: Creating a hero without age"
curl -X POST "http://localhost:8000/heroes/" \
-H "Content-Type: application/json" \
-d '{
    "name": "Batman",
    "secret_name": "Bruce Wayne"
}'
echo -e "\n"

# Test Case 3: Create a hero with invalid data (should fail)
echo "Test Case 3: Creating a hero with invalid data"
curl -X POST "http://localhost:8000/heroes/" \
-H "Content-Type: application/json" \
-d '{
    "name": "",
    "age": -5,
    "secret_name": ""
}'
echo -e "\n"
