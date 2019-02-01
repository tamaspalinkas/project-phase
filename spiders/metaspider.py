# -*- coding: utf-8 -*-

import scrapy

from metacrit.items import MetacritItem

class MetaSpider(scrapy.Spider):
    name = 'metaspider'
    allowed_domains = ['www.metacritic.com']
    start_urls = ['https://www.metacritic.com/browse/movies/score/metascore/all/filtered?page=0']
    
    
    
    def parse(self, response):
        item = MetacritItem()
        titles = response.css('h3::text').getall()
        scores = response.xpath('//div[contains(@class, "clamp-metascore")]/a[contains(@class, "metascore_anchor")]/div[contains(@class, "metascore_w")]/text()').extract()
        user_scores = response.xpath('//div[contains(@class, "clamp-userscore")]/a[contains(@class, "metascore_anchor")]/div[contains(@class, "metascore_w")]/text()').extract()
        zipped = zip(titles, scores, user_scores)

        for title, score, user_score in zipped:
            yield {'title' : title,
                   'metascore' : score,
                   'userscore' : user_score}

        next_page_url = response.xpath('//span[contains(@class, "next")]//a/@href').extract_first()
        if next_page_url:
            absolute_next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(absolute_next_page_url)