# :zap: Fuzzy-Assisted Contrastive Decoding Improving Code Generation of Large Language Models

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
    - [DeepSeek-Chat](https://huggingface.co/meta-llama/Meta-Llama-3-8B): DeepSeek-Chat is a mixture of experts (MoE) language model developed by the DeepSeek-AI organization in 2024. It was pre-trained on a diverse, high-quality corpus of 8.1 trillion tokens and is characterized by economical training and efficient inference.
    - [Llama3.1-8b](https://huggingface.co/codellama/CodeLlama-7b-hf): The CodeLlama-7b model is a specialized version of the Llama model, fine-tuned to enhance its capabilities for specific tasks, such as code generation and code comprehension. This model, developed by Meta AI, leverages the foundational architecture of Llama but incorporates targeted optimizations to improve its performance in programming-related activities. It is designed to excel in generating accurate and functional code across various programming languages, as well as understanding and analyzing code structures, making it a valuable tool for developers and researchers working on coding tasks and software development projects.
    - [Qwen2-7B-Instruct](https://huggingface.co/bigcode/starcoder): The StarCoder model, boasting 15.5 billion parameters, is a sophisticated large language model meticulously trained on a diverse dataset encompassing over 80 programming languages sourced from Stack (version 1.2). This extensive training enables StarCoder to excel in a wide range of coding tasks, leveraging the rich and varied codebases available in the Stack dataset. Designed to support advanced code generation and comprehension, the model benefits from its broad exposure to multiple programming paradigms and syntaxes, making it a powerful tool for developers and researchers working across numerous programming environments.
    - [Qwen2-1.5B-Instruct](https://huggingface.co/WizardLMTeam/WizardCoder-15B-V1.0): The WizardCoder-15b model is an advanced large language model that has been meticulously fine-tuned using the Evol-Instruct methodology, specifically tailored for enhancing the capabilities of Code-centric LLMs. This fine-tuning process optimizes the model’s performance in programming-related tasks, such as code generation, debugging, and code comprehension, by leveraging the Evol-Instruct approach to refine its understanding of coding patterns and problem-solving strategies. With 15 billion parameters, WizardCoder-15b is designed to deliver superior results in software development and computational tasks, making it a powerful tool for developers and researchers working on complex coding challenges.


  \noindent
$\bullet$ \textbf{DeepSeek-Chat}~\citep{liu2024deepseek}. DeepSeek-Chat is a mixture of experts (MoE) language model developed by the DeepSeek-AI organization in 2024. It was pre-trained on a diverse, high-quality corpus of 8.1 trillion tokens and is characterized by economical training and efficient inference.

\noindent
$\bullet$ \textbf{Llama3.1-8b}~\footnote{\url{https://github.com/meta-llama/llama-models/tree/main.}}. Llama3.1-8b is a multilingual LLM developed by the Meta team in 2024 through pre-training. It utilizes an optimized transformer architecture as an autoregressive language model. The fine-tuned version incorporates supervised fine-tuning (SFT) and Reinforcement Learning with human feedback (RLHF) to align with human preferences for usefulness and safety.

\noindent
$\bullet$ \textbf{Qwen2-7B-Instruct}~\citep{yang2024qwen2}. Qwen2-7B-Instruct is a new series of Qwen LLMs. Compared to the previously released Qwen1.5, Qwen2 outperforms most open-source models across a range of benchmarks, including language understanding, language generation, multilingual capabilities, coding, mathematics, and reasoning, demonstrating competitiveness with proprietary models. Qwen2-7B-Instruct supports a context length of up to 131,072 tokens, enabling it to handle large inputs.

\noindent
$\bullet$ \textbf{Qwen2-1.5B-Instruct}~\citep{yang2024qwen2}. Qwen2-1.5B-Instruct is an instruction-tuned language model released by Alibaba Group in 2024. Additionally, Qwen2-1.5B-Instruct is also a mixture of experts (MoE) model.

\noindent
$\bullet$ \textbf{GLM4-9b-Chat}~\citep{glm2024chatglm}. GLM4-9b-Chat is the open-source version of the latest generation of pre-trained models in the GLM4 series, launched by Zhipu AI. In evaluations across various datasets, including those for semantics, mathematics, reasoning, code, and knowledge, both GLM4-9b and its human preference-aligned version, GLM4-9b-Chat, demonstrated high performance.

\noindent
$\bullet$ \textbf{ChatGLM3-6b}~\citep{glm2024chatglm}. ChatGLM3-6b is the latest generation open-source model in the ChatGLM series. While retaining many of the excellent features of the previous two generations, such as smooth conversation and low deployment thresholds, ChatGLM3-6b introduces more diverse training data, more extensive training steps, and improved training strategies. It also supports tool invocation and code execution.

\noindent
$\bullet$ \textbf{ChatGPT}~\footnote{\url{https://platform.openai.com/docs/models/gpt-3-5-turbo.}}. ChatGPT is a LLM developed by OpenAI. It is a deep learning model based on the transformer architecture, capable of modeling and generating language. ChatGPT can handle a variety of tasks, including question answering, conversation generation, and text generation.

\noindent
$\bullet$ \textbf{Gemma2-9b-IT}~\citep{gemma_2024}. Gemma2-9b-IT is a lightweight, state-of-the-art open model series launched by Google, built using the same research and technology that created the Gemini models. The Gemma2-9b-IT model is well-suited for various text generation tasks, including question answering, summarization, and reasoning. Due to its relatively small size, Gemma2-9b-IT can be deployed in resource-constrained environments, e.g., laptops, etc.

\noindent
$\bullet$ \textbf{GPT-4o mini}~\footnote{\url{https://platform.openai.com/docs/models/gpt-4o-mini.}}. GPT-4o mini is a multimodal large model that supports input and output for text, images, video, and audio, with a maximum context length of 128K tokens. The training knowledge of GPT-4o mini is up-to-date as of October 2023.

\noindent
$\bullet$ \textbf{WizardLM-2-7B}~\footnote{\url{https://wizardlm.github.io/WizardLM2/.}}. WizardLM-2-7B is an advanced LLM developed by Microsoft in 2024. WizardLM-2-7B shows significant improvements in complex conversations, multilingual capabilities, reasoning, and agent-based tasks.
