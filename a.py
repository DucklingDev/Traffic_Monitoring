import psutil
import time

def log_total_traffic(logfile, alertfile, hourlyfile):
    old_net_io = psutil.net_io_counters()
    gb_sent_minute = 0
    gb_recv_minute = 0
    gb_sent_hourly = 0
    gb_recv_hourly = 0
    
    with open(logfile, 'a') as logf, open(alertfile, 'a') as alertf, open(hourlyfile, 'a') as hourlyf:
        while True:
            start_time = time.perf_counter()
            current_time = time.strftime("%Y-%m-%d %H:%M:%S")
            
            new_net_io = psutil.net_io_counters()
            
            gb_sent = (new_net_io.bytes_sent - old_net_io.bytes_sent) / (1024 ** 3)
            gb_recv = (new_net_io.bytes_recv - old_net_io.bytes_recv) / (1024 ** 3)
            
            gb_sent_minute += gb_sent
            gb_recv_minute += gb_recv
            gb_sent_hourly += gb_sent
            gb_recv_hourly += gb_recv
            
            print(f'Time: {current_time}, GB sent: {gb_sent:.6f}, GB received: {gb_recv:.6f}')
            
            # 每分钟写入这一分钟内的所有流量总和
            if int(time.strftime("%S")) == 59:
                logf.write(f'Time: {current_time}, GB sent: {gb_sent_minute:.6f}, GB received: {gb_recv_minute:.6f}\n')
                logf.flush()
                gb_sent_minute = 0
                gb_recv_minute = 0
            
            # 流量超过500MB就写入
            if gb_sent > 0.5 or gb_recv > 0.5:
                alertf.write(f'Time: {current_time}, GB sent: {gb_sent:.6f}, GB received: {gb_recv:.6f}\n')
                alertf.flush()
            
            old_net_io = new_net_io
            
            if int(time.strftime("%M")) == 59 and int(time.strftime("%S")) == 59:
                hourlyf.write(f'Time: {current_time}, Hourly GB sent: {gb_sent_hourly:.6f}, Hourly GB received: {gb_recv_hourly:.6f}\n')
                hourlyf.flush()
                gb_sent_hourly = 0
                gb_recv_hourly = 0
            
            end_time = time.perf_counter()
            time.sleep(max(1.0 - (end_time - start_time), 0))

log_file = "total_traffic_gb.log"
alert_file = "alert_traffic_gb.log"
hourly_file = "hourly_traffic_gb.log"
log_total_traffic(log_file, alert_file, hourly_file)
