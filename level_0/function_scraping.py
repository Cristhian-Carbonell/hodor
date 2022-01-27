from bs4 import BeautifulSoup
from requests_html import HTMLSession
from pprint import pprint

# initialize an HTTP session
session = HTMLSession()

def get_all_forms(url):
    """Returns all form tags found on a web page's `url`"""
    # GET request
    res = session.get(url)
    # for javascript driven website
    # res.html.render()
    soup = BeautifulSoup(res.html.html, "html.parser")
    return soup.find_all("form")

def get_form_details(form):
    """Returns the HTML details of a form.
    including action, method and list of form contros (inputs, etc)"""
    details = {}
    # get the form method (POST, GET, DELETE, etc)
    # if not specified, GET is the default in HTML
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})

    details["method"] = method
    details["inputs"] = inputs
    return details

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Enter the URL to vote: ")
        print("Example")
        print("python3 votes.py http://www.google.com")
        quit()
    url = sys.argv[1]
    forms = get_all_forms(url)
    for i, form in enumerate(forms, start=1):
        form_details = get_form_details(form)
        print("="*50, f"form #{i}", "="*50)
        print(form_details)

