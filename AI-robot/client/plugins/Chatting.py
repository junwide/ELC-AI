# -*- coding: utf-8-*-
# 闲聊插件

try:
    reload         # Python 2
except NameError:  # Python 3
    from importlib import reload

import sys
reload(sys)
sys.setdefaultencoding('utf8')

# Standard module stuff
WORDS = ["XIANLIAO",u"LIAOTIAN"]
SLUG = "chatting"


def handle(text, mic, profile, wxbot=None):
    """
    Responds to user-input, typically speech text

    Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
        wxbot -- wechat bot instance
    """
    if not any(word in text for word in [u"结束", u"停止", u"退出", u"不聊了"]):
        mic.say(u"那我就变身话痨啦，现在跟我说说话吧", cache=True)
        mic.chatting_mode = True
        mic.skip_passive = True
    else:
        mic.say(u"呜呜呜，好吧，先不聊啦", cache=True)
        mic.skip_passive = False
        mic.chatting_mode = False


def isValid(text):
    """
        Returns True if the input is related to weather.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return any(word in text for word in [u"闲聊", u"聊天", u"不聊了"])
