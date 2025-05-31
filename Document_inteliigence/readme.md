# 🧠 Document Intelligence Platform

A full-stack web app that allows users to upload documents and ask intelligent, context-aware questions based on their contents using **Retrieval-Augmented Generation (RAG)**.

---

## 🚀 Features

- 📤 Upload PDF, DOCX, or TXT files
- 🧠 Ask questions based on document content
- 🗂️ Automatic document chunking & vector embedding
- ⚡ Real-time answers using RAG pipeline
- 🌐 REST APIs using Django
- 🎨 Beautiful UI using Next.js + Tailwind CSS

---

## 🔧 Tech Stack

| Layer       | Technology              |
|-------------|--------------------------|
| Frontend    | Next.js, Tailwind CSS    |
| Backend     | Django, Django REST Framework |
| AI/RAG      | ChromaDB or FAISS, OpenAI |
| Storage     | Django FileSystem        |
| Vector Store| FAISS / ChromaDB         |

---

## 📁 Folder Structure

document-intelligence-platform/
├── backend/ # Django Backend
│ ├── documents/ # App: Models, Views, Serializers
│ ├── backend/ # Django Project Config
│ ├── media/ # Uploaded documents
│ ├── manage.py
│ └── requirements.txt
├── frontend/ # Next.js Frontend
│ ├── app/ or pages/ # App/page routes
│ ├── public/
│ ├── styles/
│ ├── .env.local # API config
│ └── package.json



---

## ⚙️ Step-by-Step Setup

### 🐍 1. Backend Setup (Django)

# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# OR (macOS/Linux)
source venv/bin/activate

# Install required packages
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate

# Run backend server
python manage.py runserver



# Navigate to frontend
cd ../frontend

# Install Node.js packages
npm install

# Create .env.local file
echo "NEXT_PUBLIC_API_URL=http://127.0.0.1:8000/api" > .env.local

# Start the frontend dev server
npm run dev
