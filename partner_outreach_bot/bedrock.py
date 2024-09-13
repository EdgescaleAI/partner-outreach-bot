import boto3
import json

class BedrockClient:
    def __init__(self):
        self.client = boto3.client('bedrock-runtime', region_name='us-west-2')

    async def invoke_bedrock_model(self, prompt):
        request_body = json.dumps({
            "prompt": prompt,
            "max_gen_len": 512,
            "temperature": 0.5,
            "top_p": 0.9
        })

        response = self.client.invoke_model_with_response_stream(
            modelId="meta.llama3-8b-instruct-v1:0",
            contentType="application/json",
            accept="application/json",
            body=request_body
        )

        # Collect the generated text from the event stream
        generated_text = ""
        for event in response['body']:
            chunk = event['chunk']['bytes']
            chunk_str = chunk.decode('utf-8')
            chunk_data = json.loads(chunk_str)
            generated_text += chunk_data.get('generation', '')

        return generated_text
