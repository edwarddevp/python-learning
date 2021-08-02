import requests
from bs4 import BeautifulSoup
import pandas


def getPageProperties(page):
    properties = page.find_all("div", {"class": "propertyRow"})

    for property in properties:
        propertyData = {}
        address = property.find_all("span", {"class": "propAddressCollapse"})
        propertyData["Address"] = address[0].text.strip()
        try:
            propertyData["Locality"] = address[1].text.strip()
        except (AttributeError, TypeError):
            propertyData["Locality"] = None
        propertyData["Price"] = property.find(
            "h4", {"class": "propPrice"}).text.strip()
        try:
            propertyData["Beds"] = property.find("span", {"class": "infoBed"})\
                .find('b').text.strip()
        except (AttributeError, TypeError):
            propertyData["Beds"] = None
        try:
            propertyData["Area"] = property.find("span", {"class": "infoSqFt"})\
                .find('b').text.strip()
        except (AttributeError, TypeError):
            propertyData["Area"] = None
        try:
            propertyData["Full Baths"] = property.find("span", {"class": "infoValueFullBath"})\
                .find('b').text.strip()
        except (AttributeError, TypeError):
            propertyData["Full Baths"] = None
        try:
            propertyData["Half Baths"] = property.find("span", {"class": "infoValueHalfBath"})\
                .find('b').text.strip()
        except (AttributeError, TypeError):
            propertyData["Half Baths"] = None
        for feature in property.find_all("div", {"class": "columnGroup"}):
            try:
                if "Lot Size" in feature.find('span', {"class": "featureGroup"}).text.strip():
                    propertyData["Lot Size"] = feature.find(
                        'span', {"class": "featureName"}).text.strip()
            except (AttributeError, TypeError):
                pass
        propertiesData.append(propertyData)


propertiesData = []
base_url = 'http://pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s={}.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0', }

request = requests.get(base_url.format(0), headers=headers)
content = request.content
# First Page
soup = BeautifulSoup(content, "html.parser")
getPageProperties(soup)

# get total number of pages
page_nr = int(soup.find_all("a", {"class": "Page"})[-1].text)

# iterate the other pages
for page in range(10, page_nr*10, 10):
    request = requests.get(base_url.format(str(page)), headers=headers)
    content = request.content
    soup = BeautifulSoup(content, "html.parser")
    getPageProperties(soup)


df = pandas.DataFrame(propertiesData)
df.to_csv("output.csv")
