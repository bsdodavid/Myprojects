import requests
from bs4 import BeautifulSoup

url = 'https://www.flipkart.com/search?q=mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
response = requests.get(url).text
soup = BeautifulSoup(response, 'lxml')
jobs = soup.find_all('div', class_='_2kHMtA')

for index, lists in enumerate(jobs):
    # job_position = lists.find('div', class_='entity-result__primary-subtitle').text
    # name = lists.find('a', class_='app-aware-link').text
    # ara = lists.find('p', class_='relative').text
    # scrap = [job_position, name, para]
    model_specs = lists.find('li', class_="rgWa7D").text.replace('\n', '')
    model_name = lists.find('div', class_="_4rR01T").text.replace('\n', '')
    model_price = lists.find('div', class_="_30jeq3").text.replace('\n', '')
    mobile_specs = [model_specs, model_name, model_price]
    #with open(f'posts/{index}.txt', "w", encoding='UTF-8') as file:
        #file.write(f"Model Name: {model_name.strip()}\n")
        #file.write(f"Model Specs: {model_specs.strip()}\n")
        #file.write(f"Model Price: {model_price.strip()}\n")
    print(mobile_specs)


