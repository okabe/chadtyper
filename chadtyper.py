#!/usr/bin/env python2

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from pyvirtualdisplay import Display
from BeautifulSoup import BeautifulSoup as Soup
from random import choice
from time import sleep

def get_words( source ):
    soup = Soup( source )
    words = []
    for div in soup.findAll( "div", { "id" : "row1" } ):
        for span in div.findAll( "span" ):
            words.append( span.text )
    print "[>] Gathered words: {}".format( ", ".join( words ) )
    return words

if __name__ == "__main__":
    display = Display( visible=1, size=( 800, 800 ) )
    display.start()
    chrome_options = Options()
    chrome_options.add_argument( "--no-sandbox" )
    chrome_path = "/usr/bin/chromedriver"
    browser = webdriver.Chrome( chrome_path, chrome_options=chrome_options )
    
    browser.get( "https://10fastfingers.com/account/facebook_login" )
    email = browser.find_element_by_xpath( '//*[@id="email"]' )
    email.send_keys( "" )
    password = browser.find_element_by_xpath( '//*[@id="pass"]' )
    password.send_keys( "" )
    password.send_keys( u'\ue007' )
    sleep( 2 )
    words = get_words( browser.page_source )
    type_form = browser.find_element_by_xpath( '//*[@id="inputfield"]' )
    for word in words: 
        print "[>] Chad typed: {}".format( word )
        type_form.send_keys( word )
        type_form.send_keys( u"\ue00D" )
