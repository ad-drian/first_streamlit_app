import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

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

fruit_choice = ''
streamlit.header('Fruityvice Fruit Advice!')
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
fruityvice_response_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_response_normalized)

streamlit.stop()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST")
my_data_rows = my_cur.fetchall()
streamlit.text("The Fruit Load List contains:")
streamlit.dataframe(my_data_rows)
fruit_add = streamlit.text_input('What fruit would you like to add?')
my_cur.execute("INSERT INTO FRUIT_LOAD_LIST values (fruit_add)")
streamlit.text("The fruit is being added to the Fruit Load List!!!")
