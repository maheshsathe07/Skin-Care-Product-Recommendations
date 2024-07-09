import os
import discord
from discord.ext import commands
from discord.ui import Button, View
from dotenv import load_dotenv
from recommendations import *
import json
from langchain_google_genai import GoogleGenerativeAIEmbeddings

embeddings=GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
index_name="recommend-products"

pinecone_api_key = os.getenv("PINECONE_API_KEY")
pc = Pinecone(api_key=pinecone_api_key)


load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)



@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    
@bot.command(name='recommend')
async def recommend_movies(ctx, *, query):
    
    qa = GeneralQuestionAnswering()
    docsearch = PineconeVectorStore.from_existing_index(index_name, embeddings)
    docs = docsearch.similarity_search(query)
    
    response = qa.ask_question(query, docs)
    print(response)

    json_data = response[response.find("["):response.rfind("]") + 1]
    recommendations = json.loads(json_data)
    print(recommendations)

    for product in recommendations:
        
        embed = discord.Embed(
            title=product["label"],
            description=product["name"],
            color=discord.Color.yellow()
        )

        embed.add_field(name="Brand", value=product["brand"], inline=True)
        embed.add_field(name="Price", value=product["price"], inline=True)
        embed.add_field(name="Skin Type", value=str(product["skin type"]), inline=True)
        embed.add_field(name="Concern", value=product["concern"], inline=True)

        embed.add_field(name="Reasoning", value=product["Reasoning"], inline=False)
    
        # embed.set_image(url=product["Poster"])

        view = View()
        default_url = "https://www.myntra.com/"
        button = Button(label="Watch Product", url=product["url"] if product["url"] != "N/A" else default_url, style=discord.ButtonStyle.link)
        view.add_item(button)
            
        await ctx.send(embed=embed, view=view)

bot.run(TOKEN)