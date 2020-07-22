# rms-consolidated-scrips-status

A utility that parse [ZerodhaRMS Consolidated google spreadsheet](https://docs.google.com/spreadsheets/d/1ZTyh6GiHTwA1d-ApYdn5iCmRiBLZoAtwigS7VyLUk_Y/edit#gid=0) and render category-wise scrip details(margins, multiplier, etc). 

# Installation

``` 
pip install consolidatedrms
```

# Usage and documentation

```
from consolidatedrms import ConsolidatedList

ConsolidatedSheet = ConsolidatedList()
```

#### Fetch allowed/banned mis scrips dict with multiplier value
```
ConsolidatedSheet.mis_status()
```

```
{'status': 'success', 'data': {'mis_allowed': [{'symbol': '3MINDIA', 
'multiplier': '5'}, {'symbol': 'AARTIIND', 'multiplier': '5'},{...}],
'mis_banned': [{'symbol': '21STCENMGM'}, {'symbol': '3IINFOTECH'},{..}]}}
```
#### Fetch complete margin values for BO/CO allowed scrip
```
ConsolidatedSheet.mis_margin()
```

```
{'status': 'success', 'data': [{'symbol': '3MINDIA', 'var+elm': 40.0, 
'mis_margin': 20.0, 'multiplier': 5.0, 'co_lower': 10.0, 'co_upper': 10},
{...}]}
```

#### Fetch list of scrips allowed/banned/temp banned for BO and CO
```
ConsolidatedSheet.mis_boco()
```

```
{'status': 'success', 'data': {'boco_allowed': [{'symbol': '3MINDIA'}, 
{'symbol': 'AARTIIND'}, {'symbol': 'ABB'},{...}]}}
```

#### Fetch list of scrips under Trade to Trade segment
```
ConsolidatedSheet.trade2trade()
```

```
{'status': 'success', 'data': [{'symbol': 'BAFNAPH'}, 
{'symbol': 'CASTEXTECH'}, {'symbol': 'JIKIND'},..,
{...}]}
```

#### Fetch list of scrips under ASM (Additional Surveillance Measure)
```
ConsolidatedSheet.asm_status()
```

```
{'status': 'success', 'data': [{'symbol': '3IINFOTECH'}, {'symbol': 'AARTIDRUGS'}, 
{'symbol': 'ABAN'},,..{..}]}
```

#### Fetch list of scrips under GSM (Graded Surveillance Measure)
```
ConsolidatedSheet.gsm_status()
```

```
{'status': 'success', 'data': [{'symbol': 'ADROITINFO'}, {'symbol': 'ALPSINDUS'}, 
{'symbol': 'ANKITMETAL'},..,{..}]}
```
### Fetch Margin and Multiplier details for F&O scrips
```
ConsolidatedSheet.fno_margin()
```

```
{'status': 'success', 'data': [{'symbol': 'ACC', 
'expiry': '30-Jul-2020', 'nrml_margin': 22.06, 
'mis_margin': 10.0, 'mis_multiplier': 10.0, 
'co_lower': 3.31, 'co_muliplier': 30.22},..,{..}]}
```
