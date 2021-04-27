# Pineview Clickstream Pantip Data Cleaning

![Example-data](https://github.com/poom201211/CleanPantipDataForPineview/blob/master/images/ExampleData.png)

## Description

This repository is used to clean data from the lab in order for it to fit the main Pineview backend model. The program in result will create a JSON data file that you can easily import into MongoDB in order for it to be used. Written in pure Python connected to MongoDB database from MIKE's lab. 

## Prerequisites

- Python version 3.7 or above.

## Installation

1. Open the Terminal and type the following command: 

```
$ git clone https://github.com/poom201211/CleanPantipDataForPineview.git
```

2. Locate to the directory:

```
$ cd CleanPantipDataForPineview
```

3. Install the libraries:

```
$ pip install -r requirements.txt
```

## Program Execution Order

1. run review_clickstream.py
2. run remove_commas.py
3. run review_classification.py
4. run convert_kratoo_to_json.py
5. Put completed_data.json that is created into mongo content collection


