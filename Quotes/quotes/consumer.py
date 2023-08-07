import json, pika, django
from sys import path
from os import environ

path.append("/home/major/Desktop/designing_microservice/Projects/Quotes")
environ.setdefault("DJANGO_SETTINGS_MODULE", "Quotes.settings")

django.setup()

from quotes.models import Quote

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', heartbeat=600, blocked_connection_timeout=300))
channel = connection.channel()
channel.queue_declare(queue='quotes', durable=True)

def callback(ch, method, properties, body):
    print(body)
    data = json.loads(body)
    print(data)
    
    if properties.content_type == 'quote_liked':
        try:
            quote = Quote.objects.get(id=data)
            quote.likes += 1
            quote.save()
            print("Quote likes increased.")
        except Quote.DoesNotExist:
            print("This quote object does not exist")
        
channel.basic_consume(queue='quotes', on_message_callback=callback)
print("Started consuming...")
channel.start_consuming()
channel.close()