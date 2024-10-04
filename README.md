# retail_experience
GenAI to improve retail shopping experience

# 1. Project

## 1.1. Goal 
Developing a voice assistant that accurately understands user commands is a complex challenge, especially when users express the same intent in varied ways.

The goal of this project is to demonstrate how a Generative AI (GenAI) can be effectively programmed to understand and respond to voice commands, regardless of how the user phrases their request.

For example, whether the user says, "filter by white chocolate," "select white chocolate," or "show me white chocolate," the assistant will be able to interpret the intent and execute the correct action. This project showcases how AI can bridge the gap between varied natural language inputs and precise command execution.

## 1.2. Why GenAI?
Traditional rule-based systems or conventional NLP models struggle when users phrase commands in unexpected ways. They require precise training on specific phrases or keywords, making them less adaptable to real-world interactions.

Generative AI excels at understanding diverse and nuanced language inputs:
 - Linguistic Flexibility: Users can phrase the same intent in different ways, like "filter by white chocolate" or "show me white chocolate." GenAI can recognize the intent and act accordingly.
 - Contextual Understanding: GenAI grasps context, allowing it to understand both direct and indirect requests.
 - Scalability: It learns from data, handling new commands without needing pre-programmed variations.
 - Enhanced User Experience: Users can speak naturally, and the AI will adapt, making interactions more intuitive and seamless.


# 5. Quick set-up

## 5.1. Create a .env
- Create an OpenAI API key
- Create a Pinecone API key and Index named `foodproject`
- Find [.env.example](./backend/.env.example) and write your API keys
- Rename `.env.example` to `.env`

## 5.2. Create a database and populate it
- Create a pinecone index
- Create a database following the tutorial in [here](./backend/src/data/README.md)

## 5.3 Configure your model
- Open [config.yaml](./backend/src/config/config.yaml) and choose the model you would like to use (works better with gpt-4 or gpt-4-32k)
- Feel free to tweak the parameters

## 5.4. Run it with docker
- Install docker on your machine
- Run ```docker compose up --build``` and have fun