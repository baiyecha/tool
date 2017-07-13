# -*- coding:utf-8 -*-
import os
import shutil

va_xPath = "C:\\Users\\tu\\AppData\\Local\\Microsoft\\VisualStudio\\14.0\\Extensions"
list = os.listdir(va_xPath)
va_xFile = []
for e in list:
    if e.find('.xml') != -1:
        continue
    if e.find('.cache') != -1:
        continue
    if not os.path.isdir(va_xPath + '\\' + e) :
        continue;
    for d in os.listdir(va_xPath + '\\' + e):
        if 'VA_X.dll' == d:
            va_xFile.append(va_xPath + '\\' + e);
            break

for filePath in va_xFile
    print filePath
    shutil.rmtree(filePath)

        
