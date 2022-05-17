## Decimal Numbers to Roman Numbers Converter
___

### Requirements

#### Functional

1. Accepts an integer from 1 to 3999 and converts it to roman numbers
2. Allows as many conversions as the user wants
3. Checks the entered input 

#### Non Functional

+ It needs to be fast, doesn't matter how many times its repeated
+ Needs to show the result clearly
+ Can grow in terms of the range of numbers available to conversion
+ Needs to operate in different environments

### Acceptance Criteria

**As a user, i want to convert a number from 1 to 3999, to know it's correspondent roman number.**

- *Scenario*: Convert decimal number to roman number
- *Given*: The user have supplied a valid input
- *When*: The user send a value by pressing enter
- *Then*: The system will return the corresponding roman number

**As a user, I want to be warned for any mistakes in the input, to correct that error**

- *Scenario*: Entering input
- *Given*: The user opens the applicartion
- *When*: The user enters an invalid input
- *Then*: The system will show a message about the mistake and will allow anothe try to enter a correct value.

**As a user, I want to use the application as many times as I need, to eliminate the need of reopening the application if several convertions are needed**

* *Scenario*: Staying in the application
* *Given*: The system supplied the roman number and asks if the user wants to leave the program
* *When*: The user enter a yes or no answer in the (y/n) format
* *Then*: The system will allow or deny another conversion depending on the users answer
	
### Test Scenario

The test scenarios that will be performed are: 

| Name  | Description  | Importance  |Category|
|---|---|---|---|
| TC_01  | Validates the program doesn't allow special characters  | High  |  Unit Test |
| TC_02  | Validates the program doesn't allow letters  | High  |  Unit Test |
| TC_03  | Validates the program doesn't allow numbers outside 1-3999  | High  | Unit Test |
| TC_04  | Validates the program converts the equivalent roman number to the specified decimal number  | High  |Unit Test |
| TC_04  | Validates the program repeats while the user supplies 'y'  | High  | End-to-End Test |
| TC_05  | Validates the program doesn't act upon a non 'y' or 'n' answer  | Medium  | End-to-End Test |
| TC_06  | Validates the program ends when the user supplies 'n'  | High  | End-to-End Test |








