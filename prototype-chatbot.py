import openai
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain import OpenAI, LLMChain, PromptTemplate
from googlesearch import search
openai.api_key = "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"
#Template de prompt
template = """chatbot avec chat memory.
{chat_history}
Human: {question}
AI:
"""
prompt_template = PromptTemplate(input_variables=["chat_history","question"], template=template)
memory = ConversationBufferMemory(memory_key="chat_history")

llm_chain = LLMChain(
    llm=OpenAI(openai_api_key="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"),
    prompt=prompt_template,
    verbose=True,
    memory=memory,
)
websites=[]
questions=[]
while True:
    if not questions:
       question=input("question : ")
    else:
        question = input("question : ")+questions[-1]
    questions.append(question)
    #Les recherches sur L'internet
    for link in search(question, tld="com", num=3, stop=3, pause=2):
        websites.append(link)
    print("base on the searches on internet here is three websites "+"\n".join(websites))
    print(websites)
    prompt = "Which of these three websites has the most readable content:"+websites[0]+websites[1]+websites[2]
    # Generate a response
    completion = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0,
    )

    response = completion.choices[0].text
    print("response",response)
    print("and base on the ai off the internet here is the anwser")
    anwser=llm_chain.predict(question=question)
    print(anwser)
    anwser2=llm_chain.predict(question="")

