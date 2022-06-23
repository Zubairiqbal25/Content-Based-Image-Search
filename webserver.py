import numpy as np
from PIL import Image
from feature_extractor import FeatureExtractor
from datetime import datetime
from flask import Flask, request, render_template
from pathlib import Path

app = Flask(__name__)

# use for read image features
fe = FeatureExtractor()
features = []
img_paths = []
for feature_path in Path("./static/feature").glob("*.npy"):
    features.append(np.load(feature_path))
    img_paths.append(Path("./static/img") / (feature_path.stem + ".jpg"))
features = np.array(features)

#Route use for Flask server for working on webpage
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['query_img']

        # Save input image for show on webspage as Query image
        img = Image.open(file.stream)  
        uploaded_img_path = "static/uploaded/" + datetime.now().isoformat().replace(":", ".") + "_" + file.filename
        img.save(uploaded_img_path)

        # Start search of query from dataset feature
        query = fe.extract(img)
        #Find L2 distances to features
        dists = np.linalg.norm(features-query, axis=1)
        # Select Top 30 results of image feature
        ids = np.argsort(dists)[:30]  
        Distance = [(dists[id], img_paths[id]) for id in ids]
        #Return Index page from Flask  
        return render_template('index.html',
                               query_path=uploaded_img_path,
                               Distances=Distance)
    else:
        return render_template('index.html')


if __name__=="__main__":
    app.run("0.0.0.0")
