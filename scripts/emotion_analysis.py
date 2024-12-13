from transformers import pipeline
import pandas as pd

# Загружаем модель Hugging Face для анализа эмоций
emotion_classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")

# Загружаем данные
reviews_df = pd.read_csv('data/processed_movie_reviews.csv')

def classify_emotion(text):
    result = emotion_classifier(text)
    return result[0]['label']

# Применяем анализ эмоций
reviews_df['Emotion'] = reviews_df['Cleaned_Review'].apply(classify_emotion)

# Сохраняем результаты
reviews_df.to_csv('data/emotion_analysis_results.csv', index=False)

print("Emotion analysis complete. Saved to 'data/emotion_analysis_results.csv'.")
