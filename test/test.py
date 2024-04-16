import datetime

import pytest
import CopiftLogger.logger

def test_logger():
   CopiftLogger.logger.createLogger().info('hello')
   x=open('project.log','r')

   assert f'CopiftLogger.logger - INFO - {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}  : (test.py).test_logger(7) hello\n' == x.readlines()[0]

