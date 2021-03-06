import kafka
import json
from kafka.admin import KafkaAdminClient, NewTopic

KAFKA_SERVER = 'kafka-svr:9092'
CLIENT_ID='dale-id'

class k_consumer(kafka.KafkaConsumer):
    def __init__(self):
        self.bootstrap_servers = [KAFKA_SERVER]

        super().__init__()

def get_kafka_topics():
    consumer = kafka.KafkaConsumer(client_id=CLIENT_ID, bootstrap_servers=[KAFKA_SERVER])

    return consumer.topics()

def create_kafka_topic(new_topic: str):
    if len(new_topic) > 0:
        admin_client = KafkaAdminClient(client_id=CLIENT_ID, bootstrap_servers=[KAFKA_SERVER])
        topic_list = []
        topic_list.append(NewTopic(name=f"{new_topic}", num_partitions=1, replication_factor=1))
        admin_client.create_topics(new_topics=topic_list, validate_only=False)
        return True

    return False

def get_kafka_events(topic: str):
    consumer = kafka.KafkaConsumer(client_id=CLIENT_ID,
                                   bootstrap_servers=[KAFKA_SERVER],
                                   auto_offset_reset='earliest',
                                   value_deserializer=lambda m: m.decode('utf-8'),
                                   consumer_timeout_ms=1000)
    mypartition = kafka.TopicPartition(topic, 0)
    consumer.assign([mypartition])
    consumer.seek_to_beginning(mypartition)
    msgs = []
    for msg in consumer:
        msgs.append(msg.value)
    
    return msgs

def produce_kafka_event(topic: str, event: str):
    producer = kafka.KafkaProducer(client_id=CLIENT_ID, bootstrap_servers=[KAFKA_SERVER])
    producer.send(topic, bytes(event, encoding='utf-8'))
    producer.close()
    
    return
