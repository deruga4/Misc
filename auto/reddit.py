import pyperclip
import webbrowser
import sys

browser = '/usr/bin/google-chrome %s'

if len(sys.argv) == 2:
    webbrowser.get(browser).open('https://reddit.com/r/' + sys.argv[1])
else:
    print('Two arguments only pls')
