import streamlit as st
import pandas as pd
import random
from datetime import datetime

st.set_page_config(page_title="Pure Business Capital Pro AI Dashboard", layout="wide", page_icon="💰")

# ================== CONFIG ==================
PASSWORD = "PureBCPro2026"   # ← Recommended new password (change if you want)
PRO_LINK = "https://whop.com/purebizcap/pro-ai-dashboard/"

PRODUCTS = {
    "Shelf Corporation Mastery": {"price": "$347", "link": "https://whop.com/purebizcap/shelf-corporation-mastery/", "desc": "Complete training to launch your own aged shelf corporation business."},
    "Training Access": {"price": "Enroll Now", "link": "https://whop.com/purebizcap/training-access-a6/", "desc": "Full access to Hard Money Mastery, Private Capital, and more."},
    "Shelf Corporation Reseller Program": {"price": "Join Now", "link": "https://whop.com/purebizcap/shelf-corporation-reseller/", "desc": "Resell shelf corporations + earn commissions."},
    "Careers / Remote Agent Program": {"price": "Apply Free", "link": "https://purebusinesscapital.com/careers", "desc": "Remote, no-experience-needed opportunities."}
}

# Header
st.markdown("<h1 style='text-align: center; color: #FFFFFF;'>PURE BUSINESS CAPITAL</h1>", unsafe_allow_html=True)
try:
    st.image("logo.png", use_column_width=True)
except:
    pass

# ================== IMPROVED PASSWORD GATE ==================
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.title("🔒 Pure Business Capital Pro AI Lead Mastery Dashboard")
    
    st.markdown("""
    ### Welcome to the Pro Version
    
    This exclusive dashboard is reserved for **$97/month Pro members** only.
    
    It includes:
    - Full CRM for lead management
    - AI-powered lead generation tools
    - Scripts, TikTok generators & role-play simulator
    - ROI tracker + weekly goals
    """)
    
    st.info("**Purchased on Whop?** Enter your Pro password below to unlock everything.")
    
    password_input = st.text_input("🔑 Enter Pro Password", type="password", placeholder="Enter your password here")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("🔓 Unlock Dashboard", type="primary", use_container_width=True):
            if password_input == PASSWORD:
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("❌ Incorrect password. Please check your Whop purchase confirmation.")
    with col2:
        st.link_button("🚀 Get Pro Access – $97/month", PRO_LINK, use_container_width=True)
    
    st.caption("Need the password? Check your Whop confirmation email or reply for help.")
    st.stop()

# ================== MAIN DASHBOARD (same as before) ==================
st.success("✅ Unlocked – Welcome to the Pro AI Dashboard!")

# ... (the rest of your dashboard code stays exactly the same as the last full version I gave you)

st.sidebar.caption("Pro AI Dashboard • Pure Business Capital • 2026")
