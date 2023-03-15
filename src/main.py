# encoding: utf-8
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging, os, sys, re, asyncio, time
from config import config

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="ERROR: Message caused bot error."
    )

def start(update, context):
    text = """Instructions:
Submit a completion as an open message (english or finnish) with the format "/<guild> <free message>". Example:
"/as I walked 5kilometers and lit a campfire. I deserve points for this."

Please send some sort of proof for the submissions as either a photo or a video (not required for kilometers travelled). If you want, send some photos to the main group as well to show others what you've done! By sending at least one photo to the group, you'll be listed in a raffle and get a chance to win something amazing! https://t.me/joinchat/NLI5hlZ_0U8zNWJk

If you don't receive a confirmation message for the submission, make sure you typed the command correctly. If you have any problems with the bot, feel free to ask in the general chat linked above.

Commands
/start - Show this help message
/challenges - List the challenges and their points
/rules - Rules
/as <message>- submit a points for AS
/bio <message> - submit a points for Inkubio
"""
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)

def challenges(update, context):
    text = """Challenges:
1. Make a campfire +1
    - Enjoy it for 30 minutes +1
2. Drink hot chocolate outside +1
3. Cook food outside +2
4. Sleep in a sleeping bag or a hammock +1
    - Do this outside +5
5. Build a fort +2
6. Climb a tree +1
7. For every kilometer travelled by foot +1
"""
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)

def rules(update, context):
    text = """Finish as many challenges as you can/want every day and submit them to this bot.

Each challenge is repeatable once a day for the duration of the competition, so you can do the same tasks every day and keep earning points.

For example, if you walk 3 kilometers to a campsite, climb a tree, make a campfire and cook food on it (which takes over 30 minutes), and walk back, you'll earn your guild the following points:
Campfire + 30 minutes on it (1+1)
Cook food outside (+2)
Climb a tree (+1)
Walk 6 kilometers (+6)
Total +11 points.
"""
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)


async def handlePhotoOrVideo(update, context):
    """Handle a photo sent in by user"""
    message = update.message
    messageId = message.message_id
    if not message.photo and len(message.photo) and not message.video:
        context.bot.send_message(
            chat_id=update.effective_chat.id, text="ERROR: no photo or video in message?")
        return

    context.bot.forward_message(
        chat_id=config["forwardId"], from_chat_id=update.effective_chat.id, message_id=messageId)

    context.bot.send_message(
        chat_id=update.effective_chat.id, text="File received")


def getGuildError(update):
    if not update.message:
        return "Please use the format '/<guild> <message>'"

    text = update.message.text
    parts = text.split(" ")
    if len(parts) < 2:
        return "Did you forget the message?"
    return None


def aasi(update, context):
    message = update.message
    messageId = message.message_id
    error = getGuildError(update)
    if error:
        context.bot.send_message(chat_id=update.effective_chat.id, text=error)
        return

    reply = "Submission for AS received!\n\n"
    context.bot.send_message(chat_id=update.effective_chat.id, text=reply)
    context.bot.forward_message(
        chat_id=config["forwardId"], from_chat_id=update.effective_chat.id, message_id=messageId)

    return

def inkubio(update, context):
    message = update.message
    messageId = message.message_id
    error = getGuildError(update)
    if error:
        context.bot.send_message(chat_id=update.effective_chat.id, text=error)
        return

    reply = "Submission for inkubio received!\n\n"
    context.bot.send_message(chat_id=update.effective_chat.id, text=reply)
    context.bot.forward_message(
        chat_id=config["forwardId"], from_chat_id=update.effective_chat.id, message_id=messageId)

    return


async def main():
    """Start the bot."""
    # Create the EventHandler and pass it your bot's token.
    token = config['key']

   # await data.init()

    updater = Updater(token=token)
    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.chat_type.groups, lambda a, b: None)) # ignore group chat messages
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("as", aasi))
    dp.add_handler(CommandHandler("bio", inkubio))
    dp.add_handler(MessageHandler((Filters.video | Filters.photo) & Filters.private,
                                  lambda a, b: asyncio.run(handlePhotoOrVideo(a, b))))
    dp.add_handler(CommandHandler("challenges", challenges))
    dp.add_handler(CommandHandler("rules", rules))
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    asyncio.run(main())
