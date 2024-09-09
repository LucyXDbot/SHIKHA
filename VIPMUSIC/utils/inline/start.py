from pyrogram.types import InlineKeyboardButton

import config
from VIPMUSIC import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
        ],
        [
            InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ", url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀᴛ",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ", url=config.SUPPORT_CHAT),
            InlineKeyboardButton(text="ᴜᴘᴅᴀᴛᴇ", url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton(
                text="𝖧𝖾𝗅𝗉 𝖠𝗇𝖽 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌", callback_data="settings_back_helper"
            )
        ],
    ]
    return buttons
