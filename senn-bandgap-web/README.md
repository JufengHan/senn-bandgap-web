# SENN Bandgap Web App

This is an independent Streamlit web app for the `senn-bandgap` Python package.

Users can open the deployed web page, input perovskite composition coefficients, and click **Predict Bandgap** to obtain the predicted bandgap in eV.

## Files

```text
senn-bandgap-web/
├── app.py
├── requirements.txt
├── README.md
└── .streamlit/
    └── config.toml
```

## Local Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

Then open the local URL shown in the terminal, usually:

```text
http://localhost:8501
```

## Deploy on Streamlit Community Cloud

1. Create a new GitHub repository, for example `senn-bandgap-web`.
2. Upload `app.py`, `requirements.txt`, `README.md`, and `.streamlit/config.toml`.
3. Open Streamlit Community Cloud.
4. Click **New app**.
5. Choose your GitHub repository.
6. Set **Main file path** to:

```text
app.py
```

7. Click **Deploy**.

After deployment, Streamlit will generate a public web link for the app.
