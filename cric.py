import requests,webbrowser,pprint
from bs4 import BeautifulSoup
def fun(url):
    page=requests.get(url).text
    # print (page)
    parser=BeautifulSoup(page,"html.parser")
    soup=parser.find("div",class_="cb-col cb-col-100 cb-padding-left0")
    main_Div=soup.findAll("div",class_="cb-col cb-col-100 cb-font-14 cb-lst-itm text-center")
    count=0

    for i in main_Div:
        name=i.find("div",class_="cb-col cb-col-67 cb-rank-plyr")
        a=i.find("a")["href"]
        list_Link.append(a)
        player_N=name.text
        country=i.find("div",class_="cb-font-12 text-gray").text
        count=count+1
        rating=i.find("div",class_="cb-col cb-col-17 cb-rank-tbl pull-right").text
        dic={}
        dic["player_Name"]=player_N
        dic["country"]=country
        dic["rating"]=rating
        dic["position"]=count
        pprint.pprint(dic)
        # print (count,name,rating.text)

user=(input("enter the input like- batting, bowling, all-rounder, teams   "))
url="https://www.cricbuzz.com/cricket-stats/icc-rankings/men/"+user
list_Link=[]
fun(url)
user2=int(input("enter the input and find profile of player position  "))
webbrowser.open_new_tab("https://www.cricbuzz.com"+list_Link[user2-1])
