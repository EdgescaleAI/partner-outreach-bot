import boto3
import json
from botocore.exceptions import ClientError

class BedrockClient:
    def __init__(self):
        # Initialize the Bedrock client
        self.client = boto3.client('bedrock-runtime', region_name='us-west-2')

    def invoke_bedrock_model(self, prompt):
        model_id = "meta.llama3-1-8b-instruct-v1:0"
        request_body = {
            "prompt": prompt,
            "max_gen_len": 1024,
            "temperature": 0.5,
            "top_p": 0.9
        }

        try:
            # Invoke the model
            response = self.client.invoke_model(
                modelId=model_id,
                contentType="application/json",
                accept="application/json",
                body=json.dumps(request_body)
            )

            # Print entire response for debugging
            print("Full Response: ", response)

            # Read and decode the StreamingBody content
            body = response['body'].read().decode('utf-8')
            model_response = json.loads(body)
            print("Model Response: ", model_response)

            # Extracting generation result from model_response
            if "generation" in model_response:
                generated_text = model_response["generation"]
                return generated_text
            else:
                return f"Error: 'generation' key not found in model response. Full model response: {model_response}"

        except ClientError as e:
            print(f"ERROR: Could not invoke the model '{model_id}'. Reason: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None
