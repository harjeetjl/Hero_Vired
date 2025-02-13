import psutil
import time

print("Monitoring CPU usage...")

# Using a while loop to continuously monitor the CPU usage of the program
while True:
    try:
        # Calling the psutil.cpu_percent() function with an interval of 1 second
        # which means that the function will return the CPU utilization as a percentage averaged over the last second
        cpu_percent = psutil.cpu_percent(interval=1)
        print(f"CPU Usage: {cpu_percent}%")
        if(cpu_percent > 80):
            print(f"Alert! CPU usage exceeds threshold: {cpu_percent}%")
        # sleeping for 1 second before repeating the process
        time.sleep(1)
    except Exception as e:
        print(f"Exception occured: {e}")
        raise