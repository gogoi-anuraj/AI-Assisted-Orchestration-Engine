

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st

from app.parser.brd_parser import parse_brd
from app.registry.registry_loader import load_registry
from app.engine.config_generator import generate_config
from app.simulation.simulator import simulate_integration


st.set_page_config(page_title="AI Integration Engine", layout="wide")

# Custom Styling
st.markdown("""
    <style>
    .main-title {
        font-size: 40px;
        font-weight: bold;
        color: #4CAF50;
    }
    .section-title {
        font-size: 22px;
        font-weight: bold;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# 🔥 Header
st.markdown('<div class="main-title">AI Integration Orchestrator</div>', unsafe_allow_html=True)
st.write("Convert **BRD → Config → Simulation**")

st.divider()

# 🔹 Input Section
st.markdown('<div class="section-title">📝 Enter BRD</div>', unsafe_allow_html=True)

brd_text = st.text_area(
    "",
    height=180,
    placeholder="Example: The system must integrate with KYC and GST. Name maps to full_name..."
)

# 🔹 Run Button
if st.button("Run Pipeline", use_container_width=True):

    if not brd_text.strip():
        st.warning("⚠️ Please enter BRD text")
    else:
        with st.spinner("🔄 Processing pipeline..."):

            registry = load_registry()

            # Step 1: Parse
            parsed = parse_brd(brd_text)

            if isinstance(parsed, str):
                st.error("❌ Parsing failed")
                st.text(parsed)
            else:
                # Step 2: Config
                config = generate_config(parsed, registry)

                # Step 3: Simulation
                results = simulate_integration(config)

                st.divider()

                # 🔹 Layout Split
                colA, colB = st.columns(2)

                # LEFT SIDE
                with colA:
                    st.markdown("### Parsed Output")
                    st.json(parsed)

                # RIGHT SIDE
                with colB:
                    st.markdown("### Generated Config")
                    st.json(config)

                st.divider()

                # 🔹 Simulation Section
                st.markdown("## Simulation Results")

                results_list = results["results"]

                # User Card
                if results_list:
                    st.markdown("### 👤 User Under Verification")
                    st.json(results_list[0]["input"])

                st.markdown("### 🔹 Service Results")

                for r in results_list:
                    st.markdown(f"#### 🔸 {r['service']}")

                    col1, col2 = st.columns(2)

                    with col1:
                        st.markdown("**🔄 Transformed Data**")
                        st.json(r["transformed_data"])

                    with col2:
                        st.markdown("**📤 API Response**")
                        st.json(r["response"])

                    st.divider()

                # 🔹 Status Section
                st.markdown("## 📊 Overall Status")

                if results["overall_status"] == "SUCCESS":
                    st.success("✅ Integration Successful")
                else:
                    st.error("❌ Integration Failed")

                # Metrics
                st.markdown("### 📈 Summary")
                col1, col2 = st.columns(2)

                with col1:
                    st.metric("Services Processed", len(results_list))

                with col2:
                    st.metric("Final Status", results["overall_status"])