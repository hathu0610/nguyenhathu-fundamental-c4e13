# 1. Download webpage
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
html_content = urlopen("http://dantri.com.vn/").read().decode('utf-8')

# save to file 

# html_file=open('dantri.html', 'wb')
# html_file.write(html_content)
# html_file.close()




url = "http://dantri.com.vn/"
#     #1.1 open a connection
# conn = urlopen(url)
#     #1.2 read data
# data = conn.read()
#     #1.3 decode
# html= data.decode('utf-8')
# print(html)


# 2. Extract ROI(Region Of Interest)
# html, xml, xhtml
soup = BeautifulSoup(html_content, "html.parser")
ul = soup.find("ul", "ul1 ulnew")

# 3. Extract info
li_list = ul.find_all("li")
new_list =[]
for li in li_list:
    h4 = li.find("h4")
    # h4 = li.h4 neu co 1 con directly
    # hc a = li.h4.a
    a = h4.find("a")

    title = a.string
    href = url + a['href']

    a_list = {
        "title": title,
        "link": href
    }
    new_list.append(a_list)
   
# 4. Save data to excel 
print(new_list)

