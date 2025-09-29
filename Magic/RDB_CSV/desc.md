## RDB_CSV plan

This ETL has an object to check the safety of a company employees emails and passwords. The goal is to check if any of a password or email for a service (lets say they are used for machine login) has been leaked on data breachs.


## ETL PLAN

There are some steps to follow in order to make the etl pipeline works, ensuring no overcharge will happen.

Here are the steps we are going to follow in order to create that ETL:

- **1- Define extraction mechanism from csv files**

- **2- Cleaning phase [dataframe objects]**

- **3- Validation phase including format checking**

- **4- First transformation [tto python dictionary]**

- **5- Merge both emails and password in 1 dictionary**

- **6- init checking service with tests**

- **7- Perform checking with defined strategy**

- **8- save results to python dict**

- **9- insert the results to a database after applying schema validation**

- **10- notify vulnerable employees via email**

Also there are some steps inclduded in some or all the main steps, such as:

- **sub-1 ensure logs are saved for this pipeline**

- **sub-2 Checking DB connectivity**

- **sub-3 Saving batch processing strategy parameters each trigger**

