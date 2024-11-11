import openai
import random

def generate_summation_equations(n):
    equations = []
    for _ in range(n):
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        # Store each equation as a dictionary with the equation as a message content
        equation = f"{a} + {b}"
        equations.append(equation)
    return equations

client = openai.OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="nokeyneeded",
)

def LLM(prompts):
    response = client.chat.completions.create(
        model="phi3",
        temperature=0.7,
        n=1,
        messages=prompts,
    )
    return response

n = 1000
equation_list = generate_summation_equations(n)
all_responses = []

batch_size = 20
messages = [{"role": "system", "content": "You are a helpful assistant."}]

# Dit duurt lang, maar het werkt. Dit om de limitatie van het model te omzeilen. Normaal print het maximaal 20 antwoorden.
for i in range(0, len(equation_list), batch_size):
    batch = equation_list[i:i + batch_size]
    for equation in batch:
        messages.append({"role": "user", "content": f"Calculate {equation}"})
    
    response = LLM(messages)
    all_responses.append(response.choices[0].message.content)
    messages = [{"role": "system", "content": "You are a helpful assistant."}]

for resp in all_responses:
    print("Response:", resp)
