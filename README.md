# pybot n00b
<img src="https://github.com/shafin071/pybot.n00b/blob/master/assets/pybot2.gif" width="300" height="260">

## Situation
This project is based on my dummy eLearning web app [Hello World](https://shafin-elearning.herokuapp.com/) project. The website needed testing to ensure it's functioning as expected

## Task
Wrote a script that performs automated testing on my website and emails me the test results

## Action:
* Put all the pre-defined xpaths / selectors of my web app and user single actions in `utils.py`
* Here are some examples of single action:
  * attempt login
  - attempt signup
  - go to course page
  - add course to cart
  - enter billing info
  - go to profile
  - delete account

* In `selenium_script.py`, created unit test class containing 4 unit tests:
  1. Register user
  2. Attempt to buy course without payment
  3. Login and delete account
  4. Confirm account deletion by trying to log in again

* Also in `selenium_script.py`:
  - overrode unittest.TestCase's teardown method to retrieve test results
  - converted the test results into strings 
  - wrote a method `send_email` that nicely formats the test results into an email body and emails it to me
  - The method was included in my `tearDownClass` method so it can be triggered after the tests are done

## Result:
Watch Demo:

[<img src="https://github.com/shafin071/pybot.n00b/blob/master/assets/vid_snapshot.JPG" width="300" height="260">](https://www.youtube.com/watch?v=aqrQ4hAe17Q&feature=youtu.be)

## Resources used for this project:
* python v3
* unittest
* selenium
* chromedriver
* smtplib
