import telebot, random, os, string, requests
TOKEN = os.environ.get("BOT_TOKEN")
DB = "https://naija-gem-game-default-rtdb.firebaseio.com/validCodes"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(m.chat.id, "🎮 Welcome! Pay ₦10 to OPay 08147758703 then type /getcode")

@bot.message_handler(commands=['getcode'])
def gen(m):
    code = "GEM" + str(random.randint(1000,9999)) + random.choice(string.ascii_uppercase)
    try:
        requests.put(f"{DB}/{code}.json", json={"used": False})
    except:
        pass
    bot.send_message(m.chat.id, f"✅ Your Code: {code}")

bot.infinity_polling()
