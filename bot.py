
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("TOKEN")

def analyze_pattern(results):
    if results[-4:] in (["P", "B", "P", "B"], ["B", "P", "B", "P"]):
        return "📈 เค้าไพ่ปิงปอง ➡ แทงสลับ!"
    elif all(r == results[-1] for r in results[-4:]):
        return "🔥 เค้าไพ่มังกร ➡ แทงตาม!"
    else:
        return "❓ ยังไม่ชัด ลองรอดูอีกนิดครับ"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.upper().replace(" ", "")
    results = list(text)
    if all(r in ["P", "B"] for r in results):
        response = analyze_pattern(results)
    else:
        response = "กรุณาพิมพ์แค่ P และ B เช่น: P B P B"
    await update.message.reply_text(response)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
app.run_polling()
