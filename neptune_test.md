# 测试方案



### 1. Hardware platform  

SF1、SF10

| Database   | vCPUs | Memory (GiB) | OS                            |
| ---------- | ----- | ------------ | ----------------------------- |
| TigerGraph | 16     | 128           | Ubuntu 20.04LTS |
| Neptune    | 16    | 128          | CentOS Linux release 7.2.1511 |






### 2. 测试数据导入

#### 1) TigerGraph3.4.0

TigerGraph采用官方提供的测试命令

https://github.com/tigergraph/ecosys/tree/ldbc/ldbc_benchmark/tigergraph/queries_v3




#### 2) Neptune

Neptune导入采用官方提供的opencyper方法，对原数据进行处理后导入。

https://github.com/Magnesium-24/neptune/blob/main/pre_data.py





#### 导入结果对比

TigerGraph

SF1 1.06G

SF10  10.31G

Neptune

SF1 1.31G

SF10 13.5G

Neptune导入参数时可以通过调整并行度参数parallelism,parallelism为OVERSUBSCRIBE 时加载速度最高，但是此时出现LOAD_DATA_DEADLOCK error,选择的parallelism参数为HIGH。

由于Neptune无法进行specify mapping，所以对文件进行预处理。


| dataset | database   | load consume time(s) | disk consume(G) | 压缩比 |
| ------- | ---------- | -------------------- | --------------- | ------ |
| SF1     | TigerGraph | 27.24                | 1.48            | 1.40   |
| SF1     | Neptune    | 957.91               | 0.43            | 0.29   |
| SF10    | TigerGraph | 202.42              | 15.8            | 1.53   |
| SF10    | Neptune    | 10748.63             | 7.1             | 0.53   |



### 3.查询修改
将目前的cypher修改为opencypher部分，其中部分功能不支持

1.bi4, bi8,bi13由于不能在with后使用unwind

2.bi 10 使用subgraphnodes方法不支持，bi15 allshortestpath 不支持，bi16不支持新建参数后选取属性操作，如message.title.year这种,bi 19 shortestpath不支持，bi20shortestpath不支持


### 4. 测试结果

最终的BI查询结果如下。

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
| BI12 | 0.22   | 查询时间超过2000s,查询状态cancelled,未返回报错 | 
| BI13 | 1.42   | 0        | 
| BI14 | 3.43   | 查询时间超过2000s,查询状态cancelled,未返回报错 | 
| BI15 | 0.07   | 0        | 
| BI16 | 1.43    | 0    | 
| BI17 | 2.73   | 查询时间超过2000s,查询状态cancelled,未返回报错  | 
| BI18 | 1.01   | 12.11   | 
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
| BI5   | 0.89 |   |
| BI6   | 1.31 | 0        |
| BI7   | 0.87  | |
| BI8   | 0.87 |  |
| BI9   | 1.70 | 查询时间超过4800s,查询状态cancelled,未返回报错        | 
| BI10  | 4.66 | 3925.394 | 
| BI11  | 0.82 | 查询时间超过4800s,查询状态cancelled,未返回报错 | 
| BI12  | 0.31 | 0        | 
| BI13  | 1.44 | 0        |
| BI14  | 3.47           | 0        |
| BI15  | 0.43 | 0        |
| BI16  | 1.48 |    |
| BI17  | 3.21           | 0        |
| BI18  | 1.01  |   |
| BI19  | 2.94           | 0        | 
| BI20  | 9.46 | 0        | 


