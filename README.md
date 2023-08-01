# financial_and_data_processing


# Assignment 1: Financial Data Processing

## Background:
'''

    Data Processing and Analysis on Financial Transaction 
    Dataset with API, Queue, Inheritance, List Comprehensions and Generators
     
    For this assignment, you are tasked with developing a Python program that will simulate processing 
    and analyzing a stream of financial transactions, 
    such as those you might receive in a real-time trading or banking system. 
    The data will be provided via an API. 
    The dataset contains the following fields: TraderName, TransactionType, AssetType, AssetValue, and Quantity.

'''

## Part 1: Data Structure Creation and Validation
'''

    Create a base class Person which has the attribute name. 
    Make sure to create a method within Person class to validate the name attribute. 
    The name attribute must only contain letters and spaces.

    Then, create a Trader class that inherits from the Person class. 
    It should have the following additional attributes: transactionType, assetType, assetValue, and quantity. 
    The Trader class should also include methods to validate these attributes. The validation rules are:

    transactionType should be either "buy" or "sell".
    assetValue should be a non-negative float.
    quantity should be a non-negative integer.
'''

## Part 2: Data Loading, Transformation and API

'''

    Create a RESTful API using Flask or FastAPI, which will simulate incoming transactions. 
    The API should have a POST method to create new transactions.

    As transactions are posted to the API, 
    your program should validate and transform this data into Trader objects. 
    Handle any data validation errors during this transformation and keep a count of records with errors. 
    Implement a Queue data structure for holding Trader objects as they are being created. 
    This queue should allow additions at the end (enqueue) and removals from the front (dequeue).
     

    Use list comprehension to transform the list of Trader objects into a list of dictionaries, 
    where each dictionary contains the details of a Trader.
 '''
 
## Part 3: Data Analysis and Output
'''

    As you dequeue traders from the queue, analyze their data. Implement the following methods for data analysis:
    A method to find the trader with the highest total asset value.
    A method to find the trader with the lowest total asset value.
    A method to find the most frequently traded asset type.
    A method to find the average value of assets traded.

    Each of these methods should return a generator that yields the results.

    Note: For this part, it may be necessary to first dequeue all traders and add them to another data structure 
    that allows random access, such as a list or array. Queue data structures typically do not allow random access.
'''


# Summary.

During the part 1, without reading the entire assignment, I created a sqlalchemy model to store the data in postgres.
I created a base class Person which has the attribute name.
I created a Trader class that inherits from the Person class.
I created a REST-full API using FastAPI, which will simulate incoming transactions.
Then after reading the entire assignment, 
I created a Queue data structure for holding Trader objects as they are being created.
Please check the commit history for the changes, and understand the thought process.

During the assignment, I faced challenges with the following:
 - Pydantic V2 and FastAPI latest was new and there were not much documentation available.
 - I was confused with the question statement 'As you dequeue traders from the queue, analyze their data. 
   Implement the following methods for data analysis:' I was not sure if I need to dequeue all the traders and then analyze the data or 
   I need to analyze the data as I dequeue the traders and keep all the traders appending to a list.
 - Setting up application and testing, took a lot of time than expected.


# How to run the code.
pre-requisites:
 - Docker
 - Docker-compose

Steps:

1. Clone the repository.
2. Run the following command to start the application.
   docker-compose up --build
3. Open the browser and go to http://localhost:8000/docs
4. try out the trader-queue, and analysis endpoints.
5. To run the tests, run the following command. (Note: you will have to run the 2. step before running the tests)
   docker-compose -f docker-compose-override-test.yaml up --build
