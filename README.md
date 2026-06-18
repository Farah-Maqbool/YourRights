# YourRights

**YourRights** is an AI-powered legal rights explainer that helps Pakistani citizens understand their legal rights in plain language. Describe your situation and get clear guidance on relevant laws, your rights, and concrete steps you can take.

## The Problem

Most Pakistanis don't know their legal rights. Lawyers are expensive and inaccessible. When something happens — police stops you, employer doesn't pay, landlord harasses you — you don't know what you can legally do.

## The Solution

Describe your situation in plain Urdu or English → YourRights finds the relevant Pakistani law → explains your rights and next steps in simple language.

---

## Architecture

YourRights uses a multi-agent system built on CrewAI with three specialized agents working sequentially:

1. **Situation Analyzer** — understands the legal context of your situation
2. **Law Retriever** — searches Pakistani legal documents via RAG + Tavily web search
3. **Rights Explainer** — translates legal language into clear, actionable guidance

---

## Tech Stack

* **CrewAI** — multi-agent orchestration
* **Groq (LLaMA 3.3 70B)** — LLM inference
* **ChromaDB** — vector database for legal document retrieval
* **HuggingFace Sentence Transformers** — document embeddings
* **Tavily** — real-time web search for recent legal updates
* **Streamlit** — frontend
* **RAG Pipeline** — Constitution of Pakistan, Pakistan Penal Code (PPC), Code of Criminal Procedure (CrPC)

---

## Legal Documents

* Constitution of Pakistan (with 27th Amendment)
* Pakistan Penal Code (PPC) 1860
* Code of Criminal Procedure (CrPC) 1898

---

## Live Demo

Try the deployed application:

**https://yourrights.streamlit.app/**

---

## Run Locally

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

## Environment Variables

Create a `.env` file and add:

```env
GROQ_API_KEY=your_key
TAVILY_API_KEY=your_key
MODEL=groq/llama-3.3-70b-versatile
```

---

## ⚠️ Disclaimer

YourRights provides **legal information only**, not legal advice. The information generated may be incomplete, outdated, or not applicable to your specific situation. Always consult a qualified lawyer or legal professional for advice regarding your individual circumstances.
