# from langchain_community.llms import HuggingFaceEndpoint
# from decouple import config
# from langchain.prompts import PromptTemplate

# # Load API token from environment variables
# HUGGINGFACEHUB_API_TOKEN = config('HUGGINGFACEHUB_API_TOKEN')

# # Create an instance of HuggingFaceEndpoint
 

# # Create a prompt template
# template = "<s> [INST]  WRITE YOUR ANSWER</s> {question}[/INST]" 


 

# prompt_template=PromptTemplate.from_template(template)
# formatted_prompt_template=prompt_template.format(
#     question=" 1 dirham  of uae in libya ?" 
# )

# repo_id = "mistralai/Mistral-7B-Instruct-v0.2"
 
# llm = HuggingFaceEndpoint(
#     repo_id=repo_id,  huggingfacehub_api_token =HUGGINGFACEHUB_API_TOKEN
# ) 
# response=llm.invoke(formatted_prompt_template)
# print(response)


from langchain_community.llms import HuggingFaceEndpoint

from decouple import config

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

HUGGINGFACEHUB_API_TOKEN = config('HUGGINGFACEHUB_API_TOKEN')
question = "Who won the PSL 7? "

template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate.from_template(template)


repo_id = "mistralai/Mistral-7B-Instruct-v0.2"

llm = HuggingFaceEndpoint(
    repo_id=repo_id, max_length=128, temperature=0.5, huggingfacehub_api_token =HUGGINGFACEHUB_API_TOKEN # type: ignore
)
llm_chain = LLMChain(prompt=prompt, llm=llm)
print(llm_chain.run(question))