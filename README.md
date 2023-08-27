## 服务器流量监控

> 必要环境python 

安装`psutil` 库

```shell
pip3 install psutil
```

运行脚本
```shell
python3 a.py
```


### 添加功能
1.更新控制台实时输出流量进出站情况，新增流量异常超过1G，单独新建一个新的log文件进行记录

2. 新增每个小时记录服务器进出站流量总和的日志文件
