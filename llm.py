from ollama import Client


def M_LLM(prompt):

    # print(prompt)

    client = Client(host="http://localhost:11434")
    response = client.chat(
        # model="llama3.2:1b",
        model="gemma:7b",
        messages=[
            {"role": "user", "content": prompt},
        ],
    )

    return response["message"]["content"]


prompt="Who are you?"


print(M_LLM(prompt=))
