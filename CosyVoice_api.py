import os
from fastapi import FastAPI
from fastapi.responses import FileResponse
import dashscope
from dashscope.audio.tts_v2 import VoiceEnrollmentService, SpeechSynthesizer

app = FastAPI()
url = "http://www.guoxi.fun/example.wav"
dashscope.api_key = os.getenv('DASHSCOPE_API_KEY')  # 如果您没有配置环境变量，请在此处用您的API-KEY进行替换
prefix = 'prefix'
target_model = "cosyvoice-clone-v1"
# 创建语音注册服务实例
service = VoiceEnrollmentService()


def create_voice(url: str):
    # 调用create_voice方法复刻声音，并生成voice_id
    voice_id = service.create_voice(target_model=target_model, prefix=prefix, url=url)
    os.environ['Voice_id'] = voice_id
    print(f"your voice id is {voice_id}")
    return voice_id


@app.get('/cosyvoice/')
def synthesize_voice(text: str):
    voice_id = os.getenv('Voice_id')
    print("Voice_id", voice_id)
    if voice_id is None:
        voice_id = create_voice(url)
    # 使用复刻的声音进行语音合成
    synthesizer = SpeechSynthesizer(model=target_model, voice=voice_id)
    audio = synthesizer.call(text)
    audio_path = "data/cache/cache.wav"
    # 将合成的音频文件保存到本地文件
    with open(audio_path, "wb") as f:
        f.write(audio)
    return FileResponse(audio_path)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=9881)
