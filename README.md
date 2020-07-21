# rms-consolidated-scrips-status

A utility that parse Zerodha Consolidated google spreadsheets and render category-wise scrip details(margins, multiplier, etc). 

# Installation

``` 
pip install consolidatedrms
```

# Usage and documentation

```
from consolidatedrms import ConsolidatedList

#Fetch allowed/banned mis scrips dict with multiplier detail for mis-allowed scrip

ConsolidatedList.mis_status()
```

```
{'status': 'success', 'data': {'mis_allowed': [{'symbol': '3MINDIA', 'multiplier': '5'}, 
{'symbol': 'AARTIIND', 'multiplier': '5'},{...}],
'mis_banned': [{'symbol': '21STCENMGM'}, {'symbol': '3IINFOTECH'},{..}]}}
```

```
#Fetch Var+ ELM,MIS Margin,MIS Multiplier,CO Lower Trigger,
#CO Upper Trigger values for allowed BO/CO allowed scrip

ConsolidatedList.mis_margin()
```

```
{'status': 'success', 'data': [{'symbol': '3MINDIA', 'var+elm': 40.0, 'mis_margin': 20.0, 
'multiplier': 5.0, 'co_lower': 10.0, 'co_upper': 10},..
{...}]}
```

```
#Fetch list of scrips allowed/non-allowed/temp banned for BO and CO

ConsolidatedList.mis_boco()
```

```
{'status': 'success', 'data': {'boco_allowed': [{'symbol': '3MINDIA'}, 
{'symbol': 'AARTIIND'}, {'symbol': 'ABB'},{...}]}}
```

```
#Fetch list of scrips under Trade to Trade segment

ConsolidatedList.trade2trade()
```

```
{'status': 'success', 'data': [{'symbol': 'BAFNAPH'}, {'symbol': 'CASTEXTECH'}, 
{'symbol': 'JIKIND'}, {'symbol': 'JYOTISTRUC'},..,
{...}]}
```

```
#Fetch list of scrips under ASM (Additional Surveillance Measure)

ConsolidatedList.asm_status()
```

```
{'status': 'success', 'data': [{'symbol': '3IINFOTECH'}, {'symbol': 'AARTIDRUGS'}, 
{'symbol': 'ABAN'},,..{..}]}
```

```
#Fetch list of scrips under GSM (Graded Surveillance Measure)

ConsolidatedList.gsm_status()
```

```
{'status': 'success', 'data': [{'symbol': 'ADROITINFO'}, {'symbol': 'ALPSINDUS'}, 
{'symbol': 'ANKITMETAL'},..,{..}]}
```
