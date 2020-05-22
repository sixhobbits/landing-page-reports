from settings import SCRAPING_BEE_API_KEY
import requests

def get_html(url):
    response = requests.get(
        url="https://app.scrapingbee.com/api/v1/",
        params={
            "api_key": SCRAPING_BEE_API_KEY,
            "url": url
        },

    )
    html = response.content
    return html


