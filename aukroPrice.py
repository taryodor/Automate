#Aukro price getter

import bs4, requests

def getAukroPrice(productUrl):
    res = requests.get(productUrl) #request to download a page
    res.raise_for_status() #check if page downloaded well
    
    soup = bs4.BeautifulSoup(res.text, 'html.parser') #this will load html of page
    
    elems = soup.select('#priceValue')#this selects specifis css value of shit I want
    productPrice = elems[0].text[:-3]#take text from what i want a remove last three chars
    
    return productPrice 

price = getAukroPrice('http://aukro.cz/soustruh-i6665184277.html')
print('Cena jest {} Kc.'.format(price))
