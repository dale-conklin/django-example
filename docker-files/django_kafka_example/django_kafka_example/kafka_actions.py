import kafka

def get_kafka_topics():
    consumer = kafka.KafkaConsumer(group_id='test', bootstrap_servers=['server'])
    consumer.topics()