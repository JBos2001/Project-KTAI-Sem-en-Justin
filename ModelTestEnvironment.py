import openai

class ModelTestEnvironment:
    def is_solution(self, answer, solution):
        print(answer)
        answer = answer.split(" ")
        for item in reversed(answer):
            if item.isdigit():
                if item == solution.strip():
                    return True
                else:
                    return False

    def prompt_model(self, prompt):
        client = openai.OpenAI(
            base_url="http://localhost:11434/v1",
            api_key="nokeyneeded",
        )

        user_content = f"{prompt} Only return the answer as a single number."

        response = client.chat.completions.create(
            model="phi3:medium",
            temperature=0.7,
            n=1,
            messages=[
                {"role": "system", "content": "You are a calculator."},
                {"role": "user", "content": user_content},
            ],
        )
        model_response = response.choices[0].message.content
        return model_response

    def eval_model(self):
        n_correct = 0
        with open('data/equasions.txt', 'r') as equasions, open('data/solutions.txt', 'r') as solutions:
            for equasion, solution in zip(equasions, solutions):
                zero_shot_prompt = f"What is {equasion}"
                zero_shot_response = self.prompt_model(zero_shot_prompt)
                if self.is_solution(zero_shot_response, solution):
                    n_correct += 1
        acc = n_correct / 25
        return acc