#参考:http://www.jianshu.com/p/6c060433facf?appinstall=0
import urllib.request
import requests
import time
import random
from bs4 import BeautifulSoup
from lxml import etree
import pymysql
import sys

channel='''
      https://book.douban.com/tag/小说
      https://book.douban.com/tag/外国文学
      https://book.douban.com/tag/文学
      https://book.douban.com/tag/随笔
      https://book.douban.com/tag/中国文学
      https://book.douban.com/tag/经典
      https://book.douban.com/tag/日本文学
      https://book.douban.com/tag/散文
      https://book.douban.com/tag/村上春树
      https://book.douban.com/tag/诗歌
      https://book.douban.com/tag/童话
      https://book.douban.com/tag/杂文
      https://book.douban.com/tag/王小波
      https://book.douban.com/tag/儿童文学
      https://book.douban.com/tag/古典文学
      https://book.douban.com/tag/张爱玲
      https://book.douban.com/tag/名著
      https://book.douban.com/tag/余华
      https://book.douban.com/tag/当代文学
      https://book.douban.com/tag/钱钟书
      https://book.douban.com/tag/鲁迅
      https://book.douban.com/tag/外国名著
      https://book.douban.com/tag/诗词
      https://book.douban.com/tag/茨威格
      https://book.douban.com/tag/米兰·昆德拉
      https://book.douban.com/tag/杜拉斯
      https://book.douban.com/tag/港台
      https://book.douban.com/tag/漫画
      https://book.douban.com/tag/绘本
      https://book.douban.com/tag/推理
      https://book.douban.com/tag/青春
      https://book.douban.com/tag/言情
      https://book.douban.com/tag/科幻
      https://book.douban.com/tag/东野圭吾
      https://book.douban.com/tag/悬疑
      https://book.douban.com/tag/武侠
      https://book.douban.com/tag/奇幻
      https://book.douban.com/tag/韩寒
      https://book.douban.com/tag/日本漫画
      https://book.douban.com/tag/耽美
      https://book.douban.com/tag/亦舒
      https://book.douban.com/tag/三毛
      https://book.douban.com/tag/安妮宝贝
      https://book.douban.com/tag/网络小说
      https://book.douban.com/tag/推理小说
      https://book.douban.com/tag/郭敬明
      https://book.douban.com/tag/穿越
      https://book.douban.com/tag/金庸
      https://book.douban.com/tag/轻小说
      https://book.douban.com/tag/阿加莎·克里斯蒂
      https://book.douban.com/tag/几米
      https://book.douban.com/tag/魔幻
      https://book.douban.com/tag/张小娴
      https://book.douban.com/tag/幾米
      https://book.douban.com/tag/青春文学
      https://book.douban.com/tag/科幻小说
      https://book.douban.com/tag/J.K.罗琳
      https://book.douban.com/tag/高木直子
      https://book.douban.com/tag/古龙
      https://book.douban.com/tag/沧月
      https://book.douban.com/tag/落落
      https://book.douban.com/tag/张悦然
      https://book.douban.com/tag/蔡康永
      https://book.douban.com/tag/历史
      https://book.douban.com/tag/心理学
      https://book.douban.com/tag/哲学
      https://book.douban.com/tag/传记
      https://book.douban.com/tag/文化
      https://book.douban.com/tag/社会学
      https://book.douban.com/tag/艺术
      https://book.douban.com/tag/设计
      https://book.douban.com/tag/政治
      https://book.douban.com/tag/社会
      https://book.douban.com/tag/建筑
      https://book.douban.com/tag/宗教
      https://book.douban.com/tag/电影
      https://book.douban.com/tag/数学
      https://book.douban.com/tag/政治学
      https://book.douban.com/tag/回忆录
      https://book.douban.com/tag/思想
      https://book.douban.com/tag/中国历史
      https://book.douban.com/tag/国学
      https://book.douban.com/tag/音乐
      https://book.douban.com/tag/人文
      https://book.douban.com/tag/人物传记
      https://book.douban.com/tag/戏剧
      https://book.douban.com/tag/生活
      https://book.douban.com/tag/成长
      https://book.douban.com/tag/励志
      https://book.douban.com/tag/心理
      https://book.douban.com/tag/摄影
      https://book.douban.com/tag/女性
      https://book.douban.com/tag/职场
      https://book.douban.com/tag/美食
      https://book.douban.com/tag/教育
      https://book.douban.com/tag/游记
      https://book.douban.com/tag/灵修
      https://book.douban.com/tag/健康
      https://book.douban.com/tag/情感
      https://book.douban.com/tag/手工
      https://book.douban.com/tag/养生
      https://book.douban.com/tag/两性
      https://book.douban.com/tag/人际关系
      https://book.douban.com/tag/家居
      https://book.douban.com/tag/自助游
      https://book.douban.com/tag/经济学
      https://book.douban.com/tag/管理
      https://book.douban.com/tag/经济
      https://book.douban.com/tag/商业
      https://book.douban.com/tag/金融
      https://book.douban.com/tag/投资
      https://book.douban.com/tag/营销
      https://book.douban.com/tag/创业
      https://book.douban.com/tag/理财
      https://book.douban.com/tag/广告
      https://book.douban.com/tag/股票
      https://book.douban.com/tag/企业史
      https://book.douban.com/tag/策划
      https://book.douban.com/tag/科普
      https://book.douban.com/tag/互联网
      https://book.douban.com/tag/编程
      https://book.douban.com/tag/科学
      https://book.douban.com/tag/交互设计
      https://book.douban.com/tag/用户体验
      https://book.douban.com/tag/算法
      https://book.douban.com/tag/web
      https://book.douban.com/tag/科技
      https://book.douban.com/tag/UE
      https://book.douban.com/tag/通信
      https://book.douban.com/tag/交互
      https://book.douban.com/tag/UCD
      https://book.douban.com/tag/神经网络
      https://book.douban.com/tag/程序
     '''

def getListFromPage(eachPage):
    pageData=requests.get(eachPage) #访问页面
    soup=BeautifulSoup(pageData.text.encode("utf-8"),"lxml")
    booksDetailUrl=soup.select(".info > h2 > a")
    hrefList=[]
    name=[]
    for everyTag in booksDetailUrl:
        hrefList.append(everyTag['href'])
        name.append(everyTag['title'])
    bookInfoList=soup.select(".pub")
    author=[]
    press=[]
    publishYear=[]
    price=[]
    for eachInfo in bookInfoList:
        strList=eachInfo.string.split("/")
        strList[0]=strList[0].replace("\n","")
        strList[0]=strList[0].replace(" ","")
        author.append(strList[0])
        press.append(strList[strList.__len__()-3])#倒数第三个，若出版社之间有左斜杠则只取右边第一个出版社如：████/████出版社取████出版社
        publishYear.append(strList[strList.__len__()-2])#倒数第二个
        strList[strList.__len__()-1]=strList[strList.__len__()-1].replace("\n","")
        strList[strList.__len__()-1]=strList[strList.__len__()-1].replace(" ","")
        strList[strList.__len__()-1]=strList[strList.__len__()-1].replace("元","")
        price.append(strList[strList.__len__()-1])#最后一个
    #格式化数据
    finalData=[]#存入数据库中的数据集
    for i in range(0,len(name)):
        packageData=[]#包装数据
        packageData.append(name[i])
        packageData.append(author[i])#潜在的数组越界风险
        packageData.append(press[i])#潜在的数组越界风险
        packageData.append(publishYear[i])#潜在的数组越界风险
        packageData.append(price[i])#潜在的数组越界风险
        packageData.append(hrefList[i])#潜在的数组越界风险
        finalData.append(packageData)
    #存入数据库
    try:
        conn = pymysql.connect(host='localhost',user='root',passwd='█████',db='mysql',charset='utf8')
        cur = conn.cursor()
        cur.execute("USE booksindouban")
        cur.executemany("insert into info(Title,Author,Press,PublishYear,Price,Url) values(%s,%s,%s,%s,%s,%s)",finalData)
        cur.connection.commit()
        if cur:
            cur.close()
        if conn:
            conn.close()
    except:
        print("错误：写入数据库时发生异常\n错误信息：",sys.exc_info())
    return bookInfoList

print('开始抓取。。。')
clockStart =time.clock()
count=0
for tag_url in channel.split():
    bookPageUrlList=[tag_url+"?start={}&type=T".format(str(i)) for i in range(0,980,20)]   #从channel中提取url信息，并组装成每一页的链接
    for eachPage in bookPageUrlList:
        bookList=getListFromPage(eachPage)
        count+=bookList.__len__()
        if count>=100000:
            break
        time.sleep(int(format(random.randint(0,9))))
    if count>=100000:
        break
clockEnd=time.clock()
print('抓取结束。\n运行时间:',clockEnd-clockStart)