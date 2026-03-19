import gradio as gr

from model import predict

# gradio treats output component param "label" weirdly -> [object Object] in the ui
theme = gr.themes.Soft(primary_hue="orange", neutral_hue="slate")
theme = theme.set(
    body_background_fill_dark="*neutral_950",
    block_background_fill_dark="*neutral_900",
)

demo = gr.Interface(
    fn=predict,
    inputs=gr.Textbox(
        lines=3,
        label="text",
        placeholder="type something...",
        value="i hate this movie",
    ),
    outputs=[
        gr.Textbox(label="sentiment"),
        gr.Number(label="score", precision=3),
    ],
    title="sentiment",
    flagging_mode="manual",
    examples=[["i hate this movie"]],
    analytics_enabled=False,
)

if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        theme=theme,
        css="""
        .gradio-container { max-width: 920px !important; margin: auto !important; }
        """,
        head='<meta name="color-scheme" content="dark" />',
    )
