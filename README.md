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