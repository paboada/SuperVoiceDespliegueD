import boto3
import os
import pydub
import glob
import shutil
import smtplib
import time

print("Inicio de la Ejecucion de batchMP3.py adaptado para sqs")
print(time.strftime("%d/%m/%y %H:%M:%S"))

#variables de entorno produccion
user_db = os.environ["RDS_USERNAME"]
pass_db = os.environ["RDS_PASSWORD"]
host_db = os.environ["RDS_HOSTNAME"]
name_db = os.environ["RDS_DB_NAME"]
email_host=os.environ["SES_EMAIL_HOST"]
email_port=os.environ["SES_EMAIL_PORT"]
email_user=os.environ["SES_EMAIL_HOST_USER"]
email_pass=os.environ["SES_EMAIL_HOST_PASSWORD"]

#variables de entorno DESARROLLO
#Prueba de correo
#email_host = 'smtp.gmail.com'
#email_user = 'supervoices.cloud@gmail.com'
#email_port = 587
#email_pass = ''

#rutas DESARROLLO
#path_media = 'D:/01_ESTUDIOS/MAESTRIA/4_APLICACIONES_CLOUD/Proyecto_1_to_mp3/media/'
#path_procesados = 'D:/01_ESTUDIOS/MAESTRIA/4_APLICACIONES_CLOUD/Proyecto_1_to_mp3/procesados/'

#rutas PRODUCCION
path_media = '/home/ubuntu/media/'
path_procesados = '/home/ubuntu/media/procesados/'



# Create SQS client
sqs = boto3.resource('sqs')
# Get the queue. This returns an SQS.Queue instance
queue = sqs.get_queue_by_name(QueueName='sqs_concursos')
url_queue=queue.url

cont = 0
while cont<10:
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
        print("-------------------------------------------------------------")
        print("Convirtiendo archivos WAV a MP3")
        print("-------------------------------------------------------------")
        archivo = message.message_attributes['archivo_original']['StringValue']
        print("Archivo WAV en conversion: ", archivo)
        msplit = archivo.split(".")
        mp3_file = msplit[0] + '.mp3'
        wav_file = path_media+archivo
        sound = pydub.AudioSegment.from_wav(wav_file)
        sound.export(mp3_file, format= "mp3")
        shutil.move(mp3_file, path_media)
        shutil.move(wav_file, path_procesados )
    cont=cont+1
    #print(message.receipt_handle)
    #message.delete()
# next, we delete the message from the queue so no one else will process it again
    #queue.delete_messages(QueueUrl=url_queue)
#else:
#print('Queue is now empty')
