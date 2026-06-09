import streamlit as st
def style_background_home():
    st.markdown("""
    <style>
    /* Prevent overall page scrolling */
    [data-testid="stAppViewContainer"] { 
        height: 100vh !important; 
        overflow: hidden !important; 
    }
    
    /* The fix: Use 98vh max and force border-box sizing */
    [data-testid="stMainBlockContainer"] { 
        box-sizing: border-box !important;
        height: 98vh !important; 
        max-height: 98vh !important; 
        overflow: hidden !important; 
        display: flex !important; 
        flex-direction: column !important; 
        justify-content: flex-start !important; 
        align-items: center !important;
        padding-top: 1rem !important; 
        padding-bottom: 1rem !important; 
    }

    /* Keep the main layout snug */
    [data-testid="stHorizontalBlock"] { 
        max-height: 50vh !important; 
        margin-top: 1rem !important; 
    }

    /* Safely anchor the footer to the visible floor */
    [data-testid="stMainBlockContainer"] > div:last-child {
        margin-top: auto !important; 
        padding-bottom: 0.5rem !important;
    }

    /* Main background color */
    .stApp {
        background: #5865F2 !important;
    }

    /* Custom styled student/teacher column cards */
    .stApp div[data-testid="stColumn"] {
        background-color: #E0E3FF !important;
        padding: 1.5rem 2.0rem !important;
        border-radius: 4rem !important;
    }
    </style>
    """, unsafe_allow_html=True)

def style_background_dashboard():

    st.markdown("""
        <style>
              .stApp {
                background: #E0E3FF !important;
                }  
        </style>
                
                """
                ,unsafe_allow_html=True)

def style_base_layout():

    st.markdown("""
        <style>
                
                
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&family=Outfit:wght@100..900&display=swap');

                
        
                #MainMenu, footer, header{
                visibility: hidden;
                }

                .block-container{
                padding-top:1.5rem !important
                }

                h1 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 3.5rem !important;
                line-height:1.1 !important;
                margin-bottom:0rem !important;
                }

                h2 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 2rem !important;
                line-height:0.9 !important;
                margin-bottom:0rem !important;
                }

                h3, h4, p{
                font-family:'Outfit', sans-serif;
                }

                button{
                border-radius: 1.5rem !important;
                background: #5865F2 !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

                button[kind="secondary"] {
                border-radius: 1.5rem !important;
                background: #EB459E !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                 transition: transform 0.25s ease-in-out !important;
                    }
                
                button[kind="tertiary"] {
                border-radius: 1.5rem !important;
                background: black !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important
                }

                button:hover{
                transform : scale(1.05)}

        </style>
                
                """
                ,unsafe_allow_html=True)