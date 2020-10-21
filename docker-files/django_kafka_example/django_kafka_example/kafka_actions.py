import kafka
from kafka.admin import KafkaAdminClient, NewTopic

KAFKA_SERVER = 'kafka-svr:9092'

class k_consumer(kafka.KafkaConsumer):
    def __init__(self):
        self.bootstrap_servers = [KAFKA_SERVER]

        super().__init__()

def get_kafka_topics():
    consumer = kafka.KafkaConsumer(bootstrap_servers=[KAFKA_SERVER])

    return consumer.topics()

def create_kafka_topic(new_topic: str):
    if len(new_topic) > 0:
        admin_client = KafkaAdminClient(bootstrap_servers=[KAFKA_SERVER])
        topic_list = []
        topic_list.append(NewTopic(name=f"{new_topic}", num_partitions=1, replication_factor=1))
        admin_client.create_topics(new_topics=topic_list, validate_only=False)
        return True

    return False
    