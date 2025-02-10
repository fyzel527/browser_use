from browser_use import Browser, BrowserConfig, Controller, Agent
from langchain_openai import ChatOpenAI
import asyncio
import logging
from Myprompt import MySystemPrompt

async def main():
    # 初始化日志
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    # 初始化浏览器配置
    browser_config = BrowserConfig(
        headless=False,  # 显示浏览器界面
        disable_security=True
    )

    # 初始化浏览器、控制器和代理
    browser = Browser(config=browser_config)
    controller = Controller()
    agent = Agent(
         task="访问网站，完成登陆后，进入人员入场信息页面，统计所有人员信息，然后跳转到合同管理页面，统计所有合同名称，然后跳转到用户管理页面，统计所有用户类型",
        llm=ChatOpenAI(model="gpt-4"),
        browser=browser,
        controller=controller,
        system_prompt_class=MySystemPrompt,
    )

    try:
        # 获取browser context
        context = await browser.new_context()
        
        print("浏览器已启动,请输入命令(输入'quit'退出):")
        
        while True:
            # 获取用户输入
            command = input("> ")
            
            # 检查是否退出
            if command.lower() == 'quit':
                print("正在退出...")
                break
                
            try:
                # 执行命令
                await context.input_and_execute(command)
                print("命令执行完成")
            except Exception as e:
                logger.error(f"执行命令时出错: {str(e)}")
                
    except Exception as e:
        logger.error(f"运行时出错: {str(e)}")
    finally:
        # 关闭浏览器
        await browser.close()

if __name__ == "__main__":
    # 运行主函数
    asyncio.run(main()) 