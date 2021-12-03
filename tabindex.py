from bs4 import BeautifulSoup
import requests
url=input()
html = requests.get(url).content
c=0
soup = BeautifulSoup(html, "html.parser")
for tag in soup.find_all():
    
    try:
        if len(tag['tabindex']) >0:
            attr=tag['tabindex']
            
            if int(attr)==0:
                c=1
                print("Null Tabindex found at :")
                print(tag)
                print("\n")
    except:
        continue
if(c==0):
    print("No null tabindex found")