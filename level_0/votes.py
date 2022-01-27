from bs4 import BeautifulSoup
from pprint import pprint
from urllib.parse import urljoin
import webbrowser
import sys

from function_scraping import get_all_forms, get_form_details, session


if len(sys.argv) < 2:
    print("Enter the URL to vote: ")
    print("Example")
    print("python3 votes.py http://www.google.com")
    quit()

url = sys.argv[1]

all_forms = get_all_forms(url)

for i, f in enumerate(all_forms, start=1):
    form_details = get_form_details(f)
    # pprint(form_details)
    # print("="*50)

data = {"id": "2054", "holdthedoor": "Submit+Query"}
if form_details["method"] == "post":
    for number in range(1024):
        res = session.post(url, data=data)

