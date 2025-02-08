from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = "your_openai_api_key"


@app.route("/query", methods=["POST"])
def interpret_query():
    data = request.json
    user_query = data.get("query", "")

    prompt = f"Convert this query into a PromQL query: {user_query}"
    response = openai.ChatCompletion.create(
        model="gpt-4", messages=[{"role": "user", "content": prompt}]
    )
    promql_query = response["choices"][0]["message"]["content"]

    return jsonify({"promql_query": promql_query})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
