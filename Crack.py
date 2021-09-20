import os, platform

try:

    import requests

except:

    os.system('pip2 install requests')

import requests

bit = platform.architecture()[0]

if bit == '32bit':

    from libvip import main

    main()

elif bit == '16bit':

    from libvip import main

    main()

