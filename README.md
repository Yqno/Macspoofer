# Macchanger
a Python Script that changes your MAC Address on Windows and Linux


This manual provides instructions on how to modify the Media Access Control (MAC) address on Windows and Linux operating systems. To execute the program, please perform the following steps:

Firstly, obtain a copy of the script from the Github repository by either cloning it or downloading it.

Then, launch a terminal window and navigate to the directory where the script is located.

Next, authorize the script to be executed by executing the command ```chmod +x macchanger.py```

To run the program, enter the following command:

On Windows: ```python macchanger.py [interface] -r/-m [MAC address]```



On Linux: ```sudo python3 macchanger.py [interface] -r/-m [MAC address]```

Replace [interface] with the name of your network interface you can find your interface on Windows with ```ìpconfig``` 
and on Linux ```ìfconfig```. 

Additionally, either utilize the -r flag to generate a random MAC address or the -m flag followed by a MAC address to define a specific one.

Upon successful execution, the script will exhibit your existing permanent MAC address in addition to the newly designated MAC address.

Please note that, depending on your operating system, you may be required to install supplementary packages or execute the script with administrator rights for it to function properly.
