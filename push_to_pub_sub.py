import json
import os

os.environ['GOOGLE_CLOUD_DISABLE_GRPC'] = 'true'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'creds.json'
if os.environ.get('PUBSUB_EMULATOR_HOST'):
    del os.environ['PUBSUB_EMULATOR_HOST']
from gcloud import pubsub 

pubsub_client = pubsub.Client()
payments_topic = pubsub_client.topic('MyTopic')

def publish_message(data):
    data = json.dumps(data)
    data = data.encode('utf-8')
    print 'before pushing'
    message_id = payments_topic.publish(data)
    print('Message '+repr(message_id)+'published.')


def process_order_aync(data):
    publish_message(data)

process_order_aync({'amount': 10})
