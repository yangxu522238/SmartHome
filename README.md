# SmartHome


This is a smart home control system based on qualcomm 410c, QCA40120, CSR1025 development board,
which mainly includes lighting control, smoke detection, and intelligent curtains. 
The different modules are uniformly managed by 410c and connected to the server.


Material Used
-------
pixel;
qualcomm dragonboard 410c;
qualcomm QCA4020 board;
mq-2 smoke detector;
CSR1025 develop board ;
battery ;
light bulb ;
a lots of wire;
Ordinary motor；


SoftWre requirement 
-------
Android studio;
Pyqt;
include other module (https://github.com/yangxu522238/Smartcurtain)
（https://github.com/yangxu522238/SmokeDetector）
（https://github.com/yangxu522238/SmartLight）

Instructions
===========

Hardware requirement
----
same with Material Used

software requirements
-------

First. the development steps
1.Environmental construction
(1) Pyqt environment and python environment to build
(2) Wilddog-python environment to build
In the development environment of Windows 7 and the running environment of the 410c development board,
the development environment of wilddog-python needs to be built as follows:
1. Open the cmd command line (open the terminal in the 410c development board), enter the pip list, 
and the following image appears to indicate that the pip is installed.

2. If the above image does not appear, you need to reinstall PIP. 
First download the corresponding version of the PIP file in the https://pypi.python.org/pypi/pip#downloads link, 
extract the PIP installation package to a folder, and then open it. Terminal, enter the decompressed directory,
enter python setup.py install, and then add C:\ Python34 \ Scripts to the computer environment variable;

3. After Pip confirms the installation, enter pip install pygatt,
pip install requests == 1.1.0 and pip install wilddog-python in the terminal.
The following image is displayed indicating that the installation is complete.

4. Open the async.py file in the path C:\Python34\lib\site-packages\wilddog.
Modify from lazy import LazyLoadProxy to from .lazy import LazyLoadProxy

5. Open the wilddog.py file in the path C:\Python34\lib\site-packages\wilddog\, 
modify from wilddog_token_generator import create_token to from .
wilddog_token_generator import create_token, modify from decorators import http_connection to from .
decorators import http_connection, modify from Async import process_pool is from .async import process_pool,
modify from jsonutil import JSONEncoder to from .jsonutil import JSONEncoder



6. Open the connectionpool.py file in the path C:\Python34\lib\site-packages\requests\packages\urllib3\ and modify connection = VerifiedHTTPSConnection (host=self.host,port=self.port,strict=self.strict ) for connection = VerifiedHTTPSConnection (host=self.host,port=self.port)



building the application
---------
you can find it in developer detail file;


how to start the application
---------
you can find it in developer detail file;

how to use the application
---------
you can find it in developer detail file;

how to stop the application
---------
you can find it in developer detail file;

