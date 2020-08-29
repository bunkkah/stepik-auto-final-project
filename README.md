### stepik-auto-final-project

This repository contains the final project of the autotests course at Stepik:
https://stepik.org/course/575

#### Disclaimer

Please make sure that you have the latest version of chromedriver to run tests in your latest Chrome. 
It can be downloaded here: https://chromedriver.chromium.org/

I used Python 3.8.1 on Windows 10x64.

In "requirements.txt" file, besides pytest and selenium packages, there are some others which got there automatically after "pip freeze > requirements.txt".

#### Prerequisites

Before running the tests, please make sure that you:
- have created and activated new virtual environment, 
- are in 'stepik-auto-final-project' folder,
- installed all the necessary packages 
    ```
    pip install -r requirements.txt
    ```

If something goes wrong while running the tests, please consider this (Rostislav, thanks!):
https://stepik.org/lesson/201964/step/15?discussion=1413148&unit=176022

#### Running tests

To run tests for a review:
```
 pytest -v --tb=line --language=en -m need_review
```

Thanks! :cat:
