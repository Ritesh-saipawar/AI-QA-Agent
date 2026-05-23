# AI-QA-Agent
An enterprise-grade AI QA assistant that automatically analyzes software requirements, classifies them into architectural domains using deep learning, and generates robust pytest test cases with edge-case coverage in real time.

🚀 Overview

Manual test case generation is:

⏳ Time-consuming
❌ Error-prone
🔁 Inconsistent across teams

This project solves that using a Dual-AI Hybrid Pipeline that combines:

Semantic understanding (ML)
Code generation (LLM)
💡 Key Features

✅ Automatic requirement classification
✅ AI-generated pytest test cases
✅ Edge-case & negative test handling
✅ Real-time results via Streamlit UI
✅ Scalable architecture for enterprise QA workflows

🧠 Dual-AI Architecture
1️⃣ Semantic Routing (TensorFlow + USE)
Uses Universal Sentence Encoder (USE v4)
Converts requirements → embeddings
Classifies into 14 architectural domains:
Security
API
Database
Frontend
Authentication
Logging
Performance
(and more...)
2️⃣ Generative Test Synthesis (Groq + Llama 3.1)
Uses Groq API (Llama-3.1-8B-Instant)
Injects domain context into prompt
Generates:
✅ Valid pytest code
✅ Positive test cases
✅ Negative test cases
✅ Edge scenarios



⚙️ Model Architecture
Base Model: USE (Frozen Feature Extractor)
Head:
Dense (256)
Batch Normalization
Dropout (40%)
Dense (128)
Softmax (14 classes)

📊 Validation Accuracy: ~80%
🛡️ Overfitting Protection: EarlyStopping with best-weight restoration

📂 Project Structure
AI-QA-Agent/
│── app.py
│── model/
│── utils/
│── requirements.txt
│── tf_hub_model.keras
│── README.md


🛠️ Setup Instructions
1️⃣ Clone Repository
git clone https://github.com/YOUR_USERNAME/AI-QA-Agent.git
cd AI-QA-Agent
2️⃣ Install Dependencies
pip install tensorflow tf-keras tensorflow-hub streamlit pandas numpy groq

3️⃣ Download Model File

Download the trained model from Google Drive:

👉 https://drive.google.com/drive/folders/1x5YiKWIRXD8b7mcgzMYgRaiShdR_o-0c?usp=drive_link

Place the file:

tf_hub_model.keras

inside the project root directory.

4️⃣ Run the Application
streamlit run app.py
🖥️ How It Works
User enters a requirement
Model classifies domain (e.g., Security/API)
Context is passed to LLM
AI generates pytest test suite
📈 Example Output
def test_login_valid_user():
    assert login("user", "password") == True

def test_login_invalid_password():
    assert login("user", "wrong") == False

def test_login_empty_fields():
    assert login("", "") == False
🎯 Use Cases
QA Automation Teams
Startups building MVPs
Continuous Integration Pipelines
Software Testing Education
🔥 Future Improvements
🔄 Fine-tuned LLM for domain-specific testing
📊 Dashboard for test coverage analytics
🔗 CI/CD integration (GitHub Actions)
🧪 Multi-language test generation
👨‍💻 Author

Ritesh Saipawar
