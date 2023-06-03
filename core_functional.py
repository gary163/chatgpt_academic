# 'primary' 颜色对应 theme.py 中的 primary_hue
# 'secondary' 颜色对应 theme.py 中的 neutral_hue
# 'stop' 颜色对应 theme.py 中的 color_er
# 默认按钮颜色是 secondary
from toolbox import clear_line_break


def get_sql_functions():
    return {
        "SQL语句优化": {
            # 前言
            "Prefix": """
                        你的任务是以DBA专家的角色优化用户输入的语句,检查以下方面:
                            1 - SELECT语句的优化
                            2 - JOIN操作的优化，如果是笛卡尔积的SQL，尝试提出替换的方案
                            3 - WHERE子句的优化
                            4 - 子查询的优化
                            5 - INSERT、UPDATE和DELETE语句的优化
                            6 - 数据库设计的优化

                        sql语句在Text:<>分隔符中，最后请格式化输出优化过后的SQL语句
                    Text: <\n
                    """,
            # 后语
            "Suffix": "\n>",
            "Color": r"secondary",  # 按钮颜色
        },
        "SQL解释": {
            # 前言
            "Prefix": """
                        作为一个AI语言模型，我被要求为给定的SQL代码片段提供注释:
                            1 - 表的字段信息在Text:<>分隔符中
                            2 - 请为给定的SQL代码片段生成相应的注释
                            3 - 确保注释简洁、清晰且有助于理解代码的目的和逻辑
                            4 - 对于每个主要的部分和操作，请解释它们的作用和如何与其他部分协同工作
                        Text: <\n
                        """,
            # 后语
            "Suffix": "\n>",
            "Color": r"secondary",  # 按钮颜色
        },
        "生成SQL测试语句": {
            # 前言
            "Prefix": """
                            你的任务是为用户输入的sql创建测试数据:
                                1 - 表的字段信息在Text:<>分隔符中
                                2 - 如果输入不包含表和字段，提示"请输入表的字段信息"
                                3 - 生成5条测试数据
                                4 - 编程语言是sql，直接按sql插入格式输出即可，请不用输出任何例如Python代理片段
                        Text: <\n
                        """,
            # 后语
            "Suffix": "\n>",
            "Color": r"secondary",  # 按钮颜色
        },
        "Mysql建表语句转StarRocks建表语句": {
            # 前言
            "Prefix":   """
                            你的任务是把来自mysql的建表语句转换为StarRocks的建表SQL，请遵循以下规则:
                            1 - 源sql语句在Text:<>分隔符中
                            2 - 源sql中，如果含有text,varchar类型的字段，统一转换为varchar(5000),
                                int 统一转换为bigint,decimal统一长度为decimal(30,8)
                            3 - 'AUTO_INCREMENT','UNIQUE INDEX'，'INDEX','PRIMARY KEY',
                            'DEFAULT CURRENT_TIMESTAMP'等关键字，StarRocks不支持
                            4 - 最后一个字段是 `ds` DATE，需额外加上
                            5 - 如果字段没有注释，尝试补充中文comment
                            6 - markdown格式化输出
                            统一按如下格式输出demo：
                            create table if not exists table_name(
                              `id` int(11)  NOT NULL ,
                              ...
                              `ds` DATE
                              ) COMMENT '表备注'
                            PARTITION BY RANGE (`ds`) (
                              START ("date1") END ("date2") EVERY (INTERVAL 1 MONTH)
                            )
                            DISTRIBUTED BY HASH(`id`) BUCKETS 9;
                        Text: <\n
                        """,
            # 后语
            "Suffix":    "\n>",
            "Color":    r"secondary",    # 按钮颜色
        },
        "代码转为StarRocks建表语句": {
            # 前言
            "Prefix":   """
                            你的任务是代码转换为StarRocks的建表SQL，请遵循以下规则:
                            1 - 源sql语句在Text:<>分隔符中
                            2 - 先分析代码，来源有Java的DTO,或PHP,Golang,Python的Class属性
                            3 - 源sql中，如果含有text,string,varchar类型的字段，统一转换为varchar(5000)
                            4 - 如果字段没有注释，尝试补充中文comment
                            5 - markdown格式化输出    
                            SQL请格式化输出，输出demo：
                            create table if not exists table_name(
                              `id` int(11)  NOT NULL ,
                              ...
                              `ds` DATE
                              ) COMMENT '表备注'
                            PARTITION BY RANGE (`ds`) (
                              START ("date1") END ("date2") EVERY (INTERVAL 1 DAY)
                            )
                            DISTRIBUTED BY HASH(`id`) BUCKETS 9;
                        Text: <\n
                        """,
            # 后语
            "Suffix":    "\n>",
            "Color":    r"secondary",    # 按钮颜色
        },
        "HiveSQL转StarRocks建表语句": {
            # 前言
            "Prefix": """
                                你的任务是把HiveSQL转换为StarRocks的建表SQL，请遵循以下规则:
                                1 - 源HiveSQL语句在Text:<>分隔符中
                                2 - 源sql中，如果含有string类型的字段，统一转换为varchar(5000),
                                    int 统一转换为bigint,decimal统一长度为decimal(30,8)
                                3 - 原HiveSQL中将StarRocks不支持的关键字或语法自动屏蔽
                                4 - 如果字段没有注释，尝试补充中文comment
                                5 - markdown格式化输出    
                                SQL请格式化输出，输出demo：
                                create table if not exists table_name(
                                  `id` int(11)  NOT NULL ,
                                  ...
                                  `ds` DATE
                                  ) COMMENT '表备注'
                                PARTITION BY RANGE (`ds`) (
                                  START ("date1") END ("date2") EVERY (INTERVAL 1 DAY)
                                )
                                DISTRIBUTED BY HASH(`id`) BUCKETS 9;
                            Text: <\n
                            """,
            # 后语
            "Suffix": "\n>",
            "Color": r"secondary",  # 按钮颜色
        },
        "Oracle转StarRocks建表语句": {
            # 前言
            "Prefix": """
                                你的任务是把Oracle转换为StarRocks的建表SQL，请遵循以下规则:
                                    1 - 源Oracle SQL语句在Text:<>分隔符中
                                    2 - 源sql中，如果含有text,VARCHAR2类型的字段，统一转换为varchar(5000),
                                    int 统一转换为bigint,NUMBER统一长度为decimal(30,8)
                                    3 - 原OracleSQL中将StarRocks不支持的关键字或语法自动屏蔽
                                    4 - 如果字段没有注释，尝试补充中文comment
                                    5 - markdown格式化输出    
                                    SQL请格式化输出，输出demo：
                                    create table if not exists table_name(
                                      `id` int(11)  NOT NULL ,
                                      ...
                                      `ds` DATE
                                      ) COMMENT '表备注'
                                    PARTITION BY RANGE (`ds`) (
                                      START ("date1") END ("date2") EVERY (INTERVAL 1 DAY)
                                    )
                                    DISTRIBUTED BY HASH(`id`) BUCKETS 9;
                                Text: <\n
                                """,
            # 后语
            "Suffix": "\n>",
            "Color": r"secondary",  # 按钮颜色
        },
        "代码转为Mysql建表语句": {
            # 前言
            "Prefix": """
                                你的任务是代码转换为mysql的建表SQL，请遵循以下规则:
                                1 - 源sql语句在Text:<>分隔符中
                                2 - 先分析代码，来源有Java的DTO,或PHP,Golang,Python的Class属性,也有可能来自普通文本
                                3 - 规范输出SQL建表语句，不要输出任意类型的代码块
                                4 - 如果字段没有注释，尝试补充中文comment
                                5 - markdown格式化输出
                            Text: <\n
                            """,
            # 后语
            "Suffix": "\n>",
            "Color": r"secondary",  # 按钮颜色
        },
    }

def get_code_functions():
    return {
        "生成单元测试代码": {
            # 前言
            "Prefix": """
                        作为一个AI语言模型，我被要求为给定的代码片段生成单元测试代码，
                        用户提供的代码片段可能是用 JAVA, PHP, Python或Go其中一种{language}语言写的
                        你的任务是:
                        1 - 用户输入的代码片段在Code:<>分隔符中
                        2 - 识别用户输入的代码是何种{language}，请为给定的代码片段生成 {language} 的单元测试代码
                        3 - 确保单元测试覆盖了提供代码的主要功能，并遵循编写指定语言测试的最佳实践。
                    Code: <\n
                    """,
            # 后语
            "Suffix": "\n>",
            "Color": r"secondary",  # 按钮颜色
        },
        "生成代码注释": {
            # 前言
            "Prefix": """
                        作为一个AI语言模型，我被要求为给定的代码片段生成代码注释。
                        用户提供的代码片段可能是用 JAVA, PHP, Python或Go其中一种{language}语言写的
                        你的任务是:
                        1 - 用户输入的代码片段在Code:<>分隔符中
                        2 - 识别用户输入的代码是何种{language}，请为给定的代码片段生成 {language} 的代码注释
                        3 - 确保注释简洁明了，能够帮助其他开发者理解代码的功能和逻辑。
                    Code: <\n
                    """,
            # 后语
            "Suffix": "\n>",
            "Color": r"secondary",  # 按钮颜色
        },
        "生成代码摘要": {
            # 前言
            "Prefix": """
                        作为一个AI语言模型，我被要求为给定的代码片段生成代码摘要。
                        用户提供的代码片段可能是用 JAVA, PHP, Python或Go其中一种{language}语言写的
                        你的任务是:
                        1 - 用户输入的代码片段在Code:<>分隔符中
                        2 - 识别用户输入的代码是何种{language}，请为给定的代码片段生成 {language} 的代码摘要
                        3 - 提供一个简短的摘要，概括代码的主要功能。
                    Code: <\n
                    """,
            # 后语
            "Suffix": "\n>",
            "Color": r"secondary",  # 按钮颜色
        },
        "代码优化": {
            # 前言
            "Prefix": """
                        作为一个AI语言模型，我被要求为给定的代码片段提供优化建议。
                        用户提供的代码片段可能是用 JAVA, PHP, Python或Go其中一种{language}语言写的
                        你的任务是:
                        1 - 用户输入的代码片段在Code:<>分隔符中
                        2 - 识别用户输入的代码是何种{language}，请为给定的代码片段生成 {language} 的代码优化建议
                        3 - 确保建议具有实际性和可行性，以提高代码的性能、可读性和可维护性
                        4 - 解释为什么这些建议可以优化代码，并在可能的情况下，提供具体的改进示例。
                    Code: <\n
                    """,
            # 后语
            "Suffix": "\n>",
            "Color": r"secondary",  # 按钮颜色
        },
    }

