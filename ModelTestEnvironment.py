import openai

class ModelTestEnvironment:
    def is_solution(self, answer, solution):
        print(answer)
        answer = answer.replace(".", "")
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

        user_content = f"{prompt} Return the answer as a single number."

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

    def get_zero_shot_prompt(self, equasion):
        with open('prompts/zero_shot_prompt.txt', 'r') as prompt:
            prompt = prompt.read()
            prompt = prompt.replace("[equasion]", equasion)
            return prompt

    def get_chain_of_thought_prompt(self, equasion):
        with open('prompts/chain_of_thought_prompt.txt', 'r') as prompt:
            prompt = prompt.read()
            prompt = prompt.replace("[equasion]", equasion)
            return prompt

    def eval_model(self):
        n_correct = {"zero_shot": 0, "chain_of_thought": 0}
        with open('data/equasions.txt', 'r') as equasions, open('data/solutions.txt', 'r') as solutions:
            for equasion, solution in zip(equasions, solutions):
                zero_shot_prompt = self.get_zero_shot_prompt(equasion)
                zero_shot_response = self.prompt_model(zero_shot_prompt)
                if self.is_solution(zero_shot_response, solution):
                    n_correct["zero_shot"] += 1

                #chain_of_thought_prompt = self.get_chain_of_thought_prompt(equasion)
                #chain_of_thought_response = self.prompt_model(chain_of_thought_prompt)
                #if self.is_solution(chain_of_thought_response, solution):
                #    n_correct["chain_of_thought"] += 1
        acc = {prompting: n / 25 for prompting, n in n_correct.items()}
        return acc