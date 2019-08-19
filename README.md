## 自动无限压缩图片压缩脚本

一款无限自动压缩图片工具，自动将图片压缩转化为webp，可自定义压缩率和webp的转化率。

此脚本会检测被压缩过的图片，3种方式检测：
>
> 位深度为8位，则此图片就无需再被压缩
>
> 压缩率小于50%则无需被压缩
>
> 图片大于5kb，转化为webp
>

### Requests

> Python 2.7+
>
> fake_useragent
>
> UserAgent
>
> Requests
> 
> Pillow
> 
>Image
>

### Run
>
> run TinypngCompress.py，输入需要压缩的路径，可以是整个项目路径，无需做特殊处理，此脚本会遍历自己处理，找出png和jpg图片，然后进行压缩
>


### Notice
>
> 此脚本在运行中可能出现错误，这个错误是上传图片过快导致的，重启脚本就OK了，重启后依然会从头遍历
>

### Next
>
> 增量压缩，减少压缩时间
>
> png转webp，80%压缩 done
>
