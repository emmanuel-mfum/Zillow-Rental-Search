from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C" \
      "%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122" \
      ".30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22" \
      "%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D" \
      "%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22" \
      "%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B" \
      "%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price" \
      "%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom" \
      "%22%3A12%7D "

FORM = "https://docs.google.com/forms/d/e/1FAIpQLSde_B6hdalMfP4F-0S5QHLRx7symvUKA2Xd9wqanA9eInTlqA/viewform?usp=sf_link"

header = {
    "User-Agent": "Defined",
    "Accept-Language": "en-US,en;q=0.9,fr-CA;q=0.8,fr;q=0.7"

}
response = requests.get(URL, headers=header)  # using headers is important,otherwise the GET request won't work
data = response.text

soup = BeautifulSoup(data, "html.parser")  # creates BeautifulSoup object
all_prices_elements = soup.select(".list-card-price")  # scrapes all the elements containing the prices
all_address_elements = soup.select(".list-card-info address")  # scrapes all the elements containing the addresses
all_links_elements = soup.select(".list-card-top a")  # # scrapes all the elements containing the links to the listings

print(len(all_prices_elements))
print(len(all_address_elements))
print(len(all_links_elements))

prices_list = []
address_list = []
links_list = []

for price_tag in all_prices_elements:
    price = price_tag.getText()
    if "/" in price:
        price = price.split("/")[0]
        prices_list.append(price)
    elif "+" in price:
        price = price.split("+")[0]
        prices_list.append(price)

address_list = [address.getText().split(" | ")[-1] for address in all_address_elements]

for url in all_links_elements:
    card_link = str(url.get("href"))  # get the content inside the href attribute
    if not card_link.startswith("https"):   # if the url scrapped is incomplete
        link = 'https://www.zillow.com' + card_link
        links_list.append(link)
    else:
        links_list.append(card_link)

chrome_driver = "****************************************"

driver = webdriver.Chrome(executable_path=chrome_driver)

for n in range(len(all_links_elements)):
    driver.get(FORM)
    time.sleep(5)
    address_field = driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div["
                                                 "1]/div/div[ "
                                                 "1]/input")
    address_field.send_keys(address_list[n])

    price_field = driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div["
                                               "1]/div/div[1]/input")
    price_field.send_keys(prices_list[n])

    link_field = driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div["
                                              "1]/div/div[1]/input")
    link_field.send_keys(links_list[n])

    submit_button = driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div/div/span")
    submit_button.click()
