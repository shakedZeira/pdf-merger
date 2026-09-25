import shutil
import tempfile
from pathlib import Path

from flask import Flask, after_this_request, render_template, request, send_file
from pypdf import PdfWriter

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 1024 * 1024 * 1024


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/merge", methods=["POST"])
def merge():
    files = request.files.getlist("pdfs")
    pdfs = [f for f in files if f and f.filename and f.filename.lower().endswith(".pdf")]
    if not pdfs:
        return "No PDF files uploaded.", 400

    tmp_dir = tempfile.mkdtemp(prefix="pdfmerge-")
    try:
        paths = []
        for i, f in enumerate(pdfs):
            path = Path(tmp_dir) / f"{i:04d}-{Path(f.filename).name}"
            f.save(path)
            paths.append(path)

        output_path = Path(tmp_dir) / "merged.pdf"
        try:
            writer = PdfWriter()
            for path in paths:
                writer.append(path)
            with open(output_path, "wb") as out:
                writer.write(out)
        except Exception as exc:
            return f"Could not merge PDFs: {exc}", 400

        @after_this_request
        def cleanup(response):
            shutil.rmtree(tmp_dir, ignore_errors=True)
            return response

        return send_file(
            output_path,
            as_attachment=True,
            download_name="merged.pdf",
            mimetype="application/pdf",
        )
    except Exception:
        shutil.rmtree(tmp_dir, ignore_errors=True)
        raise


if __name__ == "__main__":
    app.run(debug=True)