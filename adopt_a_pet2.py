# Import modules and classes from Flask framework
from flask import Flask, render_template, jsonify
import json

# Create a Flask application instance 
app = Flask(__name__)

# Load pet data from a JSON file ("pets.json")
def load_pet_data():
    with open('pets.json', 'r') as file:
        return json.load(file)

# Define a route to get pet data in JSON format 
@app.route('/get_pet_data')
def get_pet_data():
    # Load pet data from JSON file
    pet_data = load_pet_data()
    # Convert pet data to JSON format and return as response 
    return jsonify(pet_data)

#Define main page route
@app.route('/')
def index():
  return render_template('index.html')

# Define a route to display a list of animals of a specific type
@app.route('/animals/<pet_type>')
def animals(pet_type):
  # Load pet data from JSON file
  pet_data = load_pet_data()
    
  # Get the list of pets of the specified pet_type
  pets_of_type = pet_data.get(pet_type, [])

  # Pass pet_type and pets_of_type as context 
  return render_template('animals.html', pet_type=pet_type, pets=pets_of_type)

# Define route to display details of a specified pet
@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
    #Load pet data from JSON file
    pet_data = load_pet_data()
    
    # Get the list of pets of the specified pet_type
    pets_of_type = pet_data.get(pet_type, [])
    
    # Check if the provided pet_id is within valid range
    if 0 <= pet_id < len(pets_of_type):
        # Retrieve the selected pet based on pet_id
        selected_pet = pets_of_type[pet_id]
        return render_template('pet.html', selected_pet=selected_pet)
    else:
        return "Pet not found"

# Start Flask application when script is executed  
if __name__ == '__main__':
    app.run(debug=True)