
# coding: utf-8

# In[ ]:

import urllib
import re
import urllib.request

#html = getHtml("https://static.event.mihoyo.com/bh3_homepage/images/pic/picture/01.jpg")
#print(html)

url = 'https://static.event.mihoyo.com/bh3_homepage/images/pic/picture/'
local = 'C:\\Users\\32883\\Desktop\\mihuyo3\\'#这里设置想要保存文件的文件夹路径，文件夹不存在时会报错

'''def callback(blocknum,blocksize,totalsize):
    percent = 100*blocknum*blocksize/totalsize
    if percent>100:
        percent = 100
    print ("%.2f%%"%percent)
'''
def download(url,num,local):
    for i in range(1,num+1):
        if i < 10:
            path = url+'0'+str(i)+'.jpg'
        else:
            path = url+str(i)+'.jpg'
        urllib.request.urlretrieve(path,local+'崩坏3-'+str(i)+'.jpg')#这里的local应该是文件名而不能是文件夹或者目录
        print('Path ',i,' : ',path,'下载完毕 \n')
download(url,35,local)


# In[ ]:



