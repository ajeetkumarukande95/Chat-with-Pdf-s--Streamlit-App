# PDF Chat App

## Introduction
The PDF Chat App is a Python application that enables users to engage in conversations with multiple PDF documents. Using natural language, users can ask questions related to the content of the PDFs, and the app will provide relevant responses. The application utilizes natural language processing (NLP) techniques to analyze the text content of the PDFs and generate accurate answers.

## How It Works
1. **PDF Loading**: Users upload PDF documents using the provided file uploader.
2. **Text Extraction**: The app extracts the text content from the uploaded PDFs.
3. **Text Chunking**: The extracted text is segmented into smaller chunks for processing efficiency.
4. **Vectorization**: The text chunks are converted into vector representations using embeddings.
5. **Similarity Matching**: User questions are compared with the vectorized text chunks to identify semantically similar content.
6. **Response Generation**: Based on the identified relevant content, the app generates responses to user questions.

## Dependencies and Installation
To install and run the MultiPDF Chat App, follow these steps:

1. Clone this repository to your local machine.
2. Install the required dependencies by running:
   ```
   pip install -r requirements.txt
   ```
3. Obtain an OpenAI API key and add it to the `.env` file in the project directory.
4. Execute the `main.py` file using the Streamlit CLI:
   ```
   streamlit run app.py
   ```

## Usage
1. Upload PDF documents using the provided file uploader.
2. Click the "Process" button to initiate document processing.
3. Enter questions about the documents in the text input field and press Enter.
4. The app will display the conversation between the user and the chatbot, along with responses based on the content of the PDFs.

## Example Questions and Responses
- **Question:** What is the main topic of the first PDF?
  **Response:** The main topic of the first PDF is about AWS Lambda and event-driven architecture.

- **Question:** Can you explain AWS Lambda?
  **Response:** AWS Lambda is a serverless computing service provided by Amazon Web Services (AWS).

- **Question:** How does event-driven architecture work?
  **Response:** Event-driven architecture is a software design pattern where the production, detection, consumption, and reaction to events are central to the logic of the system.

- **Question:** What are the benefits of serverless computing?
  **Response:** Serverless computing offers benefits such as scalability, cost-effectiveness, and reduced operational overhead.

