# homework
import requests
from bs4 import BeautifulSoup
import time

# task 1
file = open("car_list.csv", "w", encoding="utf-8_sig")
headings = 'მწარმოებელი-მოდელი,წელი,ფასი,ძრავი,გარბენი,გადაცემათა კოლოფი,საჭე\n'
file.write(headings)

for page in range(1, 6):

    url = f"https://www.myauto.ge/ka/s/00/0/00/00/00/00/00/00/avtomobilebi?stype=0&currency_id=3&customs_passed=2&det_search=1&ord=7&keyword=&category_id=m0&page={page}"
    # საიტზე აქტიურია scrapping დაცვა და ჰედერით მას ვცდებით
    context = requests.get(url, headers={"User-Agent":"Mozilla/5.0"}).text
    soup = BeautifulSoup(context, 'html.parser')
    container = soup.find('div', {'class': 'search-lists-container'})
    allCars = container.find_all("div", {'class': 'current-item'})

    for car in allCars:
        name = car.a.text.strip().partition(' ')[2]
        year = car.p.text.strip().partition(' ')[0]
        engine = car.find('div', {'class': 'car-detail-in cr-engine'}).p.text.strip()
        millage = car.find('div', {'class': 'car-detail-in cr-road'}).p.text.strip()
        transmission = car.find('div', {'class': 'car-detail-in cr-wheel'}).p.text.strip()
        strWheel = car.find('div', {'class': 'car-detail-in cr-ls cr-gas'}).p.text.strip()
        try:
            price = car.find('span', {'class': 'car-price'}).text.replace(',', '')
        except:
            AttributeError
            price = "ფასი შეთანხმებით"

        file.write(
            name + ',' + year + ',' + price + ',' + engine + ',' + millage + ',' + transmission + ',' + strWheel + "\n")
    # უმჯობესია ეს ციფრი დაწით, თორემ ძაან დიდი ხანი მოუნდებით ინფოს წამოღებას :)
    time.sleep(15)
file.close()
