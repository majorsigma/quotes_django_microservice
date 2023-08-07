import json, pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', heartbeat=600, blocked_connection_timeout=300))
channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    if channel.is_open:
        channel.basic_publish(exchange='', routing_key='quotes', body=json.dumps(body), properties=properties)
    else:
        channel.close()