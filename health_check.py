import psutil
import shutil

if psutil.cpu_percent() < 80.0:
  print("Everything about CPU looks good.")
else:
  print("Your CPU usage is high.")

memory = shutil.disk_usage('/')
total_memory = memory.total
free_memory = memory.free
free_percent = (free_memory / total_memory) * 100
if free_percent < 20:
    print("Your Disk Space is less than 20%")
else:
    print("You have enough disk space")

memory = psutil.virtual_memory()
memory_MB = memory.available >> 20
if memory_MB < 500:
    print("Your have less than 500MB memory available")
else:
    print("You have enough memory")

#print(psutil.virtual_memory().percent)
#print(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total)
#Report an error if CPU usage is over 80%
#Report an error if available disk space is lower than 20%
#Report an error if available memory is less than 500MB
