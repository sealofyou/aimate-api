import base64
import os
from io import BytesIO

from openai import OpenAI
from fastapi import FastAPI, Request
from openai.types import Image
from starlette.responses import JSONResponse

app = FastAPI()

client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)


#  阿里云 base 64 编码格式
# def encode_image(image_path):
#     with open(image_path, "rb") as image_file:
#         return base64.b64encode(image_file.read()).decode("utf-8")


@app.post("/qwen_vl")
async def run_qwen_vl(request: Request):
    data = await request.json()
    # 直传的base64字符串，可以直接拿来用
    input_image_base64 = data['image']
    # 代码修改
    # image_data = base64.b64decode(input_image_base64.split(",")[1])
    # image = Image.open(BytesIO(image_data))
    msg = data['msg']
    # 阿里云的图片转码
    # base64_image = encode_image(input_image_base64)
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    # 使用格式化字符串 (f-string) 创建一个包含 BASE64 编码图像数据的字符串。
                    "image_url": {"url": f"{input_image_base64}"},
                },
                {"type": "text", "text": msg},
            ],
        }
    ]
    completion = client.chat.completions.create(
        model="qwen-vl-max-latest",
        messages=messages
    )
    print(completion)
    return JSONResponse(content={"answer": completion.choices[0].message.content})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8086)
