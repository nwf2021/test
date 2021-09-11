# -*- coding: utf-8 -*- 

# /*************************************************************************
#  Copyright (C), 2015-2020, 深圳创维数字技术有限公司.
#  module name: ATTCommonFun
#  function: 公共函数
#  Author: nwf
#  version: V1.1.3
#  date: 20200709
#  change log:
#  nwf    20151201       v1.1.1
#  nwf    20170114       v1.1.2
#  nwf    20200709       v1.1.3
# ***************************************************************************

from    datetime    import datetime
import  inspect
import  os
import  re
import  subprocess
import  sys
import  time
import  traceback
import  logging

from skycode import *



def get_time_filename_lineno_funcname():
     """
     """
     stacklevel =2  #default
     head = ""
             
     # copy warnings ; nwf 2012-08-14
     try:
         caller = sys._getframe(stacklevel)
     except ValueError:
         globals = sys.__dict__
         lineno = 1
     else:
         globals = caller.f_globals
         lineno = caller.f_lineno
         # nwf 2012-08-14
         f_code = caller.f_code
     if '__name__' in globals:
         module = globals['__name__']
     else:
         module = "<string>"
     filename = globals.get('__file__')
     if filename:
         fnl = filename.lower()
         if fnl.endswith((".pyc", ".pyo")):
             filename = filename[:-1]
     else:
         if module == "__main__":
             try:
                 filename = sys.argv[0]
             except AttributeError:
                 # embedded interpreters don't have sys.argv
                 filename = '__main__'
         if not filename:
             filename = module
     
     #
     filename = os.path.basename(filename)            
     
     dt1 = datetime.now()     
     head = "[%04d-%02d-%02d %02d:%02d:%02d.%03d] [%s] [%s:%d] [%s]:" %(
                    dt1.year, dt1.month, dt1.day, dt1.hour, dt1.minute, dt1.second, dt1.microsecond/1000,
                     module, filename, lineno, f_code.co_name)                
     
     return head



def init_logging():
    """
    """
    formatter = logging.Formatter('[%(asctime)s] [%(module)s] [%(funcName)s] [%(levelname)s]:\n\t%(message)s\n')

    # console
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(formatter)        
    logging.getLogger().addHandler(ch) 

    # file
    fh = logging.FileHandler('./logs/log.log')
    fh.setLevel(logging.INFO)
    fh.setFormatter(formatter)
    logging.getLogger().addHandler(fh)

    logging.getLogger().setLevel(logging.INFO)





def get_bit(value, n):
    return ((value >> n & 1) != 0)

def set_bit(value, n):
    return value | (1 << n)

def clear_bit(value, n):
    return value & ~(1 << n)






def test():
    """
    unit test
    """
    n_ret = ERR_FAIL
    n_ret_api = 0    
    desc = ""
    
    for nwf in [1]:
        
        try:
            pass
                                    
        except Exception as e:            
            logging.exception("An exception was thrown!")            
                        
    return n_ret
    
    

if __name__ == '__main__':
    test()
