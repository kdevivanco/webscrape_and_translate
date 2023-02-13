import requests
from bs4 import BeautifulSoup
import csv

# Send an HTTP request to the website's server
url = 'https://www.example.com'

proxies = {
  'http': 'http://10.10.1.10:3128',
  'https': 'http://10.10.1.10:1080',
}

response = requests.get(url, proxies=proxies)

if response.status_code == 200:
    print("Successful request, response code:", response.status_code)
else:
    print("Request failed, response code:", response.status_code)

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')
data = soup.find_all('div', class_='data-class')

# Extract the data
data_list = []
for item in data:
    data_item = {}
    data_item['data_field_1'] = item.find('div', class_='data-field-1').text
    data_item['data_field_2'] = item.find('div', class_='data-field-2').text
    data_list.append(data_item)

print(data_list)


# Store the data
with open('data.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['data_field_1', 'data_field_2'])
    writer.writeheader()
    for data_item in data_list:
        if data_item['data_field_1'] and data_item['data_field_2']:
            writer.writerow(data_item)

