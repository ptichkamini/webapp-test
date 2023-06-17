# webapp-test
Web app test automation project using python, selenium and unit test 

1.	INTRODUCTION 

The purpose of this project is to verify functionalities of a web application created to track basic tasks throughout the day.

2.	SCOPE

Validate functionalities of checklist web application.

Areas (tabs):
-	All
-	Active
-	Completed

Functionalities to test:

-	Input 
-	Remove
-	Counter 
-	Select / Deselect all
-	Saved list after refreshing the page 

3.	TEST CASES

Pre-condition: todolist.james.am is open in web browser 

3.1	Enter items
3.2	Remove 
3.3	Edit
3.4	Select all
3.	Counter
3.6     Refresh

4.	EXPLORATORY TESTING

Due to the non-complexity of the web application, an hour was devoted to exploratory testing. 

The following bugs were found during this session:

-	 ‘todo’ should be written with hyphen
-	there are spaces in the input field after adding an item 
-	typo in the input bar "What need's to be done?"
-	inappropriate comment in the console and errors

After completing the exploratory testing, the following improvement proposals 
emerged:

-	‘active’ should be written with capital ‘A’ for consistency
-	transferring words with a hyphen instead of cutting them off in bigger items 
-	separate count functionality for every tab to see progress 
-	possibility to drag and drop items to change their order
-	while editing large items their size should stay to make editing easier

5.	FINDINGS 

After conducting all the test cases no critical bugs were found.  In total, 8 bugs were reported including 6 minor bugs and 2 bugs of medium severity. Apart from that 5 improvements were proposed. 

