# Extend pelicanconf.py and apply some additional settings
import os, sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://marcsleegers.com'
RELATIVE_URLS = False
OUTPUT_PATH = 'output/publish/'
