import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Pure Business Capital Pro AI Dashboard", layout="wide", page_icon="💰")

# ================== CONFIG ==================
PASSWORD = "PureBCPro2026"   # ← Make sure this matches your new password
PRO_LINK = "https://whop.com/purebizcap/pro-ai-dashboard/"

PRODUCTS = {
    "Shelf Corporation Mastery": {"price": "$347", "link": "https://whop.com/purebizcap/shelf-corporation-mastery/", "desc": "Complete training to launch your own aged shelf corporation business."},
    "Training Access": {"price": "Enroll Now", "link": "https://whop.com/purebizcap/training-access-a6/", "desc": "Full access to Hard Money Mastery, Private Capital, and more."},
    "Shelf Corporation Reseller Program": {"price": "Join Now", "link": "https://whop.com/purebizcap/shelf-corporation-reseller/", "desc": "Resell shelf corporations + earn commissions."},
    "Careers / Remote Agent Program": {"price": "Apply Free", "link": "https://purebusinesscapital.com/careers", "desc": "Remote, no-experience-needed opportunities."}
}

# Header
st.markdown("<h1 style='text-align: center; color: #FFFFFF;'>PURE BUSINESS CAPITAL</h1>", unsafe_allow_html=True)

# Password Gate
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.title("🔒 Pure Business Capital Pro AI Lead Mastery Dashboard")
    st.markdown("### Pro Member Only – $97/month")
    st.write("Unlock the full dashboard with CRM, lead tools, scripts, role-play, TikTok generator, and ROI tracking.")
    
    password_input = st.text_input("Enter your Pro Password", type="password")
    if st.button("Unlock Dashboard", type="primary"):
        if password_input == PASSWORD:
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Incorrect password.")
    st.link_button("Get Pro Access – $97/month", PRO_LINK)
    st.stop()

# ================== FULL DASHBOARD LOADS HERE ==================
st.success("✅ Unlocked – Welcome to the Pro AI Dashboard!")

st.markdown("### Lead Mastery Dashboard – Your 24/7 Coach")
st.caption("Pro Member Only • Pure Business Capital")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", [
    "🏠 Home", 
    "🔍 Lead Generation", 
    "📋 My CRM", 
    "📝 Scripts Library", 
    "🎤 Role-Play Simulator", 
    "📱 TikTok Script Generator", 
    "📈 ROI & Goal Tracker", 
    "🚀 Upsells & Products", 
    "✅ Compliance"
])

# HOME
if page == "🏠 Home":
    st.write("Welcome to your Pro dashboard! Use the sidebar to access all tools.")
    col1, col2, col3 = st.columns(3)
    with col1: st.metric("Leads This Week", "18", "↑ 5")
    with col2: st.metric("Avg Reply Rate", "22%", "↑ 4%")
    with col3: st.metric("Projected Revenue", "$12,450", "↑ $2,300")

# MY CRM
elif page == "📋 My CRM":
    st.header("📋 My CRM")
    if "crm_df" not in st.session_state:
        st.session_state.crm_df = pd.DataFrame(columns=["Name", "Company", "Title", "Lead Source", "Status", "Last Contact", "Next Follow-up", "Notes", "Value Potential"])
    edited_df = st.data_editor(st.session_state.crm_df, num_rows="dynamic", use_container_width=True)
    st.session_state.crm_df = edited_df
    if st.button("Export CSV"):
        csv = edited_df.to_csv(index=False)
        st.download_button("Download CSV", csv, "my_leads.csv", "text/csv")

# Simple placeholders for other tabs (we can expand them later)
else:
    st.write(f"**{page}** tab is active. This section is ready for full features.")

st.sidebar.caption("Pro AI Dashboard • Pure Business Capital")
