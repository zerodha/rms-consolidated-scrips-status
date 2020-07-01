# rms-consolidated-scrips-status
A utility that reads <a href="https://docs.google.com/spreadsheets/d/1ZTyh6GiHTwA1d-ApYdn5iCmRiBLZoAtwigS7VyLUk_Y/edit#gid=0">RMS Consolidated google spreadsheet</a> and returns a nested dictionary with allowed/non-allowed scrip for different product types

# Basic Usage
``` 
git clone https://github.com/zerodhatech/rms-consolidated-scrips-status.git
import mis_list
mis_list()
```
# Sample Response
For MIS allowed Stocks
```
{'mis_allowed': {0: {'symbol': '3MINDIA:EQ', 'multiplier': '5X'}, 1: {'symbol': 'AARTIIND:EQ', 'multiplier': '5X'},
2: {'symbol': 'ABB:EQ', 'multiplier': '5X'}, 3: {'symbol': 'ABBOTINDIA:EQ', 'multiplier': '5X'}, 4:....}}

For Stocks not allowed for MIS 
{'mis_notallowed': {0: {'symbol': '21STCENMGM'}, 1: {'symbol': '3IINFOTECH'}, 2: {'symbol': '3PLAND'}, 
3: {'symbol': '5PAISA'}, 4: {'symbol': '63MOONS'}, 5: {'symbol': '7NR'}, 6: {'symbol': '8KMILES'}...}
