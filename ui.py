import gradio as gr
from local_generator import generate_icon

def inference(prompt, style, negative_prompt):
    try:
        result_path = generate_icon(prompt, style, negative_prompt)
        return result_path, ""
    except Exception as e:
        return None, str(e)

def launch_ui():
    styles = [
        "flat vector icon",
        "minimal line art",
        "3D style",
        "gradient filled icon",
        "pixel art"
    ]

    with gr.Blocks() as demo:
        gr.Markdown("# 🎨 IconForge – AI-Generated Icons")
        prompt = gr.Textbox(label="What icon do you need?", placeholder="e.g. cloud upload")
        style = gr.Dropdown(styles, value=styles[0], label="Style")
        negative_prompt = gr.Textbox(label="Negative Prompt (optional)", placeholder="e.g. blurry, text")

        btn = gr.Button("Generate Icon")
        icon_output = gr.Image(label="Generated Icon")
        error_output = gr.Textbox(label="Error", visible=True)

        btn.click(fn=inference, inputs=[prompt, style, negative_prompt], outputs=[icon_output, error_output])

    demo.launch()