__author__ = 'chekluev.d'
from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def create(self, contact):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # fill company
        #wd.find_element_by_name("company").click()
        #wd.find_element_by_name("company").clear()
        #wd.find_element_by_name("company").send_keys(contact.company)
        # fill address
        #wd.find_element_by_name("address").click()
        #wd.find_element_by_name("address").clear()
        #wd.find_element_by_name("address").send_keys(contact.address)
        #wd.find_element_by_name("theform").click()
        # fill phone
        #wd.find_element_by_name("home").click()
        #wd.find_element_by_name("home").clear()
        #wd.find_element_by_name("home").send_keys(contact.homephone)
        #wd.find_element_by_name("mobile").click()
        #wd.find_element_by_name("mobile").clear()
        #wd.find_element_by_name("mobile").send_keys(contact.mobilephone)
        # fill email
        #wd.find_element_by_name("email").click()
        #wd.find_element_by_name("email").clear()
        #wd.find_element_by_name("email").send_keys(contact.email)
        # fill date of birth
#        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[15]").is_selected():
#            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[15]").click()
#        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[7]").is_selected():
#            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[7]").click()
        #wd.find_element_by_name("byear").click()
        #wd.find_element_by_name("byear").clear()
        #wd.find_element_by_name("byear").send_keys("1980")
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("email", contact.email)
#        wd.find_element_by_name("middlename").click()
#        wd.find_element_by_name("middlename").clear()
#        wd.find_element_by_name("middlename").send_keys(contact.middlename)
#        wd.find_element_by_name("lastname").click()
#        wd.find_element_by_name("lastname").clear()
#        wd.find_element_by_name("lastname").send_keys(contact.lastname)
#        wd.find_element_by_name("title").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        #submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def delete_contact(self):
        self.delete_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_xpath("//*[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        self.return_to_home_page()
        self.contact_cache = None

#    def edit_contact(self, contact):
#        wd = self.app.wd
#        self.open_home_page()
#        #select contact
#        wd.find_element_by_name("selected[]").click()
#        #edit contact
#        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[5]/td[8]/a/img").click()
#        wd.find_element_by_name("firstname").click()
#        wd.find_element_by_name("firstname").clear()
#        wd.find_element_by_name("firstname").send_keys(contact.firstname)
#        wd.find_element_by_name("middlename").click()
#        wd.find_element_by_name("middlename").clear()
#        wd.find_element_by_name("middlename").send_keys(contact.middlename)
#        wd.find_element_by_name("lastname").click()
#        wd.find_element_by_name("lastname").clear()
#        wd.find_element_by_name("lastname").send_keys(contact.middlename)
#        wd.find_element_by_name("company").click()
#        wd.find_element_by_name("company").clear()
#        wd.find_element_by_name("company").send_keys(contact.company)
#        wd.find_element_by_name("address").click()
#        wd.find_element_by_name("address").clear()
#        wd.find_element_by_name("address").send_keys(contact.address)
#        wd.find_element_by_name("home").click()
#        wd.find_element_by_name("home").clear()
#        wd.find_element_by_name("home").send_keys(contact.homephone)
#        wd.find_element_by_name("mobile").click()
#        wd.find_element_by_name("mobile").clear()
#        wd.find_element_by_name("mobile").send_keys(contact.mobilephone)
#        wd.find_element_by_name("email").click()
#        wd.find_element_by_name("email").clear()
#        wd.find_element_by_name("email").send_keys(contact.email)
#        wd.find_element_by_name("byear").click()
#        wd.find_element_by_name("byear").clear()
#        wd.find_element_by_name("byear").send_keys("1985")
#        #submit update and return home page
#        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
#        self.return_to_home_page()


    def open_home_page(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/")

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            #wd.find_elements_by_xpath("//div[1]/div[4]/form[2]/table/tbody/tr[@name='entry']")
            #wd.find_elements_by_name("entry")
            self.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_xpath("//div[1]/div[4]/form[2]/table/tbody/tr[@name='entry']"):
                #�� �������� �������� tr �� �����
                text = element.find_elements_by_tag_name("td")
                lastname = text[1].text
                firstname = text[2].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(lastname=lastname, firstname=firstname, id=id))
            return list(self.contact_cache)
