import streamlit as st
import pandas as pd
import random
from datetime import datetime

st.set_page_config(page_title="Pure Business Capital Pro AI Dashboard", layout="wide", page_icon="💰")

# ================== CONFIG ==================
PASSWORD = "PBCPro2026"  # ← CHANGE THIS TO YOUR OWN PASSWORD
PRO_LINK = "https://whop.com/purebizcap/pro-ai-dashboard/"

PRODUCTS = {
    "Shelf Corporation Mastery": {
        "price": "$347",
        "link": "https://whop.com/purebizcap/shelf-corporation-mastery/",
        "desc": "Complete training and certification to launch your own aged shelf corporation business."
    },
    "Training Access": {
        "price": "Enroll Now",
        "link": "https://whop.com/purebizcap/training-access-a6/",
        "desc": "Full access to Hard Money Mastery, Private Capital, and more."
    },
    "Shelf Corporation Reseller Program": {
        "price": "Join Now",
        "link": "https://whop.com/purebizcap/shelf-corporation-reseller/",
        "desc": "Resell shelf corporations + earn commissions."
    },
    "Careers / Remote Agent Program": {
        "price": "Apply Free",
        "link": "https://purebusinesscapital.com/careers",
        "desc": "Remote, no-experience-needed opportunities."
    }
}

# Header
st.markdown("<h1 style='text-align: center; color: #FFFFFF;'>PURE BUSINESS CAPITAL</h1>", unsafe_allow_html=True)
try:
    st.image("logo.png", use_column_width=True)
except:
    pass

# Password Gate
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.title("🔒 Pure Business Capital Pro AI Lead Mastery Dashboard")
    st.markdown("### Pro Member Only – $97/month")
    st.write("Unlock CRM, lead tools, scripts, role-play, TikTok generator, and more.")
    
    password_input = st.text_input("Enter your Pro Password", type="password")
    col1, col2 = st.columns([1, 2])
    with col1:
        if st.button("Unlock Dashboard", type="primary"):
            if password_input == PASSWORD:
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("Incorrect password.")
    with col2:
        st.link_button("🚀 Get Pro Access – $97/month (2-day trial)", PRO_LINK, type="secondary")
    st.caption("Purchased? Check your Whop confirmation email for the password.")
    st.stop()

# ================== MAIN DASHBOARD ==================
st.success("✅ Unlocked – Welcome to the Pro AI Dashboard!")

st.markdown("### Lead Mastery Dashboard – Your 24/7 Coach")
st.caption("Pro Member Only • Real Estate Investors & Finance Pros")

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
    st.write("Welcome back! Use the tools on the left to generate leads and close more deals.")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Leads This Week", "18", "↑ 5")
    with col2:
        st.metric("Avg. Reply Rate", "22%", "↑ 4%")
    with col3:
        st.metric("Projected Revenue", "$12,450", "↑ $2,300")

# LEAD GENERATION
elif page == "🔍 Lead Generation":
    st.header("🔍 Lead Generation Coach")
    st.write("Target audience: Real estate investors, finance professionals, remote opportunity seekers.")
    
    tab1, tab2 = st.tabs(["LinkedIn Search Strings", "Personalized Message Generator"])
    with tab1:
        st.subheader("Copy & Paste into LinkedIn Sales Navigator")
        st.code("""Current title: ("Real Estate Investor" OR CFO OR Treasurer OR "Business Owner") 
Keywords: ("hard money" OR "private capital" OR "shelf corporation" OR "alternative financing" OR "remote agent")
Company headcount: 1-200""", language=None)
    
    with tab2:
        profile = st.text_area("Paste LinkedIn profile summary or name + title")
        if st.button("Generate Personalized Message"):
            st.success("Here's a strong first message:")
            st.write(f"Hi [Name], noticed you're active in real estate investing. Many in your position are using shelf corporations to move faster on deals. Our Shelf Corporation Mastery program ($347) has helped investors like you launch quickly... Would you be open to a quick chat?")

# MY CRM
elif page == "📋 My CRM":
    st.header("📋 My CRM")
    if "crm_df" not in st.session_state:
        st.session_state.crm_df = pd.DataFrame(columns=["Name", "Company", "Title", "Lead Source", "Status", "Last Contact", "Next Follow-up", "Notes", "Value Potential"])
    edited_df = st.data_editor(st.session_state.crm_df, num_rows="dynamic", use_container_width=True)
    st.session_state.crm_df = edited_df
    if st.button("Export as CSV"):
        csv = edited_df.to_csv(index=False)
        st.download_button("Download CSV", csv, "leads.csv", "text/csv")

# SCRIPTS LIBRARY
elif page == "📝 Scripts Library":
    st.header("📝 Scripts & Outreach Library")
    script_type = st.selectbox("Select script type", ["LinkedIn DM", "Email", "Cold Call"])
    if st.button("Generate Script"):
        if script_type == "LinkedIn DM":
            st.write("Hi [Name], saw you're building in real estate. Our Shelf Corporation Mastery program at $347 helps investors structure deals faster...")

# ROLE-PLAY SIMULATOR
elif page == "🎤 Role-Play Simulator":
    st.header("🎤 Sales Call Role-Play Simulator")
    st.write("Practice closing shelf corp or training sales calls.")
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])
    user_input = st.chat_input("Type what you'd say to the prospect...")
    if user_input:
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        reply = random.choice([
            "Great question! The $347 Shelf Corporation Mastery program includes templates and live support.",
            "Many real estate investors are using this to close deals 2-3x faster."
        ])
        st.session_state.chat_history.append({"role": "assistant", "content": reply})

# TIKTOK SCRIPT GENERATOR
elif page == "📱 TikTok Script Generator":
    st.header("📱 TikTok Video Script Generator")
    topic = st.text_input("Video topic", "How to get funding fast using shelf corporations")
    if st.button("Generate 3 Scripts"):
        st.subheader("Script 1 (15-second hook)")
        st.write("Hook: 'Banks said no? Watch this...'")
        st.write("Body: 'With our Shelf Corporation Mastery at only $347, you can have a clean aged entity in days...'")

# ROI & GOAL TRACKER
elif page == "📈 ROI & Goal Tracker":
    st.header("📈 ROI Calculator & Weekly Goals")
    leads_closed = st.number_input("Leads closed this month", 0, 100, 8)
    conv_rate = st.slider("Conversion rate (%)", 0, 100, 22)
    avg_value = st.number_input("Average deal value ($)", 100, 50000, 4500)
    revenue = leads_closed * (conv_rate / 100) * avg_value
    st.metric("Projected Monthly Revenue", f"${revenue:,.0f}")

    st.subheader("Weekly Lead Goal")
    goal = st.number_input("Weekly lead goal", 0, 100, 20)
    current = st.number_input("Leads added this week", 0, 100, 11)
    st.progress(current / goal if goal > 0 else 0)

# UPSELLS
elif page == "🚀 Upsells & Products":
    st.header("🚀 Products & Upsells")
    for name, info in PRODUCTS.items():
        with st.expander(f"{name} — {info['price']}"):
            st.write(info["desc"])
            st.link_button("View Product", info["link"])

# COMPLIANCE
elif page == "✅ Compliance":
    st.header("✅ Compliance Checklist")
    items = ["Use only public profile data", "Always personalize", "Never automate sending with bots", "Track reply rates", "Focus on value first"]
    for item in items:
        st.checkbox(item, value=True)

st.sidebar.caption("Pro AI Dashboard • Pure Business Capital")
