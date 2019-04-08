import requests,pprint,webbrowser
from bs4 import BeautifulSoup
url="https://gaana.com/playlist/gaana-dj-bollywood-top-50-1"
soup=requests.get(url).text

parser=BeautifulSoup(soup,"html.parser")
data=parser.find("div",class_="s_c")

song_Name=data.findAll("div", class_="playlist_thumb_det")
name_list=[]
url_List=[]
count=1
for i in song_Name:
    a=i.find("a")
    url_List.append(a["href"])
    a_Tag=a.text
    name_list.append(str(count)+" "+a_Tag)
    count+=1
#here I find artist names
artist=data.findAll("li", class_="s_artist p_artist desktop")
count=0
for j in artist:
    # print (j.text)
    dic={}
    dic["song_Names"]=name_list[count]
    dic["artist_Names"]=j.text
    dic["url"]=url_List[count]
    count+=1
    print (dic)
user=int(input("enter the number which you want song "))
webbrowser.open_new_tab(url_List[user-1])
