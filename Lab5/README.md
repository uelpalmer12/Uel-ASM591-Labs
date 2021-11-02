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

Attribute | Data Type | Description | Acceptable Values
-----|-----|-----|-----|
FieldID | Integer | ACRE field ID Number | >0 
Field Type | Char | List to choose from whether field is for research or commercial | 50 characters
Current State | Boolean | Choose whether or not the field is being used currently | True or False

### Worker ###

Attribute | Data Type | Description | Acceptable Values
-----|-----|-----|-----|
WorkerID | Integer | Worker ID Number | >0 
 Type | Char | List to choose from whether field is for research, technician, student or manager | 50 characters
First name | Char | Worker First Name | 50 to 64 characters
Last name | Char | Worker Last Name | 50 to 64 characters

### Job ### 

Attribute | Data Type | Description | Acceptable Values
-----|-----|-----|-----|
JobID | Integer | Job ID Number to find out information about action that was performed on the field and by who | >0 
 Date | DateTime | Date job was performed | Date only
Description | Char | Description about the work that was performed | can have many characters
Material used | Char | Material used during the job | 50 to 64 characters can be nullable
Material amount | Integer | Material amount used during job | Integer value but can nullable
Type | Char | list to choose from whether research, commercial or class teaching | List values only
Field.FieldID | Integer | Foreign key from the field table in order to link the data models | Foreign Key
Worker.WorkerID | Integer | Foreign key from the worker table in order to link the data models | Foreign key


After presenting my paper prototype to a couple of users they found it helpful that it was easy to use with a minimal amount of overhead in the user interface. Some, however found the app quite empty and wanted more multimedia content. The users also got stuck trying to go back to the previous screen "List of jobs" after entering a specific job. They had to go all the way back to first screen "All fields" and go through all the steps again. The most value came from the ease of use of the app and the capability to know what to do even on the first use. Something I would improve is to put more multimedia content and add more texture to my app.
