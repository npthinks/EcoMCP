# EcoMCP

**EcoMCP** is an eco-intelligent MCP (Model Context Protocol) agent designed to provide **carbon footprint insights for Indian foods**. It combines a FastAPI backend with MCP integration to allow AI systems or other clients to query carbon footprint data efficiently.

---

## 🚀 Features

* Query carbon footprint data by **food name**, **region**, or **food ID**.
* Supports **partial matches** for food names.
* Handles **single and combination of regions**.
* MCP integration using **FastMCP** and **stdio transport**.
* API hosted locally using **FastAPI**.

---

## 🧩 Architecture Overview

* **Transport:** `stdio`
* **API Host:** Localhost (`http://127.0.0.1:8000`)
* **MCP Host:** Perplexity
* **MCP Client:** FastMCP (handles requests and communicates with FastAPI)
* **MCP Server:** FastAPI-based backend providing carbon footprint data

**Flow:**

```
User Query → MCP Host → MCP Client → FastAPI Server → JSON Dataset → Client → Host → Response
```

---

## 🛠️ Tech Stack

* **Python 3.11
* **FastAPI** (Backend API)
* **FastMCP** (MCP client integration)
* **Transport:** stdio
* **Cursor IDE** for development

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/npthinks/EcoMCP.git
cd EcoMCP
```

2. Create a virtual environment using `uv` or `venv`:

```bash
# Using uv
uv venv create .venv
uv venv activate
```
---

## 🏗️ Usage

### Running the FastAPI Server

```bash
uvicorn main:app --reload
```

* The server will run at `http://127.0.0.1:8000/`

---



