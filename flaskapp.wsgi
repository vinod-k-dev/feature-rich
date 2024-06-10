#!/usr/bin/python3

import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/path/to/your/flaskapp/")

from app import create_app
application = create_app()
