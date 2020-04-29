# PICK Tool Installation Instructions

## Install PICK Tool Dependencies

1. Users must install and boot up the Kali Linux OS

 - From [[1](#references)], "Kali Linux is an open source [operating system] project that is maintained and funded by Offensive Security, a provider of world-class information security training and penetration testing services."
 - PICK Tool is built to run on Kali Linux. The Kali Linux ISO can be download directly from the Kali Linux website [here](https://www.kali.org/).

2. Users must install or verify the installation of Python 3.7.5

 - From [[2](#references)], "Python is a programming language that lets you work more quickly and integrate your systems more effectively."
 - PICK Tool is built using Python 3.7.5, and requires this programming language to run. Python 3.7.5 can be downloaded from the python website [here](https://www.python.org/downloads/).

3. Users must install Splunk Enterprise

 - From [[3](#references)], "Splunk captures, indexes, and correlates real-time data in a searchable repository from which it can generate graphs, reports, alerts, dashboards, and visualizations."
 - PICK Tool depends on Splunk Enterpise and requires dependency, which can be downloaded [here](https://www.splunk.com/en_us/download/splunk-enterprise.html).

4. Users must install or verify the installation of the Splunk Python JDK

 - From [[4](#references)], "The Splunk Software Development Kit (SDK) for Python contains library code and examples designed to enable developers to build applications using Splunk."
 - PICK Tool depends on Splunk Enterpise and requires dependency, which can be downloaded [here](https://www.splunk.com/en_us/download/splunk-enterprise.html).
 - Most Linux users can install the SDK using the following commands: ```pip install splunk-sdk``` or ```pip3 install splunk-sdk```.
 - Debian Users may need to clone the Github repo and follow the instructions listed therein.

5. Users must install or verify the installation of PyQt5 v5.14.1

 - From [[5](#references)], "Qt is set of cross-platform C++ libraries that implement high-level APIs for accessing many aspects of modern desktop and mobile systems. These include location and positioning services, multimedia, NFC and Bluetooth connectivity, a Chromium based web browser, as well as traditional UI development. PyQt5 is a comprehensive set of Python bindings for Qt v5."
 - Most Linux users can install PyQt5 using the following command: ```pip3 install PyQt5==5.14.1```.
 - Debian Users may need to use other download links, provided [here](https://pypi.org/project/PyQt5/#files).

## Run PICK Tool

1. From the top-level directory, enter the following command to run PICK Tool: ```python3 src/controllers/pick.py```.

## References

[1] “About Kali Linux,” Kali Linux. [Online]. Available: https://www.kali.org/about-us/. [Accessed: 29-Apr-2020].
[2] “Welcome to Python.org,” Python.org. [Online]. Available: https://www.python.org/. [Accessed: 29-Apr-2020].
[3] “Splunk,” Wikipedia, 26-Mar-2020. [Online]. Available: https://en.wikipedia.org/wiki/Splunk. [Accessed: 29-Apr-2020].
[4] Splunk, “splunk/splunk-sdk-python,” GitHub, 24-Mar-2020. [Online]. Available: https://github.com/splunk/splunk-sdk-python. [Accessed: 29-Apr-2020].
[5] “PyQt5,” PyPI. [Online]. Available: https://pypi.org/project/PyQt5/. [Accessed: 29-Apr-2020].
