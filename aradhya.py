def kanha_account_report():
    st.markdown("## 🧮 Final Accounts - Kanha Gupta")
    tabs = st.tabs(["🔹 Summary", "📑 Ledger", "📊 Trial Balance", "💸 P&L", "🏛️ Balance Sheet", "💵 Cash Flow"])

    # Summary
    with tabs[0]:
        st.markdown("### Account Summary")
        st.metric("Total Revenue", "₹12,00,000")
        st.metric("Total Expenses", "₹8,50,000")
        st.metric("Net Profit", "₹3,50,000")
        st.metric("Cash in Hand", "₹1,20,000")

    # Ledger
    with tabs[1]:
        st.markdown("### Ledger Book")
        ledger_data = {
            "Date": ["2024-04-01", "2024-04-05", "2024-04-10"],
            "Particulars": ["Opening Balance", "Sales", "Office Rent"],
            "Debit (₹)": ["", "", "20,000"],
            "Credit (₹)": ["1,00,000", "50,000", ""],
            "Balance (₹)": ["1,00,000", "1,50,000", "1,30,000"]
        }
        st.dataframe(ledger_data)

    # Trial Balance
    with tabs[2]:
        st.markdown("### Trial Balance")
        st.write("**As on 31st March 2024**")
        st.table({
            "Account": ["Cash", "Sales", "Rent Expense", "Capital"],
            "Debit (₹)": ["1,20,000", "", "80,000", ""],
            "Credit (₹)": ["", "5,00,000", "", "6,00,000"]
        })

    # Profit & Loss
    with tabs[3]:
        st.markdown("### Profit & Loss Statement")
        st.write("**For FY 2023-24**")
        st.table({
            "Particulars": ["Revenue from Operations", "Other Income", "Total Revenue",
                            "Operating Expenses", "Net Profit"],
            "Amount (₹)": ["10,00,000", "2,00,000", "12,00,000", "8,50,000", "3,50,000"]
        })

    # Balance Sheet
    with tabs[4]:
        st.markdown("### Balance Sheet")
        col1, col2 = st.columns(2)
        with col1:
            st.write("**Assets**")
            st.write("- Cash: ₹1,20,000")
            st.write("- Accounts Receivable: ₹2,50,000")
            st.write("- Equipment: ₹3,00,000")
        with col2:
            st.write("**Liabilities & Equity**")
            st.write("- Loans: ₹1,00,000")
            st.write("- Capital: ₹5,70,000")

    # Cash Flow
    with tabs[5]:
        st.markdown("### Cash Flow Statement")
        st.text("Operating Activities: +₹2,50,000\nInvesting Activities: -₹50,000\nFinancing Activities: +₹20,000")

    # Download Option
    st.download_button("📥 Download Full Report (PDF)", data="Report Content", file_name="kanha_report.pdf")

