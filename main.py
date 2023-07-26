import streamlit as st
import requests
from bs4 import BeautifulSoup
from PIL import Image
import pandas as pd

st.title("New Stationery Product Searcher")
st.subheader("Find new product, follow the trend with only one click!")
st.markdown("Search new products in stationery brands\n"
            "such as **Uni, Pilot, Pentel, and Zebra.**")
URL_uni = "https://www.mpuni.co.jp/products/new_products.html"
URL_pilot = "https://www.pilot.co.jp/products/new/"
URL_pentel = "https://www.pentel.co.jp/products/"
URL_zebra = "https://www.zebra.co.jp/pro/newpro/"

searched = st.button("Search", key="search")
if searched:
    r = requests.get(URL_uni, URL_pilot)
    r2 = requests.get(URL_pentel, URL_zebra)
    soup = BeautifulSoup(r.text, 'html.parser')
    images = soup.find_all('img')
    df = pd.DataFrame(
        {
            "brands": ["Uni", "Pilot", "Pentel", "Zebra"],
            "new products": [URL_uni, URL_pilot, URL_pentel, URL_zebra]
        }
    )
    st.dataframe(
        df,
        column_config={
            "name": "App name",
            "stars": st.column_config.NumberColumn(
                "Github Stars",
                help="Number of stars on GitHub",
                format="%d ⭐",
            ),
            "url": st.column_config.LinkColumn("App URL"),
            "views_history": st.column_config.LineChartColumn(
                "Views (past 30 days)", y_min=0, y_max=5000
            ),
        },
        hide_index=True,
    )
    # for image in images:
    #    name = image['alt']
    #    link = image['src']
    #    image_open = Image.open(image)
    #    st.image(images, caption='new items')
    #    df = pd.DataFrame(
    #        {
    #            "name": ["uni", "pilot", "pentel", "zebra"],
    #            "url": [URL_uni, URL_pilot, URL_pentel, URL_zebra],
    #           "images": [images],
    #            "debut_date": ['day'],
    #        }
    #    )
    #    st.dataframe(
    #        df,
    #        column_config={
    #            "name": "Brand name",
    #            "url": st.column_config.LinkColumn("Website URL"),
    #            "debut_date": st.column_config.NumberColumn(
    #                "",
    #                help="debut date of the product",
    #                format="%d %m %Y",
    #            ),
    #        },
    #        hide_index=False,
    #    )
# uni: https://www.mpuni.co.jp/products/new_products.html
# pilot: https://www.pilot.co.jp/
# pentel: https://www.pentel.co.jp/products/
