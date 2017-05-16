# CMDB-BE

# 配置文件
默认使用conf目录下的default.ini，自定义配置复制default.ini为cmdb.ini然后修改即可
# 导入初始化测试数据
    注意mysql建库  
执行命令：
```Bash
python manage.py makemigrations  
python manage.py makemigrations asset  
python manage.py loaddata servers.json  
```
