### 使用此脚本

**使用此脚本只需安装几个库就OK了**

* 安装python，MAC端的朋友系统自带python就无需安装
* 若没有安装pip，运行**sudo easy_install pip**
* 安装<code>fake_useragent</code>,**pip install fake_useragent**,useragent操作相关
* 安装<code>UserAgent库</code>,**pip install UserAgent**,设置动态UserAgent
* 安装<code>requests库</code>,**pip install requests**，网络处理，post图片到tinypng后台，获取respond信息
* 安装<code>PIL库</code>,**sudo pip install Pillow**，图片操作相关
* 安装<code>Image库</code>,**pip install Image**，依赖PIL库
* **brew install webp**, png转webp

   **安装以上库之后，直接下载此脚本，使用python运行就OK了**

* 在运行后，输入需要压缩的路径，可以是整个项目路径，无需做特殊处理，此脚本会遍历自己处理，找出png和jpg图片，然后进行压缩


### 需知
* 此脚本会检测被压缩过的图片，2种方式检测
  * 通过位深度，如果位深度为8位，则此图片就无需再被压缩
  * 通过压缩率，压缩率小于50%则无需被压缩

  **此脚本在运行中可能出现错误，这个错误是上传图片过快导致的，重启脚本就OK了，重启后依然会从头遍历**

### 后续优化
* 增量压缩，减少压缩时间
