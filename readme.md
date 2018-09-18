# Readme

## SQL Server

`cd mssql`

Starting SQL Server

`mssql> docker-compose up -d`

Access with SQL Management studio on `localhost:1433`

Installing fudgemart_v3  
`create database fudgemart_v3`
Download [https://raw.githubusercontent.com/mafudge/datasets/master/fudgemart/mssql.sql](https://raw.githubusercontent.com/mafudge/datasets/master/fudgemart/mssql.sql)  
Open in MSSQL and run the SQL file

Stopping SQL Server, so you don't lose data.

`mssql> docker-compose stop`

Stopping SQL Server, Full tear-down

`mssql> docker-compose down -v`


## Cloudera Hadoop

`cd hadoop`

Starting Hadoop

`docker-compose up -d`

Hue is at http://localhost:8888
User: cloudera / Pass: cloudera


Shell access:

`docker-compose exec cloudera /bin/bash`

Stopping hadoop, so you don't lose data!

`docker-compose stop`

Stopping hadoop. This is a complete tear-down.

`docker-compose down -v`

Cloudera Manager

`/home/cloudera/cloudera-manager --express`
Located at http://localhost:7180
User: cloudera / Pass: cloudera

## Mongo DB

`cd mongodb`

Starting Mongo DB

`docker-compose up -d`

Access the mongo client

`docker-compose exec mongo mongo -u admin -p pass --authenticationDatabase=admin`

Import the example

`docker-compose exec mongo mongoimport -u admin -p pass --authenticationDatabase=admin -d demo -c countries --file=europe.json --jsonArray`

Stopping mongo - won't lose data.

`docker-compose stop`

Full Tear-Down

`docker-compose down`


## Redis

`cd redis`

Starting Redis

`docker-compose up -d`

Accessing the client

`docker-compose exec redis redis-cli`

Full teardown
`docker-compose down`

## Cassandra

`cd cassandra`

Starting Cassandra 

`docker-compose up -d`

Stopping Cassandra, keep data.

`docker-compose stop`

Stopping Cassandra, full tear-down

`docker-compose down`

Accessing Cassandra CQL shell

`docker-compose exec cassandra0 cqlsh`

## Kafka (Confluent)

`cd kafka`

Start Confluent Kafka

`kafka> docker-compose up -d`

Shell Access To the Broker

`kafka> docker-compose exec broker /bin/bash`

From the Kafka Broker, list topics:
`$ kafka-topics --list --zookeeper zookeeper:2181`

Shell Access to KSQL
`kafka> docker-compose exec ksql-cli ksql http://ksql-server:8088`

From KSQL
`ksql> show topics;`

## Drill

`cd drill`

Starting Drill

`docker-compose up -d`

admin UI is on http://localhost:8047

Starting Drill Console

`docker-compose exec apache-drill drill-conf`
