from bs4 import BeautifulSoup
import requests

url="https://www.rockauto.com/en/catalog/"

make = input("Enter the name of the Manufacturer: ")
year = input("Enter the year of the vehicle: ")
model = input("Enter the model of the vehicle: ")

basic_url = url + make + "," + year + "," + model

page = requests.get(basic_url) 

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id = "treeroot[catalog]")

elements = results.find_all("a",class_ = "navlabellink nvoffset nnormal", href = True)

for element in elements:
	print(element['href'])
	print(element.get_text())
	#print(element.get_text())
	#print(element.geA
	print("Please Clap")