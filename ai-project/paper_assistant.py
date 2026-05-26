"""Paper Research Assistant - Analyze academic paper abstracts with AI."""

import anthropic


SYSTEM_PROMPT = """You are a senior research fellow helping analyze academic papers.
Given a paper title and abstract, provide a structured analysis in the following format:

## One-sentence summary
[Summarize the paper in one clear sentence]

## Key Contributions
- [Contribution 1]
- [Contribution 2]
- [Contribution 3]

## Methodology
[Brief description of the approach/methods used, 2-3 sentences]

## Potential Future Work
- [Direction 1]
- [Direction 2]

## Keywords
[5-7 keywords reflecting the core topics]

Keep the entire response concise and well-structured. Use English only."""


def analyze_paper(title: str, abstract: str, api_key: str, model: str = "claude-haiku-4-5-20251001") -> str:
    """Analyze a paper abstract and return structured insights."""
    client = anthropic.Anthropic(api_key=api_key)

    message = client.messages.create(
        model=model,
        max_tokens=1024,
        system=SYSTEM_PROMPT,
        messages=[{
            "role": "user",
            "content": f"Title: {title}\n\nAbstract: {abstract}"
        }]
    )

    return message.content[0].text


if __name__ == "__main__":
    import os

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: Set ANTHROPIC_API_KEY environment variable.")
        exit(1)

    title = input("Paper title: ").strip()
    print("Paste abstract (press Enter then Ctrl+D to finish):")
    lines = []
    try:
        while True:
            lines.append(input())
    except EOFError:
        pass
    abstract = "\n".join(lines)

    if not title or not abstract:
        print("Title and abstract are required.")
        exit(1)

    print("\n" + "=" * 60)
    result = analyze_paper(title, abstract, api_key)
    print(result)
