import itchat
itchat.auto_login(hotReload=True, enableCmdQR=True)
friends = itchat.get_friends(update=True)
remarkName = {}
for friend in friends:
    if friend['RemarkName']:
        remarkName[friend.get('NickName')] = friend['RemarkName']
@itchat.msg_register(['TEXT'], isFriendChat=True)
def reply_text(msg):
    print(msg)

itchat.run()