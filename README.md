# Flask Backend

Simple Flask API with two POST endpoints:

- `/process` — accepts JSON {"name": "...", "email": "..."}
- `/api/process` — same behavior

Quickstart

1. Create a virtualenv and activate it:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the server:

```bash
python app.py
```
