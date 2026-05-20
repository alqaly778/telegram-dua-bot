import random
import time
from telegram import Bot

TOKEN = "@daily_dua_channel"
CHANNEL_ID = "@اسم_القناة"

bot = Bot(token=TOKEN)

duas = [
    "اللهم اغفر لنا وارحمنا واهدنا وعافنا وارزقنا.",
    "اللهم اجعل القرآن ربيع قلوبنا.",
    "ربنا آتنا في الدنيا حسنة وفي الآخرة حسنة وقنا عذاب النار.",
    "اللهم فرج هم المهمومين واشف مرضانا ومرضى المسلمين.",
    "اللهم ارزقنا الطمأنينة وراحة البال.",
    "اللهم اكتب لنا الخير حيث كان.",
    "اللهم ارزقنا الجنة وما قرب إليها من قول وعمل.",
    "اللهم صل وسلم على نبينا محمد."
]

while True:
    dua = random.choice(duas)

    bot.send_message(
        chat_id=CHANNEL_ID,
        text=dua
    )

    print("تم نشر دعاء")

    time.sleep(3600)
