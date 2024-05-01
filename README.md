## Setup (Python 3.10+)

1. Configure a virtual environment for PyCharm: 
   1. File>Settings>Project Interpreter>Settings icon> Add Local 
2. Change Test Runner for PyCharm: 
   1. File>Settings>Tools>Python Integrated Tools>Default test runner>PyTest
3. Execute in terminal: 
   1. pip install -r requirements.txt
4. Change your local settings in config.json'

### Install and Configure Appium Server + Appium Inspector

1. Install and run Appium Server (https://appium.io/downloads.html)
2. Install and run Appium Inspector (https://github.com/appium/appium-inspector/releases)\
3. Add environment variables:
   1. ANDROID_HOME (C:\Users\Admin\AppData\Local\Android\Sdk)
   2. JAVA_HOME (C:\Program Files\Java\jdk1.8.0_321)
   3. Path (C:\Users\Admin\AppData\Local\Android\Sdk\platform-tools)
4. Change Remote Path in appium inspector to: /wd/hub/

### Run all tests

```
pytest
```

### Run tests matching given mark expression

```
pytest --junitxml "reports/junit-report.xml" -k TestAnalyticsProsumer
```


### Publish test results
```
trcli -n -c "config.yml" parse_junit --case-matcher=property

```


### Run an Allure report generation
1. Download and extract Allure into the Program Files (https://github.com/allure-framework/allure2/releases/)
2. Add Path in the system variables to the allure bin folder:
   1. Path (C:\Program Files\allure\bin)


```
pytest --alluredir=allure-results
allure serve tests/allure-results
```

