import os
from time import localtime, strftime, sleep

import slackweb
from selenium import webdriver
from selenium.webdriver.common.by import By

slack = slackweb.Slack(url=os.getenv('SLACK_WEBHOOK_URL'))

options = webdriver.ChromeOptions()
options.add_argument('--Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3864.0 Safari/537.36')
driver = webdriver.Remote(
    command_executor='http://selenium:4444/wd/hub',
    desired_capabilities=options.to_capabilities(),
    options=options,
)

search_url = ''


def main():
    driver.get(search_url)
    elements = driver.find_elements(By.XPATH, '//div[@class="example"]')
    for element in elements:
        pass


while True:
    main()
    slack.notify(text='slack notifiy')
    print('{} DEBUG: tracked'.format(strftime("%Y-%m-%d %H:%M:%S", localtime())))
    sleep(60)


if __name__ == "__main__":
    main()
