import psutil
import time

def log_total_traffic(logfile):
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
        
        # 将结果写入日志文件
        with open(logfile, 'a') as f:
            f.write(f'Time: {time.ctime()}, GB sent: {gb_sent:.6f}, GB received: {gb_recv:.6f}\n')
        
        # 更新网络接口信息
        old_net_io = new_net_io

# 调用函数
log_file = "total_traffic_gb.log"
log_total_traffic(log_file)
