reStructuredText example
################################

:date: 2010-12-03
:tags: thats, awesome
:category: post
:slug: my-super-post
:authors: dimitris
:summary: Scraping house prices
:status: published



We are going to use `scrapy <http://scrapy.org/>`_, a famous python library for screen scraping that uses `xpath <https://en.wikipedia.org/wiki/XPath>`_, a powerful query language for selecting nodes in xml documents


  **XPath** uses path expressions to select nodes or node-sets in an XML document. The node is selected by following a path or steps.



.. _page: http://moliware.com/


<h1>Header</h1> **dasda**
--------------------------
`Read here <http://www.in.gr/>`_

#. first
#. second

.. code-block:: html
    ::linenos: table

    <h2>text</h2>

.. code-block:: sql
    :linenos: inline
    :linenostart: 140

        DO $$
    <<first_block>>
    DECLARE
      counter integer := 0;
    BEGIN
       counter := counter + 1;
       RAISE NOTICE 'The current value of counter is %', counter;
    END first_block $$;

i am going to assume that you have a basic knowledge of python and you can install additional libraries
###Install scrapy

.. image:: {filename}../images/first.png
    :alt: the text


cleating the screen

+------------+------------+-----------+
| Header 1   | Header 2   | Header 3  |
+============+============+===========+
| body row 1 | column 2   | column 3  |
+------------+------------+-----------+
| body row 2 | Cells may span columns.|
+------------+------------+-----------+
| body row 3 | Cells may  | - Cells   |
+------------+ span rows. | - contain |
| body row 4 |            | - blocks. |
+------------+------------+-----------+


if you make the appropriate changes using xpath selectors you get all the available packages


.. code-block:: python
    :linenos: inline
    :linenostart: 140

     response.xpath('//*[@id="searchDetailsListings"]/div[1]/div/div/div[1]/div/h4/a/@href').extract()
     [u'http://www.homegreekhome.com/en/rent_Apartment_Gkyzi_-_Arios_Pagos__Athens_-l4532221?ref=searchListViewLD']

**this is test** with text `visit this page <www.in.gr>`_



Tutorial and stuff you can use
********************************

.. code-block:: python
    :linenos: inline
    :linenostart: 140


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




.. code-block:: html
    :linenos: inline

    <h1>this is </h1>



.. csv-table:: Houses
    :header: "name", "firstname", "age"
    :widths: 20, 20, 10

    "Smith", "John", 40
    "Smith", "John, Junior", 20
