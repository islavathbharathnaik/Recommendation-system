
import streamlit as st
import pandas as pd

st.title("🛒 Shopper Spectrum")
st.write("Customer Segmentation and Product Recommendation System")
menu = st.sidebar.radio(
    "Menu",
    ["Home", "Product Recommendation", "Customer Segmentation"]
)


df = pd.read_csv("online_retail.csv", encoding="ISO-8859-1")

if menu == "Home":
        st.title("🏠 Welcome to Shopper Spectrum")

        st.write("Welcome to the Customer Segmentation and Product Recommendation System.")

        st.subheader("Dataset Preview")
        st.dataframe(df.head())

        st.subheader("Top 5 Recommended Products")

        top_products = (
            df.groupby('Description')['Quantity']
            .sum()
            .sort_values(ascending=False)
            .head(5)
        )

        st.write(top_products)
elif menu == "Product Recommendation":

        st.subheader("Product Recommender")

        product_name = st.text_input("Enter Product Name")

        if st.button("Get Recommendations"):

            recommendations = (
                df.groupby('Description')['Quantity']
                .sum()
                .sort_values(ascending=False)
                .head(5)
            )

            st.write("Recommended Products:")
            st.write(recommendations)
elif menu == "Customer Segmentation":

        st.subheader("Customer Segmentation")

        recency = st.number_input("Recency (days)", min_value=0)
        frequency = st.number_input("Frequency (number of purchases)", min_value=0)
        monetary = st.number_input("Monetary (total spend)", min_value=0.0)

        if st.button("Predict Segment"):

            if monetary > 10000 and frequency > 20:
                segment = "High-Value"
            elif recency > 200:
                segment = "At-Risk"
            elif frequency > 5:
                segment = "Regular"
            else:
                segment = "Occasional"

            st.success(f"Customer belongs to: {segment}")
            st.set_page_config(
    page_title="Shopper Spectrum",
    page_icon="🛒",
    layout="wide"
)

st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}

.stButton > button {
    background-color: #4CAF50;
    color: white;
    border-radius: 10px;
}

h1 {
    color: #1f77b4;
}

h2, h3 {
    color: #2e8b57;
}
</style>
""", unsafe_allow_html=True)
