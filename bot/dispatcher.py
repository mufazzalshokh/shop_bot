import requests
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

from bot.keyboards import get_menu_keyboard, get_categories_list_keyboard, get_categories_detail_keyboard, \
    get_product_detail_keyboard
from bot.settings import BOT_TOKEN


def start(update, context):
    text = 'Menu'
    update.message.reply_text('Menu', reply_markup=get_menu_keyboard())


def categories_list(update, context):
    query = update.callback_query

    data = requests.get('http://127.0.0.1:8000/categories/').json()

    text = ''
    for category in data:
        text += f'{category["id"]}. {category["title"]}\n'

    query.edit_message_text(text=text, reply_markup=get_categories_list_keyboard(data))


def category_detail(update, context):
    query = update.callback_query
    pk = query.data.split('_')[1]

    data = requests.get(f'http://127.0.0.1:8000/categories/{pk}/').json()

    if not data:
        query.edit_message_text(text='Mo products yet',
                                reply_markup=get_categories_detail_keyboard())
        return

    text = ''
    for product in data:
        text += f'{product["id"]}. {product["title"]}\n'

    query.edit_message_text(text=text, reply_markup=get_categories_detail_keyboard(data))


def product_detail(update, context):
    query = update.callback_query
    pk = query.data.split('_')[1]

    product = requests.get(f'http://127.0.0.1:8000/products/{pk}/').json()

    text = f'Title: {product["title"]}\n' \
           f'Price: {product["price"]}\n' \
           f'Description: {product["description"]}'

    context.bot.send_photo(
        chat_id=query.message.chat.id,
        photo=requests.get(product["image"]).content,
        caption=text,
        reply_markup=get_product_detail_keyboard(product)
    )
    context.bot.delete_message(chat_id=query.message.chat_id,
                               message_id=query.message.message_id)


def search(update, context):
    pass


def back(update, context):
    query = update.callback_query

    context.bot.delete_message(chat_id=query.message.chat_id,
                               message_id=query.message.message_id)

    query.message.reply_text(text='Menu', reply_markup=get_menu_keyboard())


def main():
    updater = Updater(BOT_TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))

    dispatcher.add_handler(CallbackQueryHandler(categories_list, pattern='^categories$'))
    dispatcher.add_handler(CallbackQueryHandler(category_detail, pattern='^category_'))
    dispatcher.add_handler(CallbackQueryHandler(products_detail, pattern='^product_'))
    dispatcher.add_handler(CallbackQueryHandler(back, pattern='^back'))
    dispatcher.add_handler(CallbackQueryHandler(search, pattern='^search$'))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
