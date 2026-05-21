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
* **MCP Host:** Perplexity AI
* **MCP Client:** Perplexity's client connecting to my Localhost (`http://127.0.0.1:8000`)
* **MCP Server:** FastAPI-based backend providing carbon footprint data, FastMCP (handles requests and communicates with FastAPI)

**Flow:**

```
User Query → MCP Host → MCP Client → FastAPI Server → JSON Dataset → Client → Host → Response
```

---

## 🗂️ Dataset

The project uses a curated Indian Food Carbon Footprint dataset, originally sourced from Kaggle. It contains information on carbon footprints for various Indian foods along with their region(s) of origin.

**Dataset Pre-Processing**

* Region Normalization: Multiple regions listed for a single food item were standardized into a consistent, alphabetically sorted, comma-separated format.
* Unique ID Assignment: Each food item was assigned a unique identifier based on its region combination and order within that group.
* Format: The dataset is stored in JSON format.

**Key Columns**
* ID → Unique identifier for the food item
* Food → Name of the food item
* Region → Single or combination of regions (e.g., "North, West")
* Category → Food type (e.g., Veg, Non-Veg)
* Serving → Standard serving size
* Carbon Footprint(kg CO2e) → Emissions in kg CO₂ per kg of food

---

## 🛠️ Tech Stack

* **Python 3.11**
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

2. Create a virtual environment using `uv`:

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










