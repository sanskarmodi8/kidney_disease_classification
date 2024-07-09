import streamlit as st
from KidneyDiseaseClassifier.pipeline.prediction import PredictionPipeline
from PIL import Image

class ClientApp:
    def __init__(self, filename):
        self.filename = filename
        self.classifier = PredictionPipeline(self.filename)

# Streamlit app
st.title("Kidney Disease Prediction")


st.write("Upload an image for prediction:")
uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    try:
        # Save the uploaded file
        with open("inputImage.jpg", "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        st.write("")

        # button for classifying
        if st.button("Classify"):
            # Make prediction
            clApp = ClientApp("inputImage.jpg")
            result = clApp.classifier.predict()
            result = result[0]['image']
            st.write(result)
    except Exception as e:
        st.error(f"Error: {str(e)}")