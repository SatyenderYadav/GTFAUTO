import requests
from bs4 import BeautifulSoup



banner = """ \u001b[1;91m
 ██████╗████████╗███████╗ █████╗ ██╗   ██╗████████╗ ██████╗ 
██╔════╝╚══██╔══╝██╔════╝██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗
██║  ███╗  ██║   █████╗  ███████║██║   ██║   ██║   ██║   ██║
██║   ██║  ██║   ██╔══╝  ██╔══██║██║   ██║   ██║   ██║   ██║
╚██████╔╝  ██║   ██║     ██║  ██║╚██████╔╝   ██║   ╚██████╔╝
 ╚═════╝   ╚═╝   ╚═╝     ╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝ 
                                                            """


print(banner)
print("\u001b[1;93m[~] \u001b[1;92mEnter which binary to find : ")
print("                     \u001b[1;97m|")
print("                     \u001b[1;97m|------------",end='')



what_to_find = input("")
page = requests.get(
    f"https://gtfobins.github.io/gtfobins/{what_to_find}")
soup = BeautifulSoup(page.content, 'html.parser')


all_h1_tags = []
all_code_tags = []


for element in soup.select('h2'):
    all_h1_tags.append(element.text)


remove_code = []


for element in soup.select('.highlighter-rouge'):
    remove_code.append(element.text)

for element in soup.select('code'):
    all_code_tags.append(element.text)

for element in range(len(remove_code)):
    if  remove_code[element] in all_code_tags:
        
        all_code_tags.remove(remove_code[element])
    else:
      pass
    
for element in range(len(all_code_tags)):
    print("   \u001b[92;1m|--\u001b[1;94m[*] "+all_h1_tags[element])
    print("   \u001b[92;1m|")
    print("   \u001b[92;1mv")
    print("\u001b[1;97m"+ all_code_tags[element])
    print("\u001b[1;97m")
    print("\u001b[1;97m")
    
   
