import BeautifulSoup
import urllib

data = urllib.urlopen('http://www.daum.net')
soup = BeautifulSoup.BeautifulSoup(data)
name = soup.findAll('span',attrs={'class':'txt_issue'})

'''
for i, go in enumerate(name):
    if i % 2 == 0:
        print go
'''

link = name[0].find('a')['href']

issue_list = []
for i in range(20):
    if i % 2 == 0:
        tmp_t = name[i].find('a').text
        tmp_l = name[i].find('a')['href']
        issue_list.append((tmp_t,tmp_l))


for text, link in issue_list:
    print text, link
