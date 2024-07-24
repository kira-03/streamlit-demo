import streamlit as st

# Set the title of the web app
st.title("Pokémon Collections")

# Add a brief introduction
st.write("""
Welcome to the Pokémon Collections showcase! Here, you'll find information about various Pokémon and their characteristics.
""")

# Define a list of Pokémon with their details
pokemon_collection = [
    {"name": "Pikachu", "type": "Electric", "description": "A yellow Pokémon with electric powers."},
    {"name": "Charmander", "type": "Fire", "description": "A fire-type Pokémon resembling a small dinosaur."},
    {"name": "Bulbasaur", "type": "Grass/Poison", "description": "A grass-type Pokémon with a plant bulb on its back."},
    {"name": "Squirtle", "type": "Water", "description": "A water-type Pokémon resembling a small turtle."}
]

# Display each Pokémon's details
for pokemon in pokemon_collection:
    st.header(pokemon["name"])
    st.subheader(f"Type: {pokemon['type']}")
    st.write(pokemon["description"])
