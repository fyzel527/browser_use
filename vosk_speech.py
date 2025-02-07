import json
import wave
import pyaudio
from vosk import Model, KaldiRecognizer
import asyncio
import logging
import os

logger = logging.getLogger(__name__)

class VoiceController:
    def __init__(self, model_path: str = "browser-use/vosk-model-cn-0.22"):
        try:
            if not os.path.exists(model_path):
                raise FileNotFoundError(f"找不到语音模型文件夹: {model_path}")
                
            self.model = Model(model_path)
            self.CHUNK = 1024
            self.FORMAT = pyaudio.paInt16
            self.CHANNELS = 1
            self.RATE = 16000
            self.running = True
            
            self.recognizer = KaldiRecognizer(self.model, self.RATE)
            self.p = pyaudio.PyAudio()
            self.stream = None
            
        except Exception as e:
            logger.error(f"初始化语音识别失败: {str(e)}")
            raise
    
    async def listen(self):
        """异步语音识别生成器"""
        try:
            self.stream = self.p.open(
                format=self.FORMAT,
                channels=self.CHANNELS,
                rate=self.RATE,
                input=True,
                frames_per_buffer=self.CHUNK
            )
            
            print("开始监听语音输入...")
            
            while self.running:
                data = self.stream.read(self.CHUNK, exception_on_overflow=False)
                if self.recognizer.AcceptWaveform(data):
                    result = json.loads(self.recognizer.Result())
                    text = result.get("text", "").strip()
                    if text:
                        yield text
                await asyncio.sleep(0.01)
                
        except Exception as e:
            logger.error(f"语音识别出错: {str(e)}")
            raise
            
        finally:
            if self.stream:
                self.stream.stop_stream()
                self.stream.close()
            self.p.terminate()
    
    def stop(self):
        """停止语音识别"""
        self.running = False