import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pprint

def zomato():
    driver=webdriver.Chrome()
    driver.get("https://www.zomato.com/ncr")
    page=driver.execute_script("return document.documentElement.outerHTML")
    driver.quit()

    soup=BeautifulSoup(page,"html.parser")
    names=soup.find("div",class_="ui segment row")
    all_Names=names.findAll("a",class_="col-l-1by3 col-s-8 pbot0")
    count=1
    url_List=[]
    for i in all_Names:
        data=i.text
        dic={}
        var=""
        for j in data:
            if j=="(":
                break
            else:
                var=var+j
        ncr_names=(var.strip())
        dic[count]=ncr_names

        place=i.find("span",class_="grey-text hide-on-mobile")
        ncr_Place=(place.text[1:-1])
        dic["places"]=ncr_Place
        count+=1
        # print (dic)
        url=i["href"]
        url_List.append(url)
    return (url_List)
# print (zomato())
