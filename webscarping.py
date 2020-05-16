import requests
import bs4

res = requests.get('https://cse.mait.ac.in/cms/login/index.php')
type(res)

res.text

soup = bs4.BeautifulSoup(res.text, 'lxml')

type(soup)
temp = soup.select('title')
type(temp)

temp

temp[0]


temp2 = soup.select('link')

temp2

temp2[0]