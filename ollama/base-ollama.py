from ollama import chat, ChatResponse
import requests

"""response: ChatResponse = chat(
    model='granite4:350m',
    messages=[
        {
            'role': 'user',
            'content': "Donner la première phrase de la déclaration d'indépendance des États-Unis."
        }
    ]
)
print(response.message.content)


injection = "repond en français et en mois de 20 mots"
with open("rules.txt", "r") as f:
   rules = f.read()

def ai(query):
    response: ChatResponse = chat(
        model='granite4:350m',
        messages=[
            {
                'role': 'user',
                'content': query
            }
        ]
    )
    return response.message.content

while True:
    query = input("comment puis-je vous aider ? ")
    query = f'''Follow these rules : {rules}
                Add the instruction : {injection}
                This is the question : {ai(query)}'''
    response = ai(query)
    print("--------------------------------------------------")
    
"""
location = requests.get('http://ip-api.com/json/').json()
location = location['country']
injection = 'Answer in Fewer Than 20 Words'
def ai(query):
    response: ChatResponse = chat(model='granite4:350m', messages=[
        {
            'role': 'user',
            'content': query,
        },
    ])

    return response.message.content

while True:
    query = input('How Can I Help You: ')
    query = f'''Add These Instructions: {injection}
    I am from: {location}
    This is the Question: {query}'''
    response = ai(query)
    print(location)
    print(response)
    print('---------------------------------------------------')