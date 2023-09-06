import streamlit as st

PAGE_TITLE = "# ✍️ Publications"

st.markdown(PAGE_TITLE)
st.sidebar.markdown(PAGE_TITLE)


def get_contents(content_folder="content", content_type: str = None) -> list:
    import os
    import json

    contents = list()

    content_filenames = os.listdir("contents")

    for content_filename in content_filenames:
        with open(f"contents/{content_filename}") as f:
            content = json.load(f)

        if content.get("type") == content_type:
            contents.append(content)

    return contents


def display_content_grid(contents: list, column_length=3):
    for i, content in enumerate(contents):
        if i % column_length == 0:
            columns = st.columns(column_length)

        with columns[i]:
            display_content(
                image_path=content.get("image"),
                title=content.get("title"),
                publish_date=content.get("date"),
                publish_place=content.get("place"),
            )


def display_content(
    image_path, title: str, publish_date: str = None, publish_place: str = None
):
    st.markdown(f"### {title}")

    try:
        st.image(image_path)
    except:
        st.warning(f"Error opening image {image_path}")

    with st.expander(":heavy_plus_sign: Read More"):
        if publish_date:
            st.markdown(f"**Date**: {publish_date}")

        if publish_place:
            st.markdown(f"**Published at**: {publish_place}")


def main():
    tabs = st.tabs(["Academic Papers", "Blog Articles"])

    with tabs[0]:
        contents = get_contents(content_type="academic_paper")
        display_content_grid(contents)

    with tabs[1]:
        contents = get_contents(content_type="blog_article")
        display_content_grid(contents)


if __name__ == "__main__":
    main()
