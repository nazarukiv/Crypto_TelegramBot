from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


keyboard_education = InlineKeyboardMarkup(row_width=1)


keyboard_education.add(
        InlineKeyboardButton("Cryptocurrency Engineering and Design", url="https://youtube.com/playlist?list=PLUl4u3cNGP61KHzhg3JIJdK08JLSlcLId&si=p4HNZPEUf8XGkZbN", callback_data="mit1"),
        InlineKeyboardButton("Blockchain and Money", url="https://youtube.com/playlist?list=PLUl4u3cNGP63UUkfL0onkxF6MYgVa04Fn&si=jxI7uLEfBOBvgHjV", callback_data="mit2"),
        InlineKeyboardButton("The Complete Beginner's Crypto Crash Course", url="https://youtube.com/playlist?list=PLU52pNodXIGdM6XDgHVG7DsPytlsrR_6b&si=F4ee5xIQrW7lEaSg", callback_data="course3"),
    )


keyboard_education_tech_analysis = InlineKeyboardMarkup(row_width=1)


keyboard_education_tech_analysis.add(
        InlineKeyboardButton("Technical Analysis For Beginners", url="https://youtu.be/evAJW38orgM?si=t1cMNcLlG3UPTdOP"),
        InlineKeyboardButton("Technical Analysis Series", url="https://youtube.com/playlist?list=PLvkpxFSTppmnQ7A5DP386zEKU0Tv_fatm&si=ejtNkcLC4CAtPouu"),
        InlineKeyboardButton("What is technical analysis?", url="https://www.theblock.co/learn/286336/what-is-technical-analysis-for-crypto-trading"),
    )
