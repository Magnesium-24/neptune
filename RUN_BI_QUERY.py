!pip install neo4j

from neo4j import GraphDatabase
import time
import json

from neo4j import GraphDatabase
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest
from botocore.credentials import Credentials

SECRET_KEY = 'AKIA6B6T6R52WZZEEYHK'
ACCESS_KEY = 'i9UYqcnkts56+okWNPkAdPZgrLIBWg5r2pk7BCwb'

uri = "bolt://database-1-instance-1.clktpl2blcwo.us-east-2.neptune.amazonaws.com:8182"

credentials = Credentials(ACCESS_KEY, SECRET_KEY)
sigv4 = SigV4Auth(credentials, 'neptune-db', 'us-east-2'  )


request = AWSRequest(method='GET', url=uri)
sigv4.add_auth(request)

auth_obj = {
"Authorization" : request.headers['Authorization'],
"HttpMethod" : "GET",
"X-Amz-Date" : request.headers['X-Amz-Date'],
"Host" : uri
}

driver = GraphDatabase.driver(uri, auth=("USERNAME", json.dumps(auth_obj)), encrypted=True)


#bi 1  
start = time.time()
result = driver.session().run("""MATCH (message:Message)
WHERE message.creationDate1 < 1322668800
WITH count(message) AS totalMessageCount // this should be a subquery once Cypher supports it

MATCH (message:Message)
WHERE message.creationDate1 < 1322668800
  AND message.content IS NOT NULL
WITH
  totalMessageCount,
  message,
  message.creationDate1 AS creationDate1,
  message.year as year
WITH
  totalMessageCount,
  year,
  message:Comment AS isComment,
  CASE
    WHEN message.length <  40 THEN 0
    WHEN message.length <  80 THEN 1
    WHEN message.length < 160 THEN 2
    ELSE                           3
  END AS lengthCategory,
  count(message) AS messageCount,
  sum(message.length) / toFloat(count(message)) AS averageMessageLength,
  sum(message.length) AS sumMessageLength
RETURN
  year,
  isComment,
  lengthCategory,
  messageCount,
  averageMessageLength,
  sumMessageLength,
  messageCount / totalMessageCount AS percentageOfMessages
ORDER BY
  year desc,
  isComment ASC,
  lengthCategory ASC
  limit 1
""")
print(result.single())
end = time.time()
print('bi1')
print(end-start)



#bi 2  
start = time.time()
result = driver.session().run("""MATCH (tag:Tag)-[:hasType]->(:TagClass {name:'MusicalArtist'})
// window 1

 MATCH (message1:Message)-[:hasTag]->(tag)
  WHERE 1338480000 <= message1.creationDate1
    AND message1.creationDate1 < 1352563200
WITH tag, count(message1) AS countWindow1
// window 2
 MATCH (message2:Message)-[:hasTag]->(tag)
  WHERE 1338480000 <= message2.creationDate1
    AND message2.creationDate1 < 1352563200
WITH
  tag,
  countWindow1,
  count(message2) AS countWindow2
RETURN
  tag.name,
  countWindow1,
  countWindow2,
  abs(countWindow1 - countWindow2) AS diff
ORDER BY
  diff DESC,
  tag.name ASC
  limit 1
""")
print(result.single())
end = time.time()
print('bi2')
print(end-start)


#bi 3  
start = time.time()
result = driver.session().run("""MATCH
  (:Country {name:'Burma'} )<-[:isPartOf]-(:City)<-[:isLocatedIn]-
  (person:Person)<-[:hasModerator]-(forum:Forum)-[:containerOf]->
  (post:Message)<-[:replyOf]-(message:Message)-[:hasTag]->(:Tag)-[:hasType]->(:TagClass{name: 'MusicalArtist'})
with forum,person,count(DISTINCT message) AS messageCount
RETURN
  forum.name_ID,
  forum.title,
  forum.creationDate1,
  person.name_ID,
  messageCount
ORDER BY
  messageCount DESC,
  forum.name_ID ASC


  limit 1
""")
print(result.single())
end = time.time()
print('bi3')
print(end-start)


#bi 5  
start = time.time()
result = driver.session().run("""MATCH (tag:Tag {name: 'Abbas_I_of_Persia'})<-[:hasTag]-(message:Message)-[:hasCreator]->(person:Person)
 MATCH (message)<-[likes:likes]-(:Person)
WITH person, message, count(likes) AS likeCount
 MATCH (message)<-[:replyOf]-(reply:Message)
WITH person, message, likeCount, count(reply) AS replyCount
WITH person, count(message) AS messageCount, sum(likeCount) AS likeCount, sum(replyCount) AS replyCount
RETURN
  person.id,
  replyCount,
  likeCount,
  messageCount,
  1*messageCount + 2*replyCount + 10*likeCount AS score
ORDER BY
  score DESC,
  person.id ASC
  limit 1
""")
print(result.single())
end = time.time()
print('bi5')
print(end-start)



#bi 6 
start = time.time()
driver = GraphDatabase.driver(uri, auth=("USERNAME", json.dumps(auth_obj)), encrypted=True)
result = driver.session().run("""MATCH (tag:Tag {name:'Celine_Dion'})<-[:hasTag]-(message2:Message)-[:hasCreator]->(person1)
,(message2)<-[:likes]-(person2:Person)
,(person2)<-[:hasCreator]-(message3:Message)<-[like1:likes]-(person3:Person)
with person1,count(distinct person2) as authorityScore
RETURN
  person1.name_ID,
  authorityScore
ORDER BY
  authorityScore DESC,
  person1.name_ID ASC
  limit 1
""")
print(result.single())
end = time.time()
print('bi6')
print(end-start)




#bi 7 
start = time.time()
driver = GraphDatabase.driver(uri, auth=("USERNAME", json.dumps(auth_obj)), encrypted=True)
result = driver.session().run("""MATCH
  (tag:Tag {name: 'Enrique_Iglesias'})<-[:hasTag]-(message:Message),
  (message)<-[:replyOf]-(comment:Message)-[:hasTag]->(relatedTag:Tag)
WHERE NOT (comment)-[:hasTag]->(tag)
RETURN
  relatedTag.name,
  count(DISTINCT comment) AS count
ORDER BY
  count DESC,
  relatedTag.name ASC
 limit 1
""")
print(result.single())

end = time.time()
print('bi7')
print(end-start)



#bi 9 
start = time.time()
driver = GraphDatabase.driver(uri, auth=("USERNAME", json.dumps(auth_obj)), encrypted=True)

result = driver.session().run("""MATCH (person:Person)<-[:hasCreator]-(post:Message)<-[:replyOf*1..2]-(reply:Message)
WHERE  post.creationDate1 >= 1317398400
  AND  post.creationDate1 <= 1318608000
  AND reply.creationDate1 >= 1317398400
  AND reply.creationDate1 <= 1318608000
RETURN
  person.name_ID,
  person.firstName,
  person.lastName,
  count(DISTINCT post) AS threadCount,
  count(DISTINCT reply) AS messageCount

 limit 1
""")
print(result.single())
end = time.time()
print('bi9')
print(end - start) 

#bi 11 
start = time.time()

result = driver.session().run("""MATCH (country:Country {name: 'India'})
MATCH (a:Person)-[:isLocatedIn]->(:City)-[:isPartOf]->(country)
MATCH (b:Person)-[:isLocatedIn]->(:City)-[:isPartOf]->(country)
MATCH (c:Person)-[:isLocatedIn]->(:City)-[:isPartOf]->(country)
MATCH (a)-[k1:knows]-(b)-[k2:knows]-(c)-[k3:knows]-(a)
WHERE a.id < b.id
  AND b.id < c.id
  AND  1275321600<= k1.creationDate1
  AND 1275321600 <= k2.creationDate1
  AND 1275321600 <= k3.creationDate1
WITH DISTINCT a, b, c
RETURN count(*) AS count

 limit 1
""")
print(result.single())
end = time.time()
print('bi11')
print(end -start) 



#bi 12 
start = time.time()
driver = GraphDatabase.driver(uri, auth=("USERNAME", json.dumps(auth_obj)), encrypted=True)

result = driver.session().run("""MATCH (person:Person)
match (person)<-[:hasCreator]-(message:Message)-[:replyOf*0..1]->(post:Message)
WHERE message.content IS NOT NULL
  AND message.length < 20 
  AND message.creationDate1 > 1279728000
  AND post.language in ['ar','hu']
WITH
  person,
  count(message) AS messageCount
RETURN
  messageCount,
  count(person) AS personCount
order by 
personCount DESC,
  messageCount DESC

 limit 1
""")


print(result.single())
end = time.time()
print('bi12')
print(end-start)

#bi 14 

start = time.time()

result = driver.session().run("""MATCH
  (country1:Country {name: 'Chile'})<-[:isPartOf]-(city1:City)<-[:isLocatedIn]-(person1:Person),
  (country2:Country {name: 'Argentina'})<-[:isPartOf]-(city2:City)<-[:isLocatedIn]-(person2:Person)
WITH person1, person2, city1, 0 AS score
// subscore 1
match (person1)<-[:hasCreator]-(c:Message)-[:replyOf]->(:Message)-[:hasCreator]->(person2)
WITH DISTINCT person1, person2, city1, score + (CASE c WHEN null THEN 0 ELSE  4 END) AS score
// subscore 2
match (person1)<-[:hasCreator]-(m:Message)<-[:replyOf]-(:Message)-[:hasCreator]->(person2)
WITH DISTINCT person1, person2, city1, score + (CASE m WHEN null THEN 0 ELSE  1 END) AS score
// subscore 3
match (person1)-[k:knows]-(person2)
WITH DISTINCT person1, person2, city1, score + (CASE k WHEN null THEN 0 ELSE 15 END) AS score
// subscore 4
match (person1)-[:likes]->(m:Message)-[:hasCreator]->(person2)
WITH DISTINCT person1, person2, city1, score + (CASE m WHEN null THEN 0 ELSE 10 END) AS score
// subscore 5
match (person1)<-[:hasCreator]-(m:Message)<-[:likes]-(person2)
WITH DISTINCT person1, person2, city1, score + (CASE m WHEN null THEN 0 ELSE  1 END) AS score
// preorder

WITH
  city1,score,person1,person2
  limit 1
RETURN
  person1.name_ID,
  person2.name_ID,
  city1.name,
  score
ORDER BY
  score DESC,
  person1.name_ID ASC,
  person2.name_ID ASC
limit 1
""")
print(result.single())
end = time.time()

print('bi14')
print(end-start)



#bi 17 

driver = GraphDatabase.driver(uri, auth=("USERNAME", json.dumps(auth_obj)), encrypted=True)
start = time.time()
result = driver.session().run("""MATCH
  (tag:Tag {name: 'Celine_Dion'}),
  (person1:Person)<-[:hasCreator]-(message1:Message)-[:replyOf*0..1]->(post1:Message)<-[:containerOf]-(forum1:Forum),
  (message1)-[:hasTag]->(tag),
  (forum1)<-[:hasMember]->(person2:Person)<-[:hasCreator]-(comment:Comment)-[:hasTag]->(tag),
  (forum1)<-[:hasMember]->(person3:Person)<-[:hasCreator]-(message2:Message)-[:hasTag]->(tag),
  (comment)-[:replyOf]->(message2)-[:replyOf*0..1]->(post2:Message)<-[:containerOf]-(forum2:Forum)
WHERE forum1 <> forum2
  AND message2.creationDate1 > message1.creationDate1 + 835200000
  AND NOT (forum2)-[:hasMember]->(person1)
RETURN  person1.name_ID,count(DISTINCT message2.name_ID) AS messageCount
ORDER BY messageCount DESC, person1.name_ID ASC 
 limit 1
""")
print(result.single())
end = time.time()
print('bi17')
print(end - start)




start = time.time()
driver = GraphDatabase.driver(uri, auth=("USERNAME", json.dumps(auth_obj)), encrypted=True)

result = driver.session().run("""MATCH (person1:Person {name_ID:'26388279068088' })-[:knows]-(mutualFriend:Person)-[:knows]-(person2:Person)-[:hasInterest]->(:Tag {name: 'Celine_Dion'})
WHERE person1 <> person2
  AND NOT (person1)-[:knows]-(person2)
RETURN person2.name_ID AS person2Id, count(DISTINCT mutualFriend) AS mutualFriendCount
ORDER BY mutualFriendCount DESC, person2Id ASC
LIMIT 1

""")
print(result.single())
end = time.time()
print('bi18')
print(end - start)








