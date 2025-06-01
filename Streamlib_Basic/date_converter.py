import streamlit as st
from nepali_date_utils import converter
from datetime import date

st.title("📆 AD ↔ BS Date Converter")

mode = st.radio("Choose conversion direction:", ("AD to BS", "BS to AD"))

if mode == "AD to BS":
    ad_date = st.date_input("📅 Select a date in AD:")
    
    if st.button("Convert to BS"):
        try:
            year = ad_date.year
            month = ad_date.month
            day = ad_date.day

            bs_date = converter.ad_to_bs(year, month, day)  # ✅ Correct
            st.success(f"✅ BS Date: {bs_date}")
        except Exception as e:
            st.error(f"❌ Conversion failed: {e}")

else:
    st.markdown("📅 Enter a date in BS (Bikram Sambat):")
    bs_year = st.number_input("Year (e.g. 2081)", min_value=2000, max_value=2100, value=2081)
    bs_month = st.number_input("Month (1-12)", min_value=1, max_value=12, value=2)
    bs_day = st.number_input("Day (1-32)", min_value=1, max_value=32, value=8)

    if st.button("Convert to AD"):
        try:
            # ✅ Convert using integers, NOT string
            ad_date = converter.bs_to_ad(int(bs_year), int(bs_month), int(bs_day))
            st.success(f"✅ AD Date: {ad_date}")
        except Exception as e:
            st.error(f"❌ Conversion failed: {e}")
