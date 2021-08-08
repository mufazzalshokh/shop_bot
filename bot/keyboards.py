from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def get_menu_keyboard():
    keyboard = [
        [
            InlineKeyboardButton('Categories', callback_data='categories'),
        ],
        [
            InlineKeyboardButton('Search', callback_data='search')
        ],
    ]

    return InlineKeyboardMarkup(keyboard)


def get_categories_list_keyboard(data):
    keyboard = []
    temp = []

    for i in data:
        temp.append(
            InlineKeyboardButton(i["id"], callback_data=f'category_{i["id"]}'),
        )
    keyboard.append(temp)


    keyboard.append(
        [
            InlineKeyboardButton('Back', callback_data='back'),
        ]

    )

    return InlineKeyboardMarkup(keyboard)



def get_categories_detail_keyboard(data=None):
    keyboard = []
    if data:
        temp = []

        for i in data:
            temp.append(
                InlineKeyboardButton(i["id"], callback_data=f'product_{i["id"]}'),
            )
        keyboard.append(temp)


    keyboard.append(
        [
            InlineKeyboardButton('Back', callback_data='back'),
        ]

    )

    return InlineKeyboardMarkup(keyboard)



def get_product_detail_keyboard(product):
    keyboard = [
        # [
        #     InlineKeyboardButton('Back', callback_data='back'),
        # ],
        [
            InlineKeyboardButton('Back', callback_data='back'),
        ],
    ]

    return InlineKeyboardMarkup(keyboard)







