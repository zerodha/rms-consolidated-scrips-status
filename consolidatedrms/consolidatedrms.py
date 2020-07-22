
"""
# Copyright (c) 2020, Zerodha Tech
@author: rakeshr
"""

"""
Read RMS Consolidated scrip spreadsheet and return dictionary with different mis scrip related detail(margins, multiplier,etc)
"""
import urllib.request as request
import pandas as pd
from urllib.parse import urljoin

class ConsolidatedList(object):
    """
    RMS Consolidated list of Scrips Class
    """
    _root_url = (
        'https://docs.google.com/spreadsheets/d/1ZTyh6GiHTwA1d-ApYdn5iCmRiBLZoAtwigS7VyLUk_Y/export'
        )
    _fo_url = (
        'https://docs.google.com/spreadsheets/d/1fLTsNpFJPK349RTjs0GRSXJZD-5soCUkZt9eSMTJ2m4/export?gid=0&format=csv'
        )
    _urls = {
        'mis' : '?gid=0&format=csv',
        'mis_margin' : '?gid=1058102715&format=csv',
        'boco' : '?gid=1813575034&format=csv',
        't2t': '?gid=1643697971&format=csv',
        'asm' : '?gid=1228122613&format=csv',
        'gsm' : '?gid=1713387562&format=csv'
    } 


    def mis_status(self):
        """
        Return nested dict of allowed/non-allowed mis scrips with margin multiplier
        """
        try:
            col_list = ['Stocks allowed for MIS', 
                        'Margin allowed',
                        'Stocks not allowed for MIS',
                        'Stocks which were allowed but temporarily banned']    
            
            sheet_df = self.create_dataframe(self._urls['mis'],
                                            col_list)
            
            #Create nested_dict for Mis allowed scrip with margin multiplier
            mis_dict = {}
            mis_dict['mis_allowed'] = []
            #Exact specific column
            data_scrip = sheet_df['Stocks allowed for MIS']
            data_multi = sheet_df['Margin allowed']
            for scrip, multiplier in zip(data_scrip, 
                                                data_multi):
                #Don't read nan/empty rows
                if scrip and multiplier:
                    mis_dict['mis_allowed'].append({
                                                    'symbol':scrip,
                                                    'multiplier':multiplier.strip('X')
                                                    })

            #Create nested_dict for MIS banned scrip        
            mis_dict['mis_banned'] = self.create_ds(sheet_df,
                                            'Stocks not allowed for MIS')

            return self.format_response(mis_dict)
    
        except Exception as e:
            err_msg = {'error_type':type(e).__name__, 'error_msg':str(e)}
            return self.format_response(err_msg)   

    def mis_margin(self):
        """
        Return dict with Var+ ELM,MIS Margin,MIS Multiplier,CO Lower Trigger,
        CO Upper Trigger values for allowed BO/CO allowed scrip
        """
        try:
            col_list = ['BO/CO allowed scrips(NSE)', 
                        'Var+ ELM',
                        'MIS Margin',
                        'MIS Multiplier',
                        'CO Lower Trigger',
                        'CO Upper Trigger']

            sheet_df = self.create_dataframe(self._urls['mis_margin'],
                                            col_list,
                                            header=1)
            intraday_margin = []
            #Exact specific column
            boco_scrips = sheet_df['BO/CO allowed scrips(NSE)']
            var_elms = sheet_df['Var+ ELM']
            boco_margins = sheet_df['MIS Margin']
            multipliers = sheet_df['MIS Multiplier']
            lower_triggers = sheet_df['CO Lower Trigger']
            upper_triggers = sheet_df['CO Upper Trigger']
            for scrip,var_elm,margin,multiplier,ltrigger,utrigger in zip(boco_scrips,
                                                                var_elms,boco_margins,
                                                                multipliers,
                                                                lower_triggers,
                                                                upper_triggers):
                intraday_margin.append({'symbol':scrip, 'var+elm':var_elm, 'mis_margin':margin,
                                    'multiplier':multiplier, 'co_lower':ltrigger,
                                    'co_upper':utrigger})

            return self.format_response(intraday_margin)

        except Exception as e:
            err_msg = {'error_type':type(e).__name__, 'error_msg':str(e)}
            return self.format_response(err_msg)  

    def mis_boco(self):
        """
        Return list of scrips allowed/non-allowed/temp banned for BO and CO
        """
        try:
            col_list = ['Stocks not allowed on BO/CO', 
                        'Stocks allowed on BO/CO',
                        'Stocks which were allowed but temporarily banned in BO',
                        ]

            sheet_df = self.create_dataframe(self._urls['boco'],
                                            col_list)
            #Create dict of BO/CO allowed scrips
            boco_status = {}
            boco_status['boco_allowed'] = self.create_ds(sheet_df,
                                        'Stocks allowed on BO/CO')
            
            #Create dict of BO/CO banned scrips
            boco_status['boco_banned'] = self.create_ds(sheet_df,
                                        'Stocks not allowed on BO/CO')

            #Create dict of temporarily banned BO scrips
            boco_status['boco_tempban'] = self.create_ds(sheet_df,
                                        'Stocks which were allowed but temporarily banned in BO')
            
            return self.format_response(boco_status)
        
        except Exception as e:
            err_msg = {'error_type':type(e).__name__, 'error_msg':str(e)}
            return self.format_response(err_msg)
    
    def trade2trade(self):
        """
        Return list of scrips under Trade to Trade segment
        """
        return self.create_structure(self._urls['t2t'], 'Symbol')

    def asm_status(self):
        """
        Return list of scrips under ASM (Additional Surveillance Measure)
        """
        return self.create_structure(self._urls['asm'], 'SYMBOL', header=1)

    def gsm_status(self):
        """
        Return list of scrips under GSM (Graded Surveillance Measure)
        """
        return self.create_structure(self._urls['gsm'], 'Symbol')
    
    def fno_margin(self):
        """
        Return NRML Margin %,MIS Margin %,MIS Multiplier,CO Lower Margin%
        and CO Multiplier for F&O scrip
        """
        try:
            fno_stream = request.urlopen(self._fo_url)
            col_list = ['Scrip', 'Span Expiry Date',
                        'NRML Margin %','MIS Margin %',
                        'MIS Multiplier','CO Lower Margin%',
                        'CO Multiplier']

            fno_df = pd.read_csv(fno_stream, 
                    encoding='utf-8', usecols=col_list,
                    keep_default_na=False)

            fno_detail = []
            #Exact margin specific column
            scrips = fno_df['Scrip']
            expiries = fno_df['Span Expiry Date']
            nrml_per = fno_df['NRML Margin %']
            mis_per = fno_df['MIS Margin %']
            mis_multiplier = fno_df['MIS Multiplier']
            co_lower_per = fno_df['CO Lower Margin%']
            co_multiplier = fno_df['CO Multiplier']

            for scrip,expiry,nrml,mis,mis_multi,lco_per,co_multi in zip(scrips,expiries,
                                                                nrml_per,mis_per,
                                                                mis_multiplier,
                                                                co_lower_per,co_multiplier):
                fno_detail.append({'symbol':scrip, 'expiry':expiry, 'nrml_margin':nrml,
                                    'mis_margin':mis, 'mis_multiplier':mis_multi,
                                    'co_lower':lco_per, 'co_muliplier':co_multi})

            return self.format_response(fno_detail)

        except Exception as e:
            err_msg = {'error_type':type(e).__name__, 'error_msg':str(e)}
            return self.format_response(err_msg)
    
    def create_dataframe(self,sub_url,col_list,header=0):
        """
        Return Pandas dataframe for given csv 
        Param url:(string) - unique sub-url for required sheet
        Param col_list:(list) - List of column header to be extracted
        Param header:(int) - column header position
        """
        _sheet_url = urljoin(self._root_url, sub_url)
        try:
            #Download required spreadsheet as csv       
            sheet_stream = request.urlopen(_sheet_url)
            sheet_df = pd.read_csv(
                sheet_stream, 
                encoding='utf-8',
                usecols=col_list,
                header=header,
                keep_default_na=False)
            return sheet_df
        except Exception as e:
            raise e     

    def create_structure(self,sub_url,col_header,header=0):
        """
        Return data structure formed based on requested params
        Param url:(string) - unique sub-url for required sheet
        Param col_header:(string) - column header to be extracted
        Param header:(int) - column header position 
        """
        try:
            sheet_df = self.create_dataframe(sub_url,[col_header],header)
            #Create dict for required category
            category_ds= self.create_ds(sheet_df,col_header)
            return self.format_response(category_ds)

        except Exception as e:
            err_msg = {'error_type':type(e).__name__, 'error_msg':str(e)}
            return self.format_response(err_msg)


    def create_ds(self,csv_df,column_header):
        """
        Form dict on sepcific column based on input data
        Param csv_df:(DataFrame) - Pandas dataframe of required csv
        Param column_header:(string) - Required column header to be extracted
        """
        csv_data = csv_df[column_header]
        data_list = []
        for scrip in csv_data:
            #Don't read null/empty rows
            if scrip:
                data_list.append({'symbol':scrip})
        return data_list

    def format_response(self,response):
        """
        Format and add status to final response
        Param response:(dict) - Dict with specific rms consolidated data
        """
        if 'error_type' in response:
            response = {'status' : 'error', 'data' : response}
        else:
            response = {'status' : 'success', 'data' : response}
        return response 