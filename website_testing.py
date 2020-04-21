from selenium import webdriver
from testcase_info import name, email, subject, message
from time import sleep

class TestingTool():
    def __init__(self):
        # new Chrome session
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()

        # navigate to Home page
        self.driver.get("https://www.englishforlifeacademy.com/")
        self.driver.title

        # # navigate to Events page
        # sleep(5)
        events_tab = self.driver.find_element_by_xpath('//*[@id="comp-k6jvfbem2linkElement"]')
        # self.driver.execute_script("arguments[0].click();", events_tab)

        # # navigate to Blog page
        # sleep(5)
        blog_tab = self.driver.find_element_by_xpath('//*[@id="comp-k6jvfbem3linkElement"]')
        # self.driver.execute_script("arguments[0].click();", blog_tab)

        # # navigate to Faculty page
        # sleep(5)
        faculty_tab = self.driver.find_element_by_xpath('//*[@id="comp-k6jvfbem4linkElement"]')
        # self.driver.execute_script("arguments[0].click();", blog_tab)

        # # navigate to About Us page
        # sleep(5)
        aboutpage_tab = self.driver.find_element_by_xpath('//*[@id="comp-k6jvfbem1linkElement"]')
        # self.driver.execute_script("arguments[0].click();", aboutpage_tab)

        # iterate through the tabs
        tabs = [events_tab, blog_tab, faculty_tab, aboutpage_tab]

        for elem in tabs:
            sleep(5)
            self.driver.execute_script("arguments[0].click();", elem)


    def input_info(self):
        sleep(10)
        # fill in necessary information for the contact form
        # name_input = self.driver.find_element_by_id('comp-k6v5579cinput')
        name_input = self.driver.find_element_by_xpath('//*[@id="comp-k6v5579cinput"]')
        ## self.driver.execute_script("document.getElementById('comp-k6v5579cinput').value='{}';".format(name))
        name_input.send_keys(name)
        
        ## email_input = "document.getElementById('comp-k6v564ldinput').value='{}';"
        ## self.driver.execute_script(email_input.format(email))
        email_input = self.driver.find_element_by_xpath('//*[@id="comp-k6v564ldinput"]')
        email_input.send_keys(email)


        ## subject_input = "document.getElementById('comp-k6v56su2input').value='{}';"
        ## self.driver.execute_script(subject_input.format(subject))
        subject_input = self.driver.find_element_by_xpath('//*[@id="comp-k6v56su2input"]')
        subject_input.send_keys(subject)
    
        ## text_input = "document.getElementById('comp-k6v57sletextarea').value='{}';"
        ## self.driver.execute_script(text_input.format(message))
        text_input = self.driver.find_element_by_xpath('//*[@id="comp-k6v57sletextarea"]')
        text_input.send_keys(message)

    def submit_info(self):
        sleep(20)
        submit_button = self.driver.find_element_by_id('comp-k6v5hpb7link')
        ## self.driver.execute_script("arguments[0].click();", submit_button)
        submit_button.click()
        sleep(10)
        self.driver.quit()


if __name__ == "__main__":
    # create instance of TestingTool()
    t1 = TestingTool()
    t1.input_info()
    t1.submit_info()
    
    
