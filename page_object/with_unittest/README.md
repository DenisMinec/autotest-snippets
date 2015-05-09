# Template for auto tests in python 3 with selenium

## Requirements

* [Python 3][1] 
* Selenium: `pip3 install selenium`
* Alternative: [Browser drivers][2]

## Usage


### Files
  
* `runner.py` - main file, you can start test under python 3 as `python3 runner.py`
* `tests.py` - main file for test, add your test here
* `config.py` - configuration file, with `runner.py` you can control tests execution
* `base_test_case.py` - something like wrapper around `unittest.TestCase`
* `base_page.py` - base page functionality 

[1]: https://www.python.org/downloads/
[2]: http://docs.seleniumhq.org/download/prew