import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Pure Business Capital Pro AI Dashboard", layout="wide", page_icon="💰")

# ================== CONFIG ==================
PASSWORD = "PureBCPro2026"   # ← Your current password
PRO_LINK = "https://whop.com/purebizcap/pro-ai-dashboard/"

PRODUCTS = {
    "Shelf Corporation Mastery": {"price": "$347", "link": "https://whop.com/purebizcap/shelf-corporation-mastery/", "desc": "Complete training to launch your own aged shelf corporation business."},
    "Training Access": {"price": "Enroll Now", "link": "https://whop.com/purebizcap/training-access-a6/", "desc": "Full access to Hard Money Mastery, Private Capital, and more."},
    "Shelf Corporation Reseller Program": {"price": "Join Now", "link": "https://whop.com/purebizcap/shelf-corporation-reseller/", "desc": "Resell shelf corporations + earn commissions."},
    "Careers / Remote Agent Program": {"price": "Apply Free", "link": "https://purebusinesscapital.com/careers", "desc": "Remote, no-experience-needed opportunities."}
}

# Header with logo
st.markdown("<h1 style='text-align: center; color: #FFFFFF;'>PURE BUSINESS CAPITAL</h1>", unsafe_allow_html=True)
try:
    st.image("logo.png", use_column_width=True)
except:
    st.caption("💰 Pure Business Capital")

# ================== PASSWORD GATE ==================
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
    
    st.info("**Purchased the Pro plan?** Enter your password below to unlock everything.")
    
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

# LEAD GENERATION
elif page == "🔍 Lead Generation":
    st.header("🔍 Lead Generation Coach")
    st.write("Target: Real estate investors, finance professionals, remote opportunity seekers.")
    tab1, tab2 = st.tabs(["LinkedIn Search Strings", "Personalized Message Generator"])
    with tab1:
        st.subheader("Ready-to-use LinkedIn Searches")
        st.code("""Current title: ("Real Estate Investor" OR CFO OR Treasurer OR "Business Owner") 
Keywords: ("hard money" OR "shelf corporation" OR "private capital" OR "alternative financing")
Company headcount: 1-200""", language=None)
    with tab2:
        profile = st.text_area("Paste profile summary or name + title")
        if st.button("Generate Personalized Message"):
            st.success("Suggested Message:")
            st.write("Hi [Name], saw you're active in real estate investing. Many investors in your position are using aged shelf corporations to move faster on deals. Our Shelf Corporation Mastery program ($347) has helped dozens close deals quicker... Open to a quick 10-min chat?")

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

# SCRIPTS LIBRARY
elif page == "📝 Scripts Library":
    st.header("📝 Scripts & Outreach Library")
    script_type = st.selectbox("Select script type", ["LinkedIn DM", "Email Follow-up", "Cold Call Script"])
    if st.button("Generate Script"):
        if script_type == "LinkedIn DM":
            st.write("**Version A:** Hi [Name], noticed your work in real estate. Our $347 Shelf Corporation Mastery helps investors structure deals faster...")
            st.write("**Version B:** Hi [Name], quick question — are you still looking for faster ways to structure your real estate deals?")

# ROLE-PLAY SIMULATOR
elif page == "🎤 Role-Play Simulator":
    st.header("🎤 Sales Call Role-Play Simulator")
    st.write("Practice closing Shelf Corp or training sales calls.")
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])
    user_input = st.chat_input("Type what you would say to the prospect...")
    if user_input:
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        reply = random.choice([
            "Great question! The $347 Shelf Corporation Mastery includes templates and live support.",
            "Many real estate investors we've helped are now closing deals 2-3x faster."
        ])
        st.session_state.chat_history.append({"role": "assistant", "content": reply})

# TIKTOK SCRIPT GENERATOR
elif page == "📱 TikTok Script Generator":
    st.header("📱 TikTok Video Script Generator")
    topic = st.text_input("Video topic", "How to get funding fast with shelf corporations")
    length = st.selectbox("Video length", ["15 seconds", "30 seconds", "60 seconds"])
    if st.button("Generate Scripts"):
        st.subheader(f"{length} Script")
        st.write("**Hook:** 'Banks said no again? Watch this...'")
        st.write("**Body:** With our Shelf Corporation Mastery at just $347, you can have a clean aged entity ready to receive funding in days...")

# ROI & GOAL TRACKER
elif page == "📈 ROI & Goal Tracker":
    st.header("📈 ROI Calculator & Weekly Goals")
    leads_closed = st.number_input("Leads closed this month", 0, 200, 8)
    conv_rate = st.slider("Conversion rate (%)", 0, 100, 22)
    avg_value = st.number_input("Average deal value ($)", 100, 100000, 4500)
    revenue = leads_closed * (conv_rate / 100) * avg_value
    st.metric("Projected Monthly Revenue", f"${revenue:,.0f}")

    st.subheader("Weekly Lead Goal")
    goal = st.number_input("Weekly lead goal", 0, 100, 20)
    current = st.number_input("Leads added this week", 0, 100, 11)
    st.progress(current / goal if goal > 0 else 0)
    st.write(f"{current}/{goal} leads — {int((current/goal)*100) if goal > 0 else 0}% on track")

# UPSELLS
elif page == "🚀 Upsells & Products":
    st.header("🚀 Products & Upsells")
    for name, info in PRODUCTS.items():
        with st.expander(f"{name} — {info['price']}"):
            st.write(info["desc"])
            st.link_button("View Product", info["link"])
    st.divider()
    st.subheader("💎 You are on the Pro AI Dashboard")
    st.write("Thank you for your $97/month Pro membership!")
    st.link_button("Manage Subscription", PRO_LINK)

# COMPLIANCE
elif page == "✅ Compliance":
    st.header("✅ Compliance Checklist")
    items = ["Only use public profile data", "Always personalize every message", "Never use bots or scraping tools", "Provide real value first", "Track reply rates monthly"]
    for item in items:
        st.checkbox(item, value=True)

st.sidebar.caption("Pro AI Dashboard • Pure Business Capital • 2026")
