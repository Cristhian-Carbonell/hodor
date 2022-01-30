from bs4 import BeautifulSoup
from pprint import pprint
from urllib.parse import urljoin
import webbrowser
import sys

from function_scraping import get_all_forms, get_form_details, session

if len(sys.argv) < 3:
    print("Enter the URL to vote: ")
    print("Example")
    print("python3 votes.py url id")
    quit()

url = sys.argv[1]

for number in range(4096):
    all_forms = get_all_forms(url)
    for i, f in enumerate(all_forms, start=1):
        form_details = get_form_details(f)
    data = {"id": sys.argv[2], "holdthedoor": "Submit+Query", "key": form_details["inputs"][2]["value"]}
    if form_details["method"] == "post":
        res = session.post(url, data=data)
