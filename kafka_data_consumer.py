from confluent_kafka import Consumer, KafkaException
import sys
import json

def create_consumer(config):
    return Consumer(config)

def consume_messages(consumer, topics):
    try:
        consumer.subscribe(topics)

        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaException._PARTITION_EOF:
                    # End of partition event
                    sys.stderr.write(f'{msg.topic()} [{msg.partition()}] reached end at offset {msg.offset()}\n')
                elif msg.error():
                    raise KafkaException(msg.error())
            else:
                print(f"Received message: {msg.value().decode('utf-8')}")
    finally:
        consumer.close()

# Kafka configuration
config = {
    'bootstrap.servers': 'localhost:9092', # Change as per your server configuration
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest'
}

# Creating a Kafka consumer instance
consumer = create_consumer(config)

# Consuming messages from the 'rawdata' topic
consume_messages(consumer, ['rawdata'])

