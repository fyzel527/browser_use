from browser_use import Browser, BrowserConfig, Agent, SystemPrompt
from langchain_openai import ChatOpenAI
import asyncio
import logging
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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

async def main():
    # 确保设置了 OpenAI API 密钥
    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError("请设置 OPENAI_API_KEY 环境变量")

    # 初始化 LLM
    llm = ChatOpenAI(
        model="gpt-4o",
        temperature=0
    )
    
    # 初始化浏览器配置
    browser_config = BrowserConfig(
        headless=False,
        disable_security=True,
    )
    
    # 创建浏览器实例
    browser = Browser(config=browser_config)
    
    try:
        while True:
            command = input("请输入命令 (输入'退出'结束程序):\n")
            
            if command.lower() == '退出':
                logger.info("正在退出程序...")
                break
            
            # 使用配置好的 LLM
            agent = Agent(
                task=command,
                llm=llm,
                browser=browser,
                system_prompt_class=MySystemPrompt,
            )
            
            try:
                result = await agent.run()
                logger.info(f"执行结果: {result}")
            except Exception as e:
                logger.error(f"执行命令时出错: {str(e)}")
                continue
            
    except KeyboardInterrupt:
        logger.info("程序被用户中断")
    except Exception as e:
        logger.error(f"发生错误: {str(e)}")
    finally:
        await browser.close()
        logger.info("浏览器已关闭")

if __name__ == "__main__":
    asyncio.run(main()) 