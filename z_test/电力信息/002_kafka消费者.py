# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from confluent_kafka import Producer, Consumer, KafkaException, KafkaError



def message_handler(msg):
    """
    Callback function to handle consumed messages.
    """
    if msg.error():
        # Error occurred while consuming the message
        print(f"Error: {msg.error()}")
    else:
        # Process the consumed message
        print(f"Received message: {msg.value().decode('utf-8')}")


def consume_kafka_topic(topic):
    """
    Consume messages from a Kafka topic.
    """
    # Kafka consumer configuration
    consumer_config = {
        'bootstrap.servers': '192.168.4.175:9092',
        'group.id': 'my_consumer_group',
        'auto.offset.reset': 'earliest'
    }

    # Create Kafka consumer instance
    consumer = Consumer(consumer_config)

    # Subscribe to the Kafka topic(s)
    consumer.subscribe([topic])

    # Start consuming messages from Kafka
    try:
        while True:
            msg = consumer.poll(1.0)

            if msg is None:
                continue

            if msg.error():
                # Error occurred while consuming the message
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition, continue to the next message
                    continue
                else:
                    # Log the error
                    print(f"Error: {msg.error()}")
                    break

            # Invoke the message handler callback function
            message_handler(msg)

    except KafkaException as e:
        # Handle Kafka-related exceptions
        print(f"KafkaException: {e}")

    except KeyboardInterrupt:
        # User interrupted the consumer
        print("* 键盘停止")
        pass

    finally:
        # Close the Kafka consumer
        consumer.close()


# Example usage: Consume messages from the "my-topic" Kafka topic
consume_kafka_topic('my-topic')
