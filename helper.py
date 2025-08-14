from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
import os
from secretkey import api_key
from langchain.chains import SequentialChain, LLMChain

# Set API key
os.environ["GROQ_API_KEY"] = api_key

# Model
llm = ChatGroq(model="llama3-8b-8192", temperature=0.7)


def generte_resturant_itmes(cusine):
    prompt1 = PromptTemplate(
    input_variables=["cuisine"],
    template="Suggest a one fancy name for an {cuisine} restaurant."
    )

    # Second prompt: write a menu for that restaurant
    prompt2 = PromptTemplate(
    input_variables=["restaurant_name"],
    template="Write menu items for {restaurant_name}."
    )

    # Create individual chains
    chain1 = LLMChain(llm=llm, prompt=prompt1, output_key="restaurant_name")
    chain2 = LLMChain(llm=llm, prompt=prompt2, output_key="items")

    # Combine into a sequential chain
    overall_chain = SequentialChain(
    chains=[chain1, chain2],
    input_variables=["cuisine"],
    output_variables=["restaurant_name", "items"],

    )

    # Use invoke instead of run (works with multiple outputs)
    output = overall_chain.invoke({"cuisine": "Indian"})

    return output
if __name__=="__main__":
    print(generte_resturant_itmes('italian'))
