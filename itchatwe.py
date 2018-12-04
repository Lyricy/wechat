import itchat
import time
import re
import os
import desknotify
import random
itchat.auto_login(hotReload=True)
# itchat.send(u'你好', 'filehelper')
friends_dic = {}
friends = itchat.get_friends(update=True)
for friend in friends:
    # print(friend)
    friends_dic[friend['UserName']] = {'NickName':friend['NickName'], 'RemarkName': friend['RemarkName']}
groups_dic = {}
groups = itchat.get_chatrooms(update=True)
for group in groups:
    print(group)
    groups_dic[group['UserName']] = group['NickName']
myUserName = itchat.get_friends(update=True)[0]["UserName"]
msg_dirt = {}
@itchat.msg_register(['PICTURE', 'RECORDING', 'ATTACHMENT', 'VIDEO'])
def download_files(msg):
    #msg.download(msg['FileName'])   #这个同样是下载文件的方式
    print(msg)
    msg['Text'](msg['FileName'])      #下载文件
    print(msg['FileName'])
    #将下载的文件发送给发送者
    itchat.send('@%s@%s' % ('img' if msg['Type'] == 'Picture' else 'fil', msg["FileName"]), 'filehelper')
@itchat.msg_register(['Text','Note', 'ATTACHMENT', 'PICTURE'], isGroupChat = True)
def text_reply(msg):
    # print(msg)
    oldMsgId = ''
    ActualNickName = ''
    toUser = msg['ToUserName']
    try:
        ActualNickName = msg['ActualUserName']
        if friends_dic[ActualNickName]['RemarkName']:
            ActualNickName = friends_dic[ActualNickName]['RemarkName']
        elif friends_dic[ActualNickName]['NickName']:
            ActualNickName = friends_dic[ActualNickName]['NickName']
    except:
        pass
    if msg['FromUserName'] == myUserName:
        chatName = msg['ToUserName']
        ActualNickName = friends_dic[msg['FromUserName']]['NickName']
    else:
        chatName = msg['FromUserName']
    # 如果是非好友在群里发消息，则取备注或昵称
    if ActualNickName.find('@')>-1:
        try:
            ActualNickName = msg['ActualNickName']
        except:
            pass
    if toUser == 'filehelper':
        if msg['Text'].find('mp4')> -1:
            url = msg['Text']
            if url.find('https')>-1:
                url = url.replace('https', 'http')
            print('download from %s starting...'%url)
            download(url)
            itchat.send_msg('已将【%s】添加到下载列表.'%url, 'filehelper')
            filename = url[str(url).rfind('/')+1:]
            filepath = r'C:\Users\Administrator\Desktop\%s'%filename
            print(filepath)
            while 1:
                print('开始发送文件：%s'%filepath)
                itchat.send_msg('开始发送文件：%s'%filepath, 'filehelper')
                if os.path.exists(filepath):
                    itchat.send('@vid@%s' % filepath, 'filehelper')
                    print('发送文件：%s成功'%filepath)
                    itchat.send_msg('发送文件：%s成功'%filepath, 'filehelper')
                break
    elif msg['Text'].find('撤回了一条消息') > -1 and msg['Text'].find('好友') == -1:
        try:
            cont = msg['Content']
            cont = str(cont).replace('&lt;', '<')
            cont = str(cont).replace('&gt;', '>')
            oldMsgId = re.search(r'<msgid>(.*?)</msgid>', cont).group(1)
            itchat.send_msg('好友【%s】于【%s】在群聊【%s】撤回了一条消息：%s' % (ActualNickName, time.strftime("%Y-%m-%d %H:%M:%S",
                                                                                            time.localtime(
                                                                                                msg['CreateTime'])),
                                                              groups_dic[chatName], msg_dirt.get(oldMsgId)),
                            'filehelper')
            # print('好友【%s】于【%s】撤回了一条消息：%s' % (ActualNickName, time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(msg['CreateTime'])),
            #                                  msg_dirt.get(oldMsgId)))
            print('********群聊撤回消息提醒：【%s】************   【%s】在【%s】撤回了：【%s】' % (
            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(msg['CreateTime'])),
            ActualNickName,
            groups_dic[chatName],
            msg_dirt.get(oldMsgId))
                  )
        except:
            pass

        # return '快来看，【%s】偷偷撤回了一条消息：%s' % (ActualNickName, msg_dirt.get(oldMsgId))
    else:
        # 当消息不是由自己发出的时候
        msg_dirt[msg['MsgId']] = msg['Text']
            # 发送一条提示给文件助手
            # itchat.send_msg(u"[%s]收到好友【%s】在群聊【%s】发送的信息：%s\n" %
            #                 (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(msg['CreateTime'])),
            #                  ActualNickName,
            #                  groups_dic[chatName],
            #                  msg['Text']), 'filehelper')
        # print('收到好友【%s】于【%s】在群聊【%s】发来的消息【%s】' % (ActualNickName, time.strftime("%Y-%m-%d %H:%M:%S",
        #                                                                        time.localtime(
        #                                                                            msg['CreateTime'])),
        #                                          groups_dic[chatName],
        #                                          msg['Text']))
        if groups_dic[chatName]:
            print('群聊消息提醒-->【%s】 %s   %s：%s' % (
                groups_dic[chatName],
                time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(msg['CreateTime'])),
                ActualNickName,
                msg['Text']
                  ))
        else:
            print(msg)
            print('群聊消息提醒-->【%s】 %s   %s：%s' % (
                chatName,
                time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(msg['CreateTime'])),
                ActualNickName,
                msg['Text']
            ))
        desknotify.balloon_tip(groups_dic[chatName], msg['Text'])
    # try:
    #     if (str(msg['Text']).find('妹子')>-1 or str(msg['Text']).find('妹纸')>-1) and groups_dic[chatName] == '喝酒炒螺':
    #         imgPath = r'C:\Users\picc\Desktop\新建文件夹\spideremp\images'
    #         os.chdir(imgPath)
    #         files = os.listdir()
    #         file = files[random.randint(0, len(files))]
    #         print('发送图片--> %s：%s'%(itchat.search_chatrooms(u'喝酒炒螺')[0]['UserName'], imgPath + '\\' + file))
    #         itchat.send('@%s@%s' % ('img',imgPath + '\\' + file), itchat.search_chatrooms(u'喝酒炒螺')[0]['UserName'])
    #         itchat.send('@%s@%s' % ('img',imgPath + '\\' + file), 'filehelper')
    # except:
    #     pass
@itchat.msg_register(['Text','Note', 'PICTURE'], isFriendChat = True)
def text_reply(msg):
    # print(msg)
    oldMsgId = ''
    fromUser = msg['FromUserName']
    toUser = msg['ToUserName']
    if friends_dic[fromUser]['RemarkName']:
        fromUser = friends_dic[fromUser]['RemarkName']
    elif friends_dic[toUser]['NickName']:
        fromUser = friends_dic[fromUser]['NickName']
    if friends_dic[toUser]['RemarkName']:
        toUser = friends_dic[toUser]['RemarkName']
    elif friends_dic[toUser]['NickName']:
        toUser = friends_dic[toUser]['NickName']

    if msg['Text'].find('撤回了一条消息') > -1:
        cont = msg['Content']
        cont = str(cont).replace('&lt;', '<')
        cont = str(cont).replace('&gt;', '>')
        oldMsgId = re.search(r'<msgid>(.*?)</msgid>', cont).group(1)
        itchat.send_msg('好友【%s】于【%s】撤回了一条消息：%s' % (fromUser, time.strftime("%Y-%m-%d %H:%M:%S",
                                                                                 time.localtime(msg['CreateTime'])),
                                          msg_dirt.get(oldMsgId)), 'filehelper')
        # print('好友【%s】于【%s】撤回了一条消息：%s' % (fromUser, time.strftime("%Y-%m-%d %H:%M:%S",
        #                                                                          time.localtime(msg['CreateTime'])),
        #                                  msg_dirt.get(oldMsgId)))
        print('********好友撤回消息提醒：【%s】************   【%s】撤回了：【%s】' % (
        time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(msg['CreateTime'])),
        fromUser,
        msg_dirt.get(oldMsgId))
              )
        # return '小样，想偷偷撤回于【%s】发来的消息【%s】，没门!' % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(msg['CreateTime'])), msg_dirt.get(oldMsgId))
    else:
        msg_dirt[msg['MsgId']] = msg['Text']
        # 发送一条提示给文件助手
        # itchat.send_msg(u"[%s]收到好友【%s】的信息：%s\n" %
        #                 (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(msg['CreateTime'])),
        #                  fromUser,
        #                  msg['Text']), 'filehelper')
        # print('收到好友【%s】于【%s】发给【%s】的消息【%s】' % (fromUser, time.strftime("%Y-%m-%d %H:%M:%S",
        #                                                           time.localtime(msg['CreateTime'])),
        #                                       toUser,
        #                                   msg['Text']))
        print('好友消息提醒--> %s   %s -> %s：%s' % (
            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(msg['CreateTime'])),
            fromUser,
            toUser,
            msg['Text']
        ))
        desknotify.balloon_tip(fromUser, msg['Text'])
        # 回复给好友
        # return u'[自动回复]您好，我现在有事不在，一会再和您联系。\n已经收到您的的信息：%s\n' % (msg['Text'])
def download(url):
    thunderPosition = r'"E:\Program Files (x86)\Thunder Network\Thunder\Program\Thunder.exe " {url}'
    # argus = ' -StartType:StartMenu %s'
    try:
        os.system(thunderPosition.format(url=url))
    except Exception as e:
        print(e)
itchat.run()