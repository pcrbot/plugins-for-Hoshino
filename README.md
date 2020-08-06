# plugins-for-Hoshino
Hoshino插件合集on-mirai
## 环境
mirai + cqhttp-mirai
cqhttp-mirai项目地址
https://github.com/yyuueexxiinngg/cqhttp-mirai.git
## 使用方法
1. util4sh.py放在hoshino目录下，shebot的插件使用的一些函数及类均在此文件
2. shebot文件夹放在modules下并在config里启用该模组
3. 安装requirements.txt里的依赖
## 插件列表
### QA(你问我答)
#### 指令
|指令|说明|
|-----|-----|
|我问xxx你答xxx||
|有人问xxx你答xxx||
|删除问答<问>||
|查看问答<页数>||
|查看全部问答<页数>|SUPERUSER|

ps:
答句可以用 | 分隔，将随机挑选一个回复
答句可以用 + 分隔，将分多条消息发送
支持以下变量：
【艾特全体】、【艾特当前】、【随机图片<文件夹>】
文件夹需要创建在res/image下
### reply(自定义回复)
#### 指令(SUPERUSER使用)
|指令|说明|
|-----|-----|
|fullmatch<触发词>#<回复>|完全匹配|
|keyword<触发词>#<回复>|关键词匹配|
|rex<触发词>#<回复>|正则匹配|
|删除fullmatch\|keyword\|rex<触发词>||

### scheduledMessage(定时发送消息)
#### 指令(OWNER以上权限使用)
|指令|说明|
|-----|-----|
|闹钟|根据bot发送的消息进行设置|
|查看计划任务||
|删除计划任务<任务id>|id通过查看计划任务获得|

ps:
1. 多个时间逗号隔开，逗号使用英文逗号，且之间不要空格
2. 使用命令添加的仅当前群生效，如果要设置多个群，直接将jobs.json里groups字段设置为'default'
3. 同样支持以下变量：【艾特全体】、【艾特当前】、【随机图片<文件夹>】

### scheduledCommand(定时执行命令)
#### 指令(ADMIN以上权限使用)
|指令|说明|
|-----|-----|
|add_delay_job|根据bot发送的消息进行设置|
|add_cron_job|根据bot发送的消息进行设置|
|show_cron_job|查看定时执行命令|
|cancel_cron_job|删除定时命令|

ps:
1. 多个时间逗号隔开，逗号使用英文逗号，且之间不要空格

### liveNotice(直播提醒)
#### 指令
| 指令                 | 说明                                                     |
| ---------------------- | -------------------------------------------------------- |
| live        | 根据提示订阅一个直播间，目前只支持哔哩哔哩和斗鱼直播 |

ps:
1. 使用的是我个人的rss源，如果要换成自己的，在util4sh.py里的class RSS中更换
2. 目前只支持斗鱼和哔哩哔哩，别问为什么就这两个，因为我只看这两个

### biliVideo(B站up投稿提醒)
#### 指令
| 指令                 | 说明                                                     |
| ---------------------- | -------------------------------------------------------- |
| video        | 根据提示订阅B站up的投稿提醒 | |

ps:
同直播提醒

### infoPush(偏通用型的消息推送)
#### 指令
在__init__.py里按照注释添加service和路由，所有路由请见https://docs.rsshub.app/。并非所有类型的路由都经过测试，bilibili动态，pcr官网，github issue这些经测试都可以正常使用。

ps:
同直播提醒

### setu(涩图)
看里面的readme.txt,写累了
## 其他说明
不定期更新
