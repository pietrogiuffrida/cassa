#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from time import sleep
import os
import sys
import logging
logging.basicConfig(
  format='%(asctime)s\t%(levelname)s\t%(message)s',
  filename='test.log',
  level=logging.INFO,
  #level=logging.DEBUG,
  )

logging.info("*"*20 + " NUOVA ESECUZIONE " + "*"*20)

#print('Test29')

sleep(5)
sys.stderr.write("1")
#sys.stdout.write("1")

#os._exit(1)
