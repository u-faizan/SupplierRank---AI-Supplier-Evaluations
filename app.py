import streamlit as st
import pandas as pd
import joblib
import plotly.express as px

# ------------------------
# Load saved model & scaler
# ------------------------
MODEL_PATH = "supplier_model.pkl"
SCALER_PATH = "scaler.pkl"

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

# Detect how many features model expects
EXPECTED_FEATURES = model.n_features_in_

# ------------------------
# Page Config
# ------------------------
st.set_page_config(page_title="Supplier Evaluation Dashboard", layout="wide")

# Sidebar navigation
menu = st.sidebar.radio(
    "📌 Navigation",
    ["Supplier Evaluation Results", "Evaluate a New Supplier"]
)

st.sidebar.markdown("---")
st.sidebar.info("This dashboard evaluates suppliers using clustering (KMeans).")

# ------------------------
# Screen 1: Supplier Evaluation Results
# ------------------------
if menu == "Supplier Evaluation Results":
    st.title("📊 Supplier Evaluation Dashboard")

    st.markdown("""
    This dashboard helps evaluate suppliers based on key procurement KPIs.

    ### Dataset Column Info:
    - **Supplier**: Supplier name  
    - **Compliance**: Whether supplier met compliance (`Yes/No`)  
    - **Order_Status**: Delivered or Cancelled  
    - **Quantity**: Number of items ordered  
    - **Unit_Price**: Original item price  
    - **Negotiated_Price**: Final agreed price after negotiation  

    ### Clustering Info:
    - **Cluster 0 = Risky Suppliers** (low compliance & low delivery)  
    - **Cluster 1 = Reliable Suppliers** (high compliance & good delivery)  
    """)

    try:
        agg = pd.read_csv("supplier_ranking.csv")
        st.subheader("📌 Supplier Evaluation Results Table")
        st.dataframe(agg.head(15))

        # 🔎 Column Explanations
        with st.expander("### 📘 Column Explanation"):
            st.markdown("""
            
            - **Supplier** → Unique supplier name or ID for identification  
            - **Compliance Rate** → Percentage of orders that met all compliance requirements (higher = better)  
            - **Delivery Rate** → Percentage of orders delivered on time and in full (higher = better)  
            - **Avg Price Efficiency** → Average unit price compared to other suppliers (lower = more cost-efficient)  
            - **Quantity Share** → Proportion of total order quantity fulfilled by this supplier (higher = bigger contributor)  
            - **Total Orders** → Total number of orders placed with the supplier  
            - **Total Quantity** → Total units/items supplied across all orders  
            - **Cluster** → Group assigned by KMeans clustering model (0 = Risky, 1 = Reliable)  
            - **Supplier Score** → Weighted composite score based on compliance, delivery, price efficiency, and quantity share  
            - **Rank** → Final ranking of suppliers based on Supplier Score (1 = best supplier)  
            """)

        # Bar Chart of supplier scores
        st.subheader("📊 Supplier Scores Comparison")
        fig_bar = px.bar(
            agg.sort_values("supplier_score", ascending=False).head(15),
            x="Supplier",
            y="supplier_score",
            color="cluster",
            title="Top Supplier Scores",
            text="supplier_score"
        )
        fig_bar.update_traces(texttemplate='%{text:.2f}', textposition='outside')
        st.plotly_chart(fig_bar, use_container_width=True)

    except FileNotFoundError:
        st.warning("Supplier ranking file not found. Run the training script to generate results.")

# ------------------------
# Screen 2: New Supplier Evaluation
# ------------------------
elif menu == "Evaluate a New Supplier":
    st.title("➕ Evaluate a New Supplier")

    with st.form("supplier_form"):
        compliance_rate = st.slider("Compliance Rate", 0.0, 1.0, 0.8)
        delivery_rate = st.slider("Delivery Rate", 0.0, 1.0, 0.7)
        price_efficiency = st.number_input("Average Unit Price Efficiency", min_value=0.0, value=70.0)
        quantity_share = st.number_input("Quantity Share", min_value=0.0, value=.40)

        submitted = st.form_submit_button("Evaluate Supplier")

    if submitted:
        # Prepare input
        input_data = pd.DataFrame([{
            "compliance_rate": compliance_rate,
            "delivery_rate": delivery_rate,
            "avg_price_efficiency": price_efficiency,
            "quantity_share": quantity_share
        }])

        # Scale input
        input_scaled = scaler.transform(input_data)

        # Match training feature size
        if EXPECTED_FEATURES == input_scaled.shape[1]:
            input_features = input_scaled
        else:
            st.error(f"❌ Feature mismatch: Model expects {EXPECTED_FEATURES}, but input has {input_scaled.shape[1]}")
            st.stop()

        # Predict cluster
        cluster = model.predict(input_features)[0]

        # Show results
        st.success(f"✅ Predicted Cluster: {cluster}")
        if cluster == 1:
            st.info("This supplier is likely **Reliable** ✅")
        else:
            st.error("⚠️ This supplier is likely **Risky**")
