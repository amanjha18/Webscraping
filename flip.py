import requests,pprint
from bs4 import BeautifulSoup

def fun(url):
    all_Data_List=[]
    var=requests.get(url)
    data=(var.text)
    parser=BeautifulSoup(data,"html.parser")
    soup=parser.findAll("div", class_="_1UoZlX")
    # print (soup)
    for i in soup:
        data=i.find("div", class_="_1-2Iqu row")

        new_data=data.find("div", class_="col col-7-12")
        name=new_data.find("div", class_="_3wU53n")
        names=name.text
        # print(names)
        spec=i.find("ul",class_="vFw0gD")
        # print (spec.text)
        datas=spec.findAll("li", class_="tVe95H")
        # print(datas)
        li=[]
        for j in datas:
            specification=j.text
            li.append(specification)

        price=parser.findAll("div",class_="_1vC4OE _2rQ-NK")
        for l in price:
            mobile_price=l.text
        # print (mobile_price)
        rating=parser.find("div",class_="hGSR34")
        all_Rating=(rating.text)
        dic={
        "mobiles_name": names,
        "specifications": li,
        "prices": mobile_price,
        "rating": float(all_Rating)
        }
        all_Data_List.append(dic)
    if len(all_Data_List)>1:
        pprint.pprint (all_Data_List)
    else:
        print ("out of stock")
        # break
user=input("enter number you want which one page ")
fun("https://www.flipkart.com/search?q=redmi&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+user)
