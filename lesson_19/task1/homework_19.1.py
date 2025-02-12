import requests

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}

response = requests.get(url, params=params)

if response.status_code == 200:
    photo_data = response.json().get('photos', [])
    if photo_data:
        for i, photo_data in enumerate(photo_data, start=1):
            img_url = photo_data['img_src']
            img_data = requests.get(img_url).content
            with open(f"mars_photo{i}.jpg", 'wb') as file:
                file.write(img_data)
            print(f"Photo {i} is downloaded.")
    else:
        print("No photos with set parameters.")
else:
    print(f"Request's status code is not '2**'")

