# -*- coding: utf-8 -*-

import logging
import os

#log_file = os.path.join(os.getcwd(),'wlog.log')
#print(log_file)
log_format = "%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s: %(message)s"
logging.basicConfig(level=logging.WARNING,format=log_format)
logging.warning("warning message")
logging.error("error message")
