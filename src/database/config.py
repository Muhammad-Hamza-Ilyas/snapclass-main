import streamlit as st

try:
    import supabase
    st.write("Supabase module:", supabase)
    st.write("Supabase file:", getattr(supabase, "__file__", "No file"))
    st.write("Supabase version:", getattr(supabase, "__version__", "Unknown"))

    from supabase import create_client

    supabase_client = create_client(
        st.secrets["SUPABASE_URL"],
        st.secrets["SUPABASE_KEY"]
    )

except Exception as e:
    st.exception(e)
    raise