import streamlit as st
import json
import pandas as pd

from models import Config
from exporter import export_xlsx
import tempfile

st.title("📊 Meta Ads Grid Generator")

uploaded_file = st.file_uploader("Завантаж JSON конфіг", type=["json"])

if uploaded_file is not None:
    raw = json.load(uploaded_file)

    try:
        cfg = Config.model_validate(raw)
        st.success("JSON успішно завантажено ✅")

        df = pd.DataFrame([r.model_dump() for r in cfg.rows])
        st.dataframe(df)

        if st.button("Generate Excel"):
            tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx")
            export_xlsx(cfg, tmp_file.name)

            with open(tmp_file.name, "rb") as f:
                st.download_button(
                    label="Download Excel",
                    data=f,
                    file_name="result.xlsx"
                )

    except Exception as e:
        st.error(f"Помилка JSON: {e}")
