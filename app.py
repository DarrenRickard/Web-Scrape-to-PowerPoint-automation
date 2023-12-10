from bs4 import BeautifulSoup
import requests
# from string import Template


homePage = 'https://www.shopmyexchange.com'
crc = ''
while True:
    try:
        crc = int(input("CRC#: "))
        break
    except ValueError:
        print("Invalid input. Please enter numbers only.")

url = f'https://www.shopmyexchange.com/browse?query={crc}'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

# Item Title
itemTitle = soup.find('h1', class_ = 'aafes-page-head').text # Import this to PPSlide
print(itemTitle)

# Item Image
itemImage = soup.find('img', class_ = 'jsFeaturedImage')
imageURL = itemImage['src'] # Import this to PPSlide
print(homePage + imageURL)


# Item Description 
itemDescList = soup.find_all('span', class_ = 'product-desc')
cleanDescList = []
for desc in itemDescList:
    cleanDescList.append(desc.text.strip())

for desc in cleanDescList: 
    print(desc) # Import each desc to PPSlide


# Dimensions List 
dimList = soup.find_all('tr')
newDimList = []
for tag in dimList:
    # print(tag.text)
    if "Consumer Item" in tag.text:
        newDimList.append(tag.text.strip())

for dim in newDimList:
    print(dim) # Import each dim to PPSlide

