#!/usr/bin/env python
# -*- coding：utf-8 -*-
# http://blog.csdn.net/fontthrone/article/details/75285798
import urllib.request
import re
import os
import requests
import itertools

re_url = re.compile(r'"objURL":"(.*?)"')


# def decode(url):
#     for key, value in str_table.items():
#         url = url.replace(key, value)
#     return url.translate(char_table)


# def resolveImgUrl(html):
#     imgUrls = [decode(x) for x in re_url.findall(html)]
#     return imgUrls


def buildUrls(word):
    word = urllib.parse.quote(word)
    url = r"http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&fp=result&queryWord={word}&cl=2&lm=-1&ie=utf-8&oe=utf-8&st=-1&ic=0&word={word}&face=0&istype=2nc=1&pn={pn}&rn=60"
    urls = (url.format(word=word, pn=x) for x in itertools.count(start=0, step=60))
    print(list(urls))
    return urls


def img_spider(name_file):
    user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"
    headers = {'User-Agent': user_agent}
    # 读取名单txt，生成包括所有人的名单列表
    with open(name_file, encoding='utf-8') as f:
        name_list = [name.rstrip() for name in f.readlines()]
        f.close()
    # 遍历每一个人，爬取30张关于他的图，保存在以他名字命名的文件夹中
    for name in name_list:
        # 生成文件夹（如果不存在的话）
        if not os.path.exists('D:\\celebrity\\img_data\\' + name):
            os.makedirs('D:\\celebrity\\img_data\\' + name)
            try:
                # 有些外国人名字中间是空格，要把它替换成%20，不然访问页面会出错。
                # url = "http://image.baidu.com/search/avatarjson?tn=resultjsonavatarnew&ie=utf-8&word=%E6%AF%9B%E4%B8%8D%E6%98%93&cg=girl&rn=60&pn=60"
                # url = "https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=index&fr=&hs=0&xthttps=111111&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E6%AF%9B%E4%B8%8D%E6%98%93&oq=%E6%AF%9B%E4%B8%8D%E6%98%93&rsp=-1"

                # url = "https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&fp=result&queryWord=%E6%AF%9B%E4%B8%8D%E6%98%93&cl=2&lm=-1&ie=utf-8&oe=utf-8&st=-1&ic=0&word=%E6%AF%9B%E4%B8%8D%E6%98%93&face=0&istype=2nc=1&pn=1&rn=60"
                # res = urllib.request.urlopen(url)
                url = "https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E6%AF%9B%E4%B8%8D%E6%98%93&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=%E6%AF%9B%E4%B8%8D%E6%98%93&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn=120&rn=30&gsm=78&1515077978345="
                html = requests.get(url, timeout=10).content.decode('utf-8')
                # page = res.read()
                print(html)
                # 因为JSON的原因，在浏览器页面按F12看到的，和你打印出来的页面内容是不一样的，所以匹配的是objURL这个东西，对比一下页面里别的某某URL，那个能访问就用那个
                # img_srcs = re.findall('"objURL":"(.*?)"', html, re.S)

                p = re.compile("thumbURL.*?\.jpg")
                img_srcs = p.findall(html)

                print(name, len(img_srcs))

            except Exception as e:
                # 如果访问失败，就跳到下一个继续执行代码，而不终止程序
                print(name, " error:")
                print(e)
                continue
            j = 1
            src_txt = ''

            # 访问上述得到的图片路径，保存到本地
            for src in img_srcs:
                with open('D:\\celebrity\\img_data\\' + name + '\\' + str(j) + '.jpg', 'wb') as p:
                    try:
                        print("downloading No.%d" % j)
                        # req = urllib2.Request(src, headers=headers)
                        # 设置一个urlopen的超时，如果3秒访问不到，就跳到下一个地址，防止程序卡在一个地方。
                        img = urllib.request.urlopen(src.replace("thumbURL\":\"", ""), timeout=3)
                        p.write(img.read())
                    except Exception as e:
                        print("No.%d error:" % j)
                        print("No.%d error:", e)
                        p.close()
                        continue
                    p.close()
                src_txt = src_txt + src + '\n'
                if j == len(img_srcs):
                    break
                j = j + 1
            # 保存30个图片的src路径为txt，我要一行一个，所以加换行符
            with open('D:\\celebrity\\img_data\\' + name + '\\' + name + '.txt', 'w') as p2:
                p2.write(src_txt)
                p2.close()
                print("save %s txt done" % name)


# 主程序，读txt文件开始爬
if __name__ == '__main__':
    name_file = "D:\\repository\\python\\mypython\\name_list1.txt"
    img_spider(name_file)
    # str = '毛不易'
    # buildUrls(str)
#!/usr/bin/env python
# -*- coding：utf-8 -*-
# http://blog.csdn.net/fontthrone/article/details/75285798
import urllib.request
import re
import os
import requests
import itertools

re_url = re.compile(r'"objURL":"(.*?)"')


# def decode(url):
#     for key, value in str_table.items():
#         url = url.replace(key, value)
#     return url.translate(char_table)


# def resolveImgUrl(html):
#     imgUrls = [decode(x) for x in re_url.findall(html)]
#     return imgUrls


def buildUrls(word):
    word = urllib.parse.quote(word)
    url = r"http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&fp=result&queryWord={word}&cl=2&lm=-1&ie=utf-8&oe=utf-8&st=-1&ic=0&word={word}&face=0&istype=2nc=1&pn={pn}&rn=60"
    urls = (url.format(word=word, pn=x) for x in itertools.count(start=0, step=60))
    print(list(urls))
    return urls


def img_spider(name_file):
    user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"
    headers = {'User-Agent': user_agent}
    # 读取名单txt，生成包括所有人的名单列表
    with open(name_file, encoding='utf-8') as f:
        name_list = [name.rstrip() for name in f.readlines()]
        f.close()
    # 遍历每一个人，爬取30张关于他的图，保存在以他名字命名的文件夹中
    for name in name_list:
        # 生成文件夹（如果不存在的话）
        if not os.path.exists('D:\\celebrity\\img_data\\' + name):
            os.makedirs('D:\\celebrity\\img_data\\' + name)
            try:
                # 有些外国人名字中间是空格，要把它替换成%20，不然访问页面会出错。
                # url = "http://image.baidu.com/search/avatarjson?tn=resultjsonavatarnew&ie=utf-8&word=%E6%AF%9B%E4%B8%8D%E6%98%93&cg=girl&rn=60&pn=60"
                # url = "https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=index&fr=&hs=0&xthttps=111111&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E6%AF%9B%E4%B8%8D%E6%98%93&oq=%E6%AF%9B%E4%B8%8D%E6%98%93&rsp=-1"

                # url = "https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&fp=result&queryWord=%E6%AF%9B%E4%B8%8D%E6%98%93&cl=2&lm=-1&ie=utf-8&oe=utf-8&st=-1&ic=0&word=%E6%AF%9B%E4%B8%8D%E6%98%93&face=0&istype=2nc=1&pn=1&rn=60"
                # res = urllib.request.urlopen(url)
                url = "https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E6%AF%9B%E4%B8%8D%E6%98%93&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=%E6%AF%9B%E4%B8%8D%E6%98%93&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn=120&rn=30&gsm=78&1515077978345="
                html = requests.get(url, timeout=10).content.decode('utf-8')
                # page = res.read()
                print(html)
                # 因为JSON的原因，在浏览器页面按F12看到的，和你打印出来的页面内容是不一样的，所以匹配的是objURL这个东西，对比一下页面里别的某某URL，那个能访问就用那个
                # img_srcs = re.findall('"objURL":"(.*?)"', html, re.S)

                p = re.compile("thumbURL.*?\.jpg")
                img_srcs = p.findall(html)

                print(name, len(img_srcs))

            except Exception as e:
                # 如果访问失败，就跳到下一个继续执行代码，而不终止程序
                print(name, " error:")
                print(e)
                continue
            j = 1
            src_txt = ''

            # 访问上述得到的图片路径，保存到本地
            for src in img_srcs:
                with open('D:\\celebrity\\img_data\\' + name + '\\' + str(j) + '.jpg', 'wb') as p:
                    try:
                        print("downloading No.%d" % j)
                        # req = urllib2.Request(src, headers=headers)
                        # 设置一个urlopen的超时，如果3秒访问不到，就跳到下一个地址，防止程序卡在一个地方。
                        img = urllib.request.urlopen(src.replace("thumbURL\":\"", ""), timeout=3)
                        p.write(img.read())
                    except Exception as e:
                        print("No.%d error:" % j)
                        print("No.%d error:", e)
                        p.close()
                        continue
                    p.close()
                src_txt = src_txt + src + '\n'
                if j == len(img_srcs):
                    break
                j = j + 1
            # 保存30个图片的src路径为txt，我要一行一个，所以加换行符
            with open('D:\\celebrity\\img_data\\' + name + '\\' + name + '.txt', 'w') as p2:
                p2.write(src_txt)
                p2.close()
                print("save %s txt done" % name)


# 主程序，读txt文件开始爬
if __name__ == '__main__':
    name_file = "D:\\repository\\python\\mypython\\name_list1.txt"
    img_spider(name_file)
    # str = '毛不易'
    # buildUrls(str)
