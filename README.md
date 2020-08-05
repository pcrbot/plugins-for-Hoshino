# plugins-for-Hoshino
Hoshino插件合集on-mirai
## 环境
mirai + cqhttp-mirai
cqhttp-mirai项目地址
https://github.com/yyuueexxiinngg/cqhttp-mirai.git
## 使用方法
1.util4sh.py放在hoshino目录下，shebot的插件使用的一些函数及类均在此文件
2.shebot文件夹放在modules下并在config里启用该模组
3.安装requirements.txt里的依赖
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

ps:
自定义回复有网页端管理，按照web4reply里的readme.txt设置
同样支持以下变量：
【艾特全体】、【艾特当前】、【随机图片<文件夹>】
### setu(涩图)
看里面的readme.txt,写累了
## 其他说明
不定期更新
