import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_groq  import ChatGroq
load_dotenv()

class Prompt_Template_Groq:

    def __init__(self):
        self.llm=ChatGroq(
            model_name="llama-3.1-8b-instant", temperature=0.7
        )

    def main(self):

        print(os.getenv("GROQ_API_KEY"))
        information="""
        load_dotenv is a function from the python-dotenv package that reads key-value pairs from a .env file and adds them to the environment variables (os.environ). It is used to securely manage configuration settings like API keys or database credentials outside of the codebase, enabling easy switching between environments. 
    Key Details for Usage:
    Installation: Install via pip using pip install python-dotenv.
    Implementation: Call load_dotenv() early in your code (usually main.py or settings.py) to load variables before they are needed.
    File Location: By default, it looks for a .env file in the current directory.
    Usage Example:
    python
    import os
    from dotenv import load_dotenv

    load_dotenv()  # Loads variables from .env
    api_key = os.getenv('API_KEY')
        """ 

        summary_template="""
        Given the information {information} and I want to create:
        1. Summarize this content.
        2. convert it into hindi language.
        """   

        summary_template=PromptTemplate(
            input_variable=["information"],template=summary_template
        )
         
        llm=summary_template | self.llm 
        output=llm.invoke(input={"information":information})
        print(output.content)



obj=Prompt_Template_Groq()
obj.main()
