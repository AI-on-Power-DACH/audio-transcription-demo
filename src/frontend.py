import argparse
import ast
import pathlib

import gradio as gr
import requests

from ibm_theme import IBMTheme

custom_css = """
h1, h2 {
    color: #0F62FE;
}
"""


def get_parser() -> argparse.ArgumentParser:
    _parser = argparse.ArgumentParser()
    _parser.add_argument(
        "--host",
        help="The host, where the frontend is available at",
        default="0.0.0.0",
    )
    _parser.add_argument(
        "--port",
        type=int,
        help="The port, where the frontend is available at",
        default=7860
    )

    return _parser


def send_request(url: str, audio_path: str) -> str:
    audio_path = pathlib.Path(audio_path)
    with open (audio_path, "rb") as audio_content:
        files = {
            "file": (audio_path.name, audio_content, "multipart/form-data"),
        }
        response = requests.post(
            url=url,
            files=files,
        )

    return ast.literal_eval(response.text)["text"]


def main(host: str = "0.0.0.0", port: int = 7860):
    title = "Audio Transcription Demo"

    with gr.Blocks(title=title, theme=IBMTheme(), css=custom_css) as demo:
        gr.Markdown(f"# {title}")
        with gr.Accordion(label="Advanced Settings", open=False):
            url_box = gr.Textbox(label="Please enter the backend url", value="http://0.0.0.0:8080/inference")

        input_audio = gr.Audio(
            sources=["upload", "microphone"],
            type="filepath",
            waveform_options=gr.WaveformOptions(
                waveform_color="#a6c8ff",
                waveform_progress_color="#0F62FE",
                skip_length=2,
                show_controls=False,
            ),
        )
        transcribed_text = gr.Textbox(label="Transcribed audio text:")
        extract_btn = gr.Button("Send request", variant="primary")
        extract_btn.click(
            fn=send_request,
            inputs=[url_box, input_audio],
            outputs=[transcribed_text],
            api_name="send_request",
        )

    demo.launch(server_name=host, server_port=port, debug=True)


if __name__ == "__main__":
    parser = get_parser()
    args = parser.parse_args()
    main(args.host, args.port)
