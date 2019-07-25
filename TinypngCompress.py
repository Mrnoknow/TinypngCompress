# coding: utf-8
# create by fubiao
from fake_useragent import UserAgent
import requests
import json
import os
import imghdr
import commands
from PIL import Image


dirRoot = "/Users/fun/lianjia_android_nh_plugin"
num = 0
compressArg = 30
quality = "80"
size = 5*1024

def compressImage(imageSrc):
    ua = UserAgent(verify_ssl=False	)
    headers = {
        "content-type": "image/png",
        "User-Agent":ua.random,
        "accept": "*/*",
        "authority": "tinypng.com",
        "method": "POST",
        "path": "/web/shrink",
        "scheme": "https",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "origin": "https://tinypng.com",
        "referer": "https://tinypng.com",
    }

    global num

    url = "https://tinypng.com/web/shrink"
    with open(imageSrc, 'rb') as source:
        source_data = source.read()
    try:
        res = requests.post(url,data=source_data,headers = headers)
        resJson = json.loads(res.text)
        inputSize = resJson["input"]["size"]
        outputSize = resJson["output"]["size"]

        print '压缩图片路径：'

        if((inputSize - outputSize)*100/inputSize > compressArg):
            print(imageSrc)
            print "压缩率：",
            print((inputSize - outputSize)*100/inputSize)
            print ''

            outputUrl = resJson["output"]["url"]
            response = requests.get(outputUrl)
            num = num + 1
            with open(imageSrc,'wb') as f:
                 f.write(response.content)
            compreePngToWebp(imageSrc)          
        else:
            print imageSrc
            print("：图片已被压缩 ")
            print ''

            
    except Exception as ex :
        print(ex) 

def compreePngToWebp(path):
	if os.path.getsize(path) < size : ""
	else :
		print path
		split_name = os.path.splitext(path)
		name = split_name[0] + ".webp"
		command = "cwebp -q " + quality + " " + path + " -o " + name
		commands.getstatusoutput(command) 
		if(os.path.getsize(name) < os.path.getsize(path)):
			os.remove(path)
		else:
			os.remove(name)	


def getImage(imageDir):
    if os.path.exists(imageDir):
        dirList = os.listdir(imageDir)
        i = 0  
        for dirS in dirList:
            path = os.path.join(imageDir,dirList[i])
            if(os.path.isdir(path)):
                getImage(path)
            else:
            	if ignore(path):
            		compressImage(path)
                        
            i = i + 1
           
def ignore(path):
	if path.find('/build/') < 0 and path.find('/.git') < 0 and path.find('/.idea') < 0 and path.find('/.gradle'):
		imagetype = imghdr.what(path)
		if imagetype == 'png' or imagetype == 'jpg':
			if path.find('.9.png') < 0 and Image.open(path).mode != "P" :
				True
			else:
				False
	else: False			



if __name__ == '__main__':
	dirRoot = raw_input("please input compresses paths:")
	if os.path.exists(dirRoot):
		print "扫描中..........."
		getImage(dirRoot)
		
		print '一共压缩:',
		print num
		print '张图片'
