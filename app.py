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

# Define your color scheme
background_color = "#f0f4f8"  # Light background color
card_background_color = "#ffffff"  # White background for cards
text_color = "#333333"  # Dark text color

# Function to render Pokémon cards with complementary colors
def render_pokemon_card(name, types, image_url, description):
    st.markdown(f"""
    <div style="
        display: flex;
        flex-direction: column;
        align-items: center;
        border: 1px solid #ddd;
        border-radius: 10px;
        padding: 10px;
        margin: 10px;
        text-align: center;
        box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
        background-color: {card_background_color};
        color: {text_color};
    ">
        <img src="{image_url}" style="
            width: 120px;
            height: 120px;
            border-radius: 10px;
            object-fit: cover;
            border: 2px solid {text_color};
        " />
        <h3 style="margin: 10px 0;">{name}</h3>
        <p style="margin: 5px 0;">Type: {', '.join(types)}</p>
        <p style="margin: 5px 0;">{description}</p>
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
