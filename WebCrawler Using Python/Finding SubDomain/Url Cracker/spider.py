import requests
import re
from urllib.parse import urlparse
from urllib.parse import urljoin
from urllib import parse

def request(url):
    try:
        return requests.get("https://" + url)
    except requests.exceptions.ConnectionError:
        pass

target_url = "https://viberrbyadil.herokuapp.com/"
target_links=[]

def extract_links_from(url):
    response = requests.get(url)
    return re.findall(r'(?:href=")(.*?)"',response.content.decode('utf-8'))

def crawl(url):
    href_links = extract_links_from(url)

    for i in href_links:
        i=parse.urljoin(url,i)

        if "#" in i: # # refers to original page so avoid duplicate page again and again
            i= i.split("#")[0]

        if target_url in i and i not in target_links: #to avoid repeating the same url
            target_links.append(i)
            print ("[+]urls --->",i)
            crawl(i) #recursively crawling
    

crawl(target_url)

    
        

   

        





               

    