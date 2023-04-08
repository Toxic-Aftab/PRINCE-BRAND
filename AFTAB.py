import os, platform

try:

    import requests

except:

    os.system('pip install requests')

import requests

bit = platform.architecture()[0]

if bit == '64bit':

    from AFTAB import menu

    menu()

elif bit == '32bit':

    from AFTAB2 import menu

    menu()
