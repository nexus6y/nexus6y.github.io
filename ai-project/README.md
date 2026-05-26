# Paper Research Assistant

An AI-powered tool that analyzes academic paper abstracts and extracts structured insights using the Claude API.

## Features

- One-sentence paper summary
- Key contributions extraction
- Methodology breakdown
- Potential future work suggestions
- Keyword generation

## Quick Start

```bash
pip install -r requirements.txt
```

### CLI Usage

```bash
export ANTHROPIC_API_KEY=your-api-key
python paper_assistant.py
```

### Web Interface

```bash
export ANTHROPIC_API_KEY=your-api-key
python app.py
```

Then open http://localhost:7860 in your browser.

## Example

**Input:**
> Title: Attention Is All You Need
> Abstract: The dominant sequence transduction models are based on complex recurrent or convolutional neural networks... We propose a new simple network architecture, the Transformer...

**Output:**
> ## One-sentence summary
> This paper introduces the Transformer, a novel neural architecture that replaces recurrence with self-attention...
>
> ## Key Contributions
> - Proposes the Transformer architecture based solely on attention mechanisms
> - Achieves state-of-the-art results on machine translation tasks
> - Demonstrates superior parallelization and training efficiency
>
> ...

## Requirements

- Python 3.10+
- Anthropic API key ([get one here](https://console.anthropic.com))
