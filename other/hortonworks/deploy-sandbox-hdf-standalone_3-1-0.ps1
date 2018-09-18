#!/usr/bin/env bash

docker pull hortonworks/sandbox-hdf-standalone:3.1.0
docker run --privileged --name sandbox-hdf-standalone -h sandbox-hdf.hortonworks.com -itd `
-p 1080:1080 `
-p 2181:2181 `
-p 4200:4200 `
-p 4557:4557 `
-p 6080:6080 `
-p 6627:6627 `
-p 6667:6667 `
-p 7777:7777 `
-p 7788:7788 `
-p 8000:8000 `
-p 8080:8080 `
-p 8081:8081 `
-p 8088:8088 `
-p 8090:8090 `
-p 8744:8744 `
-p 8886:8886 `
-p 9088:9088 `
-p 9089:9089 `
-p 9090:9090 `
-p 9091:9091 `
-p 9995:9995 `
-p 16010:16010 `
-p 19888:19888 `
-p 50070:50070 `
-p 61080:61080 `
-p 61888:61888 `
-p 15500-15510:15500-15510 `
-p 2222:22 `
hortonworks/sandbox-hdf-standalone:3.1.0
