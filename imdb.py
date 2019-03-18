import requests,pprint, json
from bs4 import BeautifulSoup

# ---------------------------------TASK-1------------------------------------------------------------------------------------#
def scrape_top_list():
	url="https://www.imdb.com/india/top-rated-indian-movies/"
	page=requests.get(url)
	soup=page.text
	parser=BeautifulSoup(soup,"html.parser")
	lister=parser.find("div",class_="lister")
	tbody=lister.find("tbody",class_="lister-list")
	trs=tbody.findAll("tr")

# here are find movie name and postion.
	i=1
	movie_list=[]
	for tr in trs:
		td=tr.find("td",class_="titleColumn")
		# print td
		a=td.find("a")
		movie_name=a.text
	
## Here are find movie urls.
		urls=td.a['href']
		url1=urls[0:17]
		url="https://www.imdb.com"+url1

## here are find years of all movies
		span=td.find("span", class_="secondaryInfo")
		year=(span.text)
		years=int(year[1:5])
		
## here are find rating of movies.
		rating_column=tr.find("td", class_="ratingColumn imdbRating")
		strong=rating_column.find("strong")
		rating=strong.text
		movie_dic={
		    "name": movie_name,
		    "year":int(years),
		    "position":i,
		    "rating":float(rating),
		    "url": url
		  }
		i=i+1
		movie_list.append(movie_dic)
	return movie_list
# pprint.pprint(scrape_top_list())
scrapped=scrape_top_list()

#--------------------------------------TASK-2-------------------------------------------------------#

def group_by_year(movies):
	year_dic={}
	for movie in movies:
		year=movie['year']
		# print year
		year_dic[year]=[]
	# return(year_dic)
		for mov in movies:
			if mov["year"]==year:
				year_dic[year].append(mov)
	return year_dic
# pprint.pprint(group_by_year(scrapped))
task2=group_by_year(scrapped)

# #----------------------------------------TASK-3--------------------------------------------------#

def group_by_decade(movies):
	dic={}
	for decade in range(1950,2020,10):
		lister=[]
		for dec in range(decade,decade+10):
			mainDic={}
			for new_dec in range(len(movies)):
				yearDic=movies[new_dec]['year']
				if yearDic==dec:
					mainDic=movies[new_dec]
					lister.append(mainDic)
		dic[decade] = lister
	return dic
# pprint.pprint(group_by_decade(scrapped))
task3=group_by_decade(scrapped)

#-----------------------------------------------TASK-4----------------------------------------------#
def scrape_movie_details(link):

	# link="https://www.imdb.com/title/tt3417422/"
	page=requests.get(link)
	soup=page.text
	parser=BeautifulSoup(soup,'html.parser')
	item=parser.find("div",class_="credit_summary_item")
	director=item.findAll("a")
	director_list=[]
# Here find directors names.
	for dir in director:
		a=dir.text
		director_list.append(a)
	name=parser.title.text[0:-14]

#Here find country name and language names.
	country=parser.find("div",{"class":"article","id":"titleDetails"})
	txt_block=country.findAll("div",class_="txt-block")
	language_list=[]
	for c in txt_block:
		h4=c.find("h4")
		if h4:
			if h4.text=="Country:":
				country_name=c.find("a").text
			if h4.text=="Language:":
				language=c.findAll("a")
				for i in language:
					language_list.append(i.text)

	poster=parser.find("div",class_="poster")
	image_url=poster.find('a').img['src']
	# print (image_url)

## here find all genre of all movies.
	genre_list=[]	
	article=parser.find("div",{"class":"article","id":"titleStoryLine"})
	genre=article.findAll("div",class_="see-more inline canwrap")
	for gen in genre:
		if gen.find("h4").text=="Genres:":
			GEN=gen.findAll("a")
			for G in GEN:
				genre_list.append(G.text)

##  HERE  are find runtime of movies.
	runtime=parser.find("div",class_="title_block")
	time=runtime.find("time").text.strip()
	# print (time)
	if (len(time) == 2):
		time = int(time[0])*60
	elif time[1]=="h":
		time=int(time[0])*60+int(time[3:-3])
	else:
		time=time[:-3]

## here are find bio of all movies.
	bio=parser.find("div",class_="summary_text").text.strip()
## here are dictionary for all keys and value. 
	dic4={
		"name": name,
		"director": director_list,
		"country": country_name,
		"language": language_list,
		"poster_image_url": image_url,
		"bio": bio,
		"runtime":time,
		"genre": genre_list
	}

	return dic4
# pprint.pprint(scrape_movie_details())



##--------------------------------------------TASK-5----------------------------------------------------------##

def movie_list_details(a):
	list1 = []
	for i in range(len(a)):
		data = (scrape_movie_details(a[i]['url']))
		# print (dataq)
		list1.append(data)
	return list1
(movie_list_details(scrapped))

total_movie_data = movie_list_details(scrapped)
pprint.pprint(total_movie_data)
with open('total_movie.json', 'w') as file:
	json = json.dumps(total_movie_data)
	file.write(json)