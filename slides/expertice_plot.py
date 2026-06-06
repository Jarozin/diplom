import pandas as pd
import matplotlib.pyplot as plt

# Настройка глобальных параметров шрифта
plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 16,
    'axes.titlesize': 18,
    'legend.fontsize': 12,
    'xtick.labelsize': 13,
    'ytick.labelsize': 13
})

# Данные
data = {
    'Критерий': ['Безопасность', 'Полезность', 'Актуальность', 'Срочность', 'Критичность'],
    'Новичок': [0.48, 0.24, 0.14, 0.09, 0.05],
    'Опытный': [0.35, 0.28, 0.18, 0.12, 0.07],
    'Эксперт': [0.22, 0.28, 0.18, 0.12, 0.20]
}

df = pd.DataFrame(data)
df.set_index('Критерий', inplace=True)

# Транспонируем: строки = уровни экспертизы, столбцы = критерии
df = df.T

# Построение горизонтальной столбчатой диаграммы (stacked barh) с увеличенным размером фигуры
fig, ax = plt.subplots(figsize=(12, 7))
df.plot(kind='barh', stacked=True, ax=ax,
        color=['#4472C4', '#70AD47', '#ED7D31', '#B4C7E7', '#9B59B6'])

ax.set_xlabel('Вклад критериев', fontsize=16)
ax.set_ylabel('Уровень экспертизы', fontsize=16)
ax.set_title('Сравнение вкладов критериев для разных уровней экспертизы', fontsize=18, pad=20)
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), title='Критерии', title_fontsize=14, fontsize=13)
ax.set_xlim(0, 1)

# Добавление процентов на столбцы с увеличенным шрифтом
for c in ax.containers:
    labels = [f'{v:.0%}' if v > 0.03 else '' for v in c.datavalues]
    ax.bar_label(c, labels=labels, label_type='center', fontsize=12)

plt.tight_layout()
plt.savefig('chart.pdf', bbox_inches='tight', dpi=150)
plt.show()