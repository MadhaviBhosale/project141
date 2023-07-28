import requests
from bs4 import BeautifulSoup
import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

headers = ["Name", "Distance", "Mass", "Radius"]

star_data = []

response = requests.get(START_URL)

soup = BeautifulSoup(response.content, "html.parser")

table = soup.find("table", class_="wikitable")

for row in table.find_all("tr")[1:]:
    cells = row.find_all("td")
    name = cells[1].text.strip()
    distance = cells[3].text.strip()
    mass = cells[4].text.strip()
    radius = cells[5].text.strip()
    star_data.append({
        "Name": name,
        "Distance": distance,
        "Mass": mass,
        "Radius": radius
    })

with open("stars_data.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=headers)
    writer.writeheader()
    writer.writerows(star_data)

print("Scraped Successfully")
