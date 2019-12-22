# -*- coding: utf-8 -*-
import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.keys import Keys
from scrapy.selector import Selector

class DuckSpider(scrapy.Spider):
    name = 'duck'
    allowed_domains = ['duckduckgo.com']

    def start_requests(self):
        yield SeleniumRequest(
            url = 'http://duckduckgo.com',
            wait_time= 3,
            screenshot=True,
            callback=self.parse
        )

    def parse(self, response):
    #    img = response.meta['screenshot']
       
    #    with open('screenshot.png','wb') as f:
    #         f.write(img)
        driver = response.meta['driver']
        search_input = driver.find_element_by_xpath('//input[@id="search_form_input_homepage"]')
        search_input.send_keys('Hello World')
        search_input.send_keys(Keys.ENTER)

        html = driver.page_source
        response_obj = Selector(text=html)
        # driver.save_screenshot('enter.png')
        links = response_obj.xpath('//div[@class="result__extras__url"]/a')
        for each in links:
            yield {
                'url':each.xpath('.//@href').get()
            }