import os
import dashscope
from dashscope.audio.tts_v2 import VoiceEnrollmentService, SpeechSynthesizer

from CosyVoice_api import create_voice

dashscope.api_key = os.getenv('DASHSCOPE_API_KEY')  # 如果您没有配置环境变量，请在此处用您的API-KEY进行替换
prefix = 'prefix'
target_model = "cosyvoice-clone-v1"

# 创建语音注册服务实例
service = VoiceEnrollmentService()


if __name__ == '__main__':
    url = "http://www.guoxi.fun/example.wav"  # 请按实际情况进行替换
    voice_id = create_voice(url)
    os.putenv("Voice_id", voice_id)
    print("Voice_id设置成功，请重启IDE")
