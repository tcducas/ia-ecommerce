from flask import Flask, request
import requests

app = Flask(__name__)

 
API_KEY = "sk-or-v1-85798acdd5568dc77fe01847fd779eeb213fdac1f48c9c8d570748be8441dbf5pyu"

@app.route("/")
def home():
    return """
    <h2>Chat IA - Atendimento Automático</h2>
    <form action="/chat" method="post">
        <input type="text" name="message" placeholder="Digite sua mensagem" style="width:300px;" required>
        <button type="submit">Enviar</button>
    </form>
    """

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.form.get("message")

    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "meta-llama/llama-3-8b-instruct",
                "messages": [
                    {"role": "system", "content": "Você é um atendente virtual profissional. Seja claro e educado."},
                    {"role": "user", "content": user_message}
                ]
            }
        )

        data = response.json()

        if "choices" in data:
            reply = data["choices"][0]["message"]["content"]
        else:
            return f"Erro da API: {data}"

        return f"""
        <h3>Resposta da IA:</h3>
        <p>{reply}</p>
        <br>
        <a href="/">Voltar</a>
        """

    except Exception as e:
        return f"Erro interno: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)