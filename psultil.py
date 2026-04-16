import psutil

print(psutil.cpu_percent(interval=1))

print(*psutil.disk_partitions(), '\n')

print(psutil.disk_usage('C:/'))
