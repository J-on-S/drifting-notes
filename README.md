# Drifting Notes

A sea of notes just waiting to be heard!

Check out our [site](https://drifting-notes.vercel.app/)
and start sending and receiving anonymous notes accompanied by music now!

## Key Features

We have a frontend (html, css, js) and a backend (python/flask on Vercel, MongoDB Atlas)

- Simple HTML, JS and CSS for the win.
- Handcrafted background images for an original look and feel
- App is split into a website and server folder for easy collaboration.
- Flask (python) API routes
  - `POST` `/api/send`: HTML Form
  Performs data validation before saving a note to the database.
  Displays an error page on failure or redirects to a thank you page on success.
  - `GET` `/api/receive`: JSON
  Finds a drifting note in the sea that is our database.
  That note is given back as JSON (a data format that's JS handles well)
- Flask static directory:
  Our website and images are stored here and are served by our flask app.
- Database Password is NOT in this repository.
  - Instead, we pass it as an environment variable.

## What we have learned

- Make git branches early on, or suffer the wrath of the merge conflict
- Discuss up front the tools you'll use; it makes life so much easier.
- Vercel is great for hosting :)
- MongoDB Atlas works lovely

## Repository Layout

- Flask_backend/ — Flask backend and server code
   - [Flask_backend/app.py](Flask_backend/app.py) — Flask app
   - [Flask_backend/requirements.txt](Flask_backend/requirements.txt) — Python dependencies
   - [Flask_backend/mongo_client.py](Flask_backend/mongo_client.py) — MongoDB helper
- Hack2026_website/ — frontend demo pages (copied manually to `static`)
   - [Hack2026_website/driftingnotes.html](Hack2026_website/driftingnotes.html)
   - [Hack2026_website/readmessage.html](Hack2026_website/readmessage.html)
   - [Hack2026_website/sendmessage.html](Hack2026_website/sendmessage.html)

## Quickstart (Deployment)

Prerequisites:

- An account on Vercel
- A fork of this Repository

Go to Vercel and deploy your fork as an app. It's as simple as that!

## Contributing

Contributions are welcome (even if unexpected, lol).

1. Fork the repository and create a feature branch.
2. Add tests or a short demo showing the change.
3. Open a pull request describing your change.
