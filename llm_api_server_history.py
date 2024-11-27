import os
from openai import OpenAI
from fastapi import FastAPI, Query

app = FastAPI()
context_history = []
context_max_length = 10

client = OpenAI(
    # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)


def history(question):
    while len(context_history) > context_max_length:
        context_history.pop(0)
    context_history.append({"role": "user", "content": question})
    return context_history


@app.get("/llm/")  # 使用举例：http://127.0.0.1:8088/llm/?p=你是一个有用的助手&q=你好
async def get_result(p: str = Query(...), q: str = Query(...)):
    message = history(q)
    message.extend([{'role': 'system', 'content': p}, {'role': 'user', 'content': q}])
    completion = client.chat.completions.create(
        model="qwen-plus",
        messages=message,
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
    context_history.append({"role": "assistant", "content": response_text})
    return {"answer": response_text}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8088)
