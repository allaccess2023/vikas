import requests
import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

base_url = "https://api.telegram.org/bot<token>"

def welcome(update: Update, context: CallbackContext) -> None:
    new_members = update.message.new_chat_members
    chat_id = update.message.chat_id

    if chat_id == <group id>:   # Replace with your group ID
        for member in new_members:
            welcome_msg = f"Welcome {member.first_name} to the group! Please read the rules and enjoy your stay."
            context.bot.send_message(chat_id=chat_id, text=welcome_msg)

def read_message(offset):
    parameters = {
        "offset": offset
    }

    response = requests.get(base_url + "/getUpdates", data=parameters)
    data = response.json()

    for result in data["result"]:
        if "message" in result and "text" in result["message"]:
            message_text = result["message"]["text"].lower()
            message_id = result["message"]["message_id"]

            if "hello" in message_text:
                send_message(message_id, "hello back")
            # this one below is used for exact messages ==
            elif message_text == "hi":
                send_message(message_id, "hello back")
            elif message_text == "bye":
                send_message(message_id, "see you later")
            elif "menu" in message_text:
                send_message(message_id, "Hi there I'm a Herbalife Universe bot created to assist \nType the text in *bold* for the corresponding information:\n\n"
                                         "*products* \~ Herbalife product information and where purchase\n"
                                         "*contact* \~ provides a list of the Herbalife distributors\n"
                                         "*menu* \~ displays this command list menu\n"
                                         "*rules* \~ displays group rules\n"
                                         "*transformation* \~ Displays recent transformation pictures\n\n"
                                         "Experience the transformative power of Herbalife and unleash your true potential "
                                         "We are committed to supporting your journey towards a healthier happier you",
                             parse_mode="MarkdownV2")
            elif "products" in message_text:
                send_message(message_id, "For product information visit: https://buyherbal.online")
            elif "website" in message_text:
                send_message(message_id, "Here is our website: https://buyherbal.online")
            elif "url" in message_text:
                send_message(message_id, "Here is our website: https://buyherbal.online")
            elif "how are you" in message_text:
                send_message(message_id, "I'm doing well, thanks for asking.")
            elif "what is your name" in message_text:
                send_message(message_id, "My name is: Herbalife Information Assistant.")
            elif "what can you do" in message_text:
                send_message(message_id,
                             "I can generate text, translate languages, write different kinds of creative content, "
                             "and answer your questions in an informative way.")
            elif "tell me a joke" in message_text:
                send_message(message_id, "What do you call a fish wearing a suit? Sofishticated!")
            elif "tell me a story" in message_text:
                send_message(message_id,
                             "Once upon a time, there was a little girl named Alice who fell down a rabbit hole and "
                             "into a magical world called Wonderland.")
            elif "sing me a song" in message_text:
                send_message(message_id,
                             "Twinkle, twinkle, little star,\n How I wonder what you are! \nUp above the world so high.")
            elif "transformation" in message_text:
                send_file(message_id, r"c:\Users\europ\Downloads\twoleaves.png")
            elif "who is christina" in message_text:
                send_message(message_id,
                             "She is a wonderful *Herbalife distributor* who provides a wide range of health and wellness information",
                             parse_mode="MarkdownV2")
            else:
                pass
                # send_message(message_id, "I'm sorry, I didn't understand your message. Please try again.")

    if data["result"]:
        return data["result"][-1]["update_id"] + 1
def send_file(message_id, file_path):
    file = {'photo': open(file_path, 'rb')}
    data = {
        'chat_id': "-1001892717573",
        'reply_to_message_id': message_id
    }
    response = requests.post(base_url + "/sendPhoto", data=data, files=file)
    print(response.text)

def send_message(message_id, text, parse_mode=None):
    parameters = {
        'chat_id': "<group id",
        'text': text,
        'reply_to_message_id': message_id
    }
    if parse_mode:
        parameters["parse_mode"] = parse_mode

    response = requests.get(base_url + "/sendMessage", data=parameters)
    print(response.text)

offset = 0

while True:
    offset = read_message(offset)

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
