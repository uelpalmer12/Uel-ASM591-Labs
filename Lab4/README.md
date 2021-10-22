# ACRE LAB #

This lab is destined to designed a small concept app for the Purdue ACRE farm. 
ACRE is very dear to Purdue's College of Agriculture. It is used by researcher for reasearch project 
in many study areas going from plant breeding to digital agriculture


## Problem ##

However, ACRE has so many project that it becomes difficult to manage all the things going on at the farm. This is why creating a small data management web app that users can use to insert and retrieve data from about ACRE and/or
their research is highly important both for them and for the farm manager.

## Concept of a solution ## 

The solution thought about is to create a small web app consisting of multiple objects that have relationship together that will be linked in order to retrieve and add data in order to manage the farm. The web app will be implemented using Django.

## Data Model ##

![Data Model](https://github.com/uelpalmer12/Uel-ASM591-Labs/edit/main/Lab4/images/datamodel.png)


## Data Dictionnary ##

Here is a dictionnary of the data model I created. They serve as a description to better understand the data model.

### Field Class ###

| Attribute  |  Field Type |  Description | Acceptable Value  |
|---|---|---|---|---|
|  FieldID |  Integer | This field will be the primary of the field class  |  Integer >0 |
|  Field Type | Char  |  They will be a list to choose from either Research or Commercial | List value only  |
|  Current State | Boolean  |  Will tell if the field is being used for research or not |  True or False |