import requests

base_url = "http://127.0.0.1:8080"

def upload_image(image_path):
    try:
        with open(image_path, "rb") as img:
            response = requests.post(f"{base_url}/upload", files={"image": img})
            if response.status_code == 201:
                print("Image uploaded successfully")
                return response.json()["image_url"]
            else:
                print("Failed to upload image:", response.text)
                return None
    except Exception as e:
        print("Can't do this:", e)

def get_image_url(filename):
    response = requests.get(f"{base_url}/image/{filename}", headers={"Content-Type": "text"})
    if response.status_code == 200:
        print("Image URL:", response.json()["image_url"])
    else:
        print("Failed to retrieve image:", response.json().get('error'))

def delete_image(filename):
    response = requests.delete(f"{base_url}/delete/{filename}")
    if response.status_code == 200:
        print(f"Image {filename} deleted successfully")
    else:
        print("Failed to delete image:", response.json().get('error'))

print('- - - Positive cases: - - -')
img_ref = "../task2/some_image.jpg"
uploaded_url = upload_image(img_ref)
if uploaded_url:
    filename = uploaded_url.split("/")[-1]
    get_image_url(filename)
    delete_image(filename)

print('- - - Negative cases: - - -')
upload_image('some')
get_image_url('some')
delete_image('some')