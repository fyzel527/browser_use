from browser_use import SystemPrompt


class MySystemPrompt(SystemPrompt):
    def important_rules(self) -> str:
        existing_rules = super().important_rules()
        new_rules = """
9. MOST IMPORTANT RULE:
- 只使用文本搜索功能，不要使用任何图片相关功能
- 网站地址固定为: 'https://pms.chdgc.com.cn/'
- 需要输入的账号为：admin，需要输入的密码为：Chd!@345。输入完账号密码自动点击登陆
- 人员入场信息功能的地址为：网站地址+?r=personnel-information
- 合同管理页面的地址为：网站地址+/?r=contract
"""
        return f'{existing_rules}\n{new_rules}'


