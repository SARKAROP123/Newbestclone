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
            InlineKeyboardButton(text="❰ 𝗛𝙴֟፝ؖ۬𝙻𝙿 ❱", callback_data="settings_back_helper"),
            InlineKeyboardButton(
                text="❰ 𝐒𝙴𝚃 ❱", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(text="❰ 𝗚𝚁֟፝ؖ۬𝙾𝚄𝙿 ❱", url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="❰𝗚𝚁֟፝ؖ۬𝙾𝚄𝙿❱", url=config.SUPPORT_CHAT),
            InlineKeyboardButton(text="❰𝗠ᴏ֟፝ؖ۬ʀᴇ❱", url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton(text="❰ 𝗙𝙴𝙰𝚃֟፝ؖ۬𝚄𝚁𝙴𝚂 ❱", callback_data="settings_back_helper")
        ],
    ]
    return buttons
                
