import os
key = os.getenv('key')
token1=os.getenv('token1')
token2=os.getenv('token2')

from Adafruit_IO import Client
aio = Client('onlyhuman143',f'{key}') 







from telegram.ext import Updater, MessageHandler, Filters




def demo1(bot,update):
  chat_id = bot.message.chat_id
  bot.message.reply_text('turning on light')
  aio.send('light',1)
  
def demo2(bot,update):
  chat_id = bot.message.chat_id
  bot.message.reply_text('turning off light')
  aio.send('light',0)

def demo3(bot,update):
  chat_id = bot.message.chat_id
  bot.message.reply_text('turning on fan')
  aio.send('fan',1)

def demo4(bot,update):
  chat_id = bot.message.chat_id
  bot.message.reply_text('turning off fan')
  aio.send('fan',0)

def main(bot,update):
  a= bot.message.text.lower()
  if a =="turn on light":
    demo1(bot,update)
  elif a =="turn off light":
    demo2(bot,update)
  elif a =="turn on fan":
    demo3(bot,update)
  elif a =="turn off fan":
    demo4(bot,update)

bot_token = f'{token1}:{token2}'
u = Updater(bot_token,use_context=True)
dp = u.dispatcher
dp.add_handler(MessageHandler(Filters.text,main))
u.start_polling()
u.idle() 

      
