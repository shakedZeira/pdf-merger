# PDF Merger

A simple Flask web application for combining multiple PDF files into one downloadable document.

## Features

- Upload multiple PDF files
- Reorder files before merging
- Remove unwanted files from the upload list
- Download the result as `merged.pdf`
- Remove temporary files after each request

## Requirements

- Windows 10 or Windows 11
- Python 3.9 or newer
- Git, if you want to clone the repository

Confirm that Python is installed by opening PowerShell and running:

```powershell
py --version
```

## Run Locally

### 1. Clone the repository

```powershell
git clone https://github.com/shakedZeira/pdf-merger.git
cd pdf-merger
```

If you already downloaded the repository, open PowerShell in the project folder and continue with the next step.

### 2. Create a virtual environment

```powershell
py -m venv .venv
```

### 3. Activate the virtual environment

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks the activation script, allow it for the current terminal session and run the command again:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 5. Start the application

```powershell
python app.py
```

The terminal should show that Flask is running on `http://127.0.0.1:5000`. Open that address in your browser.

To stop the application, return to the PowerShell window and press `Ctrl+C`.

## Usage

1. Click the upload area or drag PDF files into it.
2. Use the arrow buttons to change the merge order.
3. Click the **×** button to remove a file.
4. Click **Merge PDFs**.
5. The merged document is downloaded as `merged.pdf`.

Files are merged from top to bottom in the order shown in the browser.

## Troubleshooting

### `py` is not recognized

Install Python 3.9 or newer from [python.org](https://www.python.org/downloads/windows/), make sure the Python launcher is available, and reopen PowerShell.

### PowerShell cannot load `Activate.ps1`

Run the following command and then try activating the environment again:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

### Port 5000 is already in use

Change the Flask startup line in `app.py` to use another port:

```python
app.run(debug=True, port=5001)
```

Then open `http://127.0.0.1:5001` in the browser.

### A PDF cannot be merged

Make sure the file is a valid, unencrypted PDF with a `.pdf` extension. Password-protected PDFs are not supported by this application.

## Project Structure

```text
pdf-merger/
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
└── .gitignore
```
