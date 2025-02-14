import streamlit as st
import pandas as pd
import os

def show():
    image_folder = r"C:\Users\USER\Desktop\projects\project2\project\data\img"
    image_files = ["Heatmap.jpg", "RamdomForest.jpg", "GBM.jpg", "LightGBM.jpg", "EnsembleBarChart.jpg"]
    image_titles = ["모델 성능 비교", "Radom Forest Feature Importamce", "GBM Feature Importamce", "LightGBM Feature Importamce", "Ensemble Stacked bar chart", "Final Ensemble Model - ROC Curve"]

    for image_file, image_titles in zip(image_files, image_titles):
        image_path = os.path.join(image_folder, image_file)
        
        if os.path.exists(image_path):
            st.write(f'#### {image_titles}')
            st.image(image_path, caption=image_file, use_container_width=True)
        else:
            st.warning(f"⚠️ 파일을 찾을 수 없습니다: {image_file}")