# benchmark report



### 1. Hardware platform  

SF1、SF10

| Database   | vCPUs | Memory (GiB) | OS                            |
| ---------- | ----- | ------------ | ----------------------------- |
| TigerGraph | 16     | 128           | Tigergraph 3.4.0 |
| Neptune    | 16    | 128          | Neptune 1.0.5.1.R3 |






### 2. loading data

#### 1) TigerGraph3.4.0

Use the official test command provided

https://github.com/tigergraph/ecosys/tree/ldbc/ldbc_benchmark/tigergraph/queries_v3




#### 2) Neptune

Using the official opencyper method provided, the original data is processed and imported.

https://github.com/Magnesium-24/neptune/blob/main/pre_data.py





#### Comparison of loading data results

Due to some limitations of neptune, the original file needs to be pre-processed, such as modifying the primary key, adding timestamps, adding id columns to return, adding month and other fields.So the neptune raw file size is larger than the tigergraph raw file size.

parallelism  is an optional parameter that can be set to reduce the number of threads used by the bulk load process.

parallelism :"OVERSUBSCRIBE" 
The number of threads used is the number of available vCPUs multiplied by 2. If this value is used, the bulk loader takes up all available resources.

The "OVERSUBSCRIBE" setting result in a deadlock between threads when loading openCypher data. Neptune returns the LOAD_DATA_DEADLOCK error. So we set parallelism "HIGH".




| dataset | database  | raw size | load consume time(s) | disk consume(G) | compression ration |
| ------- | ----------|--------- | -------------------- | --------------- | ------ |
| SF1     | TigerGraph| 1.06G| 27.24                | 0.53            | 0.48   |
| SF1     | Neptune   | 1.35G| 912.53               | 0.43            | 0.43   |
| SF10    | TigerGraph| 10.31G| 202.42              | 5.99            | 0.58   |
| SF10    | Neptune   | 13.5G| 8559.63s            | 7.11             | 0.53   |




### 3. Results


#### SF1:



| SF-1 |            |          | 
| ---- | ---------- | -------- | 
|      | TigerGraph | Neptune  | 
| BI1  | 0.25   | 55.38    | 
| BI2  | 0.42   | 20.03    | 
| BI3  | 2.94   | 25.51    | 
| BI4  | 2.88   | 0        | 
| BI5  | 0.82   | 5.16     | 
| BI6  | 1.04   | out of memory  | 
| BI7  | 0.82   | 44.22   | 
| BI8  | 0.82   | 0   | 
| BI9  | 1.02   | 306.29       | 
| BI10 | 3.75    | 0   | 
| BI11 | 0.81   | 186.21   | 
| BI12 | 0.22   | Query time more than 2000s, query status cancelled, did not return an error  | 
| BI13 | 1.42   | 0        | 
| BI14 | 3.43   | Query time more than 2000s, query status cancelled, did not return an error  | 
| BI15 | 0.07   | 0        | 
| BI16 | 1.43    | 0    | 
| BI17 | 2.73   | Query time more than 2000s, query status cancelled, did not return an error   | 
| BI18 | 1.01   | 0.71   | 
| BI19 | 3.08   | 0        | 
| BI20 | 9.27   | 0        | 



#### SF10：

| SF-10 |             |          | 
| ----- | ----------- | -------- |
|       | TG          | Neptune    |
| BI1   | 0.58  | 0        |
| BI2   | 0.52 |205.67  |
| BI3   | 4.33 |314.8   |
| BI4   | 3.16 | 0        |
| BI5   | 0.89 | 49.15  |
| BI6   | 1.31 | out of memory        |
| BI7   | 0.87  |1041.24 |
| BI8   | 0.87 |  |
| BI9   | 1.70 | Query time more than 4800s, query status cancelled, did not return an error         | 
| BI10  | 4.66 |  | 
| BI11  | 0.82 | Query time more than 4800s, query status cancelled, did not return an error  | 
| BI12  | 0.31 | 0        | 
| BI13  | 1.44 | 0        |
| BI14  | 3.47           | 0        |
| BI15  | 0.43 | 0        |
| BI16  | 1.48 |    |
| BI17  | 3.21           | 0        |
| BI18  | 1.01  |2.73   |
| BI19  | 2.94           | 0        | 
| BI20  | 9.46 | 0        | 


