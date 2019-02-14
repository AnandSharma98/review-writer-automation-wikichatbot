
"""review writer function that'd provide you a automated  task of writing review about places on google .
  by the help of selenium chrome driver"""


def review_writer():
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as ec

    user_input = input('do you want to go with your "own id" or wanna go with a "random one" \n'
                       'type: own or random: ').lstrip()

    """for random handle yourself"""

    REVIEW_INPUTS = ("AWESOME", "FANTASTIC", "GREAT PLACE", "supER", "FABULOUS", "RAPCHIK",)
    import random
    review_to_be_posted=random.choice(REVIEW_INPUTS)

    if user_input == "own":
        user_name = input("type your gmail id: ").lstrip()
        password = input("type your password: ").lstrip()
        prod_detail = input("type your prod_detail: ").lstrip()
        from selenium import webdriver

        browser = webdriver.Chrome('C:/Users\ANAND SHARMA\PycharmProjects\chromedriver.exe')

        browser.get('https://www.google.com/')
        browser.maximize_window()

        import pyautogui
        """its a module to click automatically anywhere in screen"""
        pyautogui.click((1290, 147))
        browser.find_element_by_css_selector('#identifierId').send_keys(user_name)
        pyautogui.click((832, 583))

        passwordField = WebDriverWait(browser, 10).until(
            ec.visibility_of_element_located((By.XPATH, "//input[@name='password']")))
        passwordField.clear()
        passwordField.send_keys(password)
        browser.find_element_by_xpath("//*[@id='passwordNext']/content/span").click()
        search_feild = WebDriverWait(browser, 10).until(
            ec.visibility_of_element_located((By.XPATH, "//input[@name='q']")))
        search_feild.clear()
        search_feild.send_keys(prod_detail)
        search_btn = WebDriverWait(browser, 10).until(
            ec.visibility_of_element_located((By.XPATH, "//input[@name='btnK']")))
        search_btn.click()
        review_button = WebDriverWait(browser, 10).until(
            ec.visibility_of_element_located((By.CLASS_NAME, "wrsf")))
        review_button.click()
        browser.implicitly_wait(10)

        browser.switch_to.frame(browser.find_element_by_class_name('goog-reviews-write-widget'))

        """now it is selecting one star only (you can customize accordingly ,it'll require few more loc)"""

        review_star_five = WebDriverWait(browser, 10).until(
            ec.visibility_of_element_located(
                (By.XPATH, "/html/body/div/div/jsl/div/div[1]/div[4]/div[2]/div[2]/div/span/span[5]")))
        review_star_five.click()
        review_text = WebDriverWait(browser, 10).until(
            ec.visibility_of_element_located((By.CLASS_NAME, "review-text")))
        review_text.clear()
        review_text.send_keys(review_to_be_posted)
        """adding post option"""
        review_post = WebDriverWait(browser, 10).until(
            ec.visibility_of_element_located((By.CLASS_NAME, "quantum-button-inner-box")))
        review_post.click()
        review_post_alert = WebDriverWait(browser, 10).until(
            ec.visibility_of_element_located((By.CLASS_NAME, "quantum-button-inner-box")))
        review_post_alert.click()
        review_post2 = WebDriverWait(browser, 10).until(
            ec.visibility_of_element_located((By.XPATH, "/html/body/div/div/jsl/div/div[2]/div[3]/div[2]/div[2]/div/div/div")))
        review_post2.click()
        '''i have not quit the browser so that you can see what is happening
         NOTE::class name , css selectors may vary or are updated time to time
          so you can check every element before proceeding .'''



