# 测试方案



### 1. Hardware platform  

SF1、SF10

| Database   | vCPUs | Memory (GiB) | OS                            |
| ---------- | ----- | ------------ | ----------------------------- |
| TigerGraph | 8     | 64           | CentOS Linux release 7.2.1511 |
| Neptune    | 16    | 128          | CentOS Linux release 7.2.1511 |






### 2. 测试数据导入

#### 1) TigerGraph

TigerGraph采用官方提供的loading job，采用`composite-merged-fk`布局的csv数据。

[loading job](https://github.com/tigergraph/ecosys/tree/ldbc/ldbc_benchmark/tigergraph/v0.4.0)

调用查询使用如下命令。首先需要下载官方ldbc_benchmark代码

[ldbc_benchmark](https://github.com/tigergraph/ecosys/tree/ldbc/ldbc_benchmark/tigergraph/v0.4.0)

```shell
# 需要切换到tigergraph用户，并且安装python
# 第一个路径是参数位置 第二个路径是调用的bi
$ python driver.py run /home/tigergraph/v0.4.0/query/sf10 bi15
```



#### 2) Neptune

Neptune导入采用官方提供的opencyper方法，对原数据进行处理后导入。

(https://github.com/Magnesium-24/neptune/blob/main/pre_data.py)





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
| SF1     | TigerGraph | 49.02                | 1.48            | 1.40   |
| SF1     | Neptune    | 957.91               | 0.43            | 0.29   |
| SF10    | TigerGraph | 444.64               | 15.8            | 1.53   |
| SF10    | Neptune    | 10748.63             | 7.1             | 0.53   |




### 6. 测试结果

最终的BI查询结果如下。

#### SF1:



| SF-1 |            |          | 
| ---- | ---------- | -------- | 
|      | TigerGraph | Neptune  | 
| BI1  | 0.845355   | 55.38    | 
| BI2  | 0.471963   | 20.03    | 
| BI3  | 3.647336   | 25.51    | 
| BI4  | 3.617661   | 0        | 
| BI5  | 0.853283   | 5.16     | 
| BI6  | 2.331225   | out of memory  | 
| BI7  | 0.855641   | 44.22   | 
| BI8  | 0.869468   | 0   | 
| BI9  | 2.544086   | 306.29       | 
| BI10 | 4.26869    | 0   | 
| BI11 | 2.538688   | 186.21   | 
| BI12 | 4.999435   | 查询时间超过2000s,查询状态cancelled,未返回报错 | 
| BI13 | 1.632628   | 0        | 
| BI14 | 7.099117   | 查询时间超过2000s,查询状态cancelled,未返回报错 | 
| BI15 | 9.206343   | 0        | 
| BI16 | 1.42729    | 0    | 
| BI17 | 17.17986   | 查询时间超过2000s,查询状态cancelled,未返回报错  | 
| BI18 | 0.812378   | 12.11   | 
| BI19 | 5859.001   | 0        | 
| BI20 | 8.879433   | 0        | 



#### SF10：

| SF-10 |             |          | 
| ----- | ----------- | -------- |
|       | TG          | Neptune    |
| BI1   | 3.38937306  | 0        |
| BI2   | 0.521155299 |205.67  |
| BI3   | 5.718892624 |314.8   |
| BI4   | 3.350742671 | 0        |
| BI5   | 0.821403217 |   |
| BI6   | 14.78865259 | 0        |
| BI7   | 0.83008606  | |
| BI8   | 0.856962959 |  |
| BI9   | 4.720126248 | 查询时间超过4800s,查询状态cancelled,未返回报错        | 
| BI10  | 4.566453037 | 3925.394 | 
| BI11  | 5.490173962 | 查询时间超过4800s,查询状态cancelled,未返回报错 | 
| BI12  | 24.19363565 | 0        | 
| BI13  | 1.812093597 | 0        |
| BI14  | 0           | 0        |
| BI15  | 31.60021443 | 0        |
| BI16  | 1.440994855 |    |
| BI17  | 0           | 0        |
| BI18  | 0.81521947  |   |
| BI19  | 0           | 0        | 
| BI20  | 2.829668115 | 0        | 


