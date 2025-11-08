import google.generativeai as genai

genai.configure(api_key="SUA_CHAVE_AQUI")

model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

print("Chat Gemini iniciado. Digite 'sair' para encerrar.\n")

while True:
    pergunta = input("Você: ")

    if pergunta.lower() in ["sair", "exit", "quit"]:
        break

    resposta = model.generate_content(pergunta)
    print("\nGemini:", resposta.text, "\n")
