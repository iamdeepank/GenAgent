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

        print("API KEY:", os.getenv("GROQ_API_KEY"))

        information = """
        load_dotenv is a function from the python-dotenv package that reads key-value pairs from a .env file 
        and adds them to the environment variables (os.environ). It is used to securely manage configuration 
        settings like API keys or database credentials outside of the codebase.
        """

        summary_template = """
        Given the following information:

        {information}

        Perform the following tasks:
        1. Summarize this content.
        2. Convert the summary into Hindi language.
        """

        prompt_template = PromptTemplate(
            input_variables=["information"],
            template=summary_template
        )

        prompt = prompt_template.format(information=information)

        output = self.llm.invoke(prompt)

        print("\nResponse:\n")
        print(output.content)


obj = Prompt_Template_Groq()
obj.main()
