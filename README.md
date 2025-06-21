# 🎨 IconForge – AI-Powered Icon Generator

**IconForge** is a local AI tool that generates high-quality vector-style icons using Stable Diffusion. With no external API tokens required, it's a lightweight and powerful solution for designers, developers, and creatives.

---

## 🚀 Features

- 🎯 Text-to-icon generation with custom styles
- 🖼️ Built on `runwayml/stable-diffusion-v1-5`
- ⚙️ Runs locally (CPU or GPU) – no API keys needed
- 💡 Supports negative prompts for better quality
- 🌐 Gradio-based web UI for easy use

---

## 📸 Example Prompts

- `"cloud upload"` with style `"flat vector icon"`
- `"chat bubble"` with style `"gradient filled icon"`
- `"rocket launch"` with style `"minimal line art"`

---

## 📦 Installation

```bash
git clone https://github.com/your-username/iconforge.git
cd iconforge
pip install -r requirements.txt
🧠 Usage

python main.py
Then open http://127.0.0.1:7860 in your browser.

📁 Project Structure

iconforge/
├── main.py                # Launches the UI
├── ui.py                  # Gradio interface
├── local_generator.py     # Core image generation logic using diffusers
├── requirements.txt       # Python dependencies
⚙️ Requirements
Python 3.8+

torch (CPU or GPU version)

diffusers, transformers, gradio, accelerate

🧪 Tips
GPU recommended for faster generation

Style options include: flat vector, line art, 3D, pixel art

Try adding a negative prompt like "blurry, text, watermark"

✨ Credits
Hugging Face

Diffusers Library

Gradio team for easy UI integration

📜 License
MIT License

Let me know if you'd like a logo, demo GIF, or a `requirements-colab.txt` file for easy Colab deployment.