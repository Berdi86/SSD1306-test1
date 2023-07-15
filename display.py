import time
import sys
from ssd1306 import SSD1306_I2C

# Initialize the display.
display = SSD1306_I2C(128, 64, i2c_bus=1, i2c_address=0x3c)

# Clear the display.
display.clear()

# Write the CPU load to the display.
cpu_load = round(100 * os.popen("top -n 1 -b -n 1 | grep 'CPU utilization' | awk '{print $2}'").read(), 1)
display.write_text(cpu_load, 0, 0)

# Write the temperature to the display.
temperature = round(os.popen("cat /sys/class/thermal/thermal_zone0/temp").read(), 1)
display.write_text(temperature, 0, 10)

# Write the network speed to the display.
network_speed = round(os.popen("speedtest -n").read(), 1)
display.write_text(network_speed, 0, 20)

# Write the disk usage to the display.
disk_usage = round(os.popen("df -h | grep '/dev/sda1' | awk '{print $5}'").read(), 1)
display.write_text(disk_usage, 0, 30)

# Display the data on the display.
display.display()

# Loop forever and update the display every second.
while True:
    time.sleep(1)
    cpu_load = round(100 * os.popen("top -n 1 -b -n 1 | grep 'CPU utilization' | awk '{print $2}'").read(), 1)
    temperature = round(os.popen("cat /sys/class/thermal/thermal_zone0/temp").read(), 1)
    network_speed = round(os.popen("speedtest -n").read(), 1)
    disk_usage = round(os.popen("df -h | grep '/dev/sda1' | awk '{print $5}'").read(), 1)
    display.clear()
    display.write_text(cpu_load, 0, 0)
    display.write_text(temperature, 0, 10)
    display.write_text(network_speed, 0, 20)
    display.write_text(disk_usage, 0, 30)
    display.display()
