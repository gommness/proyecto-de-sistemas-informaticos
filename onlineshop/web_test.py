#Para runnear esto hay que ejecutar en postgres
#python database_cleaner.py 
#python manage.py migrate
#python create_super_user.py 

# -*- coding: utf-8 -*-
# 
#NOTE, if selenium is not installed execute pip install --user selenium
#NOTE, if loremipsum is not installed execute pip install --user loremipsum 
#NOTE: chromedriver is available at moodle. For labs use version 2.22
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, os
from collections import OrderedDict
from loremipsum import get_paragraphs, get_sentences
from onlineshop.settings import MEDIA_DIR, BASE_DIR

class onLineShopTester(unittest.TestCase):
    """
    Inserta categorias y productos en el proyecto desplegado en heroku
    Author: Carlos Li
    """
    username    = "alumnodb"
    passwd      = "alumnodb"
    base_url    = "https://immense-woodland-61230.herokuapp.com/"
    #base_url     = "http://127.0.0.1:8000/"
    admin_url    = base_url + "admin/"
    addCategoryPath = "shop/category/add/"
    addProductPath  = "shop/product/add/"
    

    catList     = ["Eau de Cologne", "Eau de Parfum","Eau de Toilette"]
    
    #los jpg esperados deben llamarse como los names
    productDict = {
                catList[0]: ["Phantom Blood",
                    "Vento Aureo"],
                catList[1]: ["Onett",
                    "Twoson"],
                 catList[2]: ["Symetra",
                 "Ana"],
                }
    
    chromeDriver = os.path.join(BASE_DIR, "chromedriver")
    imagesPath = os.path.join(os.path.join(MEDIA_DIR,"images"),"products")

    def setUp(self):
#        self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome(self.chromeDriver)
##DO NOT CHANGE ANYTHING BELLOW THIS POINT
    def find_element_by_id(self,_id,value,waitFor=1):
        self.driver.find_element_by_id(_id).clear()
        self.driver.find_element_by_id(_id).send_keys(value)
        time.sleep(waitFor)

    def find_element_by_xpath(self,_xpath,waitFor=1):
        self.driver.find_element_by_xpath(_xpath).click()
        time.sleep(waitFor)

    def find_element_by_name(self,_name,waitFor=1):
        self.driver.find_element_by_name(_name).click()
        time.sleep(waitFor)

    def login(self,userName, passwd):
        self.driver.get(self.admin_url + "")
        self.find_element_by_id("id_username",userName)
        self.find_element_by_id("id_password",passwd)
        self.find_element_by_xpath('//*[@id="login-form"]/div[3]/input')

    def addCat(self,catName, waitFor=1):
        self.driver.get(self.admin_url + self.addCategoryPath)
        self.find_element_by_id("id_catName",catName, waitFor)
        self.find_element_by_name("_save", waitFor)

    def addProduct(self, cat, prodName, ext="jpg", price="1.1", stock="1", waitFor=1):
        self.driver.get(self.admin_url + self.addProductPath)

        select = Select(self.driver.find_element_by_id('id_category'))
        select.select_by_visible_text(cat)

        self.find_element_by_id("id_prodName",prodName, waitFor)
        imagePath =  os.path.join(self.imagesPath,cat.lower(),prodName+"."+ext)
        #self.driver.find_element_by_id("id_image").send_keys(imagePath)######
        self.find_element_by_id("id_image",imagePath)
        self.find_element_by_id("id_description",get_paragraphs(1)[0], waitFor)
        self.find_element_by_id("id_price",price, waitFor)
        self.find_element_by_id("id_stock",stock, waitFor)
        self.find_element_by_name("_save", waitFor)

    def seeHome(self, waitFor=1):
        self.driver.get(self.base_url)
        time.sleep(waitFor)

    def quit(self, waitFor=1):
        time.sleep(waitFor)
        self.driver.quit()

    def test_shop(self):
        #connect to Home
        self.seeHome(2)

        #login in
        self.login(self.username, self.passwd)

        #addCategories
        for catName in self.catList:
            self.addCat(catName,1)

        #addProducts
        counter =1
        for catName in self.catList:
            for prodName in self.productDict[catName]:
                self.addProduct(catName,prodName,
                                price = str(counter * 1.1),
                                stock = str(counter), waitFor = 0)
                counter += 1

        #connect to Home
        self.seeHome(1)

        #close browser
        self.quit(20)

if __name__ == "__main__":
    unittest.main()

