# Spider Links

Spider Links is a small local web application served by Python's standard
library. It provides a colorful page for opening, adding, and removing
personal quick links.

## Run

Requires Python 3.8 or newer.

```powershell
python web3.py
```

Open <http://127.0.0.1:8000> in a browser. Press `Ctrl+C` in the terminal to
stop the server.

The page stores added links in the browser's local storage, so no database or
third-party package is required.

## Features

- Opens links in a new tab with safe external-link handling.
- Validates that new links use `http` or `https`.
- Supports reduced-motion preferences and responsive layouts.

## Project layout

- `web3.py` contains the HTTP server and the embedded web page.
- `run.bat` starts the server from Windows Explorer or a terminal.
