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


### 更细日志
- 更新控制台实时输出流量进出站情况，新增流量异常超过1G，单独新建一个新的log文件进行记录

- 新增每个小时记录服务器进出站流量总和的日志文件

- 性能优化 
    - 使用time.strftime直接获取时间字符串
    - 只在整点和流量异常的时候写入文件
    - 使用time.perf_counter获取更精确的时间间隔

