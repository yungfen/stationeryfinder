import streamlit as st
import requests
from PIL import Image
import pandas as pd
from functions import cook_breakfast
import sys
from elasticsearch import Elasticsearch
sys.path.append('srcs')

st.title("New Stationery Product Searcher")
st.subheader("Find new product, follow the trend with only one click!")
st.text("Search new products in stationery brands\n"
        "such as <b>Uni, Pilot, Pentel, and Zebra.<\b>, unsafe_allow_html=True")
URL_uni = "https://www.mpuni.co.jp/products/new_products.html"
URL_pilot = "https://www.pilot.co.jp/products/new/"
URL_pentel = "https://www.pentel.co.jp/products/"
URL_zebra = "https://www.zebra.co.jp/pro/newpro/"
searched = st.button('Search', key="search")

if searched:
    cook_breakfast()
    r = requests.get(URL_uni, URL_pilot)
    r2 = requests.get(URL_pentel, URL_zebra)
    soup = BeautifulSoup(r.text, 'html.parser')
    images = soup.find_all('img')
    df = pd.DataFrame(
        {
            "brands": ["Uni", "Pilot", "Pentel", "Zebra"],
            "new products": ["https://www.mpuni.co.jp/news/images/news/f19166375014652286571f570c3224ac53cc2520.jpg",
                             "https://www.mpuni.co.jp/news/images/news/eaeab95020cdf33b82f3beece3fbf242aaefe624.jpg",
                             "https://www.mpuni.co.jp/news/images/news/1192040b7826fd32ca895701a196c38754761134.jpg",
                             "https://www.mpuni.co.jp/news/images/news/5d81ef8c8ec9c6f8e001b181dacaec44534d5cca.jpg"]
        }
    )
    st.dataframe(
        df,
        column_config={
            "name": "Brand name",
            "product images": st.column_config.ImageColumn("new products", help="new product"),
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

# srcs/streamlit_app/app.py

DOMAIN = '0.0.0.0'
es = Elasticsearch()


def main():
    st.title('Search Medium Story')
    search = st.text_input('Enter search words:')
    if search:
        results = utils.index_search(es, INDEX, search, '', 0, PAGE_SIZE)

if __name__ == "__main__":
    main()