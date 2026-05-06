import streamlit as st
from rembg import remove
from PIL import Image
import io

# Set up the page layout
st.set_page_config(page_title="Magic Background Eraser", page_icon="✨", layout="wide")

# Main Header
st.title("✨ Magic Background Eraser")
st.write("Upload a picture to instantly cut out the subject. The AI will process it and output a transparent PNG.")

# Sidebar for advanced controls
st.sidebar.header("🔧 Advanced Tuning")
st.sidebar.write(
    "The default AI is usually perfect. But if it accidentally deletes the inside of your subject (like a beige dog on a beige background), enable Alpha Matting."
)

use_alpha_matting = st.sidebar.checkbox("Enable Alpha Matting (High Quality Edges)", value=True)

# File uploader
uploaded_file = st.file_uploader("Choose an image file (JPEG, PNG)", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Read the original image
    original_image = Image.open(uploaded_file)
    
    # Create a two-column layout for side-by-side comparison
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Original Image")
        st.image(original_image, use_column_width=True)
        
    with col2:
        st.subheader("Transparent Result")
        
        with st.spinner("AI is working its magic... (This takes a few seconds)"):
            # Convert uploaded file to bytes for the AI processor
            img_byte_arr = io.BytesIO()
            original_image.save(img_byte_arr, format=original_image.format or 'PNG')
            image_bytes = img_byte_arr.getvalue()
            
            try:
                # Run the AI background removal
                result_bytes = remove(
                    image_bytes, 
                    alpha_matting=use_alpha_matting
                )
                
                # Convert the result back to an image
                result_image = Image.open(io.BytesIO(result_bytes))
                
                # Display the result (Streamlit automatically handles transparency with a grey background)
                st.image(result_image, use_column_width=True)
                
                # Prepare the download button
                out_byte_arr = io.BytesIO()
                result_image.save(out_byte_arr, format='PNG')
                out_bytes = out_byte_arr.getvalue()
                
                # Extract the original filename and append _transparent
                original_name = uploaded_file.name
                name_without_ext = original_name.rsplit('.', 1)[0]
                download_name = f"{name_without_ext}_transparent.png"
                
                st.success("Background removed successfully!")
                
                st.download_button(
                    label="⬇️ Download Transparent PNG",
                    data=out_bytes,
                    file_name=download_name,
                    mime="image/png",
                    use_container_width=True
                )
                
            except Exception as e:
                st.error(f"An error occurred while processing: {e}")

st.markdown("---")
st.markdown("<div style='text-align: center; color: gray; font-size: small;'>Powered by Streamlit and rembg AI</div>", unsafe_allow_html=True)
