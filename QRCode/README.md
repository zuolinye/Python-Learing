---
layout: post
title: 使用Python将url转换成二维码（Convert url to QR code）
description: "使用Python将url链接转换成二维码"  
tag: Python
---

### 一、描述问题
将url链接转换成二维码

### 二、分析问题
现在有很多二维码的生成工具，在线的，或者安装的软件，都可以进行生成二维码。  
今天我们用Python生成二维码。  

### 三、分解问题
1. Python是否有现成的包：Python提供了qrcode生成二维码的包
2. 找到qrcode包的说明文件：[qrcode · PyPI](https://pypi.org/project/qrcode/)

### 四、解决问题
首先需要导入qrcode模块，然后调用make方法，会生成一个图片对象，调用图片对象
的save方法就可以将生成的二维码保存下来了。
1. 安装qrcode包：```pip install qrcode```
2. 代码生成
    ```
    import qrcode
    img = qrcode.make("http://yezuolin.com/")
    img.save("C:/Users/Administrator/Desktop\/yezuolin.png")
    ```
![yezuolin1](/images/posts/PythonQRCode/yezuolin1.png)


### 五、拓展

1. 当我们希望生成不同尺寸的二维码，就需要使用QRCode类了，设置如下。  

    ```

    import qrcode
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data('http://yezuolin.com/')
    qr.make(fit=True)

    img = qr.make_image()
    img.save('C:/Users/Administrator/Desktop\/yezuolin1.png')

    ```

    version 表示二维码的版本号，二维码总共有1到40个版本，最小的版本号是1，对应的尺寸是21×21，每增加一个版本会增加4个尺寸。这里说的尺寸不是只生成图片的大小，而是值二维码的长宽被平均分为多少份。  
    error_correction指的是纠错容量，这就是为什么二维码上面放一个小图标也能扫出来，纠错容量有四个级别，分别是  
      * *ERROR_CORRECT_L L级别，7%或更少的错误能修正  
      * ERROR_CORRECT_M M级别，15%或更少的错误能修正，也是qrcode的默认级别  
      * ERROR_CORRECT_Q Q级别，25%或更少的错误能修正  
      * ERROR_CORRECT_H H级别，30%或更少的错误能修正  
    box_size 指的是生成图片的像素  
    border 表示二维码的边框宽度，4是最小值  
    ![yezuolin1](/images/posts/PythonQRCode/yezuolin1.png)
  
2. 将文字转换成二维码，同理。

### 六、小结
今天闲暇之余，想起了将url生成二维码。  使用Python生成二维码，总体来说，还是很简单方便的。  

Reference：  
[1] [qrcode包说明文件：qrcode PyPI](https://pypi.org/project/qrcode/)

<br>

转载请注明：[yezuolin的博客](http://yezuolin.com/) » [点击阅读原文](http://yezuolin.com/2018/08/PythonQRCode/) 



