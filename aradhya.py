import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="Gupta Associates Dashboard", layout="wide")

# --- Session Initialization ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'view_kanha' not in st.session_state:
    st.session_state.view_kanha = False

# --- Styled Login Page ---
def login():
    st.markdown("<h1 style='text-align: center;'>Gupta Associates</h1>", unsafe_allow_html=True)
    st.subheader("Login to your account")
    st.write("Please enter your credentials to access the dashboard.")

    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Sign In")
        if submitted:
            if username and password:
                st.session_state.logged_in = True
            else:
                st.warning("Please enter both username and password.")

    st.markdown("[🔑 Forgot password?](#)")

# --- Client Overview Table ---
def client_table():
    st.markdown("## 👥 Client Dashboard")
    st.markdown("### Select a client to view detailed reports.")

    clients = ["Kanha Gupta", "Ananya Sharma", "Rohit Verma", "Meena Jain", "Vikas Mehra", "Priya Sinha"]

    with st.container():
        for i, client in enumerate(clients):
            col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
            with col1:
                st.write(f"**{client}**")
            with col2:
                st.button("GST", key=f"gst_{i}")
            with col3:
                st.button("ITR", key=f"itr_{i}")
            with col4:
                if st.button("Tally", key=f"tally_{i}") and client == "Kanha Gupta":
                    st.session_state.view_kanha = True

    st.markdown("---")

# --- Kanha Gupta Report Page ---
def kanha_report():
    st.markdown("## 🧾 Report: Kanha Gupta")
    st.markdown("Use the expanders below to explore detailed records by year and type.")

    # GST Section
    st.subheader("📦 GST")
    with st.expander("GST Returns"):
        for year in ["2023/24", "2022/23", "2021/22"]:
            with st.container():
                st.markdown(f"**{year}**")
                st.text("• JANUARY - MARCH")
                st.text("• APRIL - AUGUST")
                st.text("• SEPTEMBER - DECEMBER")

    with st.expander("GST Notices"):
        for year in ["2023/24", "2022/23", "2021/22"]:
            with st.container():
                st.markdown(f"**{year}**")
                st.text("• JANUARY - MARCH")
                st.text("• APRIL - AUGUST")
                st.text("• SEPTEMBER - DECEMBER")

    with st.expander("GST Certificates"):
        for year in ["2023/24", "2022/23", "2021/22"]:
            st.text(f"• {year}")

    # GST Papers Highlighted
    st.info("GST Returns - JANUARY - MARCH 2023/24")
    for i in range(1, 6):
        st.text(f"📄 GST Paper {i}")

    # ITR Section
    st.subheader("💰 ITR")
    with st.expander("Audit Balance Sheets"):
        for year in ["2023/24", "2022/23", "2021/22"]:
            st.markdown(f"**{year}**")
            st.text("• JANUARY - MARCH")
            st.text("• APRIL - AUGUST")
            st.text("• SEPTEMBER - DECEMBER")

    with st.expander("ITR Notices / Demands"):
        for year in ["2023/24", "2022/23", "2021/22"]:
            st.markdown(f"**{year}**")
            st.text("• JANUARY - MARCH")
            st.text("• APRIL - AUGUST")
            st.text("• SEPTEMBER - DECEMBER")

    with st.expander("Computation Sheets"):
        for year in ["2023/24", "2022/23", "2021/22"]:
            st.text(f"• {year}")

    # Tally Section
    st.subheader("📘 Tally")
    with st.expander("Ledgers by Period"):
        for year in ["2023/24", "2022/23", "2021/22"]:
            st.markdown(f"**{year}**")
            st.text("• JANUARY - MARCH")
            st.text("• APRIL - AUGUST")
            st.text("• SEPTEMBER - DECEMBER")

    if st.button("🔙 Back to Dashboard"):
        st.session_state.view_kanha = False

# --- App Controller ---
if not st.session_state.logged_in:
    login()
elif st.session_state.view_kanha:
    kanha_report()
else:
    client_table()
