import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.footballdb.com/statistics/nfl/player-stats/rushing/2022/regular-season"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', {'class': 'statistics'})

    if table:
        rows = table.find_all('tr')
        headers = [header.text.strip() for header in rows[0].find_all('th')] 
        player_data = []

        for row in rows[1:]:
            cells = row.find_all('td')
            data = {headers[i]: cell.text.strip() for i, cell in enumerate(cells)} 
            player_data.append(data)


        with open('player_stats.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            writer.writerows(player_data)

        print(f"Podatki shranjeni. Število igralcev: {len(player_data)}")
    else:
        print("Tabela ni najdena na spletni strani.")
else:
    print(f"Napaka pri dostopu do strani. Status koda: {response.status_code}")

