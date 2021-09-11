#! /usr/bin/env python
import time
import os
import sys
import  logging
from datetime import datetime
from skycode import *
import subprocess
import sys

import cv2
import numpy as np
#from matplotlib import pyplot as plt
import wmi
import re

import requests

def hello(func):                                                                                            
    def inner(n):                                                                                            
        print("Hello ")                                                                                     
        func(n)                                                                                              
    return inner

@hello
def name(n):                                                                                                 
    print(n)                                                                                          
                                                                                                            
                                                                                                            
import time                                                                                                               
                                                                                                                          
def measure_time(func):                                                                                                   
                                                                                                                          
  def wrapper(*arg):                                                                                                      
      t = time.time()                                                                                                     
      res = func(*arg)                                                                                                    
      print("Function took " + str(time.time()-t) + " seconds to run")                                                    
      return res                                                                                                          
                                                                                                                          
  return wrapper                                                                                                          
                                                                                                                          
                                                                                                                          
@measure_time                                                                                                             
def myFunction(n):                                                                                                        
  time.sleep(n)                                                                                                           
                                                                                                                          



def test_opencv_adaptiveThreshold():
    """
    """
    n_ret = ERR_FAIL
    n_ret_api = 0    
    desc = ""
    
    for nwf in [1]:
        
        try:
          
            pass
          
            import cv2
            import numpy as np
            from matplotlib import pyplot as plt
            
            img = cv2.imread('dave.jpg',0)
            img2 = cv2.medianBlur(img,5)
            
            ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
            th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)
            th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
            
            titles = ['Original Image', 'medianBlur', 'Global Thresholding (v = 127)',
                        'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
            images = [img, img2, th1, th2, th3]
            
            for i in range(5):
                plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
                plt.title(titles[i])
                plt.xticks([]),plt.yticks([])
            plt.show()          

                                    
        except Exception as e:            
            logging.exception("An exception was thrown!")            
                        
    return n_ret




def test_pdfplumber():
    """
    """
    n_ret = ERR_FAIL
    n_ret_api = 0    
    desc = ""
    
    import pdfplumber
    
    for nwf in [1]:
        
        try:
          
            pass
            pdf =  pdfplumber.open(r"E:\lang\Python\project\_working3\pdfTest.pdf")
            print (pdf.metadata)
          
            first_page = pdf.pages[1]

            print('页码：', first_page.page_number)
            print('页宽：', first_page.width)
            print('页高：', first_page.height)
          
            text = first_page.extract_text()

            print (text)
          
          

                  
                                    
        except Exception as e:            
            logging.exception("An exception was thrown!")            
                        
    return n_ret



def test_wmi_usb():
    """
    """
    n_ret = ERR_FAIL
    n_ret_api = 0    
    desc = ""
    
    for nwf in [1]:
        
        try:
          
            c = wmi.WMI()
            wql = "Select * From Win32_USBControllerDevice"
            for item in c.query(wql):
                q = item.Dependent.Caption
                print (q)
                if re.findall("Webcam",q):
                    print("-------------------------------", q)                    
                    
                    
          
            #test_pdfplumber()

                  
                  
                                    
        except Exception as e:            
            logging.exception("An exception was thrown!")            
                        
    return n_ret


def test_embed_qrcode_to_image():
    """
    """
    n_ret = ERR_FAIL
    n_ret_api = 0    
    desc = ""
    
    for nwf in [1]:
        
        try:
          
          import qrcode
          
          from PIL import Image
          
          img_bg = Image.open('d:/frog.jpg')
          
          qr = qrcode.QRCode(box_size=2)
          qr.add_data('I am nwf')
          qr.make()
          img_qr = qr.make_image()
          
          pos = (img_bg.size[0] - img_qr.size[0], img_bg.size[1] - img_qr.size[1])
          
          img_bg.paste(img_qr, pos)
          img_bg.save('d:/qrcode_frog.png')
     

                  
                                    
        except Exception as e:            
            logging.exception("An exception was thrown!")            
                        
    return n_ret


def test_embed_image_to_qrcode():
    """
    """
    n_ret = ERR_FAIL
    n_ret_api = 0    
    desc = ""
    
    for nwf in [1]:
        
        try:
          
          import qrcode
          
          from PIL import Image
          
          face = Image.open('d:/frog.jpg').crop((175, 90, 235, 150))
          
          qr_big = qrcode.QRCode(
              error_correction=qrcode.constants.ERROR_CORRECT_H
          )
          qr_big.add_data('I am frog')
          qr_big.make()
          img_qr_big = qr_big.make_image().convert('RGB')
          
          pos = ((img_qr_big.size[0] - face.size[0]) // 2, (img_qr_big.size[1] - face.size[1]) // 2)
          
          img_qr_big.paste(face, pos)
          img_qr_big.save('d:/frog_name.png')
     

                  
                                    
        except Exception as e:            
            logging.exception("An exception was thrown!")            
                        
    return n_ret


def test_json_path():
    """
    """
    n_ret = ERR_FAIL
    n_ret_api = 0    
    desc = ""
    
    import jsonpath
    
    for nwf in [1]:
        
        try:
          
            class_info = {"class_one": {
    "students": [
        {"name": "张一",
         "sex": "男",
         "age": 18,
         "height": 170.5
         },
        {"name": "张二",
         "sex": "女",
         "age": 20,
         "height": 160.5
         },
        {"name": "张三",
         "sex": "男",
         "age": 18,
         "height": 170.5
         },
    ],
    "teacher": {
        "name": "李小二",
        "sex": "男",
        "age": 30,
        "height": 185.5,
        "teacher":"递归搜索测试"
    }
}
}

          
            result = jsonpath.jsonpath(class_info, '$.class_one.students')
            print(result)


                  
                  
                                    
        except Exception as e:            
            logging.exception("An exception was thrown!")            
                        
    return n_ret



def test_wxpy():
    """
    """
    n_ret = ERR_FAIL
    n_ret_api = 0    
    desc = ""
    
    for nwf in [1]:
        
        try:
          
            # 导入模块
            from wxpy import Bot, MALE
            # 初始化机器人，扫码登陆
            bot = Bot()
            
            # 搜索名称含有 "游否" 的男性深圳好友
            my_friend = bot.friends().search('郑小霞', sex=MALE, city="深圳")[0]
            
            # 发送文本给好友
            my_friend.send('robot 男人的长寿是女人给的')
            # 发送图片
            my_friend.send_image('d:/frog.jpg')            
                  
                  
                                    
        except Exception as e:            
            logging.exception("An exception was thrown!")            
                        
    return n_ret


import pywifi
from pywifi import const
import time
import datetime


# 测试连接，返回链接结果
def wifiConnect(pwd,ssid="MMI22"):
    # 抓取网卡接口
    wifi = pywifi.PyWiFi()
    # 获取第一个无线网卡
    ifaces = wifi.interfaces()[0]
    # 断开所有连接
    ifaces.disconnect()
    time.sleep(1)
    wifistatus = ifaces.status()
    if wifistatus == const.IFACE_DISCONNECTED:
        # 创建WiFi连接文件
        profile = pywifi.Profile()
        # 要连接WiFi的名称
        profile.ssid = ssid
        # 网卡的开放状态
        profile.auth = const.AUTH_ALG_OPEN
        # wifi加密算法,一般wifi加密算法为wps
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        # 加密单元
        profile.cipher = const.CIPHER_TYPE_CCMP
        # 调用密码
        profile.key = pwd
        # 删除所有连接过的wifi文件
        ifaces.remove_all_network_profiles()
        # 设定新的连接文件
        tep_profile = ifaces.add_network_profile(profile)
        ifaces.connect(tep_profile)
        # wifi连接时间
        time.sleep(2)
        if ifaces.status() == const.IFACE_CONNECTED:
            return True
        else:
            return False
    else:
        print("已有wifi连接")



# 读取密码本
def readPassword(ssid):
    success = False
    print("****************** WIFI破解 ******************")
    # 密码本路径
    path = "pwd.txt"
    # 打开文件
    file = open(path, "r")
    start = datetime.datetime.now()
    while True:
        try:
            pwd = file.readline()
            # 去除密码的末尾换行符
            pwd = pwd.strip('\n')
            bool = wifiConnect(pwd,ssid)
            if bool:
                print("[*] 密码已破解：", pwd)
                print("[*] WiFi已自动连接！！！")
                success = True
                break
            else:
                # 跳出当前循环，进行下一次循环
                print("正在破解 SSID 为 %s 的 WIFI密码，当前校验的密码为：%s"%(ssid,pwd))
        except:
            continue
    end = datetime.datetime.now()
    if(success):
        print("[*] 本次破解WIFI密码一共用了多长时间：{}".format(end - start))
    else:
        print("[*] 很遗憾未能帮你破解出当前指定WIFI的密码，请更换密码字典后重新尝试！")




def test_pywifi():
    """
    """
    n_ret = ERR_FAIL
    n_ret_api = 0    
    desc = ""
    
    for nwf in [1]:
        
        try:
          
            readPassword("MMI22")


                  
                  
                                    
        except Exception as e:            
            logging.exception("An exception was thrown!")            
                        
    return n_ret




def test_zip_extract():
    """
    """
    n_ret = ERR_FAIL
    n_ret_api = 0    
    desc = ""
    from zipfile import ZipFile
    
    for nwf in [1]:
        
        try:
          
            pass
            
            file_name = r"E:\lang\Python\project\RF\SkyRobot\temp\plugin.zip"
            dir1 = os.path.dirname(file_name)
            with ZipFile(file_name, 'r') as zip:
                zip.printdir()
                zip.extractall(dir1)
                                    
        except Exception as e:            
            logging.exception("An exception was thrown!")            
                        
    return n_ret



def get_all_file_paths(directory):
  
    # initializing empty file paths list
    file_paths = []
  
    # crawling through directory and subdirectories
    for root, directories, files in os.walk(directory):
        for filename in files:
            # join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
  
    # returning all file paths
    return file_paths
  

def test_zip_write():
    """
    """
    n_ret = ERR_FAIL
    n_ret_api = 0    
    desc = ""
    from zipfile import ZipFile
    
    for nwf in [1]:
        
        try:
          
            # path to folder which needs to be zipped
            directory = r'E:\lang\Python\project\RF\SkyRobot\temp\plugin'
            dir1 = os.path.dirname(directory)
            zip_path = os.path.join(dir1, "plugin.zip")
          
            # calling function to get all file paths in the directory
            file_paths = get_all_file_paths(directory)
          
            # printing the list of all files to be zipped
            print('Following files will be zipped:')
            for file_name in file_paths:
                print(file_name)
          
            # plugin.zip=\lang\Python\project\RF\SkyRobot\temp\plugin
            with ZipFile(zip_path,'w') as zip:
                # writing each file one by one
                for file in file_paths:
                    zip.write(file)
          
            print('All files zipped successfully!')     
            
            
                                    
        except Exception as e:            
            logging.exception("An exception was thrown!")            
                        
    return n_ret


def test_zip_write_rel():
    """
    """
    n_ret = ERR_FAIL
    n_ret_api = 0    
    desc = ""
    import zipfile
    from zipfile import ZipFile
    
    for nwf in [1]:
        
        try:
          
            pass

            src = r"E:\lang\Python\project\RF\SkyRobot\temp\plugin"
            zip_filename = r"E:\lang\Python\project\RF\SkyRobot\temp\plugin.zip"
            zipFile = zipfile.ZipFile(zip_filename, 'w')
            src_rel = os.path.dirname(src)
            
            for fs in os.walk(src):
                
                # cur path file prior    
                for f in fs[2]:
                    abs_filename = os.path.join(fs[0], f)
                    rel_filename = os.path.relpath(abs_filename, src_rel)
                    
                    zipFile.write(abs_filename, rel_filename, zipfile.ZIP_DEFLATED)
                
                # folder
                for d in fs[1]:
        
                    d_path = os.path.join(fs[0], d)                    
                    rel_filename = os.path.relpath(d_path, src_rel)
                    
                    zipFile.write(d_path, rel_filename, zipfile.ZIP_DEFLATED)
            
            zipFile.close()           
            
            
                                    
        except Exception as e:            
            logging.exception("An exception was thrown!")            
                        
    return n_ret



def session_for_src_addr(addr: str) -> requests.Session:
    """
    Create `Session` which will bind to the specified local address
    rather than auto-selecting it.
    """
    session = requests.Session()
    for prefix in ('http://', 'https://'):
        session.get_adapter(prefix).init_poolmanager(
            # those are default values from HTTPAdapter's constructor
            connections=requests.adapters.DEFAULT_POOLSIZE,
            maxsize=requests.adapters.DEFAULT_POOLSIZE,
            # This should be a tuple of (address, port). Port 0 means auto-selection.
            source_address=(addr, 0),
        )

    return session



def test_http_bind():
    """
    """
    n_ret = ERR_FAIL
    n_ret_api = 0    
    desc = ""

    
    for nwf in [1]:
        
        try:
          
            # usage example:
            #s = session_for_src_addr('192.168.10.55')
            s = session_for_src_addr('192.168.10.77')
            x = s.get('http://192.168.10.1/')
            print (x)
                     
            
            
                                    
        except Exception as e:            
            logging.exception("An exception was thrown!")            
                        
    return n_ret


def body(buf):
    sys.stdout.write(str(buf))
def header(buf):
    sys.stdout.write(str(buf))

def test_pyc_interface():
    """
    """
    n_ret = ERR_FAIL
    n_ret_api = 0    
    desc = ""
    import pycurl
    
    for nwf in [1]:
        
        try:

            c = pycurl.Curl()
            c.setopt(pycurl.URL, "http://pycurl.io/docs/latest/callbacks.html#writefunction")
            c.setopt(pycurl.WRITEFUNCTION, body)
            c.setopt(pycurl.HEADERFUNCTION, header)
            c.setopt(pycurl.INTERFACE, "192.168.9.77")
            
            c.perform()
                                 
            
            
                                    
        except Exception as e:            
            logging.exception("An exception was thrown!")            
                        
    return n_ret



def test_plot_locator():
    """
    """
    n_ret = ERR_FAIL
    n_ret_api = 0    
    desc = ""

    
    for nwf in [1]:
        
        try:
          
            pass

            import numpy as np
            import matplotlib.pyplot as plt
            x=np.arange(0,30,1)
            plt.plot(x,x)
            # x轴和y轴分别显示20个
            plt.locator_params(nbins=20)
            plt.show()              
            
            
                                    
        except Exception as e:            
            logging.exception("An exception was thrown!")            
                        
    return n_ret



# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# noise removal
def remove_noise(image):
    return cv2.medianBlur(image,5)
 
#thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

#dilation
def dilate(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.dilate(image, kernel, iterations = 1)
    
#erosion
def erode(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.erode(image, kernel, iterations = 1)

#opening - erosion followed by dilation
def opening(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

#canny edge detection
def canny(image):
    return cv2.Canny(image, 100, 200)



#  https://nanonets.com/blog/ocr-with-tesseract/
#skew correction
def deskew(image):
    coords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated




#template matching
def match_template(image, template):
    return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED) 


def test_pytesseract():
    """
    """
    n_ret = ERR_FAIL
    n_ret_api = 0    
    desc = ""
    import cv2
    import numpy as np
    import pytesseract
    
    for nwf in [1]:
        
        try:
          
            pass
          
            pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files\Tesseract-OCR\tesseract.exe'
            custom_config = r'--oem 3 --psm 6'
            
            image = cv2.imread('img_skew.png')
            
            i = deskew(image)
            x = pytesseract.image_to_string(i, config=custom_config)
            print (x)
                        
            i = image
            x = pytesseract.image_to_string(i, config=custom_config)
            print (x)
                        
            
            image = cv2.imread('english_img.png')
            gray = get_grayscale(image)
            thresh = thresholding(gray)
            open = opening(gray)
            can = canny(gray)
            
            
            imgs = [gray, thresh, open, can]
            for i in imgs:
                 x = pytesseract.image_to_string(i, config=custom_config)
                 print (x)
            

            
                                    
        except Exception as e:            
            logging.exception("An exception was thrown!")            
                        
    return n_ret



def test():
    """
    """
    n_ret = ERR_FAIL
    n_ret_api = 0    
    desc = ""
    import cv2
    import numpy as np
    
    for nwf in [1]:
        
        try:
          
            pass
            import numpy as np
            import cv2
            import math
            from scipy import ndimage
            
            img_before = cv2.imread('rotate_me.png')
            
            cv2.imshow("Before", img_before)    
            key = cv2.waitKey(0)
            
            img_gray = cv2.cvtColor(img_before, cv2.COLOR_BGR2GRAY)
            img_edges = cv2.Canny(img_gray, 100, 100, apertureSize=3)
            lines = cv2.HoughLinesP(img_edges, 1, math.pi / 180.0, 100, minLineLength=100, maxLineGap=5)
            
            angles = []
            
            for [[x1, y1, x2, y2]] in lines:
                cv2.line(img_before, (x1, y1), (x2, y2), (255, 0, 0), 3)
                angle = math.degrees(math.atan2(y2 - y1, x2 - x1))
                angles.append(angle)
            
            cv2.imshow("Detected lines", img_before)    
            key = cv2.waitKey(0)
            
            median_angle = np.median(angles)
            img_rotated = ndimage.rotate(img_before, median_angle)
            
            print(f"Angle is {median_angle:.04f}")
            cv2.imwrite('rotated.jpg', img_rotated)            
            
            

            
                                    
        except Exception as e:            
            logging.exception("An exception was thrown!")            
                        
    return n_ret




if __name__ == '__main__':
    """
    """
    print ("start test...")
    

    ret = test()
    
    
    print  ("finish test...")
    
    #os.system("pause") 





