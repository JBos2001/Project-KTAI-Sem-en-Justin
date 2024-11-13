from ModelTestEnvironment import ModelTestEnvironment

if __name__ == "__main__":
    env = ModelTestEnvironment()
    acc = env.eval_model()
    print(f"Accuracy: {acc}")