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

# Layout with columns for cards
col1, col2, col3, col4 = st.columns(4)

# Create a card for each Pokémon
for idx, pokemon_name in enumerate(pokemon_list):
    data = fetch_pokemon_data(pokemon_name)
    if data:
        name = data["name"].capitalize()
        types = [t["type"]["name"] for t in data["types"]]
        description = f"A {', '.join(types)} type Pokémon."

        # Fetch Pokémon image
        image_url = data["sprites"]["front_default"]

        # Determine which column to place the card in
        if idx % 4 == 0:
            with col1:
                st.image(image_url, caption=name, use_column_width=True)
                st.markdown(f"### {name}")
                st.write(description)
        elif idx % 4 == 1:
            with col2:
                st.image(image_url, caption=name, use_column_width=True)
                st.markdown(f"### {name}")
                st.write(description)
        elif idx % 4 == 2:
            with col3:
                st.image(image_url, caption=name, use_column_width=True)
                st.markdown(f"### {name}")
                st.write(description)
        else:
            with col4:
                st.image(image_url, caption=name, use_column_width=True)
                st.markdown(f"### {name}")
                st.write(description)
