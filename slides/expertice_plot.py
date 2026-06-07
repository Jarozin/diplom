import pandas as pd
import matplotlib.pyplot as plt

# Настройка глобальных параметров шрифта (увеличено)
plt.rcParams.update({
    'font.size': 18,
    'axes.labelsize': 20,
    'axes.titlesize': 22,
    'legend.fontsize': 16,
    'xtick.labelsize': 16,
    'ytick.labelsize': 16
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

# Контрастные цвета
colors = ['#1A5276', '#1E8449', '#D35400', '#6C3483', '#B7950B']

# Построение горизонтальной столбчатой диаграммы
fig, ax = plt.subplots(figsize=(14, 8))
bars = df.plot(kind='barh', stacked=True, ax=ax, color=colors, edgecolor='black', linewidth=1.5)

ax.set_xlabel('Вклад критериев', fontsize=20)
ax.set_ylabel('Уровень экспертизы', fontsize=20)
ax.set_title('Сравнение вкладов критериев для разных уровней экспертизы', fontsize=22, pad=20)
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), title='Критерии', title_fontsize=16, fontsize=14, frameon=True, edgecolor='black')
ax.set_xlim(0, 1)

# Утолщение границ
ax.spines['top'].set_linewidth(1.5)
ax.spines['right'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['left'].set_linewidth(1.5)
ax.grid(axis='x', linestyle='--', alpha=0.5, linewidth=0.8)

# Добавление процентов на столбцы (без жирного шрифта)
for c in ax.containers:
    labels = [f'{v:.0%}' if v > 0.03 else '' for v in c.datavalues]
    ax.bar_label(c, labels=labels, label_type='center', fontsize=14)

plt.tight_layout()
plt.savefig('chart.pdf', bbox_inches='tight', dpi=300)
plt.show()