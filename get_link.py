import requests
from bs4 import BeautifulSoup as bs 

def video_link(query = 'sun'):

	query = query.replace(' ', '+')
	search = 'https://www.youtube.com/results?search_query=' + query

	r = requests.get(search)

	soup = bs(r.content, 'html5lib') 
	soup.prettify() 

	for a in soup.find_all('a', href=True):
		if '/watch?' in a['href']:
			final_link = a['href']
			final_link = final_link.replace('watch?v=', 'embed/')
			break

	iframe_link = 'http://www.youtube.com'+final_link
	return str(iframe_link)
