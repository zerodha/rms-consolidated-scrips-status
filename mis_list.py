
"""
# Copyright (c) 2020, Zerodha Tech
@author: rakeshr
"""

"""
Read RMS Consolidated scrip spreadsheet and return dictionary with allowed/non-allowed scrip
"""
import urllib.request as request
import codecs,csv,datetime
import pandas as pd

def mis_status():
    """
    Download Spreadsheet as csv and return nested dict of allowed/non-allowed scrips
    """
    sheet_url = (
        'https://docs.google.com/spreadsheets/d/1ZTyh6GiHTwA1d-ApYdn5iCmRiBLZoAtwigS7VyLUk_Y/export?gid=0&format=csv'
        )
    #Download google spreadsheet as csv       
    sheet_stream = request.urlopen(sheet_url)
    col_list = ['Stocks allowed for MIS', 
                'Margin allowed',
                'Stocks not allowed for MIS',
                'Stocks which were allowed but temporarily banned']    
    mis_csv = pd.read_csv(
        sheet_stream, 
        encoding='utf-8',
        usecols=col_list,
        keep_default_na=False)
    #Create nested_dict for Mis allowed scrip with margin multiplier
    mis_dict = {}
    mis_dict['mis_allowed'] = {}
    data_scrip = mis_csv['Stocks allowed for MIS']
    data_multi = mis_csv['Margin allowed']
    for serial,scrip, multiplier in zip(range(data_scrip.size),
                                            data_scrip, 
                                            data_multi):
        #Don't read nan/empty rows
        if scrip and multiplier:
            mis_dict['mis_allowed'][serial] = {
                                            'symbol':scrip,
                                            'multiplier':multiplier
                                            }
    #Create nested_dict for Mis not allowed scrip        
    mis_dict['mis_notallowed'] = {}
    data_nonmis = mis_csv['Stocks not allowed for MIS']
    for serial,scrip in zip(range(data_nonmis.size), data_nonmis):
        mis_dict['mis_notallowed'][serial] = {'symbol':scrip}

    return mis_dict  
