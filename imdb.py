import requests,pprint, json,os,random
import time
from bs4 import BeautifulSoup

# ---------------------------------TASK-1------------------------------------------------------------------------------------#
def scrape_top_list():
	time.sleep(random.randint(10,60))
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


# #--------------------------------------TASK-2-------------------------------------------------------#
#
# def group_by_year(movies):
# 	year_dic={}
# 	for movie in movies:
# 		year=movie['year']
# 		# print year
# 		year_dic[year]=[]
# 	# return(year_dic)
# 		for mov in movies:
# 			if mov["year"]==year:
# 				year_dic[year].append(mov)
# 	return year_dic
# # pprint.pprint(group_by_year(scrapped))
# task2=group_by_year(scrapped)
#
# # #----------------------------------------TASK-3--------------------------------------------------#
#
# def group_by_decade(movies):
# 	dic={}
# 	for decade in range(1950,2020,10):
# 		lister=[]
# 		for dec in range(decade,decade+10):
# 			mainDic={}
# 			for new_dec in range(len(movies)):
# 				yearDic=movies[new_dec]['year']
# 				if yearDic==dec:
# 					mainDic=movies[new_dec]
# 					lister.append(mainDic)
# 		dic[decade] = lister
# 	return dic
# # pprint.pprint(group_by_decade(scrapped))
# task3=group_by_decade(scrapped)
#
# #-----------------------------------------------TASK-4----------------------------------------------#
def scrape_movie_details(link):
	# one_link="https://www.imdb.com/title/tt3417422/"
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
	movie_time=runtime.find("time").text.strip()
	# print (time)
	if (len(movie_time) == 2):
		movie_time = int(movie_time[0])*60
	elif movie_time[1]=="h":
		movie_time=int(movie_time[0])*60+int(movie_time[3:-3])
	else:
		movie_time=movie_time[:-3]

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
		"runtime":movie_time,
		"genre": genre_list
	}

	return dic4
# pprint.pprint(scrape_movie_details(data))



# ##--------------------------------------------TASK-5----------------------------------------------------------##
#
# def movie_list_details(a):
#
# 	for i in range(len(a)):
# 		data = (scrape_movie_details(a[i]['url']))
# 		return (data)
# pprint.pprint(movie_list_details(scrapped))
# task5=(movie_list_details()
# #
# total_movie_data = movie_list_details(scrapped)
# pprint.pprint(total_movie_data)
# with open('total_movie.json', 'w') as file:
# 	json = json.dumps(total_movie_data)
# 	file.write(json)
##-------------------------------------TASK-6-----------------------##
# with open("total_movie.json","r") as f:
# 	movie_list_json=json.load(f)
# def analyse_movies_(movie_list):
# 	lan_list=[]
# 	dic={}
# 	for i in movie_list[0:10]:
# 		lan=i["language"]
# 		for j in lan:
# 			if j not in lan_list:
# 				lan_list.append(j)
# 		# print (lan_list)
# 	for k in lan_list:
# 		count=0
# 		for i in movie_list[0:10]:
# 			lan=i["language"]
# 			if k in lan:
# 				count=count+1
# 		dic[k]=count
# 	return (dic)
# # langueses=pprint.pprint (analyse_movies_(movie_list_json))
#
# ##---------------------------------------TASK-7-----------------------------##
# with open("total_movie.json", "r") as f:
# 	movie_dir=json.load(f)
# def analyse_movies_directors(movie_list):
# 	dir_list=[]
# 	dic={}
# 	for dir in movie_list[0:10]:
# 		director=dir["director"]
# 		# print (director)
# 		for i in director:
# 			# print (i)
# 			if i not in dir_list:
# 				dir_list.append(i)
# 		# return (dir_list)
# 	for new_dir in dir_list:
# 		count=0
# 		for dir in movie_list[0:10]:
# 			director=dir["director"]
# 			if new_dir in director:
# 				count=count+1
# 		dic[new_dir]=count
# 	return (dic)
# pprint.pprint(analyse_movies_directors(movie_dir))
# ##---------------------------------------TASK-8 AND TASK-9----------------------------##
# def catching(param):
	# new_list=[]
	# random_sleep=random.randint(1, 3) # task-9
	# for i in param:
	# 	data=i["url"]
	# 	# print (data)
	# 	new_list.append(data)
	# # print new_list
	# for j in new_list:
	# 	movie_id=(j[27:-1])+".json"
	# 	time.sleep(random_sleep) #task-9
	# 	print (random_sleep)
	# 	if not(os.path.exists(movie_id)):
	# 		with open(movie_id, "w") as f:
	# 			parser=scrape_movie_details(data)
	# 			datas=json.dumps(parser)
	# 			f.write(datas)
# pprint.pprint (catching(scrape_top_list()))

##----------------------------------------TASK-10--------------------------##
def analyse_language_and_directors():
	with open('total_movie.json','r+') as k:
		data = json.load(k)
	Director_list=[]
	Language_list=[]
	for i in data:
		directors=i["director"]
		language=i['language']
		for j in directors:
			if j not in Director_list:
				Director_list.append(j)
		for k in language:
			if k not in Language_list:
				Language_list.append(k)
	# print (Director_list,Language_list)
	mainDic={}
	for i in Director_list:
		dic={}
		for j in Language_list:
			count=0
			for k in data:
				directors=k["director"]
				language=k['language']
				if i in directors:
					if j in language:
						count+=1
			if count != 0:
				dic[j]=count
		mainDic[i]=dic
	print (mainDic)
# analyse_language_and_directors()

##-----------------------------TASK-11-------------------------------------
def analyse_movies_genre():
	with open("total_movie.json","r+") as file:
		data=json.load(file)
	Genre_list=[]
	for i in data:
		genre=i["genre"]
		for j in genre:
			if j not in Genre_list:
				Genre_list.append(j)
	dic={}
	for i in Genre_list:
		count=0
		for j in data:
			genre=j["genre"]
			if i in genre:
				count+=1
		if count!=0:
			dic[i]=count

	print (dic)
# analyse_movies_genre()

##---------------------------------------TASK-12----------------------------------------
def scrape_movie_cast(url):
	page=requests.get(url)
	soup=page.text
	parser=BeautifulSoup(soup,'html.parser')
	table=parser.find("table",class_="cast_list")
	td=table.findAll("td",class_="primary_photo")
	movies_list=[]
	for i in td:
		dic={}
		movie_id= (i.find("a")["href"][6:15])
		img_name=i.find("a").find("img").get("title")
		# print (img)
		dic["imdb_id"]=movie_id
		dic["name"]=img_name
		movies_list.append(dic)
	return(movies_list)
# pprint.pprint(scrape_movie_cast("https://www.imdb.com/title/tt0066763/fullcredits?ref_=tt_cl_sm#cast"))
# new_fun=(scrape_movie_cast("https://www.imdb.com/title/tt0066763/fullcredits?ref_=tt_cl_sm#cast"))



##----------------------------------------TASK-13--------------------------------------
def scrape13():
	movie_list=[]
	a=0
	with open("total_movie.json", "r+") as file:
		data=json.load(file)
	for i in scrapped:
		all_data=i["url"][27:-1]
		url=all_data+".json"
		if not(os.path.exists(url)):
			var=scrape_movie_cast("https://www.imdb.com/title/"+all_data+"/fullcredits?ref_=tt_cl_sm#cast")
			data[a]["cast"]=var
			with open(url,"w+") as files:
				var_dump=json.dumps(data[a])
				files.write(var_dump)
				a+=1
		with open(url,"r+")as file:
			file_load=json.load(file)
			movie_list.append(file_load)
	return(movie_list)
# pprint.pprint(scrape13())
scrape15=(scrape13())

##-------------------------------- TASK-15 ----------------------------------------
def analyse_actors():
	dic1={}
	dic2={}
	for i in scrape15:
		cast=i["cast"]
		for j in cast:
			id=j["imdb_id"]
			if id in dic1:
				dic1[id]+=1
			else:
				dic1[id]=1
	for i in dic1:
		for j in scrape15:
			cast=j["cast"]
			for k in cast:
				if i==k["imdb_id"] and i not in dic2:
					dic2[i]={"name":k["name"],"num_movies":dic1[i]}
	print (dic2)						
analyse_actors()
##-----------------------------TASK-14-----------------------------------------
