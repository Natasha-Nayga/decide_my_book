
import random
import requests
from bs4 import BeautifulSoup

#key: 43ZQpMsuzW8ipjdbQ2tLNQ
#secret: WcBSF8AufNewoHoHT7375zdV6UqOX68C3gFfHmo


#no free api to get subject for isbn


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

url = 'https://www.amazon.co.uk/Best-Sellers-Books-Fiction/zgbs/books/62/ref=zg_bs_unv_b_2_275053_1'

response = requests.get(url, headers=headers)

#The retrieved answer can be viewed by running:

#print(response.text)

soup = BeautifulSoup(response.content, features="lxml")

#link = soup.select(".zg-item-immersion")
#print (link)

#for a in link.find('a', href=True):
    #print ("Found the URL:", a['href'])


title = soup.find_all(attrs={"data-rows": "1"})
random_list = []


for i in range(len(title)):
    #print (type(title[i]))
    #element_to_object = BeautifulSoup(title[i])
    element_to_object = title[i]
    result = element_to_object.get_text()
    stripped_list = result.lstrip("\n").rstrip("\n").strip()
    random_list.append(stripped_list)
    #stripped_list = random_list.strip("\n")

    #print (result)

#random.shuffle(random_list)
#print (random_list)

#stripped_list = random_list.strip("\n")
#print (random.sample(stripped_list, k=1))
print(random.sample(random_list, k=1))
#print (random.sample(random_list, k=1))
#random.sample(random_list, k=1)
#print (random_list.strip("\n"))


    #random_list = []
    #random_list.append(result.rstrip("\n"))
    #random.shuffle(random_list)
    #print (random_list)
    #print (random.shuffle(random_list))
    #print (random.sample(random_list, k=1))
    #print (new_list)
    #print (random.shuffle(result))


#[print (i) for i in title]
#print (title)
#iterate through a list
#turn list into a soup object to then find the text only
