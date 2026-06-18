# ⚖️ YourRights — Know Your Pakistani Legal Rights

**YourRights** is an AI-powered legal rights explainer that helps Pakistani citizens understand their legal rights in plain language. Describe your situation and get clear guidance on relevant laws, your rights, and concrete steps you can take.

## 🚨 The Problem

Most Pakistanis don't know their legal rights. Lawyers are expensive and inaccessible. When something happens — police stop you, employer doesn't pay, landlord harasses you — you don't know what you can legally do.

## 💡 The Solution

Describe your situation in plain Urdu or English → YourRights finds the relevant Pakistani law → explains your rights and next steps in simple language.

---

## ✨ Key Features

* 🔍 **Legal Document Retrieval (RAG)** — Searches Pakistani legal documents to find relevant laws and constitutional provisions.
* 🤖 **Multi-Agent AI Workflow** — Specialized agents analyze situations, retrieve legal information, and explain rights.
* 🌐 **Real-Time Legal Research** — Uses Tavily web search to supplement legal knowledge with recent information.
* 🇵🇰 **Pakistan-Focused** — Built specifically around Pakistani laws and legal documents.
* 🗣️ **Plain Language Explanations** — Converts complex legal language into easy-to-understand guidance.
* 📋 **Actionable Next Steps** — Provides practical guidance on what users can do next.
* ⚡ **Fast Responses** — Powered by Groq's high-speed LLM inference.

---

## 🏗️ Architecture

YourRights uses a multi-agent system built on CrewAI with three specialized agents working sequentially:

1. **Situation Analyzer** — Understands the legal context of the user's situation.
2. **Law Retriever** — Searches Pakistani legal documents using RAG and Tavily web search.
3. **Rights Explainer** — Translates legal language into clear, actionable guidance.

---

## 🛠️ Tech Stack

* **CrewAI** — Multi-agent orchestration
* **Groq (LLaMA 3.3 70B)** — LLM inference
* **ChromaDB** — Vector database for legal document retrieval
* **HuggingFace Sentence Transformers** — Document embeddings
* **Tavily** — Real-time web search
* **Streamlit** — Frontend application
* **RAG Pipeline** — Legal document retrieval system

---

## 📚 Legal Documents

* Constitution of Pakistan (with 27th Amendment)
* Pakistan Penal Code (PPC) 1860
* Code of Criminal Procedure (CrPC) 1898

---

## 🚀 Live Demo

Try the deployed application:

**https://yourrights.streamlit.app/**

---

## ⚙️ Run Locally

```bash
git clone https://github.com/Farah-Maqbool/YourRights.git
cd YourRights/yourrights

uv sync
uv add pdfplumber sentence-transformers tavily-python

# Build the vector database
python src/yourrights/rag_pipeline.py

# Run the application
streamlit run src/yourrights/app.py
```

---

## 🔑 Environment Variables

Create a `.env` file and add:

```env
GROQ_API_KEY=your_key
TAVILY_API_KEY=your_key
MODEL=groq/llama-3.3-70b-versatile
```

---

## ⚠️ Disclaimer

YourRights provides **legal information only**, not legal advice. The information generated may be incomplete, outdated, or not applicable to your specific situation. Always consult a qualified lawyer or legal professional for advice regarding your individual circumstances.
