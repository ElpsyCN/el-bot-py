from mirai import Mirai, Plain, MessageChain, Friend, Group, GroupMessage, FriendMessage
import asyncio
import os

import config

print(config.setting)
# httpapi所在主机的地址端口, 如果 setting.yml 文件里字段 "enableWebsocket" 的值为 "true" 则需要将 "/" 换成 "/ws", 否则将接收不到消息.
mirai_api_http_locate = 'localhost:' + str(config.setting['port'])
if config.setting['enableWebsocket']:
    mirai_api_http_locate += '/ws'

app = Mirai(
    f"mirai://{mirai_api_http_locate}?authKey={config.setting['authKey']}&qq={config.data['qq']}")

msg_count = 0
last_msg = ''


@app.receiver("GroupMessage")
async def msg_indeed(app: Mirai, group: Group, message: MessageChain):
    global last_msg
    if message.__root__[1].text == last_msg:
        await app.sendGroupMessage(group, [
            Plain(text="确实")
        ])
    last_msg = message.__root__[1].text

if __name__ == "__main__":
    app.run()
