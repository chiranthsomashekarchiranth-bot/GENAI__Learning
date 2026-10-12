# type

print(type(3.4))



#type Hits 

model_name: str = "gemini-2.0-flash"
temperature: float = 0.7 # float
max_token: int = 103 #int 
is_streaming: bool = False #boolean
content_box: str|None = None #None
print(type(model_name))


# String: immutable | string formatting


# old version 
name = "LLM"
score = 97.0
print(" hello %s"%name)
print(" hello %.1f"%score)

# string formate(py 3.6 +)
print(f"name:{name}")
print(f"score:{score}")
# Expressions inside f-strings
word_limit=200
print(f"{'over'if word_limit>150 else'under'}limit")
data={"topic":"RAG"}
print(f"topic:{data['topic']}")

#Format specifiers
pi=3.14159265
print(f"pi:{pi:.2f}")
#Debugging=
temp=0.7
print(f"{temp=}")

#Multi line f-strings formatting 
user_inpute="What is Langchain?"
context_text="Langchain is framework"\
"for building LLM apps"
system_prompt=f"""
you are a helpful AI tutor.
Context provided:{context_text}
student question:{user_inpute}
Instruction:
-Answer based only on the context above
-If the answer is not in the context,say "I don't know"
-keep your answers under 3 sentences
""".strip()
print(system_prompt)
#Lists:ordered,mutable,heterogenous sequences
#In Gen AI: Chat history,chunks of retreived documents
#Token sequences
chat_history:list[dict]=[
    {"role":"uger","content":"What is an LLM"},
    {"role":"assistant","content":"A LLM is a neural"
     "n/wtrained on vast amounts of text."},
]
#Access
first_msg=chat_history[0]
print(first_msg)
print(chat_history[-1]["content"])# last element

# Modify
chat_history.append({"role":"user","content":"What is content"})
print(chat_history)
chat_history.pop(0)
print(chat_history)

#Iterate
for msg in chat_history:
    print(f"{msg['role'].upper()}:{msg['content']}")
# List of document chunks
chunks:list[str]=[
    "Rag stands for Restreival Augmented Generation",
    "It combines a retreiver with a generator",
]
#Filter chunks based on length
valid_chunks=[c for c in chunks if len(c.split())>=6]
print(valid_chunks)

 
