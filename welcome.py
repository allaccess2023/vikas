from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

def welcome(update: Update, context: CallbackContext) -> None:
    new_members = update.message.new_chat_members
    chat_id = update.message.chat_id

    if chat_id == <group id>:  # Replace with your group ID
        for member in new_members:
            welcome_msg = f"Welcome {member.first_name} to the group! Please read the rules and enjoy your stay."
            context.bot.send_message(chat_id=chat_id, text=welcome_msg)

def main() -> None:
    # Create the Updater and pass your bot's token here
    updater = Updater("token")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register the welcome function to handle new members joining
    dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, welcome))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you send a stop command (Ctrl+C)
    updater.idle()

if __name__ == '__main__':
    main()
