import base64
import io
import models

from flask import Flask, make_response, request, abort


app = Flask(__name__)


with open("/app/src/index.html", "rb") as f_in:
    INDEX_HTML = f_in.read()


@app.route("/", methods = ["GET"])
def index():
    response = make_response(INDEX_HTML)
    response.headers.set("Content-Type", "text/html")
    return response


@app.route("/prompt", methods = ["POST"])
def prompt_generate():

    prompt = request.form.get("prompt")
    if not prompt:
        abort(400)

    buffer = io.BytesIO()
    models.MODEL_PIPELINE(prompt, num_inference_steps=4, guidance_scale=0).images[0].save(buffer, format="PNG")

    resp = "<img src=\"data:image/png;base64,%s\" />" % base64.b64encode(buffer.getvalue()).decode("ascii")

    response = make_response(resp)
    response.headers.set("Content-Type", "text/html")
    return response
