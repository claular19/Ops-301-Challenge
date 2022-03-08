#!/bin/python3

# Script should be run with sudo initially

# import the os library
import os

# Displays a message stating that CPU hardware specs are being displayed below it
print("Displaying system info for CPU")

# Declares a variable that runs the bash script for fetching CPU info
call_cpu_specs = os.system("lshw -c cpu | grep -e 'product' -e 'vender' -e 'physical id' -e 'bus info' -e 'width'")

# Calls previous variable and runs bash script
call_cpu_specs

# Displays a message stating that RAM hardware specs are being displayed below it
print("Displaying system info for RAM")

# Declares a variable that runs the bash script for fetching RAM info
call_ram_specs = os.system("lshw -c memory | grep -e 'description' -e 'physical id' -e 'size'")

# Calls previous variable and runs bash script
call_ram_specs

# Displays a message stating that display adapter hardware specs are being displayed below it
print("Displaying system info for display adapter")

# Declares a variable that runs the bash script for fetching display adapter info
call_display_specs = os.system("lshw -c display | grep -e 'description' -e 'product' -e 'vendor' -e 'physical id' -e 'bus info' -e 'width' -e 'clock' -e 'capabilities' -e 'configuration'")

# Calls previous variable and runs bash script
call_display_specs
