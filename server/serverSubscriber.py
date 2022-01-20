import pika
import yaml


def getCredentials():
    credentials = yaml.safe_load(open('./client/credentials.yaml'))
    user = credentials['user']
    pwd = credentials['pwd']
    return user, pwd


def run():
    user, pwd = getCredentials()
    credentials = pika.PlainCredentials(user, pwd)
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='stingray.rmq.cloudamqp.com', credentials=credentials, virtual_host='akdjroei'))  # Connect to CloudAMQP
    channel = connection.channel()  # start a channel
    channel.queue_declare(queue='test')

    def callback(ch, method, properties, body):
        print("Received %r" % body)

    channel.basic_consume(
        queue='test', on_message_callback=callback, auto_ack=True)

    print('Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


run()
