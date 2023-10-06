import os 
os.environ['OPENAI_API_KEY']= ''
os.environ['SERPAPI_API_KEY'] = ''
from langchain.llms import OpenAI as ai
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
from langchain.chains import SequentialChain
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferWindowMemory

def generate_restaurant_name(cuisine):
    llm = ai(temperature = 0.8)
    name = PromptTemplate(
    input_variables=['cuisine'],
    template="I want to open a restuarant for {cuisine} food. suggest a fancy name for this."
    )

    name_chain = LLMChain(llm=llm, prompt=name, output_key= 'restaurant_name')

    # print(name_chain.run("Pakistani"))

    item = PromptTemplate(
        input_variables=['restaurant_name'],
        template="suggest some menu items for {restaurant_name} returned as comma separated values."
    )

    food_chain = LLMChain(llm=llm, prompt=item, output_key='menu_items')
    # simple_seq_chain = SimpleSequentialChain(chains=[name_chain, food_chain])
    # responses = simple_seq_chain.run('mexican')
    # print(responses)

    chain = SequentialChain(
        chains= [name_chain,food_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name','menu_items']
    )
    response = chain({'cuisine':cuisine})
    return response

if __name__ == "__main__":
    llm = ai(temperature = 0.7)
    print(generate_restaurant_name("Italian"))
    tools = load_tools(["wikipedia", 'llm-math'], llm=llm)
    agent = initialize_agent(
        tools,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    )
    print(agent.run("what was the us gdp in 2022?"))
    tools2 = load_tools(["serpapi", 'llm-math'], llm=llm)
    agent2 = initialize_agent(
        tools2,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose = True
    )
    print(agent2.run("what was the gdp of US in 2022 plus 5"))
    
    ##by default it comes with in built memory
    memory = ConversationBufferWindowMemory(k=1) ## set param equal to 1 for chat gpt to remember only the last answer
    convo = ConversationChain(llm = llm, memory=memory)
    print(convo.prompt.template)
    memory = ConversationBufferWindowMemory(k=1)
    while True: 
        user=input("\nType in ur question: ")
        print(convo.run(user))
        if user.lower() == 'Exit'.lower():
            break
        
    print (convo.memory.buffer)