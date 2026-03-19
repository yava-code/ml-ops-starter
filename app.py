import gradio as gr
from transformers import pipeline

clf = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")


def predict(text):
    if not text or not str(text).strip():
        return "(empty)", 0.0
    res = clf(text)[0]
    return res["label"], round(res["score"], 3)


demo = gr.Interface(
    fn=predict,
    inputs=gr.Textbox(lines=3, placeholder="type something..."),
    outputs=[gr.Textbox(label="label"), gr.Number(label="score")],
    title="sentiment",
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
