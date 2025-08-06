import os
import gradio as gr
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_API_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION", "2025-04-01-preview"),
)
DEPLOYMENT = os.getenv("AZURE_OPENAI_API_MODEL", "gpt-oss-120b")

def call_llm(user_message, history, show_reasoning):
    # Build Azure OpenAI chat messages
    messages = []
    for msg in history:
        # history uses OpenAI-style dicts now
        messages.append({"role": msg["role"], "content": [{"type": "text", "text": msg["content"]}]})
    messages.append({"role": "user", "content": [{"type": "text", "text": user_message}]})

    comp = client.chat.completions.create(
        model=DEPLOYMENT,
        messages=messages,
        max_tokens=1600,
        temperature=0.7,
        top_p=0.95,
    )
    msg = comp.choices[0].message
    return msg.content, getattr(msg, "reasoning_content", "")

# Custom CSS to make layout responsive
css = """
#chatbot .chatbot-message-container { height: calc(100vh - 200px) !important; overflow-y: auto; }
#input-row { width: 100%; }
#textbox textarea { height: auto; max-height: 100px; resize: vertical; }
"""

with gr.Blocks(title="Azure OpenAI Chat (Responsive)", css=css) as demo:
    gr.Markdown(
        "## Chat with gpt-oss-120b on Azure OpenAI\n"
    )

    # Chat history area (uses OpenAI-style messages format)
    chatbot = gr.Chatbot(elem_id="chatbot", type="messages")

    # Input and control row
    with gr.Row(elem_id="input-row"):
        textbox = gr.Textbox(
            placeholder="Type your message…",
            show_label=False,
            elem_id="textbox",
            scale=6
        )
        submit_btn = gr.Button("Submit", variant="primary", scale=1)
        clear_btn = gr.Button("Clear Chat", variant="secondary", scale=1)

    # Reasoning toggle below controls
    show_reasoning = gr.Checkbox(label="Show reasoning", value=False)

    def add_user_msg(user_message, history):
        if not user_message:
            return "", history
        # append as dict for messages
        history = history + [{"role": "user", "content": user_message}]
        return "", history

    def add_bot_reply(history, show_reasoning):
        # do nothing if no pending user turn
        if not history or history[-1]["role"] != "user":
            return history
        # fetch and replace
        answer, reasoning = call_llm(history[-1]["content"], history[:-1], show_reasoning)
        # build nested bubbles html
        if show_reasoning and reasoning:
            content = (
                "<div style='display:flex; flex-direction:column; gap:8px;'>"
                "<div style='background:#f0f0f0; padding:8px; border-radius:8px;'>"
                f"<strong>Reasoning</strong><br>{reasoning}</div>"
                "<div style='background:#ffffff; padding:8px; border-radius:8px; border:1px solid #ddd;'>"
                f"<strong>Answer</strong><br>{answer}</div>"
                "</div>"
            )
        else:
            content = answer
        # append assistant dict with html
        history = history + [{"role": "assistant", "content": content}]
        return history

    # wire up both Enter and button
    textbox.submit(add_user_msg, [textbox, chatbot], [textbox, chatbot]) \
           .then(add_bot_reply, [chatbot, show_reasoning], chatbot)
    submit_btn.click(add_user_msg, [textbox, chatbot], [textbox, chatbot]) \
              .then(add_bot_reply, [chatbot, show_reasoning], chatbot)

    # clear chat resets
    clear_btn.click(lambda: ([], ""), None, [chatbot, textbox])

if __name__ == "__main__":
    demo.launch()