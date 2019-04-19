from zomato import zomato
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pprint
import json

total_data=[]
for i in zomato():
    dic={}
    driver=webdriver.Chrome()
    driver.get(i)
    page=driver.execute_script("return document.documentElement.outerHTML")
    driver.quit()
    soup=BeautifulSoup(page,"html.parser")

    seeMore=soup.findAll("a",class_="zred")
    for j in seeMore:
        seeMore_All=j["href"]

        driver2=webdriver.Chrome()
        driver2.get(seeMore_All)
        single_Page=driver2.execute_script("return document.documentElement.outerHTML")
        driver2.quit()
        soup2=BeautifulSoup(single_Page,"html.parser")

        names=soup2.findAll("div",class_="col-s-12")
        rating=soup2.findAll("div",class_="ta-right floating search_result_rating col-s-4 clearfix")
        address=soup2.findAll("div",class_="col-m-16 search-result-address grey-text nowrap ln22")
        price=soup2.findAll("span",class_="col-s-11 col-m-12 pl0")
        for i in range(len(names)-1):
            all_name=names[i].text.strip().split("\n")
            # print(all_name)
            if len(all_name)==5:
                dic["name"]=all_name[1].strip()
            else:
                dic["name"]=all_name[0].strip()

            place=all_name[-1]
            dic["place"]=place
        # print(dic)

            all_rating=rating[i].find("div")
            rating_text=all_rating.text.strip()
            dic["rating"]=rating_text

            votes=rating[i].find("span")
            if type(votes) != type(None):
                dic["reviews"]=votes.text
            else:
                dic["reviews"]="0 votes"

        #    here I find address of hotel.
            dic["address"]=address[i].text

            id=all_rating.get("data-res-id")
            dic["id"]=id

            all_price=price[i].text
            dic["price"]=all_price[1:]
            pprint.pprint(dic)
            total_data.append(dic)
    # break
with open("zomatox.json","w+") as file:
    data=json.dumps(total_data)
    file.write(data)
