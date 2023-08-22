import streamlit
import pandas
import requests

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Favourites')
streamlit.text('🥣 Omega 3 & Blueberry oatmeal')
streamlit.text('🥗 Kale Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard Boiled Free Ranged Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect("Pick some fruits? ", list(my_fruit_list.index))
show_fruits = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(show_fruits)

streamlit.header('Fruityvice Fruit Advice!')
fruit_choice = text_input("Which fruit would you like to know about?")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
fruityvice_response_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_response_normalized)

