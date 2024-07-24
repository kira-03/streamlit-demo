import streamlit as st
import requests

# Set the title of the web app
st.title("Pokémon Collections")

# Add a brief introduction
st.write("""
Welcome to the Pokémon Collections showcase! Here, you'll find information about various Pokémon, including their images, types, and descriptions.
""")

# Define a function to fetch Pokémon data from the API
def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        st.error(f"Error fetching data for {pokemon_name}")
        return None

# Define a list of Pokémon to display
pokemon_list = ["pikachu", "charmander", "bulbasaur", "squirtle"]

# Function to render Pokémon cards
def render_pokemon_card(name, types, image_url, description):
    st.markdown(f"""
    <div style="
        border: 2px solid #ddd;
        border-radius: 10px;
        padding: 10px;
        margin: 10px;
        text-align: center;
        box-shadow: 0px 0px 15px rgba(0,0,0,0.2);
        transition: transform 0.2s ease-in-out;
        background-color: #f9f9f9;
    " onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
        <img src="{image_url}" style="
            width: 150px;
            height: 150px;
            border-radius: 10px;
            object-fit: cover;
        " />
        <h3>{name}</h3>
        <p>{', '.join(types)}</p>
        <p>{description}</p>
    </div>
    """, unsafe_allow_html=True)

# Create a grid layout for the cards
cols = st.columns(4)

# Render each Pokémon card
for idx, pokemon_name in enumerate(pokemon_list):
    data = fetch_pokemon_data(pokemon_name)
    if data:
        name = data["name"].capitalize()
        types = [t["type"]["name"] for t in data["types"]]
        description = f"A {', '.join(types)} type Pokémon."
        image_url = data["sprites"]["front_default"]
        
        # Determine which column to use for the card
        col_idx = idx % 4
        with cols[col_idx]:
            render_pokemon_card(name, types, image_url, description)
