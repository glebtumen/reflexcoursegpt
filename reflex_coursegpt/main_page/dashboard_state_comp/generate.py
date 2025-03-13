import os
from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()


async def generate_content(
    prompt: str,
    creativity: int = 6,
    language: str = "ru",
) -> str:
    """Generate a single variant using OpenAI API."""
    client = AsyncOpenAI(api_key=os.environ["OPENAI_API_KEY"])
    temperature = creativity / 10
    response = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": f"Пиши на {language} языке Ты - профессионал со знаниями в науке, который помогает студентам писать курсовые работы. Ты должен писать ответы максимально полно и так, будто они были написаны студентом.",
            },
            {"role": "user", "content": prompt},
        ],
        temperature=temperature,
    )

    return response.choices[0].message.content


async def generate_content_perplexity(
    prompt: str,
    creativity: int = 6,
    language: str = "ru",
) -> str:
    """Generate a single variant using OpenAI API."""
    client = AsyncOpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.environ["OPENROUTER_API_KEY"],
    )

    completion = await client.chat.completions.create(
        extra_body={"search_domain_filter": ["cyberleninka.ru"]},
        model="perplexity/sonar",
        messages=[
            {
                "role": "system",
                "content": f"Пиши на {language} языке Ты - профессионал со знаниями в науке, который помогает студентам писать курсовые работы. Ты должен писать ответы максимально полно и так, будто они были написаны студентом.",
            },
            {"role": "user", "content": prompt},
        ],
        temperature=creativity / 10,
    )
    result = completion.choices[0].message.content
    citations = completion.citations
    return result + "\n\n" + "\n".join(citations)


async def generate_content_table(
    prompt: str, creativity: int = 6, language: str = "ru"
) -> str:
    """Generate a single variant using OpenAI API."""
    client = AsyncOpenAI(api_key=os.environ["OPENAI_API_KEY"])
    temperature = creativity / 10
    response = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": f"Пиши на {language} языке Ты - профессионал со знаниями в науке, который помогает студентам писать курсовые работы. Ты должен писать ответы максимально полно и так, будто они были написаны студентом.",
            },
            {"role": "user", "content": prompt},
        ],
        temperature=temperature,
        response_format={"type": "json_object"},
    )
    return response.choices[0].message.content
