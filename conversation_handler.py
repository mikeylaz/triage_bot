# conversation_handler.py
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

# Initialize the chat model
chat = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.2
)

# Create the system prompt
system_prompt = """You are an empathetic and professional medical assistant having a conversation with a patient.
Your goal is to understand their medical concerns through friendly conversation.
Always ask relevant follow-up questions like a doctor would, to better understand:
- Their symptoms
- Duration of symptoms
- Any relevant medical history
- Lifestyle factors that might be relevant
- Any treatments they've already tried

Keep your responses conversational but professional, and always ask at least one follow-up question until you have enough information to determine if the patient needs to see a doctor."""

# Create the prompt template
prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(system_prompt),
    MessagesPlaceholder(variable_name="history"),
    HumanMessagePromptTemplate.from_template("{input}")
])

# Initialize memory
memory = ConversationBufferMemory(return_messages=True)

# Create the conversation chain
conversation_chain = ConversationChain(
    memory=memory,
    prompt=prompt,
    llm=chat,
    verbose=True
)

def get_initial_greeting():
    return "Hello! How are you feeling today? I'm here to ask you a few questions to help understand your health concerns."

def get_response(user_input):
    response = conversation_chain.predict(input=user_input)
    return response