#!/bin/bash

/opt/kafka-2.6.0-src/bin/zookeeper-server-start.sh /opt/kafka-2.6.0-src/config/zookeeper.properties &
sleep 10
/opt/kafka-2.6.0-src/bin/kafka-server-start.sh /opt/kafka-2.6.0-src/config/server.properties