from bs4 import BeautifulSoup as BS
import requests
from lxml import etree


url = "https://yandex.ru/pogoda/bryansk/details"
headers = {
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.134 YaBrowser/22.7.0.1842 Yowser/2.5 Safari/537.36"
}


def parse_from_yandex():
    list_temp = parse_from_yandex_temp()
    condition = parse_from_yandex_condition()
    pressure = parse_from_yandex_pressure()
    humidity = parse_from_yandex_humidity()
    print(list_temp[0])




def parse_from_yandex_temp():
    list_temp = []
    req = requests.get(url=url, headers=headers)
    soup = BS(req.text, "lxml")
    all = soup.find_all("table", class_="weather-table")
    day = soup.find_all("tr", class_="weather-table__row")
    #print(all)
    temp_morning = soup.find_all("div", class_="weather-table__temp")
    count = 0
    for i in temp_morning:
        if count == 4:
            break
        list_temp.append(i.get_text())
        count += 1
    #print(list_temp)
    return list_temp


def parse_from_yandex_condition():
    req = requests.get(url=url, headers=headers)
    soup = BS(req.text, "lxml")
    ost = soup.find_all("td", class_="weather-table__body-cell weather-table__body-cell_type_condition")
    condition = []
    count = 0
    for i in ost:
        if count == 4:
            break
        condition.append(i.get_text())
        count += 1
    #print(condition)
    return condition



def parse_from_yandex_pressure():
    req = requests.get(url=url, headers=headers)
    soup = BS(req.text, "lxml")
    ost = soup.find_all("td", class_="weather-table__body-cell weather-table__body-cell_type_air-pressure")
    pressure = []
    count = 0
    for i in ost:
        if count == 4:
            break
        pressure.append(i.get_text())
        count += 1
    # print(pressure)
    return pressure

# def youtube(search):
#     url = "https://www.youtube.com/results?search_query=пашка"
#     req = requests.get(url=url, headers=headers)
#     soup = BS(req.text, "lxml")
#     tree = etree.HTML(req.text)
#     qa = tree.xpath('//*[@id="video-title"]/yt-formatted-string')
#     #print(soup)
#     print(qa)
#     asd = soup.find("a", id = "video-title")
#     #print(asd)
#     return humidity

def parse_from_yandex_humidity():
    req = requests.get(url=url, headers=headers)
    soup = BS(req.text, "lxml")
    ost = soup.find_all("td", class_="weather-table__body-cell weather-table__body-cell_type_humidity")
    humidity = []
    count = 0
    for i in ost:
        if count == 4:
            break
        humidity.append(i.get_text())
        count += 1
    # print(humidity)
    return humidity


# pars()
a = "пашка"
parse_from_yandex()