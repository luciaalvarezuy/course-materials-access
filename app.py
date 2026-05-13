import streamlit as st
from datetime import datetime
import pandas as pd


st.set_page_config(
    page_title="Materials del curs",
    page_icon="📘",
    layout="centered"
)


def load_config():
    return {
        "title": st.secrets["app"]["title"],
        "start_time": st.secrets["app"]["start_time"],
        "end_time": st.secrets["app"]["end_time"],
        "code_a": st.secrets["versions"]["code_a"],
        "code_b": st.secrets["versions"]["code_b"],
        "url_a": st.secrets["versions"]["url_a"],
        "url_b": st.secrets["versions"]["url_b"],
    }


def get_resource(access_code, config):
    code = access_code.strip()

    if code == config["code_a"]:
        return True, "Material A", config["url_a"]

    if code == config["code_b"]:
        return True, "Material B", config["url_b"]

    return False, None, None


def create_log(resource_name):
    return pd.DataFrame(
        {
            "timestamp": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
            "resource": [resource_name],
        }
    )


try:
    config = load_config()
except Exception:
    st.error("La configuració no està disponible.")
    st.stop()


st.title("📘 Materials del curs")
st.subheader(config["title"])

st.info(f"Disponible de **{config['start_time']}** a **{config['end_time']}**.")

st.markdown(
    "Introduïu el codi d'accés indicat per obtenir el material corresponent."
)

access_code = st.text_input(
    "Codi d'accés",
    type="password",
    placeholder="Introdueix el teu codi"
)

if st.button("Accedir al material"):
    is_valid, resource_name, resource_url = get_resource(access_code, config)

    if is_valid:
        st.success(f"Codi correcte: **{resource_name}**")

        st.link_button(
            label="Abrir material",
            url=resource_url
        )

        log = create_log(resource_name)

        with st.expander("Registro"):
            st.dataframe(log, use_container_width=True)

    else:
        st.error("El codi ingressat no és correcte.")


st.divider()

st.caption("Eina d'accés als materials del curs")
st.caption(" IT Academy | Fundamentos ")
