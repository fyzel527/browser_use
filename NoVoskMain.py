from langchain_openai import ChatOpenAI
from browser_use import Agent, Browser
from vosk_speech import VoiceController
import asyncio
from dotenv import load_dotenv
from Myprompt import MySystemPrompt

# 加载环境变量
load_dotenv()

async def main():
    # 初始化语音控制器
    voice_controller = VoiceController()
    
    # 初始化代理
    agent = Agent(
        task="访问网站，完成登陆后，进入人员入场信息页面，统计所有人员信息，然后跳转到合同管理页面，统计所有合同名称，然后跳转到用户管理页面，统计所有用户类型",
        llm=ChatOpenAI(model="gpt-4"),
        system_prompt_class=MySystemPrompt,
    )
    
    try:
        # 启动语音监听
        async for command in voice_controller.listen():
            print(f"\n识别到的指令: {command}")
            
            # 发送语音命令给代理
            agent.set_voice_command(command)
            
            # 如果收到退出命令，结束程序
            if any(cmd in command.lower() for cmd in ["退出", "关闭", "停止", "结束"]):
                print("\n收到退出指令，正在关闭...")
                break
                
            # 执行任务
            try:
                result = await agent.run()
                if result:
                    print(f"\n任务执行结果: {result}")
                print("\n请继续说出指令，说'退出'可以结束程序...")
                
            except Exception as e:
                print(f"\n任务执行出错: {str(e)}")
                print("\n出现错误，请重试...")
    
    finally:
        # 清理资源
        voice_controller.stop()
        print("\n程序已结束")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n程序被手动中断")
    finally:
        print("程序已结束") 