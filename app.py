import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Pure Business Capital Pro AI Dashboard", layout="wide", page_icon="💰")

# ================== CONFIG ==================
PASSWORD = "PBCPro2026"  # ← CHANGE THIS TO YOUR OWN SECURE PASSWORD
PRO_LINK = "https://whop.com/purebizcap/pro-ai-dashboard/"  

# PRODUCTS - Updated with correct Shelf Corporation Mastery price
PRODUCTS = {
    "Shelf Corporation Mastery": {
        "price": "$347",   # ← Corrected price here
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

# Safe logo + header
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
    st.markdown("### This is a **Pro-only** tool for paid members ($97/month).")
    st.write("Unlock the full dashboard with CRM, scripts, role-play, TikTok generator, and more.")
    
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
    
    st.caption("Purchased on Whop? Check your confirmation email for the password.")
    st.stop()

# ================== AUTHENTICATED DASHBOARD ==================
st.success("✅ Unlocked – Welcome to the Pro AI Dashboard!")

st.markdown("### Lead Mastery Dashboard – Your 24/7 Coach for Real Estate Investors, Finance Pros & Remote Opportunity Seekers")
st.caption("Pro Member Only • Built exclusively for Pure Business Capital")

# Sidebar
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

# HOME
if page == "🏠 Home":
    st.write("Welcome to your Pro AI Lead Mastery Dashboard!")
    st.info("Use the sidebar to generate leads, manage your CRM, practice calls, create TikTok scripts, and more.")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Leads This Week", "12", "↑ 4")
    with col2:
        st.metric("Conversion Rate", "18%", "↑ 3%")

# MY CRM (basic version)
elif page == "📋 My CRM":
    st.header("📋 My CRM")
    if "crm_df" not in st.session_state:
        st.session_state.crm_df = pd.DataFrame(columns=["Name", "Company", "Title", "Lead Source", "Status", "Last Contact", "Next Follow-up", "Notes", "Value Potential"])
    edited_df = st.data_editor(st.session_state.crm_df, num_rows="dynamic", use_container_width=True)
    st.session_state.crm_df = edited_df
    if st.button("Export CSV"):
        csv = edited_df.to_csv(index=False)
        st.download_button("Download CSV", csv, "my_leads.csv", "text/csv")

# UPSELLS & PRODUCTS (updated)
elif page == "🚀 Upsells & Products":
    st.header("🚀 Pure Business Capital Products & Upsells")
    st.subheader("Main Training & Offers")
    for name, info in PRODUCTS.items():
        with st.expander(f"{name} — {info['price']}"):
            st.write(info["desc"])
            st.link_button("Go to Product →", info["link"])
    
    st.divider()
    st.subheader("💎 You are on the Pro AI Dashboard")
    st.write("Thank you for being a Pro member at $97/month! You already have full access.")
    st.link_button("Manage Your Subscription", PRO_LINK)

# COMPLIANCE
elif page == "✅ Compliance Checklist":
    st.header("✅ Compliance & Best Practices")
    items = ["Only use public profile data", "Always personalize messages", "Never use bots or scraping", "Provide real value first", "Track reply rates monthly"]
    for item in items:
        st.checkbox(item, value=True)

# Placeholder for other pages (you can expand these later)
else:
    st.write("This page is ready for expansion. Let me know if you want full scripts, role-play, TikTok generator, or ROI tracker added next.")

st.sidebar.caption("Pro Member Dashboard • Pure Business Capital • April 2026")
