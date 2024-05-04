# 获取最新水位脚本

## 当下痛点
人工查找水信息网站水文站水位数据，费时费力，容易发生数据摘抄错误。


## 功能简介

### 功能1
运行程序，生成含目标水位信息的csv文件，通过wps导入此文件更新表格中水位数据。

### 功能2
运行程序，自动生成以当前日期命名预制好的表格文件，并填好相应水位数据及日期。


## 程序打包
打包命令:
```shell
pyinstaller -n 水位小助手 -D src/main.py
```
