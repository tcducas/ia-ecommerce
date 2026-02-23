from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

# API key for the AI service (keep this secret in production)
API_KEY = "sk-or-v1-85798acdd5568dc77fe01847fd779eeb213fdac1f48c9c8d570748be8441dbf5pyu"

@app.route("/")
def home():
    # Render a template that contains our chat widget
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def  chat():
    """Endpoint usado pelo widget em javascript. Espera JSON com "message" e retorna JSON com "reply".

    Continuamos oferecendo o mesmo comportamento para formulários enviados por conveniência, mas o foco
    é a comunicação assíncrona via fetch para manter a conversa dentro da página.
    """
    # suporte ao corpo JSON e ao formulário tradicional
    if request.is_json:
        user_message = request.json.get("message")
    else:
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
            return jsonify(error="API response mal formatada", data=data), 500

        # se foi uma requisição JS, retornamos JSON
        if request.is_json:
            return jsonify(reply=reply)
        else:
            # fallback para o formulário tradicional
            return f"""
            <h3>Resposta da IA:</h3>
            <p>{reply}</p>
            <br>
            <a href="/">Voltar</a>
            """

    except Exception as e:
        if request.is_json:
            return jsonify(error=str(e)), 500
        else:
            return f"Erro interno: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)