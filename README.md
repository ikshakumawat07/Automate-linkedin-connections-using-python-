# Automate-linkedin-connections-using-python-
# LinkedIn Connection Automation Bot

## Overview

This project is a Python automation tool that sends LinkedIn connection requests automatically using Selenium.

The bot:

* Searches LinkedIn profiles
* Sends connection requests automatically
* Clicks "Send without note"
* Allows the user to choose how many requests to send
* Randomizes delays to mimic human behavior

## Technologies Used

* Python
* Selenium
* Chrome WebDriver

## Features

* Automatic LinkedIn search
* Auto connection requests
* Random profile selection
* Progress updates in terminal

## Usage

1. Start Chrome in debugging mode:

```
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\chrome-profile"
```

2. Login to LinkedIn manually.

3. Run the script:

```
python bot.py
```

4. Enter the number of connection requests to send.

## Disclaimer

This project is for educational purposes only. Excessive automation may violate LinkedIn’s terms of service.
