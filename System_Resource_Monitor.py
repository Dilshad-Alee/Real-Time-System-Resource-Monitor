import time
import psutil

def display_usage(cpu_usage, memory_usage, bars=50):
    # Calculate the CPU usage bar
    cpu_percent = cpu_usage / 100.0
    cpu_bar = '▊' * int(cpu_percent * bars) + '-' * (bars - int(cpu_percent * bars))
    
    # Calculate the memory usage bar
    mem_percent = memory_usage / 100.0
    mem_bar = '▊' * int(mem_percent * bars) + '-' * (bars - int(mem_percent * bars))
    
    # Print the CPU and Memory usage with progress bars
    print(f"\rCPU usage:    |{cpu_bar}| {cpu_usage:.2f}%  ", end="")
    print(f"Memory usage: |{mem_bar}| {memory_usage:.2f}%", end="")
while True:
    # Get CPU and Memory usage
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    display_usage(cpu, memory)
    time.sleep(0.5)