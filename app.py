from bs4 import BeautifulSoup
import requests
import sys

def scrape_data():
    HOME_PAGE = 'https://www.shopmyexchange.com'
    CRC = ''
    COMPUTERS = ['macbook', 'laptop', 'notebook', 'pc']
    while True:
        try:
            CRC = int(input("CRC#: "))
            break
        except ValueError:
            print("Invalid input. Please enter numbers only.")

    url = f'https://www.shopmyexchange.com/browse?query={CRC}'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    try:
        # Item Title
        itemTitle = soup.find('h1', class_ = 'aafes-page-head').text


        # Item Image
        itemImage = soup.find('img', class_ = 'jsFeaturedImage')
        imageURL = itemImage['src']
        imageURL = (HOME_PAGE + imageURL)


        # Item Description
        if any(word in itemTitle.lower() for word in COMPUTERS):
            tmpDescList = soup.find_all('span', class_ = 'product-desc')
            itemDescList = []
            for desc in tmpDescList:
                itemDescList.append(desc.text.strip())
        else:
            itemDescList = []


        # Dimensions List
        if not any(word in itemTitle.lower() for word in COMPUTERS):
            tmpDimList = soup.find_all('tr')
            dimList = []
            for tag in tmpDimList:
                # print(tag.text)
                if "Consumer Item" in tag.text:
                    dimList.append(tag.text.strip())
        else:
            dimList = []


        return itemTitle, imageURL, itemDescList, dimList, CRC
    except Exception as e:
        print(f'Error: {e}')
        sys.exit()


if __name__ == "__main__":
    itemTitle, imageURL, itemDescList, dimList = scrape_data()