# -*- coding: utf-8 -*-

''''' 
Python - OpenCV Tutorial
指定画像をそのまま表示する

以下を丸々参考に
http://www.takunoko.com/blog/pyenv%E3%81%A7python%E3%81%AEopencv%E7%92%B0%E5%A2%83%E3%82%92%E6%95%B4%E3%81%88%E3%82%8B/
'''

import cv2
import sys
 
argvs = sys.argv
if (len(argvs) != 2):
    print 'Usage: python %s filename' % argvs[0]
    quit()

imagefilename = argvs[1]
try:
    img = cv2.imread(imagefilename, 1)
except:
    print 'faild to load %s' % imagefilename
    quit()
 
# view image
windowName = 'LoadImage'
cv2.imshow( windowName, img)
print 'press any key to exit.'
 
cv2.waitKey(0)
