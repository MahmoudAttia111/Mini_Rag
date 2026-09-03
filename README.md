# Mini-RAG

This is a minimal implementation of the RAG (Retrieval-Augmented Generation) model for question answering.

## The Course

This is an educational project where all of the code was explained (step by step) via a set of Arabic YouTube videos by Abu Bakr (bakrianoo). This repository documents my own implementation while following along with the course.

| # | Title | Link | Codes |
|---|---|---|---|
| 1 | About the Course ماذا ولمـــاذا | Video | NA |
| 2 | What will we build ماذا سنبنى في المشروع | Video | NA |
| 3 | Setup your tools الأدوات الأساسية | Video | NA |
| 4 | Project Architecture | Video | branch |
| 5 | Welcome to FastAPI | Video | branch |
| 6 | Nested Routes + Env Values | Video | branch |
| 7 | Uploading a File | Video | branch |
| 8 | MongoDB Integration | Video | branch |
| 9 | Indexes, Assets & Docker Credentials | Video | tutorial-06 |

## Requirements

- Python 3.10 or later

### Install Python using MiniConda

1. Download and install MiniConda from [here](https://docs.anaconda.com/free/miniconda/#quick-command-line-install)
2. Create a new environment using the following command:
```bash
$ conda create -n mini-rag python=3.10
```
3. Activate the environment:
```bash
$ conda activate mini-rag
```

(Optional) Setup your command line interface for better readability:
```bash
export PS1="\[\033[01;32m\]\u@\h:\w\n\[\033[00m\]\$ "
```

## Installation

### Install the required packages
```bash
$ pip install -r requirements.txt
```

### Setup the environment variables
```bash
$ cp .env.example .env
```

Set your environment variables in the `.env` file. Like `OPENAI_API_KEY` and `MONGODB_URL` values.

### Database Setup

This project supports two options for MongoDB:

**Option 1: MongoDB Atlas (Cloud)**

Use a MongoDB Atlas connection string directly in your `.env` file:

MONGODB_URL=mongodb+srv://<username>:<password>@<cluster>.mongodb.net/?appName=Cluster0
MONGODB_DATABASE=mini_rag_db


**Option 2: Run MongoDB locally with Docker Compose**
```bash
$ cd docker
$ cp .env.example .env
```
Update `.env` with your own MongoDB credentials, then:
```bash
$ sudo docker compose up -d
```
Update your project's `.env` `MONGODB_URL` to point to `localhost:27007` with the credentials you set.

### Run the FastAPI server
```bash
$ uvicorn src.main:app --reload --host 0.0.0.0 --port 5000
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/v1/` | Welcome / health check |
| POST | `/api/v1/data/upload/{project_id}` | Upload a file (txt/pdf) to a project |
| POST | `/api/v1/data/process/{project_id}` | Process an uploaded file (or all project files) into chunks |

## POSTMAN Collection

Download the POSTMAN collection from `/src/assets/mini-rag-app.postman_collection.json`

## Project Structure

src/
├── controllers/ # Business logic (file validation, processing, project paths)
├── helpers/ # App configuration and settings
├── models/
│ ├── db_schemes/ # Pydantic schemas (Project, DataChunk, Asset)
│ ├── enums/ # Enums (DataBaseEnum, ResponseEnums, ProcessingEnum, AssetTypeEnum)
│ └── *Model.py # Async database models (ProjectModel, ChunkModel, AssetModel)
├── routes/ # FastAPI routers (base, data)
└── main.py # FastAPI application entrypoint
