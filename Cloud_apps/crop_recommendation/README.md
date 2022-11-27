# Credits

[David Revelo Luna](https://github.com/DavidReveloLuna/API_Gcloud_Streamlit)

## Deployment on Google Cloud Platform: Environtment Preparation

    $   conda create -n ApiCrop
    $   conda activate ApiCrop
    $   conda install python=3.7
    $   pip install -r requirements.txt
    $   streamlit run app.py

## Deployment on Google Cloud Platform: Production

    $ gcloud init
    $ gcloud app deploy app.yaml --project "project_name"
    
## Access to the app:
[Crop Recommendation](https://croppred.rj.r.appspot.com/)
    
