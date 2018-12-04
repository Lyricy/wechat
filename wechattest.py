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

# for men in memberList:
#     if men['NickName'] == '圈圈':
#         itchat.add_member_into_chatroom(room['NickName'], [men], useInvitation=False)
ccc = itchat.search_friends(name='叉叉')[0]
# print(ccc)
# itchat.send_msg('今天有点安静', room['UserName'])
# 删除群聊内的用户
itchat.delete_member_from_chatroom(room['NickName'], [ccc])
# 增加用户进入群聊
# itchat.add_member_into_chatroom(room['NickName'], [ccc], useInvitation=False)
# groups = itchat.get_chatrooms()
# print(groups)