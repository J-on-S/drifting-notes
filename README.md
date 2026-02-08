# Drifting Notes

A sea of notes just waiting to be heard!
Check out our [site](https://drifting-notes.vercel.app/)

Lightweight note-exchange project with a small Flask backend and a simple static frontend. Intended as a minimal demo/project for sending and receiving short messages (notes) between clients.

## Key Features

- Simple Flask API with two endpoints: `/api/send` and `/api/receive`.
- Static frontend files for quick demos and local testing.
- Small, easy-to-read codebase suitable for hackdays and prototypes.

## Repository Layout

- Flask_backend/ — Flask backend and server code
   - [Flask_backend/app.py](Flask_backend/app.py) — main Flask app
   - [Flask_backend/requirements.txt](Flask_backend/requirements.txt) — Python dependencies
   - [Flask_backend/mongo_client.py](Flask_backend/mongo_client.py) — MongoDB helper
- Hack2026_website/ — static frontend demo pages (copied manually to `static`)
   - [Hack2026_website/driftingnotes.html](Hack2026_website/driftingnotes.html)
   - [Hack2026_website/readmessage.html](Hack2026_website/readmessage.html)
   - [Hack2026_website/sendmessage.html](Hack2026_website/sendmessage.html)

## Quickstart (Development)

Prerequisites:

- Python 3.8+ (3.10 recommended)
- Optional: MongoDB if you plan to enable persistence via `mongo_client.py`

Backend:

1. Create and activate a virtual environment:

```bash
cd Flask_backend
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies and run the Flask app:

```bash
pip install -r requirements.txt
export FLASK_APP=app.py
flask run --host=127.0.0.1 --port=5000
```

The backend exposes these endpoints (simple demo responses):

- `GET /api/receive` — placeholder endpoint to receive a note
- `GET /api/send` — placeholder endpoint to send a note

Frontend (static demo):

We use vercel for website hosting and api.

## Usage Examples

Open the static demo pages in your browser to view/send notes.

## Development Notes

- The backend currently returns placeholder text for the API routes in [Flask_backend/app.py](Flask_backend/app.py). Extend these handlers to integrate with `mongo_client.py` or other storage.
- See [Flask_backend/pymongo_test_query.py](Flask_backend/pymongo_test_query.py) for example MongoDB queries used during development.

## Contributing

Contributions are welcome. Suggested workflow:

1. Fork the repository and create a feature branch.
2. Add tests or a short demo showing the change.
3. Open a pull request describing your change.

For significant changes, open an issue first to discuss the design.

## Where to get help

- Open an issue in this repository with reproduction steps and expected behavior.
- For quick questions, contact the maintainers listed in the repository (if provided).
