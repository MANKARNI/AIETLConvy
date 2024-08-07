import os

from promptflow.core import Prompty, AzureOpenAIModelConfiguration

AZURE_OPENAI_ENDPOINT="https://AOAI-ETL.openai.azure.com/"
AZURE_OPENAI_CHAT_DEPLOYMENT="Trial4o"
AZURE_OPENAI_API_KEY="c81b1674d1f84cccbbd858fa136f6405"
AZURE_OPENAI_API_VERSION="2024-02-15-preview"

model_config = AzureOpenAIModelConfiguration(
    azure_deployment=AZURE_OPENAI_CHAT_DEPLOYMENT,
    api_key=AZURE_OPENAI_API_KEY,
    api_version=AZURE_OPENAI_API_VERSION,
    azure_endpoint=AZURE_OPENAI_ENDPOINT
)

prompty = Prompty.load("chat.prompty", model={'configuration': model_config})

in_file_object  = open("m_Sample_Hackathon.xml", "r+")
input_xml = in_file_object.read()

#print(result)

# result = prompty(
#    # chat_history=[
#    #     {"role": "user", "content": "Does Azure OpenAI support customer managed keys?"},
#    #     {"role": "assistant", "content": "Yes, customer managed keys are supported by Azure OpenAI."}
#    # ],
#     chat_input=input_xml)

result = {'message': 'Azure OAI json response'}
print(result)

#out_file_object  = open("ADFfile.json", "w+")
#out_file_object.write(result)



# import os
# import requests
# import base64

# # Configuration
# GPT4V_KEY = "c81b1674d1f84cccbbd858fa136f6405"
             
# # IMAGE_PATH = "YOUR_IMAGE_PATH"
# # encoded_image = base64.b64encode(open(IMAGE_PATH, 'rb').read()).decode('ascii')
# headers = {
#     "Content-Type": "application/json",
#     "api-key": GPT4V_KEY,
# }

# # Payload for the request
# payload = {
#   "messages": [{'role':'system', "content":"you are an AI assistent"}],
#   "temperature": 0.7,
#   "top_p": 0.95,
#   "max_tokens": 800
# }

# GPT4V_ENDPOINT = "https://aoai-etl.openai.azure.com/openai/deployments/Trial4o/chat/completions?api-version=2024-02-15-preview"

# # Send request
# try:
#     response = requests.post(GPT4V_ENDPOINT, headers=headers, json=payload)
#     response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
# except requests.RequestException as e:
#     raise SystemExit(f"Failed to make the request. Error: {e}")

# # Handle the response as needed (e.g., print or process)
# print(response.json())

# # import requests  
# # import json  
  
# # # Replace these values with your own Azure OpenAI resource details  
# # api_key = 'c81b1674d1f84cccbbd858fa136f6405'
# # endpoint = 'https://aoai-etl.openai.azure.com'

# # deployment_name = 'gpt-4o'  # Example: 'davinci-codex'  
# # # azureml://registries/azure-openai/models/gpt-4o/versions/2
# # # The prompt you want to send  
# # prompt = 'Write a poem about the sea.'  
  
# # # Construct the URL for the API call  
# # api_url = f'{endpoint}/openai/deployments/{deployment_name}/completions?api-version=2024-05-13'  
  
# # # Set the headers for the request  
# # headers = {  
# #     'Content-Type': 'application/json',  
# #     'api-key': api_key  
# # }  
  
# # # Create the data payload  
# # data = {  
# #     'prompt': prompt,  
# #     'max_tokens': 100,  # Adjust as needed  
# #     'temperature': 0.7,  # Adjust as needed  
# # }  
  
# # # Convert the data payload to a JSON string  
# # data_json = json.dumps(data)  
  
# # # Make the API call  
# # response = requests.post(api_url, headers=headers, data=data_json)  
# # print(response)
# # # Check if the request was successful  
# # if response.status_code == 200:  
# #     response_data = response.json()  
# #     print('Response:', response_data['choices'][0]['text'].strip())  
# # else:  
# #     print('Error:', response.status_code, response.text)  
