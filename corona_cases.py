import requests
from tabulate import tabulate as table
from bs4 import BeautifulSoup as bs
data=[]
page=requests.get("https://www.livemint.com/news/india/coronavirus-cases-in-india-cross-37-000-death-toll-at-1-218-state-wise-tally-11588388406126.html")
#print(page.status_code)
parsed_page=bs(page.content,"lxml")
rows=parsed_page.find_all('p')
for row in rows:
         if '-' in row.text:
                  if row.text.split("-")[1].rstrip().lstrip().isnumeric():
                           row=row.text.split("-")
                           data.append((row[0].strip(),row[1].strip()))

print(table(data,headers=("STATES","TOTAL CASES"),tablefmt="grid"))                    

