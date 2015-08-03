# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class first_autotest(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_first_autotest(self):
        success = True
        wd = self.wd
        wd.get("http://localhost/addressbook/group.php")
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_id("LoginForm").click()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()
        if not wd.find_element_by_name("selected[]").is_selected():
            wd.find_element_by_name("selected[]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/span[2]/input").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/span[2]/input").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/span[3]/input").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/span[3]/input").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/span[4]/input").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/span[4]/input").click()
        wd.find_element_by_xpath("//div[@id='content']/form/input[5]").click()
        wd.find_element_by_link_text("group page").click()
        if not wd.find_element_by_name("selected[]").is_selected():
            wd.find_element_by_name("selected[]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/span[2]/input").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/span[2]/input").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/span[3]/input").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/span[3]/input").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/span[4]/input").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/span[4]/input").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/span[5]/input").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/span[5]/input").click()
        wd.find_element_by_xpath("//div[@id='content']/form/input[5]").click()
        wd.find_element_by_link_text("group page").click()
        if not wd.find_element_by_name("selected[]").is_selected():
            wd.find_element_by_name("selected[]").click()
        wd.find_element_by_css_selector("#content > form").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/span[3]/input").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/span[3]/input").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/span[2]/input").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/span[2]/input").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/span[4]/input").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/span[4]/input").click()
        wd.find_element_by_xpath("//div[@id='content']/form/input[5]").click()
        wd.find_element_by_link_text("group page").click()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("23f23f")
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("23f23f23f")
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("23f23f23f")
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("group page").click()
        wd.find_element_by_link_text("Logout").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
