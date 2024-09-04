# retail_experience
GenAI to improve retail shopping experience



# 3. Quick set-up

## 3.1. Create a .env
- Create an OpenAI API key
- Create a Pinecone API key and Index named `auto-food-order`
- Find [.env.example](./backend/.env.example) and write your API keys
- Rename `.env.example` to `.env`

## 3.2. Create a database and populate it
- Create a pinecone index
- Create a database following the tutorial in [here](./backend/src/data/README.md)

## 3.3 Configure your model
- Open [config.yaml](./backend/src/config/config.yaml) and choose the model you would like to use (works better with gpt-4 or gpt-4-32k)
- Feel free to tweak the parameters

## 3.4. Run it with docker
- Install docker on your machine
- Run ```docker compose up --build``` and have fun