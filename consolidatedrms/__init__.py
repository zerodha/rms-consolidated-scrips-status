"""
# Copyright (c) 2020, Zerodha Tech
@author: rakeshr
"""

"""
Read RMS Consolidated scrip spreadsheet and return dictionary with different 
mis scrip related detail(margins, multiplier,etc)
"""

from .consolidatedrms import ConsolidatedList

__all__ = ["ConsolidatedList"]