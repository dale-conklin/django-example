FROM alpine:3

RUN apk update && apk upgrade && apk add bash && apk add curl && apk add openjdk11
COPY ./kafka-2.6.0-src.tgz /opt

WORKDIR /opt
RUN tar -xzf kafka-2.6.0-src.tgz
WORKDIR /opt/kafka-2.6.0-src

RUN ./gradlew jar -PscalaVersion=2.13.2

EXPOSE 9092
RUN rm -rf /opt/kafka-2.6.0-src/config

COPY ./startup.sh /

CMD ["/startup.sh"]

