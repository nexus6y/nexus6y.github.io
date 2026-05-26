"""Paper Research Assistant — Gradio Web Interface."""

import os
import gradio as gr
from paper_assistant import analyze_paper, SYSTEM_PROMPT


def run_analysis(title: str, abstract: str, api_key: str, model: str):
    if not api_key.strip():
        return "Please enter your API key."
    if not title.strip() or not abstract.strip():
        return "Please provide both title and abstract."

    try:
        result = analyze_paper(title.strip(), abstract.strip(), api_key.strip(), model)
        return result
    except Exception as e:
        return f"Error: {e}"


with gr.Blocks(theme=gr.themes.Soft(), title="Paper Research Assistant") as demo:
    gr.Markdown("# Paper Research Assistant")
    gr.Markdown(
        "Analyze academic paper abstracts with AI. "
        "Paste a title and abstract to get structured insights including "
        "key contributions, methodology, and future work directions."
    )

    with gr.Row():
        with gr.Column(scale=1):
            api_key = gr.Textbox(
                label="Anthropic API Key",
                type="password",
                placeholder="sk-ant-...",
                value=os.environ.get("ANTHROPIC_API_KEY", "")
            )
            model = gr.Dropdown(
                label="Model",
                choices=[
                    "claude-haiku-4-5-20251001",
                    "claude-sonnet-4-6-20251001",
                    "claude-opus-4-7-20251001"
                ],
                value="claude-haiku-4-5-20251001"
            )
            title = gr.Textbox(label="Paper Title", placeholder="Enter the paper title...", lines=2)
            abstract = gr.Textbox(label="Abstract", placeholder="Paste the paper abstract here...", lines=10)
            submit = gr.Button("Analyze", variant="primary")

        with gr.Column(scale=1):
            output = gr.Markdown(value="*Results will appear here...*")

    submit.click(
        fn=run_analysis,
        inputs=[title, abstract, api_key, model],
        outputs=output
    )

if __name__ == "__main__":
    demo.launch()
