import psutil

def check_syatem_metrics():
    cpu_threshold = int(input("Enter CPU usage threshold"))
    disk_threshold = int(input("Enter Disk usage threshold"))
    memory_threshold = int(input("Enter Memory usage threshold"))

    cpu_threshold = psutil.cpu_percent(interval=1)
    disk_threshold = psutil.disk_usage('/').percent
    memory_threshold = psutil.virtual_memory().percent

    print("current CPU %:", cpu_threshold)
    print("current Disk %:", disk_threshold)
    print("current Memory %:", memory_threshold)

    if cpu_threshold > cpu_threshold:
        print("CPU usage is above the threshold")
    else:
        print("CPU usage is below the threshold")
        if disk_threshold > disk_threshold:
            print("Disk usage is above the threshold")
        else:
            print("Disk usage is below the threshold")
            if memory_threshold > memory_threshold:
                print("Memory usage is above the threshold")
            else:
                print("Memory usage is below the threshold")

check_syatem_metrics()