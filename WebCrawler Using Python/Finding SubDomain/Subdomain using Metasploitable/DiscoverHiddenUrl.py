import requests

def request(url):
	try:
		return requests.get("http://" + url)
	except requests.exceptions.ConnectionError:
		pass

target_url = "192.168.37.133/mutillidae/"
if target_url==True:
	print("Found")

with open(r"C:\Users\Windows 10\Desktop\Subdomain\common.txt","r") as wordlist_file:
	for line in wordlist_file:
		word = line.strip()
		test_url = word + "." + "/"+ target_url
		response = request(test_url)
		if response :
			print ("[+] Discovered subdomain ----> "+test_url)