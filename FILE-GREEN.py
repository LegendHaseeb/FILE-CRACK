import os, platform
 
try:
 
        import requests
 
except:
 
        os.system('pip2 install requests')
 
 
 
import requests
 
bit = platform.architecture()[0]
 
if bit == "64bit":
 
        from MAHADIF import __login
 
        __login()
 
 
 
elif bit == "32bit":
 
        from MAHADIF32 import __login
 
 
        __login()
 
 
