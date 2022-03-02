# neptune

## Pre-requisite


gsutil -m cp gs://ldbc_small/sf1.tar.gz .

tar -xf sf1.tar.gz


## Data pre-processing

run pre_data.py

## load data

curl -X POST \
    -H 'Content-Type: application/json' \
    https://database-1-instance-1.clktpl2blcwo.us-east-2.neptune.amazonaws.com:8182/loader -d '
    {
      "source" : "s3://ces-neptune-bucket/new_data/Comment_hasCreator_Person_00002.csv",
      "format" : "opencypher",
      "iamRoleArn" : "arn:aws:iam::966275272565:role/NeptuneLoadFromS3",
      "region" : "us-east-2",
        "mode":"NEW",
      "failOnError" : "FALSE",
      "parallelism" : "MEDIUM",
      "updateSingleCardinalityProperties" : "TRUE",
      "queueRequest" : "TRUE",
        "userProvidedEdgeIds":"False"

    }'
    
    
## run bi query

run bi


