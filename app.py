import streamlit as st
import pandas as pd

st.set_page_config(page_title="Pure Business Capital Pro AI Dashboard", layout="wide", page_icon="💰")

# ================== CONFIG ==================
PASSWORD = "PureBCPro2026"   # ← Your current password
PRO_LINK = "https://whop.com/purebizcap/pro-ai-dashboard/"

# Header with logo
st.markdown("<h1 style='text-align: center; color: #FFFFFF;'>PURE BUSINESS CAPITAL</h1>", unsafe_allow_html=True)

try:
    st.image("logo.png", use_column_width=True)
except:
    st.caption("💰 Pure Business Capital")

# Password Gate - Nicer Version
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.title("🔒 Pure Business Capital Pro AI Lead Mastery Dashboard")
    
    st.markdown("""
    ### Welcome to the Pro Version
    
    This exclusive dashboard is for **$97/month Pro members** only.
    
    Inside you'll find:
    - Full CRM for managing leads
    - AI-powered LinkedIn & TikTok lead tools
    - Ready-to-use scripts and outreach templates
    - Sales call role-play simulator
    - TikTok video script generator
    - ROI calculator & weekly goal tracker
    """)
    
    st.info("**Purchased the Pro plan?** Enter your password below to unlock the full dashboard.")
    
    password_input = st.text_input("🔑 Enter Pro Password", type="password", placeholder="Enter password here")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("🔓 Unlock Dashboard", type="primary", use_container_width=True):
            if password_input == PASSWORD:
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("❌ Incorrect password. Please check your Whop purchase email.")
    with col2:
        st.link_button("🚀 Get Pro Access – $97/month", PRO_LINK, use_container_width=True)
    
    st.caption("Need help? Check your Whop confirmation or reply to support.")
    st.stop()

# ================== MAIN DASHBOARD ==================
st.success("✅ Unlocked – Welcome to the Pro AI Dashboard!")

st.markdown("### Lead Mastery Dashboard – Your 24/7 Coach for Real Estate & Finance Pros")
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
    st.write("Welcome to your Pro dashboard! Use the tools on the left to generate leads and scale your business.")
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

# Placeholder for other tabs
else:
    st.write(f"**{page}** is ready. We can expand this tab with full features next.")

st.sidebar.caption("Pro AI Dashboard • Pure Business Capital • 2026")
