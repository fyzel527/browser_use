<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./static/browser-use-dark.png">
  <source media="(prefers-color-scheme: light)" srcset="./static/browser-use.png">
  <img alt="Shows a black Browser Use Logo in light color mode and a white one in dark color mode." src="./static/browser-use.png"  width="full">
</picture>

<h1 align="center">Enable AI to control your browser 🤖</h1>

[![GitHub stars](https://img.shields.io/github/stars/gregpr07/browser-use?style=social)](https://github.com/gregpr07/browser-use/stargazers)
[![Discord](https://img.shields.io/discord/1303749220842340412?color=7289DA&label=Discord&logo=discord&logoColor=white)](https://link.browser-use.com/discord)
[![Documentation](https://img.shields.io/badge/Documentation-📕-blue)](https://docs.browser-use.com)
[![Cloud](https://img.shields.io/badge/Cloud-☁️-blue)](https://cloud.browser-use.com)
[![Twitter Follow](https://img.shields.io/twitter/follow/Gregor?style=social)](https://x.com/gregpr07)
[![Twitter Follow](https://img.shields.io/twitter/follow/Magnus?style=social)](https://x.com/mamagnus00)
[![Weave Badge](https://img.shields.io/endpoint?url=https%3A%2F%2Fapp.workweave.ai%2Fapi%2Frepository%2Fbadge%2Forg_T5Pvn3UBswTHIsN1dWS3voPg%2F881458615&labelColor=#EC6341)](https://app.workweave.ai/reports/repository/org_T5Pvn3UBswTHIsN1dWS3voPg/881458615)


🌐 Browser-use is the easiest way to connect your AI agents with the browser. 

💡 See what others are building and share your projects in our [Discord](https://link.browser-use.com/discord) - we'd love to see what you create!

🌩️ Skip the setup - try our hosted version for instant browser automation! [Try it now](https://cloud.browser-use.com).

# Quick start

With pip:

```bash
pip install browser-use
```

install playwright:

```bash
playwright install
```

Spin up your agent:

```python
from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
load_dotenv()

async def main():
    agent = Agent(
        task="Go to Reddit, search for 'browser-use', click on the first post and return the first comment.",
        llm=ChatOpenAI(model="gpt-4o"),
    )
    result = await agent.run()
    print(result)

asyncio.run(main())
```

Add your API keys for the provider you want to use to your `.env` file.

```bash
OPENAI_API_KEY=
```

For other settings, models, and more, check out the [documentation 📕](https://docs.browser-use.com).


### Test with UI

You can test [browser-use with a UI repository](https://github.com/browser-use/web-ui)

Or simply run the gradio example:

```
uv pip install gradio
```

```bash
python examples/ui/gradio_demo.py
```

# Demos

[Prompt](https://github.com/browser-use/browser-use/blob/main/examples/browser/real_browser.py): Write a letter in Google Docs to my Papa, thanking him for everything, and save the document as a PDF.

![Letter to Papa](https://github.com/user-attachments/assets/242ade3e-15bc-41c2-988f-cbc5415a66aa)

<br/><br/>

[Prompt](https://github.com/browser-use/browser-use/blob/main/examples/use-cases/find_and_apply_to_jobs.py): Read my CV & find ML jobs, save them to a file, and then start applying for them in new tabs, if you need help, ask me.'

https://github.com/user-attachments/assets/171fb4d6-0355-46f2-863e-edb04a828d04

<br/><br/>

Prompt: Find flights on kayak.com from Zurich to Beijing from 25.12.2024 to 02.02.2025.

![flight search 8x 10fps](https://github.com/user-attachments/assets/ea605d4a-90e6-481e-a569-f0e0db7e6390)

<br/><br/>

[Prompt](https://github.com/browser-use/browser-use/blob/main/examples/custom-functions/save_to_file_hugging_face.py): Look up models with a license of cc-by-sa-4.0 and sort by most likes on Hugging face, save top 5 to file.

https://github.com/user-attachments/assets/de73ee39-432c-4b97-b4e8-939fd7f323b3

## More examples

For more examples see the [examples](examples) folder or join the [Discord](https://link.browser-use.com/discord) and show off your project.

# Vision

Tell your computer what to do, and it gets it done.

## Roadmap

- [ ] Improve memory management
- [ ] Enhance planning capabilities
- [ ] Improve self-correction
- [ ] Fine-tune the model for better performance
- [ ] Create datasets for complex tasks
- [ ] Sandbox browser-use for specific websites
- [ ] Implement deterministic script rerun with LLM fallback
- [ ] Cloud-hosted version
- [ ] Add stop/pause functionality
- [ ] Improve authentication handling
- [ ] Reduce token consumption
- [ ] Implement long-term memory
- [ ] Handle repetitive tasks reliably
- [ ] Third-party integrations (Slack, etc.)
- [ ] Include more interactive elements
- [ ] Human-in-the-loop execution
- [ ] Benchmark various models against each other
- [ ] Let the user record a workflow and browser-use will execute it
- [ ] Improve the generated GIF quality
- [ ] Create various demos for tutorial execution, job application, QA testing, social media, etc.

## Contributing

We love contributions! Feel free to open issues for bugs or feature requests. To contribute to the docs, check out the `/docs` folder.

## Local Setup

To learn more about the library, check out the [local setup 📕](https://docs.browser-use.com/development/local-setup).

## Cooperations

We are forming a commission to define best practices for UI/UX design for browser agents.
Together, we're exploring how software redesign improves the performance of AI agents and gives these companies a competitive advantage by designing their existing software to be at the forefront of the agent age.

Email [Toby](mailto:tbiddle@loop11.com?subject=I%20want%20to%20join%20the%20UI/UX%20commission%20for%20AI%20agents&body=Hi%20Toby%2C%0A%0AI%20found%20you%20in%20the%20browser-use%20GitHub%20README.%0A%0A) to apply for a seat on the committee.
## Citation

If you use Browser Use in your research or project, please cite:


    
```bibtex
@software{browser_use2024,
  author = {Müller, Magnus and Žunič, Gregor},
  title = {Browser Use: Enable AI to control your browser},
  year = {2024},
  publisher = {GitHub},
  url = {https://github.com/browser-use/browser-use}
}
```
 


 <div align="center"> <img src="https://github.com/user-attachments/assets/402b2129-b6ac-44d3-a217-01aea3277dce" width="400"/> 
 
[![Twitter Follow](https://img.shields.io/twitter/follow/Gregor?style=social)](https://x.com/gregpr07)
[![Twitter Follow](https://img.shields.io/twitter/follow/Magnus?style=social)](https://x.com/mamagnus00)
 
 </div> 

<div align="center">
Made with ❤️ in Zurich and San Francisco
 </div> 

# 语音控制功能

## 快速开始

1. 安装额外依赖:
```bash
pip install vosk pyaudio
```

2. 下载中文语音模型:
```bash
python download_model.py
```

3. 运行带语音控制的示例:
```bash
python vosk_speech.py
```

## 语音控制说明

- 程序启动后会持续监听语音输入
- 说出任务指令，程序会自动执行
- 说"退出"/"结束"/"停止"可以结束程序
- 浏览器会保持打开状态直到收到退出指令

## 示例用法

```python
from langchain_openai import ChatOpenAI
from browser_use import Agent
from vosk_speech import VoiceController
import asyncio

async def main():
    voice_controller = VoiceController()
    agent = Agent(
        task="等待语音指令",
        llm=ChatOpenAI(model="gpt-4"),
    )
    
    try:
        await agent.run_with_voice()
    except Exception as e:
        print(f"程序出错: {str(e)}")
    finally:
        voice_controller.stop()

if __name__ == "__main__":
    asyncio.run(main())
```

## 注意事项

1. 首次使用需要下载语音模型（约1.8GB）
2. 确保系统已授予麦克风权限
3. macOS 用户可能需要先安装 portaudio:
```bash
brew install portaudio
```

4. 支持的语音指令:
   - 任务指令：直接说出要执行的任务
   - 退出指令：说"退出"/"结束"/"停止"

5. 错误处理:
   - 如果语音识别失败，会在控制台显示错误信息
   - 程序会继续运行等待下一个指令
   - 任务执行错误不会导致程序退出

## 自定义配置

可以通过修改 VoiceController 类的参数来自定义语音识别行为:

```python
voice_controller = VoiceController(
    model_path="path/to/your/model",  # 自定义模型路径
)
```




