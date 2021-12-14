from pyrogram import Client
import access_creds
from pyrogram.errors.exceptions.bad_request_400 import PeerIdInvalid, UsernameInvalid, UsernameNotOccupied, ChatAdminRequired
from pyrogram.errors.exceptions.flood_420 import FloodWait 

app = Client(session_name='my_session', api_id=access_creds.api_id, api_hash=access_creds.api_hash)

def Chat_info():
    chat_info = input("Enter correct numeric chat ID or chat username or chat link in 't.me/joinchat/454535yrf2 format': ")
    try:
        with app:
            json_object = app.get_chat(chat_info)
        print('\033[1;90mGetting information...\n\033[1;00m')
    except (KeyError, UsernameInvalid, UsernameNotOccupied):
        print("\033[1;91mNot correct input!\033[1;00m")
    try:
        with app:
            print('\033[1;96mtitle\033[1;00m:', json_object.title)
            print('\033[1;96mid\033[1;00m:', json_object.id)
            print('\033[1;96mtype\033[1;00m:', json_object.type)
            print('\033[1;96mis verified\033[1;00m:', json_object.is_verified)
            print('\033[1;96mis restricted\033[1;00m:', json_object.is_restricted)
            print('\033[1;96mis scam\033[1;00m:', json_object.is_scam)
            print('\033[1;96mis fake\033[1;00m:', json_object.is_fake)
            print('\033[1;96musername\033[1;00m:', json_object.username)
            print('\033[1;96mdescription\033[1;00m:', json_object.description)
            print('\033[1;96minvite link\033[1;00m:', json_object.invite_link)
            print('\033[1;96mmembers count\033[1;00m:', json_object.members_count)
            print('\033[1;96mlinked chat\033[1;00m =>')
            print('               \033[1;96mtitle\033[1;00m:', json_object.linked_chat.title)
            print('               \033[1;96mid\033[1;00m:', json_object.linked_chat.id)
            print('               \033[1;96mtype\033[1;00m:', json_object.linked_chat.type)
            print('               \033[1;96mis verified\033[1;00m:', json_object.linked_chat.is_verified)
            print('               \033[1;96mis restricted\033[1;00m:', json_object.linked_chat.is_restricted)
            print('               \033[1;96mis scam\033[1;00m:', json_object.linked_chat.is_scam)
            print('               \033[1;96mis fake\033[1;00m:', json_object.linked_chat.is_fake)
            print('               \033[1;96musername\033[1;00m:', json_object.linked_chat.username)
            print('               \033[1;96mdescription\033[1;00m:', json_object.linked_chat.description)
            print('               \033[1;96minvite link\033[1;00m:', json_object.linked_chat.invite_link)
            print('               \033[1;96mmembers count\033[1;00m:', json_object.linked_chat.members_count)
    except UnboundLocalError:
        pass
    except ChatAdminRequired:
        print('\033[1;93mChat Admin permissions required!\033[1;00m')
    except FloodWait:
        print('\033[1;93m\nOne should wait a moments and try again later.\033[1;00m')
    except AttributeError:
        pass
    except (PeerIdInvalid, UsernameInvalid, UsernameNotOccupied, IndexError):
        print("\033[1;91mNot correct input!\033[1;00m")
