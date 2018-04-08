import boto3

# Create SQS client
sqs = boto3.resource('sqs')
# Get the queue. This returns an SQS.Queue instance
queue = sqs.get_queue_by_name(QueueName='sqs_concursos')
url_queue=queue.url

cont = 0
while True:
    messages = queue.receive_messages(QueueUrl=url_queue, AttributeNames=['All'], MessageAttributeNames=['All'], MaxNumberOfMessages=10) # adjust MaxNumberOfMessages if needed
    #if 'Messages' in messages: # when the queue is exhausted, the response dict contains no 'Messages' key
    print("Longitud de mensajes" , len(messages))
    for message in messages: # 'Messages' is a list
    # process the messages
    #print(message)
    #print(message.body)
    #print(message.queue_url)
    #print(message.attributes)
    #print(message.message_attributes)
        print(message.message_attributes['archivo_original']['StringValue'])
        print(message.message_attributes['id_audio']['StringValue'])
        cont = cont + 1
        if cont == 10:
            break
    #print(message.receipt_handle)
    #message.delete()
# next, we delete the message from the queue so no one else will process it again
    #queue.delete_messages(QueueUrl=url_queue)
#else:
#print('Queue is now empty')
