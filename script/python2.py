import os
import platform

print("hello kenslor")

if platform.system() == "Windows":
    os.system("date /T")  # Windows command for date
else:
    os.system("date")     # Unix command for date
    os.system("uname -r") # Unix command for kernel version
