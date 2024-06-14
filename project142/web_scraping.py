import requests
from bs4 import BeautifulSoup
import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

HEADERS = ["Name", "Distance", "Mass", "Radius"]
stars_data = []

response = requests.get(START_URL)
soup = BeautifulSoup(response.content, "html.parser")

tables = soup.find_all("table", {"class": "wikitable"})
table = tables[0]
star_table = soup.find_all('table')
table_rows = star_table[7].find_all('tr')
rows = table.find_all("tr")

for row in rows[1:]:
    columns = row.find_all("td")
    
    if len(columns) < 4:
        continue
    
    star_data = {
        "Name": columns[0].text.strip(),
        "Distance": columns[1].text.strip(),
        "Mass": columns[2].text.strip(),
        "Radius": columns[3].text.strip()
    }
    
    stars_data.append(star_data)

with open("stars_data.csv", "w", newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=HEADERS)
    writer.writeheader()
    writer.writerows(stars_data)

print("CSV file created successfully.")