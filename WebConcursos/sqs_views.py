import boto3

def sqs_registrar_mensaje(id_audio, archivo_original):
    # Create SQS client
    sqs = boto3.resource('sqs')
    queue = sqs.get_queue_by_name(QueueName='sqs_concursos')
    url_queue=queue.url
    # Create a new message
    response = queue.send_message(MessageBody='Registrando Mensaje',
                                  MessageAttributes={
                                                        'id_audio': {
                                                                    'Value': id_audio,
                                                                    'DataType': 'Number'
                                                                    },
                                                        'archivo_original': {
                                                                    'StringValue': archivo_original,
                                                                    'DataType': 'String'
                                                                    }
                                                    })
    print(response.get('MessageId'))
    print(response.get('MD5OfMessageBody'))
