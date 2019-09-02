# -*- coding: <UTF-8> -*-
import telebot
import os
import io
from google.cloud import vision

TOKEN_TELEGRAM = "TOKEN_HERE" #Preencha com o token fornecido pelo BotFather
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "GOOGLE_CREDENTIAL_HERE" #Preencha com a credencial fo
bot = telebot.TeleBot(TOKEN_TELEGRAM)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Estou pronto, Basta me enviar a foto que deseja obter o texto!")

@bot.message_handler(content_types=['text', "sticker", 'document', 'audio'])
def received_photo(message):
	bot.reply_to(message, "Me envie uma foto!")

@bot.message_handler(content_types=['photo'])
def received_photo(message):

	photo_message = message.photo[0].file_id
	path = photo_message+".jpg"
	
	file_info = bot.get_file(photo_message)
	downloaded_file = bot.download_file(file_info.file_path)
	
	with open(path,'wb') as new_file:
    		new_file.write(downloaded_file)

    	client = vision.ImageAnnotatorClient()

    	with io.open(path, 'rb') as image_file:
        		content = image_file.read()

    	image = vision.types.Image(content=content)

    	response = client.text_detection(image=image)
    	texts = response.text_annotations

    	texto = ''
    	index = 0
    	for text in texts:
    		if index == 0:
    			texto += text.description
    		index += 1
        bot.reply_to(message, texto)        

bot.polling()
