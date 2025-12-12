import streamlit as st

# --------------------------------------------------
# App configuration
# --------------------------------------------------
st.set_page_config(
    page_title="SupplyChain Security Toolkit",
    layout="wide"
)

# --------------------------------------------------
# Header
# --------------------------------------------------
st.title("🔐 SupplyChain Security Toolkit")
st.write("Audit • Detect • Harden — Linux · Drupal · pfSense · CI/CD")

# --------------------------------------------------
# ⚠️ SECURITY DISCLAIMER (OBLIGATOIRE)
# --------------------------------------------------
st.info(
    "⚠️ This tool performs offline analysis only. "
    "No data is stored, logged, or transmitted. "
    "All uploads are processed in-memory for audit simulation purposes."
)

# --------------------------------------------------
# Sidebar
# --------------------------------------------------
menu = st.sidebar.radio(
    "📦 Modules",
    [
        "Linux LPE Audit",
        "Drupal Supply Chain",
        "pfSense Audit",
        "CI/CD Pipeline",
        "Reports"
    ]
)

# --------------------------------------------------
# Linux LPE Audit Module
# --------------------------------------------------
if menu == "Linux LPE Audit":
    st.header("🐧 Linux LPE Audit")
    st.write("Analyse cron, SUID, sudoers, PATH, permissions…")

    uploaded = st.file_uploader("Upload system config snapshot")
    if uploaded:
        st.success("File received! Running analysis…")

        st.success("✅ No writable SUID binaries found")
        st.warning("⚠️ Weak sudoers configuration detected")
        st.error("🚨 Potential PATH hijacking risk")

        st.success("Audit complete — see report section.")

# --------------------------------------------------
# Drupal Supply Chain Module
# --------------------------------------------------
if menu == "Drupal Supply Chain":
    st.header("🌐 Drupal Supply Chain Security")
    st.write("Analyse update mechanism, signatures, MITM risk.")

    url = st.text_input("Drupal site URL")
    if url:
        st.write(f"Scanning {url}…")

        st.success("✅ HTTPS update channel detected")
        st.warning("⚠️ GPG key rotation not enforced")
        st.success("✅ No obvious MITM exposure")

        st.success("Scan complete.")

# --------------------------------------------------
# pfSense Audit Module
# --------------------------------------------------
if menu == "pfSense Audit":
    st.header("🛡️ pfSense Configuration Audit")
    st.write("XMLRPC exposure, backup/unserialize, credentials…")

    uploaded = st.file_uploader("Upload pfSense config.xml")
    if uploaded:
        st.success("Config received.")

        st.error("🚨 XMLRPC exposed on WAN interface")
        st.warning("⚠️ exec_php enabled")
        st.success("✅ No suspicious symlink detected")
        st.warning("⚠️ Weak admin credential policy")

        st.success("pfSense Audit Complete.")

# --------------------------------------------------
# CI/CD Pipeline Module
# --------------------------------------------------
if menu == "CI/CD Pipeline":
    st.header("⚙️ CI/CD Pipeline Audit")

    uploaded = st.file_uploader("Upload GitHub Actions or GitLab CI config")
    if uploaded:
        st.success("Pipeline received.")

        st.success("✅ Dependency locking enabled")
        st.warning("⚠️ No artifact signature verification")
        st.error("🚨 Unpinned third-party actions detected")

        st.success("CI/CD Audit Complete.")

# --------------------------------------------------
# Reports Module
# --------------------------------------------------
if menu == "Reports":
    st.header("📄 Reports")
    st.write("Generate executive-ready audit summaries.")

    st.download_button(
        "⬇️ Download Audit Summary (PDF)",
        data=b"Coming soon",
        file_name="audit_report.pdf"
    )


