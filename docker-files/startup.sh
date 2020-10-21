#!/bin/bash

/opt/kafka-2.6.0-src/bin/zookeeper-server-start.sh config/zookeeper.properties &
/opt/kafka-2.6.0-src/bin/kafka-server-start.sh config/server.properties &