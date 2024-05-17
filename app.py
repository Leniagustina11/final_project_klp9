import os
import uvicorn
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from keras.models import load_model
import tensorflow as tf
import numpy as np
import tempfile

app = FastAPI()

flower_names = ['daisy', 'dandelion', 'rose', 'sunflower', 'tulip']
model = load_model('final_lab.h5')

def classify_images(image_path):
    input_image = tf.keras.utils.load_img(image_path, target_size=(180, 180))
    input_image_array = tf.keras.utils.img_to_array(input_image)
    input_image_exp_dim = np.expand_dims(input_image_array, 0)

    predictions = model.predict(input_image_exp_dim)
    result = tf.nn.softmax(predictions[0])
    flower_name = flower_names[np.argmax(result)]
    confidence_score = np.max(result) * 100
    outcome = f"Hasil klasifikasi: {flower_name}, Akurasi: {confidence_score:.2f}%"
    return outcome

@app.post("/classify_image/")
async def classify_image(file: UploadFile = File(...)):
    with tempfile.NamedTemporaryFile(delete=False) as temp:
        temp.write(await file.read())
        temp_path = temp.name
    result = classify_images(temp_path)
    os.remove(temp_path)  # Menghapus file sementara setelah selesai
    return {"result": result}

@app.get("/")
async def get_index():
    with open("index.html", "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content, status_code=200)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
