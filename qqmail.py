import random
import itchat
itchat.auto_login(hotReload=True)
memberList = itchat.get_friends(update=True)
# 创建群聊，topic键值为群聊名
# chatroomUserName = itchat.create_chatroom(memberList, '@techatroom')
itchat.update_chatroom(True)
room = itchat.search_chatrooms(name='喝酒炒螺')[0]
for i in range(0,random.randint(10,15)):
    itchat.send('美女', room['UserName'])