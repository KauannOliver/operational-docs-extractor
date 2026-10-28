# Operational Documentation Extractor

A Selenium utility for exporting selected authenticated documentation pages as text.

**Python, Selenium**

## What it does

- Opens a configured login page and uses credentials supplied at runtime.
- Reads the selected page list from a local JSON file.
- Extracts page content into separate text files for later organization.

## Workflow

```mermaid
flowchart LR
  N0["Configured page list"] --> N1
  N1["Authenticated navigation"] --> N2
  N2["Content extraction"] --> N3
  N3["Text files"]
```

## Local setup and use

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python main.py
```
Python 3.11+ is recommended. Tkinter requires a desktop Python installation.
Copy `pages.example.json` to ignored `pages.local.json` and use only pages you are authorized to export. Set `DOCS_LOGIN_URL`, `DOCS_USERNAME`, `DOCS_PASSWORD` and optionally `DOCS_PAGES_FILE` in the process environment. Adapt the DOM selectors to your own portal.

## Configuration

Environment names declared by the included examples (values must be supplied locally):

`DOCS_PAGES_FILE`.

## Boundaries and limitations

The internal page inventory and all exported documentation have been removed. The example uses a non-routable demonstration domain. Portal DOM changes can break the selectors.

This is a source snapshot, not a claim of production readiness. Business results, dates and unmeasured performance are intentionally not asserted. Application UI language is preserved.

## License

No new distribution license is granted for this corporate source edition. Public visibility does not grant reuse rights; obtain permission from the relevant rights holder. Existing third-party notices remain applicable.

## Verification record

See [snapshot checks and remaining limitations](docs/VERIFICATION.md).
