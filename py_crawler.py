import urllib
import re
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


def P_info(g_info):
        pattern = re.compile('<p>.+?：(.+?)<[\S\s]+?：(.+?)<[\S\s]+?：(.+?)<[\S\s]+职业：(.+?)<')
#       pattern = re.compile('<p>.+')
        items = re.findall(pattern, g_info)
        return items




base_url = "http://date.jobbole.com/page/"


for i in range(1, 8):
	url = base_url + str(i)
	page = urllib.request.urlopen(url)

	soup = BeautifulSoup(page.read())

	links = soup.find_all('h3',class_='p-tit')

	links.pop(0)


	girl_urls=[] #Store links for each sublink


	for link in links:
		girl_urls.append(link.a.get('href'))

	for girl_url in girl_urls:
		print(girl_url)
		flag = 0
		num = 0
		new_soup = BeautifulSoup(urllib.request.urlopen(girl_url).read())
		imgs = new_soup.find_all('img',class_='alignnone')
		img_name = new_soup.find('div',class_='p-entry')
		print (img_name)
		temp_name = P_info(str(img_name))
		print (temp_name)
		file_temp =""
		for i in range(0,4):
			try:
				file_temp +=temp_name[0][i]
			except IndexError:
				flag = 1
				print ("This one is gone \n")
		if flag == 0:
			for img in imgs:
				filename = file_temp + str(num)
				num += 1
				print (filename)
				try:
					urllib.request.urlretrieve(img.get('src'), filename)
				except Exception:
					continue


