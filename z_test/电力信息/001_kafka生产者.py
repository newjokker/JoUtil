# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import time
from JoTools.utils.TimeUtil import TimeUtil
from confluent_kafka import Producer, Consumer, KafkaException

# Create a Kafka producer configuration
producer_config = {
    'bootstrap.servers': '192.168.4.175:9092',  # Kafka broker(s) address
    'client.id': 'my_producer'  # Client ID for the producer
}

# Create the Kafka producer instance
producer = Producer(producer_config)

# Produce a message to a specific Kafka topic
topic = 'my-topic'

for i in range(100):

    message = f'Hello, Kafka! {TimeUtil.get_time_str()}'

    print(message)

    producer.produce(topic, value=message.encode('utf-8'))

    # Flush the producer to ensure the message is sent to Kafka
    producer.flush()

    time.sleep(1)


