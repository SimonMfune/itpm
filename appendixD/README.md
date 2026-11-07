# Appendix D companion files

Code and data for Appendix D of *Information Technology Project Management: Traditional Foundations, Agile Delivery and AI-Enhanced Practice* (Simon Mfune, DevDash Professional).

Repository: https://github.com/SimonMfune/itpm

| File | Purpose |
|---|---|
| `pm_analytics.py` | The script built in Listings D.1 to D.7 |
| `data/healthsync_sprints.csv` | HealthSync sprint data (illustrative) |
| `data/migration_network.csv` | Migration and cutover network for the Monte Carlo schedule |
| `.github/workflows/ci.yml` | The continuous integration workflow in Listing D.8 |
| `requirements.txt` | Python packages |
| `run_output.txt` | Expected output, for checking your run |

Run it:

```
python -m venv .venv
.venv/bin/pip install -r requirements.txt   # on Windows: .venv\Scripts\pip
.venv/bin/python pm_analytics.py
```

All data is fictional and used for teaching.
