# IA Ecommerce Chat Widget

Este pequeno projeto demonstra um servidor Flask com um widget de chat localizado no canto inferior direito da página. Ele serve como base para implementar um suporte automatizado em um e-commerce usando uma IA de conversação.

## Recursos
- Chatbox flutuante no canto inferior direito
- Comunicação assíncrona com o backend via `fetch`
- Backend em Flask que envia mensagens para um modelo de linguagem

## Como executar
1. (Opcional) crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure sua chave de API no arquivo `app.py` (variável `API_KEY`).
4. Inicie o servidor:
   ```bash
   python app.py
   ```
5. Abra o navegador em `http://localhost:5000` e clique no cabeçalho do widget para abrir o chat.

## Estrutura de arquivos
- `app.py` – aplicação Flask com a lógica de roteamento e chamada à API de IA.
- `templates/index.html` – página principal contendo o widget de suporte com HTML, CSS e JavaScript.
- `requirements.txt` – lista de dependências do Python.

---

Sinta‑se à vontade para estilizar e expandir o widget conforme necessário para o seu projeto.  Ele já está pronto para integração com um serviço de IA ou backend do e-commerce.