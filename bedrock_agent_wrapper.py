# bedrock_agent_wrapper.py

import logging
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)

class BedrockAgentRuntimeWrapper:
    """Encapsulates Amazon Bedrock Agents Runtime actions."""

    def __init__(self, runtime_client):
        self.agents_runtime_client = runtime_client

    def invoke_agent(self, agent_id, agent_alias_id, session_id, prompt):
        """
        Sends a prompt to the Bedrock agent and returns the response with detailed logging.
        """
        try:
            response = self.agents_runtime_client.invoke_agent(
                agentId=agent_id,
                agentAliasId=agent_alias_id,
                sessionId=session_id,
                inputText=prompt,
            )
            
            # Log detailed response for traceability
            logger.info(f"Full response from Bedrock agent: {response}")

            # Concatenate the response chunks for the completion text
            completion = "".join(
                event["chunk"]["bytes"].decode() for event in response.get("completion", [])
            )

            logger.info(f"Final completion response: {completion}")
            return completion

        except ClientError as e:
            logger.error(f"Failed to invoke agent: {e}")
            raise

