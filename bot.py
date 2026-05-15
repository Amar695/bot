from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8986634546:AAEkQPfXg7GqnlEosedQuJt3v8SF88XDIB4"

IMAGES = [
    "https://i.ibb.co/cc0M4CpX/IMG-20260515-210347-760.jpg",
    "https://i.ibb.co/WW6WjpFF/IMG-20260515-201220-071.jpg",
    "https://i.ibb.co/WZfydVg/IMG-20260515-210347-859.jpg",
    "https://i.ibb.co/mf6Vm9X/IMG-20260515-210348-093.jpg"
]

INFO_TEXT = """أولا عليك تحديث تليجرام الأصلي الى آخر إصدار!

طريقة ربط البوت بحسابك:
• إتجه الى: 1- الملف الشخصي 2- تعديل البيانات 3- المحادثات الآلية 4- اكتب يوزر البوت واضغط إضافة وأعطه صلاحية إدارة الرسائل
• إذا كنت مشترك في تليجرام المميز: اذهب الى الإعدادات ثم تليجرام الأعمال ثم بوتات المحادثة وأضف البوت
• بمجرد ربط البوت أي رسالة يتم حذفها أو تعديلها يعاد إرسالها لك

ملاحظة: الميزة رسمية من تليجرام وآمنة ولا يمكن للبوت الوصول لبياناتك
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📌 المعلومات", callback_data="info")],
        [InlineKeyboardButton("❓ Help", callback_data="help")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("أهلاً 👋 اختر خيار:", reply_markup=reply_markup)


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "info":
        media = [InputMediaPhoto(img) for img in IMAGES]

        await context.bot.send_media_group(
            chat_id=query.message.chat_id,
            media=media
        )

        await context.bot.send_message(
            chat_id=query.message.chat_id,
            text=INFO_TEXT
        )

    elif query.data == "help":
        await context.bot.send_message(
            chat_id=query.message.chat_id,
            text="راسل المطور: @CC_NN5"
        )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
