import boto3

messages = queue.receive_messages(QueueUrl=url_queue, AttributeNames=['All'], MessageAttributeNames=['All'], MaxNumberOfMessages=10) # adjust MaxNumberOfMessages if needed
#if 'Messages' in messages: # when the queue is exhausted, the response dict contains no 'Messages' key
print("Longitud de mensajes" , len(messages))
for message in messages: # 'Messages' is a list
# process the messages
    #print(message)
    print(message.body)
    #print(message.queue_url)
    #print(message.attributes)
    #print(message.message_attributes)
    #print(message.message_attributes['Author'])
    print(message.message_attributes['archivo_original']['StringValue'])
    print(message.message_attributes['id_audio']['StringValue'])
    #print(message.receipt_handle)
    #message.delete()
# next, we delete the message from the queue so no one else will process it again
    #queue.delete_messages(QueueUrl=url_queue)
#else:
#print('Queue is now empty')
