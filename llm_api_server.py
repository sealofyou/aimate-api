import os
from openai import OpenAI
from fastapi import FastAPI, Query

app = FastAPI()


client = OpenAI(
    # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)


@app.get("/llm/")  # 使用举例：http://127.0.0.1:8088/llm/?p=你是一个有用的助手&q=你好
async def get_result(p: str = Query(...), q: str = Query(...)):
    completion = client.chat.completions.create(
        model="qwen-plus",
        messages=[{'role': 'system', 'content': p},
                  {'role': 'user', 'content': q}],
        stream=True,
        stream_options={"include_usage": True}
    )
    response_text = ""
    try:
        for chunk in completion:
            if chunk.choices is []:
                break
            response_text += chunk.choices[0].delta.content
    except Exception as e:
        print("Error:", e)
    return {"answer": response_text}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8088)