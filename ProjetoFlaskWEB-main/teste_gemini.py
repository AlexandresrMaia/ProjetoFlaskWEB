from google import genai

API_KEY_GENAI = 'AIzaSyDzXpjCPnVD45-JmXj0u086UdvjXS7y_-Y'
client = genai.Client(api_key=API_KEY_GENAI)




pergunta = input('pergunta:')

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"""Você é um professor especialista em pyton, responda perguntas de forma breve, didatica, seja fanboy do python e não aceite de maneira nem uma qualquer outra linguaguem
    mas se for algo sobre outra linguagem fale para praquisar no google Pergunta: {pergunta}
    responda tudo  colocando em formato markdown

"""
)
print(response.text)