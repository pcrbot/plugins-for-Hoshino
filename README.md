# plugins-for-Hoshino
Hoshino插件合集
## 环境
go-cqhttp
go-cqhttp项目地址
https://github.com/Mrs4s/go-cqhttp.git
## 使用方法
1. shebot文件夹放在modules下并在config里启用该模组
2. 安装requirements.txt里的依赖
## 插件列表

### liveNotice(直播提醒)
#### 指令
| 指令                 | 说明                                                     |
| ---------------------- | -------------------------------------------------------- |
| live        | 根据提示订阅一个直播间，目前只支持哔哩哔哩和斗鱼直播 |

ps:
1. 使用的是我个人的rss源，如果要换成自己的，在_util里的class RSS中更换
2. 目前只支持斗鱼和哔哩哔哩，别问为什么就这两个，因为我只看这两个

### infoPush(rss消息推送)
#### 指令
在__init__.py里按照注释添加service和路由，所有路由请见https://docs.rsshub.app/。 并非所有类型的路由都经过测试，bilibili动态，pcr官网，github issue这些经测试都可以正常使用。

ps:
同直播提醒

### webServiceManager(Hoshino服务开关网页控制)
#### 指令
| 指令                 | 说明                                                     |
| ---------------------- | -------------------------------------------------------- |
| 服务管理/bot设置(私聊bot)        | bot将发送服务管理的链接 |
本插件为hoshinoV2的服务管理插件，提供web控制各个群的各项服务启(禁)用，并支持一键启(禁)用某群所有服务，或者一键启(禁)用所有群某服务

安装使用：
修改view.py里公网ip和密码
私聊bot发送bot设置

注意事项：
hoshino config文件夹__bot__.py中的HOST请设置为 0.0.0.0以开放公网访问
请注意服务器放行端口
请设置好密码，开放公网访问带来的任何安全问题与本人无关

### setu(涩图)
看里面的readme.txt,写累了

### concatHead(接头霸王)
利用百度人脸识别api接臭鼬头，详见concatHead文件夹下readme

## 其他说明
不定期更新
