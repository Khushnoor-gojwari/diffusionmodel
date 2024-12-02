import streamlit as st
from session3 import query  # Import the query function from session3
import io
from PIL import Image

st.title("Diffusion Model")

# Create a text input widget
ingested_query = st.text_input("Enter your query")

if ingested_query:
    # Call the query function and get the image bytes
    image_bytes = query({
        "inputs": ingested_query,
    })

    # Check if the query function returned bytes
    if isinstance(image_bytes, bytes):
        try:
            # Debugging: Print the first few bytes to check if it looks like image data
            st.text(f"First 100 bytes of image data: {image_bytes[:100]}")

            # Open the image from the bytes
            image = Image.open(io.BytesIO(image_bytes))
            
            # Display the image in the Streamlit app
            st.image(image)
        except Exception as e:
            st.error(f"Failed to open image: {e}")
    else:
        st.error("Query function did not return valid image bytes.")
