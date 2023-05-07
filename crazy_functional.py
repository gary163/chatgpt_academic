from toolbox import HotReload  # HotReload 的意思是热更新，修改函数插件后，不需要重启程序，代码直接生效


def get_crazy_functions():
    ###################### 第一组插件 ###########################
    from crazy_functions.读文章写摘要 import 读文章写摘要
    from crazy_functions.生成函数注释 import 批量生成函数注释
    from crazy_functions.解析项目源代码 import 解析项目本身
    from crazy_functions.解析项目源代码 import 解析一个Python项目
    from crazy_functions.解析项目源代码 import 解析一个C项目的头文件
    from crazy_functions.解析项目源代码 import 解析一个C项目
    from crazy_functions.解析项目源代码 import 解析一个Golang项目
    from crazy_functions.解析项目源代码 import 解析一个Java项目
    from crazy_functions.解析项目源代码 import 解析一个前端项目
    from crazy_functions.高级功能函数模板 import 高阶功能模板函数
    from crazy_functions.代码重写为全英文_多线程 import 全项目切换英文
    from crazy_functions.Latex全文润色 import Latex英文润色
    from crazy_functions.询问多个大语言模型 import 同时问询
    from crazy_functions.解析项目源代码 import 解析一个Lua项目
    from crazy_functions.解析项目源代码 import 解析一个CSharp项目
    from crazy_functions.总结word文档 import 总结word文档
    from crazy_functions.解析JupyterNotebook import 解析ipynb文件
    from crazy_functions.对话历史存档 import 对话历史存档
    from crazy_functions.对话历史存档 import 载入对话历史存档
    from crazy_functions.对话历史存档 import 删除所有本地对话历史记录
    
    from crazy_functions.批量Markdown翻译 import Markdown英译中
    function_plugins = {
        "载入对话历史存档（先上传存档或输入路径）": {
            "Color": "stop",
            "Function": HotReload(载入对话历史存档)
        },
        "批量生成函数注释": {
            "Color": "stop",    # 按钮颜色
            "Function": HotReload(批量生成函数注释)
        },
        "保存当前的对话": {
            "Function": HotReload(对话历史存档)
        },

    }
    ###################### 第二组插件 ###########################
    # [第二组插件]: 经过充分测试
    from crazy_functions.批量总结PDF文档 import 批量总结PDF文档
    from crazy_functions.批量总结PDF文档pdfminer import 批量总结PDF文档pdfminer
    from crazy_functions.批量翻译PDF文档_多线程 import 批量翻译PDF文档
    from crazy_functions.谷歌检索小助手 import 谷歌检索小助手
    from crazy_functions.理解PDF文档内容 import 理解PDF文档内容标准文件输入
    from crazy_functions.Latex全文润色 import Latex中文润色
    from crazy_functions.Latex全文翻译 import Latex中译英
    from crazy_functions.Latex全文翻译 import Latex英译中
    from crazy_functions.批量Markdown翻译 import Markdown中译英

    function_plugins.update({
        "理解PDF文档内容": {
            # HotReload 的意思是热更新，修改函数插件代码后，不需要重启程序，代码直接生效
            "Color": "stop",
            "Function": HotReload(理解PDF文档内容标准文件输入)
        },
    })

    ###################### 第三组插件 ###########################
    #[第三组插件]: 尚未充分测试的函数插件，放在这里
    from crazy_functions.联网的ChatGPT import 连接网络回答问题
    function_plugins.update({
        "连接网络回答问题（先输入问题，再点击按钮，需要访问谷歌）": {
            "Color": "stop",
            "AsButton": False,  # 加入下拉菜单中
            "Function": HotReload(连接网络回答问题)
        }
    })


    ###################### 第n组插件 ###########################
    return function_plugins
