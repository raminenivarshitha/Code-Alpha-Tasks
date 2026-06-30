import streamlit as st
from PIL import Image
from io import BytesIO
from utils import detect_objects

st.set_page_config(
    page_title="Smart Object Detection",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 Smart Object Detection Dashboard")
st.markdown("Detect objects in uploaded images or capture a live photo using your webcam.")

# ---------------- Sidebar ---------------- #

st.sidebar.title("⚙️ Detection Settings")

confidence = st.sidebar.slider(
    "Confidence Threshold",
    min_value=0.10,
    max_value=1.00,
    value=0.50,
    step=0.05
)

mode = st.sidebar.radio(
    "Choose Detection Mode",
    ["📤 Upload Image", "📷 Webcam Capture"]
)

image = None

# ---------------- Upload Mode ---------------- #

if mode == "📤 Upload Image":

    uploaded_file = st.file_uploader(
        "Choose an image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file:
        image = Image.open(uploaded_file).convert("RGB")

# ---------------- Webcam Mode ---------------- #

else:

    camera_image = st.camera_input("Take a Picture")

    if camera_image:
        image = Image.open(camera_image).convert("RGB")

# ---------------- Detection ---------------- #

if image:

    with st.spinner("Detecting objects..."):

        detected_image, counts = detect_objects(
            image,
            confidence
        )

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📷 Original Image")
        st.image(image, use_container_width=True)

    with col2:
        st.subheader("🎯 Detection Result")
        st.image(detected_image, use_container_width=True)

    st.markdown("---")

    st.subheader("📊 Detection Summary")

    if counts:

        total = sum(counts.values())

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Total Objects",
                total
            )

        with col2:

            st.metric(
                "Unique Classes",
                len(counts)
            )

        st.markdown("### Objects Detected")

        for obj, count in counts.items():

            st.success(f"✅ **{obj.title()}** : {count}")

    else:

        st.warning("No objects detected.")

    # Download Image

    buffer = BytesIO()

    detected_image.save(
        buffer,
        format="JPEG"
    )

    buffer.seek(0)

    st.download_button(
        label="💾 Download Detected Image",
        data=buffer,
        file_name="detected_result.jpg",
        mime="image/jpeg"
    )

else:

    st.info("📤 Upload an image or capture one using your webcam to begin detection.")
