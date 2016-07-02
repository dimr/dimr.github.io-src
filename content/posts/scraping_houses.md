title: Scraping for houses-part 1
date:   2016-06-15 04:47:56
tags: python,scrapy,tutorial
slug:scraping-for-houses
status:published

This is the first part of a tutorial series i am planning to write about the process of
acquiring data,cleaning data,analyzing data and visualizing. In this first part, i will show how to
scrape data from a  greek real estate website.


We are going to use [scrapy](http://scrapy.org/), a famous python library for screen scraping and i will use [xpath](https://en.wikipedia.org/wiki/XPath), a powerful query language for selecting nodes in xml/html documents.
For the full python code of this part, please visit this link.

>XPath uses path expressions to select nodes or node-sets in an XML document. The node is selected by following a path or steps.

i am going to assume that you have a basic knowledge of python and you can install additional libraries with pip.

####Some general information about scraping
1. First things first, when you want to scrape a website the first thing to do is disable javascript from the browser. Scrapy does **not** load it for you, with disabled javascript you see what scrapy sees when it visits the page. For example, if you check the page of a [random house](http://www.homegreekhome.com/en/rent_Apartment_Rigilis__Athens_-l3589786) at homegreekhome.com you will
see that pictures are not shown. There are ways to parse elements loaded via javascript by using either [selenium webdriver](http://www.seleniumhq.org/) with a normal browser like Firefox or with a headless browser like [Phantom.js](http://phantomjs.org/) or like [splash browser](https://splash.readthedocs.io/en/stable/).

2. Google chrome dev tools is your friend. It has some a really super helpful tool that you can use to extract the xpath of any element that you want to extract.

####The thing to start first
Assuming that you have installed scrapy correctly, lets first check a webpage. I will search for houses that are in the center of Athens.

    :::python
    scrapy shell http://www.homegreekhome.com/en/search/results/residential/rent/r100/m100m?ref=homepageMapSearchSR

and you will see info printed out. The basic idea is that scrapy loaded the page that you requests and you have the a response object with various attributes.
then copy paste this. Explanation follows

    :::python
    response.xpath('//*[@id="searchDetailsListings"]/div[1]/div/div/div[1]/div/h4/a/@href').extract()
    [u'http://www.homegreekhome.com/en/rent_Apartment_Nosokomeio_Pedon__Athens_-l4546456?ref=searchListViewLD']

and you got the link of the first house listed. The way to do it is to open the google chrome dev tools, select the element you want, right click and select copy xpath.


<img src="{filename}/images/scraping/first_pic.png" width="760">


here is how to get them all

    :::python
    response.xpath('//*[@id="searchDetailsListings"]//div/div/div/div[1]/div/h4/a/@href').extract()


and you get

    :::python
    [u'http://www.homegreekhome.com/en/rent_Apartment_Fokionos_Negri__Athens_-l4537141?ref=searchListViewLD',
     u'http://www.homegreekhome.com/en/rent_Apartment_Pedion_Areos__Athens_-l4501809?ref=searchListViewLD',
     u'http://www.homegreekhome.com/en/rent_Apartment_Ampelokipoi__Athens_-l4505771?ref=searchListViewLD',
     u'http://www.homegreekhome.com/en/rent_Apartment_Alsos_Pagkratiou__Athens_-l4485866?ref=searchListViewLD',
     u'http://www.homegreekhome.com/en/rent_Apartment_Plateia_Koliatsou__Athens_-l4554881?ref=searchListViewLD',
     u'http://www.homegreekhome.com/en/rent_Apartment_Kipseli__Athens_-l4535603?ref=searchListViewLD',
     u'http://www.homegreekhome.com/en/rent_Apartment_Plaka__Athens_-l4297290?ref=searchListViewLD',
     u'http://www.homegreekhome.com/en/rent_Apartment_Kolonaki__Athens_-l4550968?ref=searchListViewLD',
     u'http://www.homegreekhome.com/en/rent_Apartment_Kolonaki__Athens_-l4547891?ref=searchListViewLD',
     u'http://www.homegreekhome.com/en/rent_Apartment_Agios_Ioannis__Athens_-l2432021?ref=searchListViewLD']




Notice the difference between the first call and the second. We replaced `**/div[1]**` with `**//div**` and we got all this links. In xpath's world, when you write `div[1]` you get the first div element
after `**[@id="searchDetailsListings"]**` while `//` gets all the elements that are nested inside the previous element. Xpath is powerful, it may take you some time to get used to it, but it is word the try.

When the spider starts collecting the data it needs to store them in a data structure somewhere in the project. This is a simple as writing the fields that you choose to collect. In our example, these are the fields that we need to  set in our items.py filename

    #!python
      class HousesItem(scrapy.Item):
      # define the fields for your item here like:
            price=scrapy.Field()
            url=scrapy.Field()
            construction_year=scrapy.Field()
            heating_system=scrapy.Field()
            floor=scrapy.Field()
            house_type=scrapy.Field(default='Appartment')
            area=scrapy.Field()
            longitude=scrapy.Field()
            latitude=scrapy.Field()
            bathrooms=scrapy.Field(default=1)
            pics=scrapy.Field()
            phone=scrapy.Field()


Notice that we also scraped the coordinates of each house and the pics and the phone number that requires a bit more advanced operation that probably requires a different post. However, pics and coordinates although not visible to where hardcoded in each webpage and it was as simple as searching for the them in the html document to acquire them.

####Follow all pages
However, we do not want to get only the first page of the search results, we want all of them. The way to do it is to set a Rule. In essence, we want to tell scrapy to simulate a behavior where it presses the
next button at the bottom of the page and scrape next page until there is not page at all. As we did before, you can get xpath from google chrome.


<img src="{filename}/images/scraping/follow.png" width="760">


    #!python
    start_urls = [
        #Athens Center
        'http://www.homegreekhome.com/en/search/results/residential/rent/r100/m100m/',
        #Thessaloniki Center
        #'http://www.homegreekhome.com/en/search/results/residential/rent/r108/m108m'
    ]

    rules = (
        Rule(LinkExtractor(allow=(),restrict_xpaths=('//*[@id="pagination"]/ul/li[8]/a') ) , callback='parse_item', follow=True),
    )

The `start_urls` list tells from which pages to start, as you can see but just adding a second line from another city or another area in Athens you will get all the houses. Pretty cools, indeed.

####Parse information for each house
However, we need information for each house. We need to get the price and all the other information that are under the `"Key features"` on each house webpage. You continue the same way, you select the element and copy its xpath. Instead of going back to your scrapy shell each time you copy the xpath you can actually test in google`s chrome console.

For example if you paste the following expression in the console of this [page](http://www.homegreekhome.com/en/rent_Apartment_Pedion_Areos__Athens_-l4501809?ref=searchListViewLD)


    :::javascript
    $x('//*[@id="listingDetailsMainContent"]/div[9]/div[1]/div[2]/span')[0]


<img src="{filename}/images/scraping/chrome_console.png" width="760">

The process of extracting the information you want to keep from each house is somewhat similar. You select the time, get its xpath expression and you pass it scrapy's response object.
You can see the source code of this project `HERE`. Getting familiar with scrapy's project structure is something that you can learn by reading its excellent documentation. You can see how you start a project, where are you settings, how do you save the data that you parse etc.



####Some important things
* I used here xpath, in the scrapy world these are called [selectors](http://doc.scrapy.org/en/latest/topics/selectors.html). You can also parse html elements by CSS. Choose whatever you feel more comfortable with.  [This](http://www.zvon.org/comp/r/tut-XPath_1.html) a very good xpath tutorial.
* When scraping you should not hit the website hard. By default, scrapy follows the robots.txt directives of each site it visits but you can also tell it to ignore them. Be sure to enable the [AutoThrottle](http://doc.scrapy.org/en/latest/topics/autothrottle.html) extension and that you set the AUTOTHROTTLE_ENABLED to True.
