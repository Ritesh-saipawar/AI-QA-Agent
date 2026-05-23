import os
os.environ["TF_USE_LEGACY_KERAS"] = "1" 

import streamlit as st
import tensorflow as tf
import tf_keras as keras  
import tensorflow_hub as hub
import numpy as np
import json
from groq import Groq


GROQ_API_KEY = "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" 

@st.cache_resource
def load_labels():
    with open("label_mapping.json", "r") as f:
        return json.load(f)

@st.cache_resource
def load_my_model():
    return keras.models.load_model(
        "tf_hub_model.keras", 
        custom_objects={'KerasLayer': hub.KerasLayer}
    )

def generate_code_via_llm(requirement, category):
    
    try:
        client = Groq(api_key=GROQ_API_KEY)
        
       
        prompt = f"""
        You are a Senior QA Automation Engineer.
        Task: Write a Python 'pytest' test suite for the following {category} requirement.
        Requirement: '{requirement}'
        
        Instructions:
        1. Include a test for the 'Happy Path' (valid input).
        2. Include at least two edge cases or failure scenarios.
        3. Use mock data or comments to show where real data would go.
        4. Output ONLY the raw Python code. Do not include markdown blocks or explanations.
        """
        
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"# Groq API Error: Make sure your key is valid and you are connected to the internet.\n# Error Details: {e}"


st.set_page_config(page_title="AI QA Agent", page_icon="🧪", layout="centered")
st.title("🧪 Smart QA Automation Agent")
st.markdown("Powered by **TF-Hub Universal Sentence Encoder** & **Llama-3**.")

try:
    labels_map = load_labels()
    model = load_my_model()
    
    user_input = st.text_area(
        "Paste an enterprise software requirement:", 
        placeholder="e.g., The system must lock the user account after 5 consecutive failed login attempts."
    )

    if st.button("Analyze & Build Test Suite", type="primary"):
        if user_input.strip():
            with st.spinner("TensorFlow Hub mapping semantic architecture..."):
                
                
                predictions = model.predict(np.array([user_input]))
                predicted_idx = int(np.argmax(predictions[0]))
                confidence = np.max(predictions[0]) * 100
                category_name = labels_map.get(str(predicted_idx), "Unknown")

            st.success(f"🧠 **TensorFlow Result:** Categorized as `{category_name}` ({confidence:.1f}% confidence)")
            
            with st.spinner("Llama-3 synthesizing pytest scenarios..."):
                
               
                code_output = generate_code_via_llm(user_input, category_name)
                st.subheader("Generated Test Suite")
                st.code(code_output, language="python")
               
           
        else:
            st.warning("Please type a requirement first.")
except Exception as e:
    st.error(f"Error loading system: {e}")
