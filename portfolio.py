import streamlit as st
import pandas as pd


def main():
    st.set_page_config(layout="wide")

    st.title("João Felipe Guedes")

    st.subheader("Senior Data Scientist @ Globo")

    "Hi! My name is João Felipe and..."

    st.markdown("### Contact")
    columns = st.columns(4)

    with columns[0]:
        st.write(
            ":man-frowning: [LinkedIn](https://www.linkedin.com/in/joao-felipe-guedes/)"
        )

    with columns[1]:
        st.write(":email: [Mail](mailto:guedes.joaofelipe@poli.ufrj.br)")

    with columns[2]:
        st.write(":male-technologist: [Github](https://github.com/guedes-joaofelipe)")

    with columns[3]:
        st.write(":pencil2: [Medium](https://medium.com/@guedes.joaofelipe)")


if __name__ == "__main__":
    main()
