import streamlit
import pandas

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Favourites')
streamlit.text('🥣 Omega 3 & Blueberry oatmeal')
streamlit.text('🥗 Kale Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard Boiled Free Ranged Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.dataframe(my_fruit_list)

fruits_selected = streamlit.multiselect("Pick some fruits? ", list(my_fruit_list.index))
show_fruits = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(show_fruits)
