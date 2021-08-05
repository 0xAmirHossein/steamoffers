from urllib.request import urlopen as uReq 
from bs4 import BeautifulSoup as soup

#opening up the connection, grabs the webpage
my_url = 'https://store.steampowered.com/specials/#p=0&tab=TopSellers'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

# grabs each offer
containers = page_soup.findAll("a", {"class":"tab_item"})
 
filename = "steam_offers.csv"
f = open(filename, "w", encoding="utf-8")
headers = "game_name, discount\n"
f.write(headers)


for container in containers:
	# gets the name of the game
	name_container = container.findAll("div", {"class": "tab_item_name"})
	game_name = name_container[0].text
	

	# gets the dicount percentage
	pct_container = container.findAll("div", {"class": "discount_pct"})
	pct = pct_container[0].text
	
	print("game_name: " + game_name)
	print("pct: " + pct)

	f.write(game_name.replace("," , "|") + "," + pct + "\n")
f.close()