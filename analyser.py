import streamlit as st
import boto3
from botocore.exceptions import ClientError
from bedrock_agent_wrapper import BedrockAgentRuntimeWrapper
import uuid
import logging
from io import StringIO
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
aws_session_token = os.getenv("AWS_SESSION_TOKEN")
aws_region = os.getenv("AWS_DEFAULT_REGION")
agent_id = os.getenv("AGENT_ID")
agent_alias_id = os.getenv("AGENT_ALIAS_ID")

# Set up logging to capture logs in Streamlit
log_stream = StringIO()
logging.basicConfig(stream=log_stream, level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Bedrock Agent client
try:
    bedrock_client = boto3.client(
        'bedrock-agent-runtime',
        region_name=aws_region,
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        aws_session_token=aws_session_token
    )
    agent_wrapper = BedrockAgentRuntimeWrapper(bedrock_client)
except ClientError as e:
    logger.error(f"Failed to initialize Bedrock client: {e}")
    st.error("Could not initialize Bedrock client. Check your AWS credentials and permissions.")

# Streamlit UI
st.title("Analyse financière des rapports annuels")

secteur = st.selectbox("Choisissez un secteur d'activité", ["Télécommunications", "Services Publics", "Industriel", "Consommation de Base"])
#indicator = st.selectbox("Choisissez un indicateurs financiers", ["Chiffres d'affaire", "Marge brute", "Flux de trésorerie libre", "Dette nette", "Bénéfice", " Bénéfice par actions"])

if secteur == "Télécommunications":
    company = st.selectbox("Choisissez une entreprise", ["Bell", "Cogeco", "Telus", "Rogers", "Quebecor"])
elif secteur == "Services Publics":
    company = st.selectbox("Choisissez une entreprise", ["Hydro One", "Fortis", "AltaGas"])
elif secteur == "Industriel":
    company = st.selectbox("Choisissez une entreprise", ["CPKC", "CN"])
else:
    company = st.selectbox("Choisissez une entreprise", ["Métro", "Couche-Tard", "Loblaws", "Empire"])


prompt = f"Dans le secteur {secteur}, montre-moi une analyse financière détaillée de l'entreprise {company}, composée d'un résumé détaillé du rapport financier de chaque année disponible."

if st.button("Soumettre"):
    # Clear previous log
    log_stream.truncate(0)
    log_stream.seek(0)

    if not prompt:
        st.warning("Please fill in all fields before submitting.")
    else:
        # Generate a unique session ID
        session_id = str(uuid.uuid4())
        try:
            # Call the Bedrock agent and get response
            response = agent_wrapper.invoke_agent(agent_id, agent_alias_id, session_id, prompt)
            st.subheader("Agent Response:")
            st.write(response)
        except ClientError as e:
            logger.error(f"Failed to invoke agent: {e}")
            st.error(f"Could not invoke the agent. Please check your inputs and try again. {e}")