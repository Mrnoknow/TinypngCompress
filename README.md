#### tinypng简介
**TinyPNG uses smart lossy compression techniques to reduce the file size of your PNG files. By selectively decreasing the number of colors in the image, fewer bytes are required to store the data. The effect is nearly invisible but it makes a very large difference in file size!**

* 有损压缩

#### 为什么使用tinypng

在实验过程中，tinypng的压缩效果是最好的并且在视觉效果上没有影响，所以在最后选择压缩的工具中，就选择了此工具


#### 使用此脚本
**使用此脚本只需安装几个库就OK了**

* 安装python，MAC端的朋友系统自带python就无需安装
* 若没有安装pip，运行**sudo easy_install pip**
* 安装<code>UserAgent库</code>,**pip install UserAgent**,设置动态UserAgent
* 安装<code>requests库</code>,**pip install requests**，网络处理，post图片到tinypng后台，获取respond信息
* 安装<code>imghdr库</code>,**pip install imghdr**，获取图片类型
* 安装<code>PIL库</code>,**pip install PIL**，获取图片位深度
* 安装<code>Image库</code>,**pip install Image**，依赖PIL库

**安装以上库之后，直接下载此脚本，使用python运行就OK了**