
# Financial Report Analysis App

This Streamlit application allows users to analyze financial reports of various companies within selected industry sectors. The app utilizes Amazon Bedrock's agent to generate detailed summaries of annual financial reports.

## Features
- **Sector Selection**: Choose from Telecommunications, Utilities, Industrial, or Basic Consumption sectors.
- **Company Selection**: Based on the selected sector, choose a company for analysis.
- **Financial Report Summarization**: The app generates a detailed analysis of the chosen company's annual financial reports.

## Prerequisites
- Python 3.7 or higher
- AWS credentials with access to Amazon Bedrock
- Streamlit
- Boto3
- Python-dotenv

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/EstelleP972/analyseRapportFinancier.git
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up AWS Credentials**:
   - Create a `.env` file in the project directory with the following content:
     ```env
     AWS_DEFAULT_REGION="your-region"
     AWS_ACCESS_KEY_ID="your-access-key-id"
     AWS_SECRET_ACCESS_KEY="your-secret-access-key"
     AWS_SESSION_TOKEN="your-session-token"
     AGENT_ID="PPKOUQTMHH"
     AGENT_ALIAS_ID="XHPKEVI3UV"
     ```

## Usage

1. **Run the Application**:
   ```bash
   python -m streamlit run analyser.py
   ```

2. **Interact with the App**:
   - Select an industry sector.
   - Choose a company from the dropdown.
   - Submit the form to get a detailed analysis of the company's financial reports.

## Logging
Logs are captured and displayed within the Streamlit app for troubleshooting purposes.

## Troubleshooting
- Ensure AWS credentials are valid and not expired.
- If encountering `ExpiredTokenException`, refresh your AWS credentials and update the `.env` file.
