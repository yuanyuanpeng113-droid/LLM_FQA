# :zap: A Novel Data-Driven Framework Based on Fuzzy Evaluation and Ensemble Agent for LLMs Transfer in Farmland Protection

### Environment

```bash
pip install transformers>=4.25.1
pip install accelerate>=0.13.2
pip install datasets>=2.6.1
pip install evaluate>=0.3.0
pip install pyext==0.7
pip install mosestokenizer==1.0.0
pip install huggingface_hub>=0.11.1
pip install fsspec<2023.10.0
```

### Model

We provide the following models used in our experiments:

- Models:
    - [DeepSeek-Chat](https://huggingface.co/deepseek-ai/DeepSeek-V2-Chat): DeepSeek-Chat is a mixture of experts (MoE) language model developed by the DeepSeek-AI organization in 2024. It was pre-trained on a diverse, high-quality corpus of 8.1 trillion tokens and is characterized by economical training and efficient inference.
    - [Llama3.1-8b](https://huggingface.co/meta-llama/Llama-3.1-8B): Llama3.1-8b is a multilingual LLM developed by the Meta team in 2024 through pre-training. It utilizes an optimized transformer architecture as an autoregressive language model. The fine-tuned version incorporates supervised fine-tuning (SFT) and Reinforcement Learning with human feedback (RLHF) to align with human preferences for usefulness and safety.
    - [Qwen2-7B-Instruct](https://huggingface.co/Qwen/Qwen2-7B-Instruct): Qwen2-7B-Instruct is a new series of Qwen LLMs. Compared to the previously released Qwen1.5, Qwen2 outperforms most open-source models across a range of benchmarks, including language understanding, language generation, multilingual capabilities, coding, mathematics, and reasoning, demonstrating competitiveness with proprietary models. Qwen2-7B-Instruct supports a context length of up to 131,072 tokens, enabling it to handle large inputs.
    - [Qwen2-1.5B-Instruct](https://huggingface.co/Qwen/Qwen2-1.5B-Instruct): Qwen2-1.5B-Instruct is an instruction-tuned language model released by Alibaba Group in 2024. Additionally, Qwen2-1.5B-Instruct is also a mixture of experts (MoE) model.
    - [GLM4-9b-Chat](https://huggingface.co/THUDM/glm-4-9b-chat): GLM4-9b-Chat is the open-source version of the latest generation of pre-trained models in the GLM4 series, launched by Zhipu AI. In evaluations across various datasets, including those for semantics, mathematics, reasoning, code, and knowledge, both GLM4-9b and its human preference-aligned version, GLM4-9b-Chat, demonstrated high performance.
    - [ChatGLM3-6b](https://huggingface.co/THUDM/chatglm3-6b): ChatGLM3-6b is the latest generation open-source model in the ChatGLM series. While retaining many of the excellent features of the previous two generations, such as smooth conversation and low deployment thresholds, ChatGLM3-6b introduces more diverse training data, more extensive training steps, and improved training strategies. It also supports tool invocation and code execution.
    - [ChatGPT](https://platform.openai.com/docs/models/gpt-3-5-turbo): ChatGPT is a LLM developed by OpenAI. It is a deep learning model based on the transformer architecture, capable of modeling and generating language. ChatGPT can handle a variety of tasks, including question answering, conversation generation, and text generation.
    - [Gemma2-9b-IT](https://huggingface.co/google/gemma-2-9b-it): Gemma2-9b-IT is a lightweight, state-of-the-art open model series launched by Google, built using the same research and technology that created the Gemini models. The Gemma2-9b-IT model is well-suited for various text generation tasks, including question answering, summarization, and reasoning. Due to its relatively small size, Gemma2-9b-IT can be deployed in resource-constrained environments, e.g., laptops, etc.
    - [GPT-4o mini](https://platform.openai.com/docs/models/gpt-4o-mini): GPT-4o mini is a multimodal large model that supports input and output for text, images, video, and audio, with a maximum context length of 128K tokens. The training knowledge of GPT-4o mini is up-to-date as of October 2023.
    - [WizardLM-2-7B](https://huggingface.co/dreamgen/WizardLM-2-7B): WizardLM-2-7B is an advanced LLM developed by Microsoft in 2024. WizardLM-2-7B shows significant improvements in complex conversations, multilingual capabilities, reasoning, and agent-based tasks.
