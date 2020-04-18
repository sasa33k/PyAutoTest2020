# Welcome to my new PyAutoTest 2020!  :)

This project aims to allow normal users to manage their own auto test cases with Excel only.

### Key Features:
* Excel Auto Testing Template
    * **Define which test to run**: users can manage all test cases in one file but select to run cases as neeed.
    * **Repeat by tests & cases with dynamic variables**: some times you just need to repeat the whole case with different paramenters e.g. going to yahoo.com and repeat to search different keywords. Manage it with data sheet tab!
        * For example:
            * Case 1 have Step 1,2,3
            * Case 2 have Step 4,5
            * Test 1 includes both Case 1 and Case 2
        * Repeat Case 1 for 2 times will run: [1,2,3],[1,2,3]
        * Repeat Test 1 for 2 times will run: [1,2,3,4,5],[1,2,3,4,5]
        * Repeating Test 1 for 2 times, with Case 1 itself runing 2 times?
            * Just like that! [ ([1,2,3],[1,2,3]) , (4,5) ] , [ ([1,2,3],[1,2,3]) , (4,5) ]
* Web Test with Selenium - quick and high accuracy (currently support Chrome only =P , default version 81 included)
* GUI Test by image or position (to handle non-web test~ of course..) ** special handling done for mac retina display
* And some bugs~ XD (forgive me i am not really a developer... haha)
* Check out more in PyAutoTest\tests\AutoTestTemplate.xlsx

### Test folder structure 
(Tested for Windows executable, similar structure can be found in PyAutoTest/tests):
<pre>
[AutoTesting]
   |_ [img]
        |_ mail.png
   |_ [resources]
        |_ [win] or [mac]
            |_ e.g. Chromedriver
   |_ (AutoTestTemplate).xlsx --> sample can be found in PyAutoTest/tests
   |_ PyAutoTest.exe
   
   
   |_ [Results] > Auto generated on first run
</pre>


####Steps to setup the project (in PyCharm) 
1. Add interpreter (pyCharm most bottom right) --> create venv
2. Go to requirements.txt ==> click install (pip install -r requirements.txt)
3. Check Config.ini and update if required
4. Update PyAutoTest/resources for Chrome driver
    * For mac: find PyAutoTest/resources/mac/chromedriver in finder, right click Open (get open permission)
    * Allow PyCharm to controm Accessibility & Screenrecording? in system preference
5. Run PyAutoTest\\\_\_main\_\_.py

### Step to build executable
(tested on windows os), one file executable
<pre>
pyinstaller PyTest.spec PyAutoTest\__main__.py
</pre>