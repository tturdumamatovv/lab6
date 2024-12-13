import pandas as pd
from sklearn.metrics import accuracy_score, classification_report

# Загрузка результатов анализа тональности
results_df = pd.read_csv('data/sentiment_analysis_results.csv')

# Предположим, что у вас есть истинные метки (например, в отдельном файле)
true_labels = [...]  # Замените на ваши истинные метки

# Получение предсказанных меток
predicted_labels = results_df['Sentiment_Score'].apply(lambda x: 1 if x > 0 else 0)  # Пример: 1 для положительных, 0 для отрицательных

# Оценка модели
accuracy = accuracy_score(true_labels, predicted_labels)
print(f'Accuracy: {accuracy:.2f}')

# Дополнительная информация
print(classification_report(true_labels, predicted_labels))
