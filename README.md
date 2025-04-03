# AI_Blog_Generator

# 📝 AI Blog Content Generator

An interactive AI-powered web app built with **LangChain**, **Hugging Face Transformers**, and **Streamlit** that helps users generate engaging blog content based on a topic of their choice. From suggesting catchy titles to generating full-length blogs, this tool streamlines your content creation workflow.

---

LangChain is an open-source framework designed to simplify working with Large Language Models (LLMs) like GPT, LLaMA, or Falcon in production-grade applications. It lets you chain together LLM calls, prompts, tools, agents, and memory to build advanced NLP workflows.

Key Benefits:
Combines models + logic into modular chains

Supports tools like Hugging Face, OpenAI, Cohere, etc.

Includes PromptTemplates, LLM Wrappers, and Chain Classes

🛠️ LangChain in this Project
In this application, LangChain is used for:

Component	LangChain Feature Used	Purpose
Blog Title Generation	PromptTemplate + HuggingFaceEndpoint	Generates 10 catchy blog titles
Blog Content Generation	PromptTemplate + HuggingFaceEndpoint	Writes full blog post based on selected title and inputs
You're using PromptTemplate to structure your LLM queries and HuggingFaceEndpoint to access the LLaMA 3 model via Hugging Face.

🔄 SimpleSequentialChain vs SequentialChain
LangChain provides two helpful chaining utilities for running multiple prompts/tasks step-by-step.

✅ SimpleSequentialChain
Use Case: A linear sequence where output of one step becomes input of the next

Structure: No need to explicitly define input/output keys



## 🧠 Tech Stack

| Tool/Library       | Purpose                                           |
|--------------------|---------------------------------------------------|
| [Streamlit](https://streamlit.io/)        | Web UI framework                                  |
| [LangChain](https://www.langchain.com/)   | LLM orchestration and prompt templates             |
| [Hugging Face Hub](https://huggingface.co/) | LLM model hosting and API                         |
| LLaMA 3 (8B Instruct) | Transformer model for text generation               |
| Python `os` module  | Secure handling of API keys via environment variables |

---

## 📁 Project Structure

