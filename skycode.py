# /*************************************************************************
#  Copyright (C), 2015-2020, 深圳创维数字技术有限公司.
#  module name: 
#  function: 
#  Author: ATT development group
#  version: 
#  date: 2020-06-18
#  change log:
#  nwf     20200618    created
#
# ***************************************************************************

# 通用返回码
_ERR_START      = 0x0000
ERR_SUCCESS     = (_ERR_START + 0)              # 成功只有一种
ERR_FAIL        = (_ERR_START + 1)              # 一般错误
ERR_FATAL       = (_ERR_START + 2)              # 致命错误 中断流程