FROM alpine:3

RUN apk update && apk upgrade && apk add bash && apk add curl && apk add openjdk11
COPY ./kafka-2.6.0-src.tgz /opt
COPY ./startup.sh /

WORKDIR /opt
RUN tar -xzf kafka-2.6.0-src.tgz
WORKDIR /opt/kafka-2.6.0-src

RUN ./gradlew jar -PscalaVersion=2.13.2

EXPOSE 2181 2888 3888 9092

CMD ["./startup.sh"]

