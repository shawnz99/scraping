from urllib2 import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/p/pl?d=ssds&N=100011692'

# Opening up connection, grabbing the page
uClient = uReq(my_url)


# Offloads the content into a Variable
page_html = uClient.read()

# Closes Stream?
uClient.close()

# Parses Html
page_soup = soup(page_html, "html.parser")

# Grabs each Product
containers = page_soup.findAll("div", {"class":"item-container"})

for container in containers:
	brand = container.div.div.a.img["title"]

	title_container = container.findAll("a", {"class":"item-title"})
	product_name = title_container[0].text
	
	shipping_containter = container.findAll("li",{"class":"price-ship"})
	shipping = shipping_containter[0].text.strip()

	print("brand:"+ brand)
	print("product name:"+ product_name)
	print("shipping" + shipping)