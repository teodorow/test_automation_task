from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class ElementNotFound(Exception):
    pass


def ten_clouds_task():
    web_driver = webdriver.Chrome(r'C:\chromedriver.exe')
    try:
        web_driver.get('http://google.com')
        search_bar = web_driver.find_elements_by_xpath('//*[@id="tsf"]/div[2]/div/div[1]/div/div[1]/input')
        search_bar[0].send_keys('10clouds')
        search_bar[0].send_keys(Keys.ENTER)
        matched_elements = web_driver.find_elements_by_xpath('//a[starts-with(@href, "https://10clouds")]')
        if matched_elements:
            matched_elements[0].click()
        else:
            raise ElementNotFound
        all_case_studies_button = web_driver.find_element_by_xpath("/html/body/section[2]/div/div[2]/a")
        web_driver.execute_script("arguments[0].click();", all_case_studies_button)
        glucose_mama = web_driver.find_elements_by_xpath("/html/body/section[2]/div/div/div[5]")
        if glucose_mama:
            actions = ActionChains(web_driver)
            actions.move_to_element(glucose_mama[0]).perform()
        else:
            raise ElementNotFound
        web_driver.save_screenshot("screenshot.png")
    finally:
        web_driver.close()


if __name__ == '__main__':
    ten_clouds_task()
