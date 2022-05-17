# Test Cases
___

| Test Name  | Description  | Tested component| Input  | Expected Result  | Test Result  |
|---|---|---|---|---|---|
| test01  | Validate the conversion of a simple digit decimal number |intToRoman | 1  |  I | ok  |
| test02  |  Validates the conversion of a double digit decimal number|intToRoman | 53  | LIII  |  ok |
| test03  | Validates the conversion of a double digit decimal number| intToRoman | 81  | LXXXI | ok  |
| test04  | Validates the conversion of a triple digit decimal number| intToRoman | 746  |  DCCXLVI| ok  |
| test05  |  Validates the conversion of a triple digit decimal number|intToRoman |  239 | CCXXXIX |  ok |
| test06  |  Validates the conversion of a 4-digit decimal number| intToRoman| 3496  | MMMCDXCVI |  ok |
| test07  |  Validates the conversion of a 4-digit decimal number|intToRoman | 1519  | 	MDXIX  |  ok |
| test08  | Validates the input having an special character|validation  | -96  |  False |  ok |
| test09  |  Validates the input having a letter|validation | 1f5  | False  |  ok |
| test10  | Validates the input having numbers| validation | 136  | True  |  ok |
|test11|Validates the conversion of the number isn't bigger than 3999 | validation|6794 | False| ok|
|test12|Validates the conversion of the number isn't smaller than 1 | validation|0 |False |ok |