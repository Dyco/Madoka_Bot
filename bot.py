import nonebot
from nonebot.adapters.onebot.v11 import Adapter as ONEBOT_V11_Adapter

# 初始化 NoneBot
nonebot.init()

# 注册适配器
driver = nonebot.get_driver()
driver.register_adapter(ONEBOT_V11_Adapter)


# 第三方插件
nonebot.load_plugin("nonebot_plugin_alconna")
nonebot.load_plugin("nonebot_plugin_datastore") 

# 本地插件
nonebot.load_plugins("plugins")


if __name__ == "__main__":
    nonebot.run()

