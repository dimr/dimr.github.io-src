title: Scraping for houses-part 1
category: post
date:   2016-04-07 04:47:56
tags: python,scrapy,tutorial
slug:scraping-for-houses
status:published

This is the first part of a tutorial series i am planning to write about the process of
acquiring data,cleaning data,analyzing data and visualizing. In this first part, i will show you how to
scrape data from a popular greek real estate house prices


We are going to use [scrapy](http://scrapy.org/), a famous python library for screen scraping that uses [xpath](https://en.wikipedia.org/wiki/XPath), a powerful query language for selecting nodes in xml documents

>XPath uses path expressions to select nodes or node-sets in an XML document. The node is selected by following a path or steps.

i am going to assume that you have a basic knowledge of python and you can install additional libraries
###Install scrapy
    :::python
    pip install scrapy

cleating the screen

    :::python

    In [15]: response.xpath('//*[@id="searchDetailsListings"]/div[1]/div/div/div[1]/div/h4/a/@href').extract()
    Out[15]: [u'http://www.homegreekhome.com/en/rent_Apartment_Gkyzi_-_Arios_Pagos__Athens_-l4532221?ref=searchListViewLD']

if you make the appropriate changes using xpath selectors you get all the available packages


<img src="{filename}/images/tut1.png" width="760">


    :::python
    In [16]: response.xpath('//*[@id="searchDetailsListings"]//div[@class="media search_listing_title"]//h4/a/@href').extract()
    Out[16]:
    [u'http://www.homegreekhome.com/en/rent_Apartment_Gkyzi_-_Arios_Pagos__Athens_-l4532221?ref=searchListViewLD',
     u'http://www.homegreekhome.com/en/rent_Apartment_Agios_Thomas__Athens_-l4526622?ref=searchListViewLD',
     u'http://www.homegreekhome.com/en/rent_Apartment_Agios_Ioannis__Athens_-l2432021?ref=searchListViewLD',
     u'http://www.homegreekhome.com/en/rent_Apartment_Neapoli_Exarcheion__Athens_-l4541851?ref=searchListViewLD',
     u'http://www.homegreekhome.com/en/rent_Apartment_Kentro__Athens_-l4458219?ref=searchListViewLD',
     u'http://www.homegreekhome.com/en/rent_Apartment_Fokionos_Negri__Athens_-l4537141?ref=searchListViewLD',
     u'http://www.homegreekhome.com/en/rent_Apartment_Neapoli_Exarcheion__Athens_-l3570529?ref=searchListViewLD',
     u'http://www.homegreekhome.com/en/rent_Apartment_Agios_Eleftherios__Athens_-l4474027?ref=searchListViewLD',
     u'http://www.homegreekhome.com/en/rent_Apartment_Kolonaki__Athens_-l4416560?ref=searchListViewLD',
     u'http://www.homegreekhome.com/en/rent_Apartment_Hilton__Athens_-l4517768?ref=searchListViewLD']
