# 测试方案

### 1. 测试数据集说明

##### 1) SF1

###### vertices

|            | Total     | comment     | post        | company | university | city   | country | continent | forum     | person    | tag       | tagclass |
| ---------- | --------- | ----------- | ----------- | ------- | ---------- | ------ | ------- | --------- | --------- | --------- | --------- | -------- |
| attributes |           | 6           | 8           | 3       | 3          | 3      | 3       | 3         | 3         | 10        | 3         | 3        |
| raw data   | 517.53MiB | 351,581,470 | 177,817,556 | 852,170 |            | 86,179 |         |           | 8,983,021 | 2,179,853 | 1,168,234 | 4,153    |
| vertices   | 3.96M     | 2,580,332   | 1,229,275   | 1,575   | 6,380      | 1,343  | 111     | 6         | 109,617   | 11,000    | 16,080    | 71       |

###### edges

|            | Total    | CONTAINER_OF | HAS_CREATOR | HAS_INTEREST | HAS_MEMBER  | HAS_MODERATOR | HAS_TAG     | HAS_TYPE | IS_LOCATED_IN | IS_LOCATED_IN | IS_PART_OF | IS_SUBCLASS_OF | KNOWS      | LIKES       | REPLY_OF  | STUDY_AT | WORK_AT   |
| ---------- | -------- | ------------ | ----------- | ------------ | ----------- | ------------- | ----------- | -------- | ------------- | ------------- | ---------- | -------------- | ---------- | ----------- | --------- | -------- | --------- |
| attributes |          | 0            | 0           | 0            | 1           | 0             | 0           | 0        | 0             | 0             | 0          | 0              | 1          | 1           | 0         | 1        | 1         |
| raw data   | 547.4MiB |              |             | 12,552,989   | 189,035,695 |               | 210,964,349 |          |               |               |            |                | 13,205,423 | 146,490,382 |           | 481,424  | 1,260,466 |
| edges      | 22.2 M   | 1,229,275    | 3809607     | 255596       | 3268415     | 109617        | 4317735     | 16080    | 3828562       |               | 1,454      | 70             | 226,293    | 2,521,160   | 2,580,332 | 8,880    | 23,600    |

##### 2) SF10

###### vertices

|            | Total   | comment       | post          | company | university | city  | country | continent | forum   | person     | tag        | tagclass  |
| ---------- | ------- | ------------- | ------------- | ------- | ---------- | ----- | ------- | --------- | ------- | ---------- | ---------- | --------- |
| attributes |         | 6             | 8             | 3       | 3          | 3     | 3       | 3         | 3       | 10         | 3          | 3         |
| raw data   | 4.61GiB | 3,495,316,465 | 1,378,417,294 | 852,170 |            |       | 86,179  |           |         | 59,729,970 | 14,495,324 | 1,168,234 |
| vertices   | 35.5M   | 25,652,008    | 9,020,368     | 1,575   | 6,380      | 1,343 | 111     | 6         | 725,661 | 73,000     | 16,080     | 71        |

###### edges

|            | Total  | CONTAINER_OF | HAS_CREATOR | HAS_INTEREST | HAS_MEMBER    | HAS_MODERATOR | HAS_TAG       | HAS_TYPE | IS_LOCATED_IN | IS_LOCATED_IN | IS_PART_OF | IS_SUBCLASS_OF | KNOWS       | LIKES         | REPLY_OF   | STUDY_AT  | WORK_AT   |
| ---------- | ------ | ------------ | ----------- | ------------ | ------------- | ------------- | ------------- | -------- | ------------- | ------------- | ---------- | -------------- | ----------- | ------------- | ---------- | --------- | --------- |
| attributes |        | 0            | 0           | 0            | 1             | 0             | 0             | 0        | 0             | 0             | 0          | 0              | 1           | 1             | 0          | 1         | 1         |
| raw data   | 5.7GiB |              |             | 84,078,065   | 2,022,081,398 |               | 2,081,671,631 |          |               |               |            |                | 139,352,052 | 1,782,149,319 |            | 3,176,415 | 8,496,561 |
| edges      | 22.2M  | 9,020,368    | 34,672,376  | 1,709,747    | 34,787,469    | 725,661       | 42,508,747    | 16,080   | 34,753,331    | 34,753,331    | 1,454      | 70             | 2,380,850   | 30,599,157    | 25,652,008 | 58,526    | 158,977   |



##### 3) SF100

###### vertices

|            | Total    | comment        | post           | company         | university | city  | country | continent | forum     | person      | tag        | tagclass  |
| ---------- | -------- | -------------- | -------------- | --------------- | ---------- | ----- | ------- | --------- | --------- | ----------- | ---------- | --------- |
| attributes |          | 6              | 8              | 3               | 3          | 3     | 3       | 3         | 3         | 10          | 3          | 3         |
| raw data   | 43.34GiB | 34,695,841,296 | 11,325,997,135 | 852,170         |            |       | 86,179  |           |           | 415,561,503 | 99,132,684 | 1,168,234 |
| vertices   | 325.8M   | 251,056,181    |                | 69,239,9931,575 | 6,380      | 1,343 | 111     | 6         | 4,983,975 | 499,000     | 16,080     | 71        |

###### edges

|            | Total    | CONTAINER_OF | HAS_CREATOR | HAS_INTEREST | HAS_MEMBER     | HAS_MODERATOR | HAS_TAG        | HAS_TYPE | IS_LOCATED_IN | IS_LOCATED_IN | IS_PART_OF | IS_SUBCLASS_OF | KNOWS         | LIKES          | REPLY_OF  | STUDY_AT   | WORK_AT    |
| ---------- | -------- | ------------ | ----------- | ------------ | -------------- | ------------- | -------------- | -------- | ------------- | ------------- | ---------- | -------------- | ------------- | -------------- | --------- | ---------- | ---------- |
| attributes |          | 0            | 0           | 0            | 1              | 0             | 0              | 0        | 0             | 0             | 0          | 0              | 1             | 1              | 0         | 1          | 1          |
| raw data   | 60.08GiB |              |             | 573,984,428  | 20,414,686,866 |               | 20,791,706,746 |          |               |               |            |                | 1,397,918,820 | 21,249,073,004 |           | 21,690,783 | 58,114,499 |
| edges      | 2.45B    | 69,477,546   | 320,533,727 | 11,663,500   | 345,533,481    | 4,983,975     | 416,098,265    | 16,080   | 321,040,682   | 321,040,682   | 1,454      | 70             | 23,841,591    | 358,946,274    | 251056181 | 399,334    | 1,086,342  |



### 2. Hardware platform  

SF1、SF10测试机器

| Database   | vCPUs | Memory (GiB) | OS                            |
| ---------- | ----- | ------------ | ----------------------------- |
| TigerGraph | 8     | 64           | CentOS Linux release 7.2.1511 |
| Neo4j      | 8     | 64           | CentOS Linux release 7.2.1511 |
| JanusGraph | 8     | 64           | CentOS Linux release 7.2.1511 |



SF100测试机器

| Database   | vCPUs | Memory (GiB) | OS                 |
| ---------- | ----- | ------------ | ------------------ |
| TigerGraph | 16    | 128          | Ubuntu 18.04.5 LTS |
| Neo4j      | 16    | 128          | Ubuntu 18.04.5 LTS |
| JanusGraph | 16    | 128          | Ubuntu 18.04.5 LTS |





### 3. 测试数据导入

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



#### 2) Neo4j

Neo4j导入采用官方提供的环境创建方式。但与TigerGraph不同的是，它采用的是`composite-projected-fk`布局，点和边拆分开。

可以使用官方提供的convertor，但安装环境可能会有一些问题，我使用python脚本抽取数据。

[cypher](https://github.com/ldbc/ldbc_snb_bi/tree/main/cypher)

调用查询使用以下命令

```
$ python bi.py
```



#### 3) JanusGraph

JanusGraph 官方提供的大量数据导入方法是一种json。但是这种json与一般csv不同，需要做大量准备工作。它需要描述点和入边出边等信息，处理为该种格式较为复杂。

所以没有采用上述方案导入。

最开始采用gremlin提供的客户端导入。在sf 1和 sf 10 的情况下，可以花费可以接受的时间导入。但当数据集到达sf 100时，导入速度太慢，无法完成导入工作。所以最终采用分割文件 + 多线程导入。将导入速度提升大约十倍。最终观察到机器 CPU 占满。线程池不能再往上调整，如果往上调整，会导致连接中断等问题。

如果按照单线程导入，速度约为4k/s。改用多线程导入后，速度到达 4w/s

1 需要先切分文件，主要需要切分的文件有以下几个

```
Comment.csv
Comment_hasTag_Tag.csv
Forum_hasMember_Person.csv
Person_likes_Comment.csv
Person_likes_Post.csv
Post.csv
Post_hasTag_Tag.csv
```

切分方法可以调用以下脚本

进入以上文件所在文件夹后，调用以下脚本即可，传入参数为 文件名去掉后缀。执行后，切分文件位置在当前目录下有一个文件夹 。

例如 Comment.csv 切分后所在位置： $dir/Comment

```shell
#!/bin/bash
mkdir $1
`split -l 2000000 $1.csv -d -a 4 $1/$1_split_`
`sed -i '1d' $1/$1_split_0000`
`sed -i '1i\header'  $1/*`
```



2 调用java代码

JanusGraph的配置文件 sf100.properties

```properties
gremlin.graph=org.JanusGraph.core.JanusGraphFactory
storage.backend=cql
storage.hostname=127.0.0.1

# 需要改为图名
storage.cql.keyspace=sf100
cache.db-cache = true

cache.db-cache-clean-wait = 20
cache.db-cache-time = 180000
cache.db-cache-size = 0.5
index.search.backend=elasticsearch
index.search.hostname=127.0.0.1
# index后要改为自己的图名  =后也要改
index.sf100.index-name=sf100

graph.set-vertex-id=true
```



```shell
# 首先打包 
mvn assembly:assembly

# 首先创建图 后方为图的配置文件
java -cp target/janus-1.0-SNAPSHOT-jar-with-dependencies.jar com.tigergraph.janus.load.CreateGraph /opt/JanusGraph-0.5.3/conf/sf100.properties

# 导入点 第一个参数为图的配置文件  第二个为数据所在位置(末尾必须加/)。 第三个参数为一批发送多少
java -cp target/janus-1.0-SNAPSHOT-jar-with-dependencies.jar com.tigergraph.janus.load.LoadVertex /opt/JanusGraph-0.5.3/conf/sf100.properties /home/ubuntu/sf100/format/ 10000

# 批量导入大点  Comment Post
# 第一个参数为图配置文件
# 第二个为切分后的文件夹
# 第三个为一批发送多少
# 第四个参数是类名
java -cp target/janus-1.0-SNAPSHOT-jar-with-dependencies.jar com.tigergraph.janus.multiLoad.MultiLoad /opt/JanusGraph-0.5.3/conf/sf100.properties /home/ubuntu/sf100/format/Comment 10000 VertexLoadComment

java -cp target/janus-1.0-SNAPSHOT-jar-with-dependencies.jar com.tigergraph.janus.multiLoad.MultiLoad /opt/JanusGraph-0.5.3/conf/sf100.properties /home/ubuntu/sf100/format/Post 10000 VertexLoadPost


`cd /home/ubuntu/janus`
`java -cp target/janus-1.0-SNAPSHOT-jar-with-dependencies.jar com.tigergraph.janus.multi.MultiLoad /opt/JanusGraph-0.5.3/conf/sf100.properties /home/ubuntu/sf100/Comment_hasTag_Tag 10000 EdgeLoadComment_hasTag_Tag`
`cp err.log EdgeLoadComment_hasTag_Tag.log`
echo "EdgeLoadComment success"

`java -cp target/janus-1.0-SNAPSHOT-jar-with-dependencies.jar com.tigergraph.janus.multi.MultiLoad /opt/JanusGraph-0.5.3/conf/sf100.properties /home/ubuntu/sf100/Forum_hasMember_Person 10000 EdgeLoadForum_hasMember_Person`
`cp err.log EdgeLoadForum_hasMember_Person.log`
echo "EdgeLoadForum_hasMember_Person success"

`java -cp target/janus-1.0-SNAPSHOT-jar-with-dependencies.jar com.tigergraph.janus.multi.MultiLoad /opt/JanusGraph-0.5.3/conf/sf100.properties /home/ubuntu/sf100/Person_likes_Comment 10000 EdgeLoadPerson_likes_Comment`
`cp err.log EdgeLoadPerson_likes_Comment.log`
echo "EdgeLoadPerson_likes_Comment success"

`java -cp target/janus-1.0-SNAPSHOT-jar-with-dependencies.jar com.tigergraph.janus.multi.MultiLoad /opt/JanusGraph-0.5.3/conf/sf100.properties /home/ubuntu/sf100/Post 10000 EdgeLoadPost`
`cp err.log EdgeLoadPost.log`
echo "EdgeLoadPost success"

`java -cp target/janus-1.0-SNAPSHOT-jar-with-dependencies.jar com.tigergraph.janus.multi.MultiLoad /opt/JanusGraph-0.5.3/conf/sf100.properties /home/ubuntu/sf100/Person_likes_Post 10000 EdgeLoadPerson_likes_Post`
`cp err.log EdgeLoadPerson_likes_Post.log`
echo "EdgeLoadPerson_likes_Post success"


`java -cp target/janus-1.0-SNAPSHOT-jar-with-dependencies.jar com.tigergraph.janus.multi.MultiLoad /opt/JanusGraph-0.5.3/conf/sf100.properties /home/ubuntu/sf100/Post_hasTag_Tag 10000 EdgeLoadPost_hasTag_Tag`
`cp err.log Post_hasTag_Tag.log`
echo "EdgeLoadPost_hasTag_Tag success"

# 导入其他边
java -cp target/janus-1.0-SNAPSHOT-jar-with-dependencies.jar com.tigergraph.janus.load.LoadEdge /opt/JanusGraph-0.5.3/conf/sf100.properties /home/ubuntu/sf100/format/ 10000
```



```shell
# 查询的启动命令
java -cp target/janus-1.0-SNAPSHOT-jar-with-dependencies.jar com.tigergraph.janus.query.BI2 -conf /opt/JanusGraph-0.5.3/conf/sf1.properties -parameter /home/tigergraph/v0.4.0/query/sf1/bi-2.txt -output /root/janus/out
```





#### 导入结果对比

说明：因为JanusGraph的SF100是使用的多线程导入，所以需要将数据切分，多线程运行会有很多问题，所以导入时是按照类型导入的，没有一次导入，所以它的时间计算不准确。

SF1 1.06G

SF10  10.31G

SF100  103.42G

| dataset | database   | load consume time(s) | disk consume(G) | 压缩比 |
| ------- | ---------- | -------------------- | --------------- | ------ |
| SF1     | TigerGraph | 49.02                | 1.48            | 1.40   |
| SF1     | Neo4j      | 67.922               | 2.359           | 2.23   |
| SF1     | JanusGraph | 882.31               | 2.76            | 2.60   |
|         |            |                      |                 |        |
| SF10    | TigerGraph | 444.64               | 15.8            | 1.53   |
| SF10    | Neo4j      | 480.29               | 22.28           | 2.16   |
| SF10    | JanusGraph | 8703.35              | 19.0            | 1.84   |
|         |            |                      |                 |        |
| SF100   | TigerGraph | 5206.63              | 130             | 1.26   |
| SF100   | Neo4j      |                      |                 |        |
| SF100   | JanusGraph | >875000              | 256             | 2.47   |

SF1原始数据1.06G，TigerGraph数据缩放比1.40，Neo4j为2.23，JanusGraph为3.70。由此可见，TigerGraph存储数据所占磁盘较小。

TigerGraph对数据压缩较好，所占磁盘较小。Neo4j其次，JanusGraph最差。



![image-20210618114104974](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210618114104974.png)



### 4. 测试代码验证

验证TigerGraph、JanusGraph实现的BI逻辑是否与官方Neo4j示例一致。

JanusGraph实现BI的逻辑是按照TigerGraph的实现逻辑实现的。最终对比结果也发现是一致的。

TigerGraph和Neo4j的结果对比将在稍后完成。



### 5. 测试说明

查询时间定义:

​	测试参数提供5组，每组参数运行5次，取中位数作为该组的运行时间。

​	使用5组的平均时间作为最终的测试结果。如果测试时间太久，会将运行次数降为3次。







### 6. 测试结果

最终的BI查询结果如下。

#### SF1:

**JanusGraph &Tiger &Neo4j**

| SF-1 |            |          |          |                       |                  |
| ---- | ---------- | -------- | -------- | --------------------- | ---------------- |
|      | TigerGraph | Janus    | Neo4j    | JanusGraph/TigerGraph | Neo4j/TigerGraph |
| BI1  | 0.845355   | 0        | 6.1649   | 0                     | 7.292673         |
| BI2  | 0.471963   | 46.843   | 0.97206  | 99.25141              | 2.05961          |
| BI3  | 3.647336   | 141.386  | 0.80934  | 38.76419              | 0.221899         |
| BI4  | 3.617661   | 1568.844 | 暂未实现 | 433.6625              |                  |
| BI5  | 0.853283   | 2.8514   | 0.0255   | 3.34168               | 0.029885         |
| BI6  | 2.331225   | 696.958  | 7.60598  | 298.9664              | 3.262654         |
| BI7  | 0.855641   | 17.096   | 0.03112  | 19.98034              | 0.03637          |
| BI8  | 0.869468   | 2.206    | 1.50308  | 2.537185              | 1.728736         |
| BI9  | 2.544086   | 0        | 0.00266  | 0                     | 0.001046         |
| BI10 | 4.26869    | 13.314   | 0.29806  | 3.11899               | 0.069825         |
| BI11 | 2.538688   | 62.584   | 0.0505   | 24.65211              | 0.019892         |
| BI12 | 4.999435   | 0        | 0.01374  | 0                     | 0.002748         |
| BI13 | 1.632628   | 0        | 0.87716  | 0                     | 0.537269         |
| BI14 | 7.099117   | 277.518  | 44.0542  | 39.0919               | 6.205589         |
| BI15 | 9.206343   | 0        | 290.9224 | 0                     | 31.60021         |
| BI16 | 1.42729    | 3.662    | 0.021075 | 2.565701              | 0.014766         |
| BI17 | 17.17986   | 955.508  | 8.124    | 55.61793              | 0.472879         |
| BI18 | 0.812378   | 0.554    | 0.0069   | 0.681948              | 0.008494         |
| BI19 | 5859.001   | 0        | 2955.239 | 0                     | 0.504393         |
| BI20 | 8.879433   | 0        | 37.26248 | 0                     | 4.196493         |

对于小数据集，TigerGraph和Neo4j的查询效率差别不大。但对于JanusGraph来说，一些复杂的业务逻辑，查询十分困难，速度非常慢。

TigerGraph比JanusGraph快2-400倍。



![image-20210618164024065](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210618164024065.png)

#### SF10：

| SF-10 |             |          |          |               |          |
| ----- | ----------- | -------- | -------- | ------------- | -------- |
|       | TG          | Janus    | neo4j    | JanusGraph/TG | Neo4j/TG |
| BI1   | 3.38937306  | 0        | 102.0658 | 0             | 30.11347 |
| BI2   | 0.521155299 | 174.429  | 26.1859  | 334.6967794   | 50.24587 |
| BI3   | 5.718892624 | 11814.67 | 8.15842  | 2065.901876   | 1.426573 |
| BI4   | 3.350742671 | 0        | 0        | 0             | 0        |
| BI5   | 0.821403217 | 120.822  | 0.43636  | 147.0921923   | 0.531237 |
| BI6   | 14.78865259 | 0        | 496.1478 | 0             | 33.54922 |
| BI7   | 0.83008606  | 4180.299 | 0.69548  | 5035.982657   | 0.837841 |
| BI8   | 0.856962959 | 1809.392 | 113.8859 | 2111.400478   | 132.8948 |
| BI9   | 4.720126248 | 0        | 0.0106   | 0             | 0.002246 |
| BI10  | 4.566453037 | 3925.394 | 8.3216   | 859.6155414   | 1.822333 |
| BI11  | 5.490173962 | 4401.437 | 804.2035 | 801.6935402   | 146.4805 |
| BI12  | 24.19363565 | 0        | 0.20236  | 0             | 0.008364 |
| BI13  | 1.812093597 | 0        | 55.07296 | 0             | 30.3919  |
| BI14  | 0           | 0        | 0        |               |          |
| BI15  | 31.60021443 | 0        | 317.0491 |               | 10.03313 |
| BI16  | 1.440994855 | 9.464    | 19.13872 | 6.567684796   | 13.2816  |
| BI17  | 0           | 0        | 69.27028 |               |          |
| BI18  | 0.81521947  | 1.357    | 0.066825 | 1.664582423   | 0.081972 |
| BI19  | 0           | 0        | 0        |               |          |
| BI20  | 2.829668115 | 0        | 0        | 0             | 0        |

![image-20210618164011382](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210618164011382.png)

#### SF100:

对于JanusGraph来说，SF100无法得到结果，所以只将数据导入之后，BI查询测试便不能进行了。







**结论：**

1.单数据库查询效率对比

- TigerGraph的BI查询随着数据集增大，时间增长在0.31-10倍之间，时间在线性增长。


- JanusGraph时间增长在2-820倍之间，耗时增长非常快。而且，在sf10数据集上，已经有超过一半的查询无法得到结果。
- Neo4j时间增长在4-75之间，有一个查询甚至到达15924倍。中位数在60倍，可以看出，随着数据规模的增大，查询的耗时变得非常大，耗时并非是线性增长。



2.数据库间对比

- TigerGraph比JanusGraph在sf1数据集上，快了0.68-433倍，超过TigerGraph的只有一个。在sf10上，JanusGraph可以在一小时内返回结果的查询中，TigerGraph比JanusGraph快了1.66-5036倍。
- TigerGraph比Neo4j在sf1数据集上，两者表现接近。TigerGraph有7个查询优于Neo4j，范围在1.72-31之间；有12个慢于Neo4j，范围在0.008-0.54之间；在sf10上，TigerGraph比Neo4j快的有12个，范围在1.42-132之间；慢的有5个，范围在0.002-0.8；有3个查询两者均无法得到结果。

从以上可以看出，TigerGraph比JanusGraph在BI查询中拥有更好的性能。在小数据集上，TigerGraph和Neo4j表现相当，但在大数据集上，Neo4j性能明显降低，有一些参数无法跑出结果，怀疑是遇到了邻居较多的节点，但TigerGraph查询的时间增长并不是很快。