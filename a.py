import psutil
import time

def log_total_traffic(logfile, alertfile):
    # 获取初始的网络接口信息
    old_net_io = psutil.net_io_counters()
    
    while True:
        # 等待一秒钟
        time.sleep(1)
        
        # 再次获取网络接口信息
        new_net_io = psutil.net_io_counters()
        
        # 计算发送和接收的字节，并转换为GB
        gb_sent = (new_net_io.bytes_sent - old_net_io.bytes_sent) / (1024 ** 3)
        gb_recv = (new_net_io.bytes_recv - old_net_io.bytes_recv) / (1024 ** 3)
        
        # 输出流量情况到控制台
        print(f'Time: {time.ctime()}, GB sent: {gb_sent:.6f}, GB received: {gb_recv:.6f}')
        
        # 将结果写入日志文件
        with open(logfile, 'a') as f:
            f.write(f'Time: {time.ctime()}, GB sent: {gb_sent:.6f}, GB received: {gb_recv:.6f}\n')
        
        # 如果流量超过1GB，将结果写入异常流量日志文件
        if gb_sent > 1 or gb_recv > 1:
            with open(alertfile, 'a') as f:
                f.write(f'Time: {time.ctime()}, GB sent: {gb_sent:.6f}, GB received: {gb_recv:.6f}\n')
        
        # 更新网络接口信息
        old_net_io = new_net_io

# 调用函数
log_file = "total_traffic_gb.log"
alert_file = "alert_traffic_gb.log"
log_total_traffic(log_file, alert_file)