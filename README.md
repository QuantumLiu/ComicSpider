# ComicSpider
The first open-source crawler of raw comics images on [dmzj](http://manhua.dmzj.com/) website.  
第一个开源的[动漫之家](http://manhua.dmzj.com/)漫画站电脑版原图爬虫
# 尊重版权，只供爱好者研究使用，禁止商业用途，保留追究法律责任的权利
# Requirements依赖项
    python3,requests,phantomJS,selenium
    optional:pyinstaller
# Description描述
The first open-source crawler of raw comics images on [dmzj](http://manhua.dmzj.com/) website.Used [PhantomJS](http://phantomjs.org/),and [selenuium](https://github.com/SeleniumHQ/selenium) to get the index of pages for each chapter of a comic.  Download and save the all pages to local files.  
  
第一个从[动漫之家](http://manhua.dmzj.com/)漫画站爬取电脑版原图的开源爬虫。使用[PhantomJS](http://phantomjs.org/),和 [selenuium](https://github.com/SeleniumHQ/selenium)获取每个漫画章节的分页索引。爬取并下载漫画图片到本地文件。  
# Usage  
## English version:
### From source:
In cmd/shell:  
    git clone https://github.com/QuantumLiu/ComicSpider.git  
Please create a text file in `ComicSpider/` and write the urls of comics you want to download.  
For example,write following urls in `url.txt`:  
    http://manhua.dmzj.com/dcyuzhouchongsheng/  
    http://manhua.dmzj.com/sanweiyitiv2/  
![url](./pics/url.PNG)  

So the program will download those two comics:  

![cs](./pics/重生.PNG)
![three](./pics/三位一体.PNG)  
Download [PhantomJS](http://phantomjs.org/), and copy it to the same floder of .py files.Or add the path of the .exe file to PATH.  
Then in cmd/shell:  
    cd ComicSpider  
    python download_f.py url.txt 1
There are two arguments:  
First is used to configure the url text file,the default value is './url.txt'.
The last argument is weather using multi threads.'1' for 'True' else for 'False'.Deafult for 'False'.
Results:
![运行](./pics/运行.PNG)
![结果](./pics/结果.PNG)
As you see, the program collected a comic in one floder and below the floder are chapter floders, in each chapter floder there are .jpg files of all pages of the chapter.  
## From binary (Windows) :   
Download the lastest [releases](https://github.com/QuantumLiu/ComicSpider/releases).  
The `ComicSpider.exe` is a packaged binary file of `download_f.py`.  
Double click `ComicSpider.exe` to run with deafult arguments. 
Or in cmd/shell/.bat:  
    ComicSpider [your file] [multi-threads flag]
## 中文版本:
### 使用源码:
在命令行cmd或终端:  
    git clone https://github.com/QuantumLiu/ComicSpider.git  
请在 `ComicSpider/` 文件夹创建一个文本文件，并写入你要下载的漫画的网址。  
例如，将以下内容写入 `url.txt`:  
    http://manhua.dmzj.com/dcyuzhouchongsheng/  
    http://manhua.dmzj.com/sanweiyitiv2/  
![url](./pics/url.PNG)  

那么程序将下载这两部漫画:  

![cs](./pics/重生.PNG)
![three](./pics/三位一体.PNG)  
下载 [PhantomJS](http://phantomjs.org/), 解压并将`phantomjs.exe`文件放在.py 文件的同一个文件夹。或者把phantom.exe所在路径添加到环境变量PATH。  
在cmd/shell:  
    cd ComicSpider  
    python download_f.py url.txt 1  
有两个可选参数:  
第一个参数用来指定存放要下载的漫画地址的文本文件的路径，默认值为 './url.txt'.
最后一个参数用来指定是否使用多线程。'1' 即 'True' e其他的是 'False'.默认值 'False'.
运行结果:
![运行](./pics/运行.PNG)
![结果](./pics/结果.PNG)
如你所见，程序创建了一个漫画文件夹，里面是各个章节的文件夹，每个章节文件夹内存放每一页的jpg文件。    
## 使用二进制文件 (Windows) ：    
下载最新的 [releases](https://github.com/QuantumLiu/ComicSpider/releases).  
`ComicSpider.exe` 是打包好的`download_f.py`.  
双击 `ComicSpider.exe` 将以默认值运行。  
或者在 cmd/shell/.bat:  
    ComicSpider [your file] [multi-threads flag]  
# Future
更多可指定参数  
更好的异常处理  
更通用的win32发布版本  
基于itchat的微信扩展