import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import random

st.set_page_config(page_title="Pure Business Capital Lead Mastery", layout="wide", page_icon="💰")
st.markdown("<h1 style='text-align: center;'>Pure Business Capital</h1>", unsafe_allow_html=True)

# Logo
st.image("logo.png", use_column_width=True)

st.markdown("### Lead Mastery Dashboard – Your 24/7 Coach for Real Estate Investors, Finance Pros & Remote Opportunity Seekers")
st.caption("Built exclusively for Pure Business Capital students & members")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", [
    "🏠 Home", 
    "🔍 Lead Generation", 
    "📋 My CRM", 
    "📝 Scripts & Outreach", 
    "🎤 Role-Play Simulator", 
    "📱 TikTok Script Generator", 
    "📈 ROI & Goal Tracker", 
    "🚀 Upsells & Products", 
    "✅ Compliance Checklist"
])

# PRODUCTS – easy to update later
PRODUCTS = {
    "Shelf Corporation Mastery": {
        "price": "$997",
        "link": "https://whop.com/purebizcap/shelf-corporation-mastery/",
        "desc": "Complete training to launch your own aged shelf corporation business."
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

# $47/month Pro pitch (you can change the link anytime)
PRO_LINK = "https://whop.com/purebizcap/training-access-a6/"  # ← REPLACE THIS WITH YOUR EXACT $47/MONTH WHOP LINK WHEN YOU CREATE IT

# HOME
if page == "🏠 Home":
    st.success("Welcome! This dashboard helps you generate leads, manage your CRM, write perfect scripts, track ROI, and scale your real estate/finance business — all while showing you the best Pure Business Capital upsells.")
    st.info("**Pro Tip:** Use the tabs on the left. Everything is beginner-friendly and compliant with LinkedIn & TikTok rules.")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Leads This Week", "12", "↑ 4")
    with col2:
        st.metric("Conversion Rate", "18%", "↑ 3%")

# LEAD GENERATION
elif page == "🔍 Lead Generation":
    st.header("🔍 Lead Generation Coach")
    st.write("Target: Real estate investors, finance professionals, and remote/help-wanted seekers.")
    method = st.selectbox("Choose platform", ["LinkedIn Search Strings", "TikTok Content Hooks"])
    
    if method == "LinkedIn Search Strings":
        st.subheader("Ready-to-use LinkedIn Sales Navigator Searches")
        st.code("""Current title: CFO OR Treasurer OR "Real Estate Investor" 
Company headcount: 1-50 
Industry: Real Estate OR Construction OR Finance
Keywords: "hard money" OR "private capital" OR "alternative financing" OR "remote agent" """, language="text")
        st.caption("Copy → paste into LinkedIn Sales Nav → export leads → import into CRM below")
    
    st.subheader("Generate Personalized Message")
    profile = st.text_area("Paste a LinkedIn profile or name + title here")
    if st.button("Generate Personalized Outreach"):
        st.success("✅ Generated!")
        st.write("Hi [Name], saw you're a real estate investor in [City]. Our Shelf Corporation Mastery program helps investors like you launch fast with zero headache...")

# MY CRM
elif page == "📋 My CRM":
    st.header("📋 My CRM")
    if "crm_df" not in st.session_state:
        st.session_state.crm_df = pd.DataFrame(columns=["Name", "Company", "Title", "Lead Source", "Status", "Last Contact", "Next Follow-up", "Notes", "Value Potential"])
    
    edited_df = st.data_editor(st.session_state.crm_df, num_rows="dynamic", use_container_width=True)
    st.session_state.crm_df = edited_df
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Export CSV"):
            csv = edited_df.to_csv(index=False)
            st.download_button("Download CSV", csv, "my_leads.csv", "text/csv")
    with col2:
        st.write("**Google Sheets Sync:** Copy the table above → paste into a new Google Sheet. Want auto-sync in Pro version? Upgrade below.")

# SCRIPTS & OUTREACH
elif page == "📝 Scripts & Outreach":
    st.header("📝 Scripts & Outreach Library")
    script_type = st.selectbox("Choose script type", ["LinkedIn DM", "Email", "Cold Call Script"])
    if st.button("Generate Scripts"):
        st.write("**LinkedIn DM Example:** Hi [Name], as a fellow real estate investor I noticed you're exploring new opportunities...")

# ROLE-PLAY SIMULATOR
elif page == "🎤 Role-Play Simulator":
    st.header("🎤 Sales Call Role-Play Simulator")
    st.write("Practice closing real estate investors or remote agent candidates.")
    if "messages" not in st.session_state:
        st.session_state.messages = []
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])
    prompt = st.chat_input("Type what you would say on the call...")
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        reply = random.choice(["Great question — here's how our Shelf Corporation program works...", "Perfect fit for you as a finance pro looking for remote opps."])
        st.session_state.messages.append({"role": "assistant", "content": reply})
        st.chat_message("assistant").write(reply)

# TIKTOK SCRIPT GENERATOR
elif page == "📱 TikTok Script Generator":
    st.header("📱 TikTok Video Script Generator")
    topic = st.text_input("What’s the video about?", "How to get funding in 7 days with shelf corporations")
    if st.button("Generate 3 Scripts"):
        st.write("**Hook (0-3s):** 'Tired of bank loans killing your real estate deals?'")
        st.write("**Script 1 (15s):** [Full script here...]")

# ROI & GOAL TRACKER
elif page == "📈 ROI & Goal Tracker":
    st.header("📈 ROI Calculator & Weekly Goal Tracker")
    leads = st.number_input("Leads closed this month", 0, 100, 8)
    conv_rate = st.slider("Conversion rate %", 0, 100, 18)
    avg_deal = st.number_input("Average deal value $", 1000, 50000, 7500)
    revenue = leads * (conv_rate / 100) * avg_deal
    st.metric("Projected Revenue", f"${revenue:,.0f}")
    
    st.subheader("Weekly Lead Goal")
    goal = st.number_input("Weekly lead goal", 0, 50, 15)
    entered = st.number_input("Leads entered this week", 0, 50, 9)
    st.progress(entered / goal if goal else 0)
    st.write(f"{entered}/{goal} leads — {((entered/goal)*100):.0f}% on track")

# UPSELLS & PRODUCTS
elif page == "🚀 Upsells & Products":
    st.header("🚀 Pure Business Capital Products & Upsells")
    st.write("**Why upgrade to the $47/month Pro AI Dashboard?**")
    st.markdown(f"""
    • Hosted version (no setup)  
    • Unlimited Grok-powered AI coach  
    • Weekly prompt updates  
    • Private community  
    • 50 fresh leads/month  
    • Priority email support  
    • Auto-CRM sync  
    **One-click upgrade → [Click here]({PRO_LINK})**
    """)
    
    st.divider()
    for name, info in PRODUCTS.items():
        with st.expander(f"{name} — {info['price']}"):
            st.write(info["desc"])
            st.link_button("Go to Product →", info["link"])

# COMPLIANCE CHECKLIST
elif page == "✅ Compliance Checklist":
    st.header("✅ Compliance & Best Practices")
    checklist = [
        "Only use public LinkedIn/TikTok data",
        "Never use bots or scraping tools",
        "Always personalize with real profile info",
        "Include value-first messaging",
        "Track reply rates monthly"
    ]
    for item in checklist:
        st.checkbox(item, value=True)

st.sidebar.caption("Built with ❤️ for Pure Business Capital by Grok • April 2026")
