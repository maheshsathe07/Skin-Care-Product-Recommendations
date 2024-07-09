# Skin Care Product Recommendation System

This project is a Skin Care Product Recommendation System that utilizes a general skin care products dataset from Myntra. The system leverages the Gemini-Pro LLM to create vector embeddings from the dataset and stores these embeddings in a Pinecone vector database. The project also includes a Discord bot that accepts prompts in the format of `!recommend prompt`, which the Gemini-Pro LLM uses to retrieve data from the vector database and suggest products.

## Prerequisites

Before running the project, ensure you have the following:

1. **DISCORD_BOT_TOKEN**: Your Discord bot token.
2. **GOOGLE_API_KEY**: Your Google API key.
3. **PINECONE_API_KEY**: Your Pinecone API key.

## Setup

### Step 1: Install Dependencies

Ensure you have Python 3.x installed. Install the required packages using pip:

```sh
pip install -r requirements.txt
```

### Step 2: Configure Pinecone

Set the dimension for the vector index on Pinecone to 768 for the Gemini-Pro LLM.

### Step 3: Set Environment Variables

Set the following environment variables in your environment:

```sh
export DISCORD_BOT_TOKEN='your_discord_bot_token'
export GOOGLE_API_KEY='your_google_api_key'
export PINECONE_API_KEY='your_pinecone_api_key'
```

## Running the Project

### Step 1: Create Vector Database

Run the `rag.ipynb` Jupyter Notebook file to create the vector database. This step processes the dataset, generates vector embeddings using the Gemini-Pro LLM, and stores these embeddings in the Pinecone vector database.

### Step 2: Start the Discord Bot

Run the `bot.py` file to start the Discord server. This server listens for prompts from users in the format `!recommend prompt`.

```sh
python bot.py
```

### Step 3: Retrieve Recommendations

When a user sends a prompt to the Discord bot, the `recommendations.py` file is invoked. This file retrieves the relevant data from the vector database and displays the recommended products on the Discord server.

## Files and Directories

- **rag.ipynb**: Jupyter Notebook for creating the vector database.
- **bot.py**: Script to start the Discord bot server.
- **recommendations.py**: Script to retrieve data from the vector database and suggest products.

## Example Usage

1. Run `rag.ipynb` to create the vector database.
2. Start the Discord bot by running `bot.py`.
3. In your Discord server, enter a prompt in the format `!recommend your_prompt`.
4. The bot will respond with product recommendations based on the input prompt.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
