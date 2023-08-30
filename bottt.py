import logging
import psutil
import time
import datetime
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Initialize bot and dispatcher
API_TOKEN = '6112396584:AAEPTxKGD89gua70NecvKzJa1XV6S9O0qnw'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
ADMINS = {5933750923}
START_TIME = datetime.datetime.now()


def get_uptime():
    now = datetime.datetime.now()
    uptime = now - START_TIME
    return uptime

# Start command


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user_name = message.from_user.first_name
    caption = (
        f"Hey {user_name}, 🥀\n\n"
        "This is Ariez✘, a fast & powerful Telegram bot with some awesome features.\n\n"
        "Supported Platforms: Telegram\n"
        "──────────────────"
    )
    start_image_url = "https://graph.org/file/c0c0fc2df64eb6e661804.jpg"

    keyboard = InlineKeyboardMarkup(row_width=1)
    button_hub = InlineKeyboardButton("Hub", url="https://t.me/Akimaxmovies_0")
    button_movie = InlineKeyboardButton("Movie", callback_data="movie")
    button_chat = InlineKeyboardButton("Chat", callback_data="chat")
    button_cloud = InlineKeyboardButton("Cloud", callback_data="cloud")
    button_admin = InlineKeyboardButton("Admin", callback_data="admin")

    keyboard.add(button_hub)
    keyboard.row(button_movie, button_chat)
    keyboard.row(button_cloud, button_admin)

    await bot.send_photo(message.chat.id, start_image_url, caption=caption, reply_markup=keyboard)


# Callback handler for main buttons
@dp.callback_query_handler(lambda c: c.data in ['movie', 'chat', 'cloud', 'admin'])
async def main_button_callbacks(callback_query: types.CallbackQuery):
    callback_data = callback_query.data
    user_id = callback_query.from_user.id

    # Check if user is an admin for the 'admin' button
    if callback_data == "admin" and user_id not in ADMINS:
        await bot.answer_callback_query(callback_query.id, "You're not authorized to access this!", show_alert=True)
        return

     # Delete the original message
    await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)

    # Define the sub-buttons, image, and caption based on the pressed main button
    if callback_data == "movie":
        caption = (
            "the list of al the movies channel we have "
        )
        image_url = "https://graph.org/file/a66fa8fe396bd2800cd8b.jpg"
        buttons = [
            InlineKeyboardButton(
                "⚡️AK Imax 2.0⚡️", url="https://t.me/akimax_3"),
            InlineKeyboardButton(
                "Poster Town™ ♨️", url="https://t.me/PosterTown")
        ]
    elif callback_data == "chat":
        caption = (
            "the list of al the chat channel we have "
        )
        image_url = "https://telegra.ph/file/f4f81f79e4ee0010e3728.jpg"
        buttons = [
            InlineKeyboardButton("Hindi English Club 🎧",
                                 url="https://t.me/hin_eng"),
            InlineKeyboardButton("AK Discussion Group 🔥",
                                 url="https://t.me/Ak_Discussion"),
            InlineKeyboardButton("AI Support", callback_data="ai_support")
        ]
    elif callback_data == "cloud":
        caption = (
            "the list of al the movies channel we have "
        )
        image_url = "https://telegra.ph/file/f4f81f79e4ee0010e3728.jpg"
        buttons = [
            InlineKeyboardButton("Ak Imax Cloud ☁️(Updates)",
                                 url="https://t.me/akimaxmovies_2"),
            InlineKeyboardButton("AK Bypass ♻️", url="https://t.me/AKBypass"),
            InlineKeyboardButton("AK Imax Cloud ☁️",
                                 url="https://t.me/AKImaxCloud"),
            InlineKeyboardButton("AK Imax Cloud 18+",
                                 url="https://t.me/+_dVsd2Ejje04Mzdl")
        ]
    elif callback_data == "admin":
        caption = (
            "the list of all the movies channels we have"
        )
        image_url = "https://graph.org/file/9290ef572bd937d4cc93d.jpg"
        buttons = [
            InlineKeyboardButton("Admins⚡️αк-ιмαχ⚡️",
                                 url="https://t.me/+a-pVgLSkIb43Njk1"),
            InlineKeyboardButton("BIG⚡️",
                                 url="https://t.me/+86_tf7xP5bE2N2M1"),
            InlineKeyboardButton("IMAX Support⚡️",
                                 url="https://t.me/akimaxadmin"),
            InlineKeyboardButton("Cam-Rip🍬(Sasti Masti)",
                                 url="https://t.me/+opNj1tZLH-1kN2M9"),
            InlineKeyboardButton("OnGoing Series 📛",
                                 url="https://t.me/+DnFSyvBEXHZmZDJl"),
            InlineKeyboardButton("PREMIUM DATABSE",
                                 url="https://t.me/+snPwIE-ycZViZmE1"),
            InlineKeyboardButton("⚡️AK Movies Collection⚡️",
                                 url="https://t.me/+VM0DrnCpE0tjOWY1"),
            InlineKeyboardButton("⚡️AK Series Collection⚡️",
                                 url="https://t.me/+PSpHr4yD_qU4OGM1"),
            InlineKeyboardButton("Please Join🍿",
                                 url="https://t.me/+7mSo_SLrQKgzMWI1"),
            InlineKeyboardButton("Shehzada Muthbaaz",
                                 url="https://t.me/+hjL-_xJm13JiNTM5"),
            InlineKeyboardButton("Buffer Files⏳",
                                 url="https://t.me/+xv7-wixEIHQ1MGM9"),
            InlineKeyboardButton("Leech Dump 📦",
                                 url="https://t.me/+aYGKv8-0t3Q2MTM1"),
            InlineKeyboardButton("AK MEMBERS LOG 📚",
                                 url="https://t.me/+j3dzt9D0CX05OGQx"),
            InlineKeyboardButton("Soft",
                                 url="https://t.me/+RZf8eXgiyzkzZTI1"),
            InlineKeyboardButton("Red Room",
                                 url="https://t.me/+IP9KrqbfrQg1NzFh"),
            InlineKeyboardButton(
                "AK Mirror Leech", url="https://t.me/+8j_oal4LJj5kNWZl")
        ]

    # Create rows of buttons
    # <-- Set resize_keyboard to True
    keyboard = InlineKeyboardMarkup(resize_keyboard=True)
    button_rows = [buttons[i:i + 2] for i in range(0, len(buttons), 2)]

    # Add button rows to the keyboard
    for row in button_rows:
        keyboard.row(*row)

    # Add the "Back" button
    keyboard.add(InlineKeyboardButton("Back", callback_data="back"))

    # Send the appropriate image with caption and buttons based on the button pressed
    await bot.send_photo(callback_query.message.chat.id, image_url, caption=caption, reply_markup=keyboard)


# Handler for /add command (unchanged)

@dp.message_handler(commands=['add'], user_id=ADMINS)
async def add_admin(message: types.Message):
    try:
        new_admin_id = int(message.text.split()[1])
        ADMINS.add(new_admin_id)
        await message.reply(f"User {new_admin_id} added as an admin!")
    except (IndexError, ValueError):
        await message.reply("Please provide a valid user ID. E.g., /add 123456789")

# Handler for /del command to remove admins


@dp.message_handler(commands=['del'], user_id=ADMINS)
async def remove_admin(message: types.Message):
    try:
        admin_id_to_remove = int(message.text.split()[1])
        if admin_id_to_remove in ADMINS:
            ADMINS.remove(admin_id_to_remove)
            await message.reply(f"User {admin_id_to_remove} removed from admins!")
        else:
            await message.reply(f"User {admin_id_to_remove} is not an admin!")
    except (IndexError, ValueError):
        await message.reply("Please provide a valid user ID. E.g., /del 123456789")


# /stat command handler
@dp.message_handler(commands=['stat'])
async def bot_stats(message: types.Message):
    # Calculate uptime
    uptime = get_uptime()

    # Get CPU usage percentage
    cpu_percent = psutil.cpu_percent(interval=1)

    # Ping
    start = time.time()
    await message.reply("Pong!")
    end = time.time()
    ping_time = round((end - start) * 1000, 2)

    caption = (
        f"Bot Stats\n\n"
        f"Ping: {ping_time} ms\n"
        f"Uptime: {uptime}\n"
        f"CPU Usage: {cpu_percent}%"
    )
    image_url = "https://telegra.ph/file/f4f81f79e4ee0010e3728.jpg"

    keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton("Donation", url="https://telegra.ph/file/84ea28b2c377a4fb41d08.jpg"))

    await bot.send_photo(message.chat.id, image_url, caption=caption, reply_markup=keyboard)

# Donation button callback (unchanged)


@dp.callback_query_handler(lambda c: c.data == 'donation')
async def donation_callback(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.message.chat.id, "Thank you for considering a donation! Your support is greatly appreciated.")


# /about command handler
@dp.message_handler(commands=['about'])
async def about_command(message: types.Message):
    user_name = message.from_user.first_name
    caption = (
        f"Hey {user_name}, 🥀\n\n"
        "We mostly prefer 720p, so don't ask for other qualities. 😄\n"
        "For Support ~ @AkImax_Bot\n"
        "🧡⚡️ Join, Share, Support ⚡️💚\n"
        "🍁 ༺🅣🅗🅐🅝🅚 🅨🅞🅤༻ 🍁\n"
        "🍁 ※ 𝚂𝚒𝚗𝚌𝚎 : 18 July, 2021\n"
        "Some more text like this. Add on your own. Keep it concise."
    )

    start_image_url = "https://telegra.ph/file/84ea28b2c377a4fb41d08.jpg"

    keyboard = InlineKeyboardMarkup(row_width=1)
    admin_list_button = InlineKeyboardButton(
        "Admins", callback_data="admin_list")
    donation_button = InlineKeyboardButton(
        "Donation", url="https://telegra.ph/file/84ea28b2c377a4fb41d08.jpg")

    keyboard.add(admin_list_button, donation_button)

    await bot.send_photo(message.chat.id, start_image_url, caption=caption, reply_markup=keyboard)
    await bot.delete_message(message.chat.id, message.message_id)

# Callback handler for the "Admins" and "Donation" buttons in the /about command


@dp.callback_query_handler(lambda c: c.data in ['admin_list', 'donation'])
async def about_callback_buttons(callback_query: types.CallbackQuery):
    callback_data = callback_query.data

    if callback_data == 'admin_list':
        admin_list_text = "List of Admins:\n\n"
        for admin_id in ADMINS:
            user = await bot.get_chat(admin_id)
            monogram = "".join(part[0].upper()
                               for part in user.first_name.split())
            admin_list_text += f"{user.first_name} (@{user.username}) ({monogram}) - {admin_id}\n"

        back_button = InlineKeyboardButton("Back", callback_data="back")
        keyboard = InlineKeyboardMarkup().add(back_button)

        # Send the new message
        await bot.send_message(callback_query.message.chat.id, admin_list_text, reply_markup=keyboard)

    elif callback_data == 'donation':
        donation_text = "Thank you for considering a donation! Your support is greatly appreciated."
        back_button = InlineKeyboardButton("Back", callback_data="back")
        keyboard = InlineKeyboardMarkup().add(back_button)

        # Send the new message
        await bot.send_message(callback_query.message.chat.id, donation_text, reply_markup=keyboard)

    # Delete the previous /about message
    await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)


@dp.callback_query_handler(lambda c: c.data == 'admin_list')
async def admin_list_callback(callback_query: types.CallbackQuery):
    admin_list_message = "List of Admins:\n\n"

    for admin_id in ADMINS:
        user = await bot.get_chat(admin_id)
        monogram = "".join(part[0].upper() for part in user.first_name.split())
        admin_list_message += f"{user.first_name} (@{user.username}) ({monogram}) - {admin_id}\n"

    back_button = InlineKeyboardMarkup().add(
        InlineKeyboardButton("Back", callback_data="back"))
    admin_list_message += "\nYou can contact these users for admin-related queries."

    await bot.send_message(callback_query.message.chat.id, admin_list_message, reply_markup=back_button)


# /help command handler
# /help command handler
@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    user_name = message.from_user.first_name
    help_text = (
        f"Hey {user_name}, here are the available commands:\n\n"
        "/start - Start using the bot\n"
        "/about - About the bot\n"
        "/help - List of available commands\n"
        "/stat - Bot statistics\n"
        "/add - Add a user as an admin (only for admins)\n"
        "/del - Remove a user from admins (only for admins)"
    )
    image_url = "https://graph.org/file/b397e5dddd21d6495aa38.jpg"
    keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton(
            "Donation", url="https://telegra.ph/file/84ea28b2c377a4fb41d08.jpg")
    )

    await message.reply_photo(image_url, help_text, reply_markup=keyboard)

# Handle "back" callback to show the main menu


@dp.callback_query_handler(lambda c: c.data == 'back')
async def go_back(callback_query: types.CallbackQuery):
    await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
    await send_welcome(callback_query.message)

# Handle sub-button callbacks if needed (e.g., for AI Support, Admin 1, and Admin 2)


@dp.callback_query_handler(lambda c: c.data in ['ai_support', 'admin_1', 'admin_2'])
async def sub_button_callbacks(callback_query: types.CallbackQuery):
    callback_data = callback_query.data

    if callback_data == "ai_support":
        text = "Welcome to AI Support!"
    elif callback_data == "admin_1":
        text = "Welcome to Admin 1!"
    elif callback_data == "admin_2":
        text = "Welcome to Admin 2!"
    else:
        text = "Something went wrong."

    await bot.send_message(callback_query.message.chat.id, text)

    # Send the new page/message
    keyboard = InlineKeyboardMarkup()
    button_back = InlineKeyboardButton("Back", callback_data="back")
    keyboard.add(button_back)
    await bot.send_message(callback_query.message.chat.id, text, reply_markup=keyboard)


if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)

