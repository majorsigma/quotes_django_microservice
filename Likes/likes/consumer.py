import json, pika, django
from sys import path
from os import environ

path.append('/home/major/Desktop/designing_microservice/Projects/Likes')

environ.setdefault('DJANGO_SETTINGS_MODULE', 'Likes.settings')
print("Django Settings: %s" % environ.get('DJANGO_SETTINGS_MODULE'))

django.setup()

from likes.models import Quote

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', heartbeat=600, blocked_connection_timeout=300))
channel = connection.channel()
channel.queue_declare(queue='likes')


def callback(ch, method, properties, body):
    print("Received in likes...")
    print(body)
    data = json.loads(body)
    print("Data: %s" % data)
    
    if properties.content_type == 'quote_created':
        quote = Quote.objects.create(id=data['id'], title=data['title'])
        quote.save()
        print('Quote created: %s' % quote.title)
        
    elif properties.content_type == 'quote_updated':
        quote = Quote.objects.get(id=data['id'])
        quote.title = data['title']
        quote.save()
        print('quote updated')
        
    elif properties.content_type == 'quote_deleted':
        print("Data of delete event: %s" % data)
        quote = Quote.objects.get(id=data)
        quote.delete()
        print('qoute deleted')
    
channel.basic_consume(queue='likes', on_message_callback=callback, auto_ack=True)
print("Started Consuming...")
channel.start_consuming()