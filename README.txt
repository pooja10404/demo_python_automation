Preinstallation : 
python, pytest, jproperties, pytest-html, selenium

To run the test : 
pytest --html=output\report.html
It will generate the html report in the output folder.

framework details:

Language :  Python
framework : pytest
Methodology : PageObject
Report : Python html base report

Folder structure:
1) input
		This folder contains only one file ( I kept all inputs in one location for demo purpose), more files can be add in the future, or this file can be categories further.
		This is basically contains URL, address input, delivery store input , item name, item description
2) output
		Result file will be added here.
3) resources
		Currently, it is used for windows chrome driver, we can add more whenever required.
4) src
		This folder contains all code, and devided further in following categories :
		a) common:
			This package contains common files used throughout the suites. it contains 2 files:
				a.1) base_test.py : This file contains setup before and after tests.
				a.2) webdriver_utility.py : This file contains wrapper over the selenium webdriver's APIs
				
		b) page_object
			This package contains page wise element and operations on elements. It contains 3 files:
				b.1) menu_page.py : this is for catelog page related operations
				b.2) order_page.py : this is for order page related operations.
				b.3) product_details_page.py : this is for product details page related operations
				
		c) tests:
			This package contains suite files which are having testcases written inside. It contains 1 file:
				c.1) test_order_operations.py : This contains only one test right now.
				
Improvement Areas: 
1) result file can improve , I used basic pytest-html results and right now that is generated through command.
2) Input files can be devided as per categories and add more input files.
3) Can add more wrapping functions in the webdriver_utility.py, I added which are required for current testcase.
4) Enhance base_test.py for more enrichment of the before and after for setup and clearing the objects by using fixtures.
 				
