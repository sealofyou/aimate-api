# 枫云AI虚拟伙伴探索版-DLC 阿里云api调用版
> 电脑带不动DLC不如白嫖阿里云的api :)
>
>非小白向，小白建议整合包，我是电脑不太支持部署大模型，linux用给的开源代码有问题。
> 又因为白嫖魔搭社区未果，所以自己写了（白嫖）阿里云的api。
>
>  [枫云AI虚拟伙伴探索版](https://swordswind.github.io/2024/09/12/mateexp/)

## 使用流程
###  调用准备
> 主要是获取apikey和apisecret

1. [如何获取API Key_大模型服务平台百炼(Model Studio)-阿里云帮助中心](https://help.aliyun.com/zh/model-studio/developer-reference/get-api-key)

开通送Token(半年有效期,能用多久还没试)

2. [如何添加百炼的API Key到环境变量中_大模型服务平台百炼(Model Studio)-阿里云帮助中心](https://help.aliyun.com/zh/model-studio/developer-reference/configure-api-key-through-environment-variables?spm=a2c4g.11186623.0.0.77b17980KxSW6C)

CMD 命令：
```bash
setx DASHSCOPE_API_KEY "sk-1145141919810"
```

3. [安装阿里云百炼SDK_大模型服务平台百炼(Model Studio)-阿里云帮助中心](https://help.aliyun.com/zh/model-studio/developer-reference/install-sdk)

`pip install openai`

### 调用api
1. 选择你想玩的模型，我这里使用[通义千问-Max](https://bailian.console.aliyun.com/?spm=5176.29004136.0.0.d717778bUI20Jq#/model-market/detail/qwen-max?tabKey=sdk)
2. 根据你选择的模型复制需要的代码运行即可。(自己使用输出需要调整，仓库中是调好的)
3. 根据需求添加其他，例如fastapi等部署成后端应用。

# 介绍
[模型介绍](https://swordswind.github.io/2024/03/13/engine/)

## Qwen-Max
对应 Qwen整合包，这里使用Qwen2.5-0.5B，开源地址:
[gen_llm_api_server](https://github.com/swordswind/gen_llm_api_server)

这里阿里云api调用Qwen-max，如需降低模型，请自行修改对应模型名。

代码如llm_api_server_history.py和llm_api_server.py，使用对应环境python运行即可。


## CosyVoice

和本地部署类似但有不同。wav文件需要线上，可以尝试oss或者各种代码仓库
[阿里云OSS上传文件](https://help.aliyun.com/zh/oss/user-guide/simple-upload?spm=0.0.0.i23#a632b50f190j8)
也可以通过阿里云oss图形化界面进行上传。
> 音频时间不能长，不然可能有问题（我遇到了500内部问题报错，换了个音频解决了）

example效果很差，等后续吧
延时不小，不确定是模式还是就这样


## Qwen-VL

效果还行，比CosyVoice强，还不用怎么debug。


## 调用指南
llm_api_server.py和llm_api_server_history.py是千问的对话模型。

CosyVoice_api.py是语音转文字，然后调用千问。

Qwen_VL_api.py是视觉大模型。