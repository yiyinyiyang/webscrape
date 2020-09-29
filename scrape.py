#hi if anyone found this problem?
#  i am a newbie to learn the python to  scrap the website

# in the website there are class_="excerpt excerpt-1"
# class_="excerpt excerpt-2"
# ...
# class_="excerpt excerpt-9"

# i want to use the loop to display  1 to 9 in the the class_="excerpt excerpt-1"

# for i in range(1,10):
#     new_title =soup.find_all("article", class_="excerpt excerpt-"+ str(i))
#     print(new_title)


# i try to solve the problem use way 1
#     new_title =soup.find_all("article", class_="excerpt excerpt-"+str（i）)



import requests
from bs4 import BeautifulSoup

url = "http://www.yangyanghub.com"
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
html_page = requests.get(url,headers=headers)
soup = BeautifulSoup(html_page.content,'lxml')



# print(soup.title)#方法一


#方法2 .get_text() 是获取标题的文字 title 标签不显示

# title=soup.find("title").get_text()
# print(title)

# 爬取最新文章
for i in range(1,10):
    header_info = soup.find_all("div", class_="title")
    new_title =soup.find_all("article", class_="excerpt excerpt-" + str (i))

# new_title =soup.find_all("div", class_="title")

    print(header_info)
    print(new_title)




