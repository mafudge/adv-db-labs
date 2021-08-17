FROM jupyter/pyspark-notebook:latest

USER root
RUN apt-get update -y &&  apt-get install -y curl wget
RUN curl https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.11.704/aws-java-sdk-bundle-1.11.704.jar --output /usr/local/spark/jars/aws-java-sdk-bundle-1.11.704.jar
RUN curl https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.1.2/hadoop-aws-3.1.2.jar --output /usr/local/spark/jars/hadoop-aws-3.1.2.jar
RUN sed -i 's/env_reset/env_keep="http_proxy ftp_proxy https_proxy no_proxy"/g' /etc/sudoers
RUN echo 'jovyan    ALL=(ALL:ALL) NOPASSWD:ALL' >> /etc/sudoers
#COPY spark-defaults.conf /usr/local/spark/conf/
RUN mkdir -p /tmp/s3a && mkdir -p /tmp/staging && chmod 777 /tmp
USER jovyan