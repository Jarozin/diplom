import matplotlib.pyplot as plt
import numpy as np

# Данные из графика
alternatives = np.array([5, 10, 16, 20, 30, 50])
time_classic = np.array([0.20, 0.80, 1.58, 2.50, 5.80, 16.0])
time_modified = np.array([0.20, 0.42, 0.45, 0.60, 0.85, 1.30])

# Глобальная настройка шрифтов
plt.rcParams['font.size'] = 18
plt.rcParams['axes.labelsize'] = 18
plt.rcParams['axes.titlesize'] = 18
plt.rcParams['legend.fontsize'] = 16
plt.rcParams['xtick.labelsize'] = 14
plt.rcParams['ytick.labelsize'] = 14

# Параметры группировки столбцов
x = np.arange(len(alternatives))
width = 0.35

# Построение гистограммы с различными узорами для ЧБ печати
fig, ax = plt.subplots(figsize=(10, 6))

# Используем разные штриховки и оттенки серого
bars1 = ax.bar(x - width/2, time_classic, width, 
               label='Классический МАИ', 
               facecolor='white', edgecolor='black', linewidth=1.5,
               hatch='///')  # диагональная штриховка

bars2 = ax.bar(x + width/2, time_modified, width, 
               label='Модификация МАИ', 
               facecolor='lightgray', edgecolor='black', linewidth=1.5,
               hatch='\\\\\\')  # обратная диагональная штриховка

# Альтернативные варианты штриховок:
# '///'  - диагональные линии вправо
# '\\\\\\' - диагональные линии влево  
# '|||' - вертикальные линии
# '---' - горизонтальные линии
# 'xxx' - перекрестные линии
# '...' - точки
# 'OOO' - кружочки

# Оформление
ax.set_xlabel('Количество альтернатив (m)')
ax.set_ylabel('Время (часы)')
ax.set_title('Сравнение временных затрат на попарные сравнения')
ax.set_xticks(x)
ax.set_xticklabels(alternatives)
ax.legend()
ax.grid(axis='y', linestyle='--', alpha=0.5)

# Подписи значений на столбцах
for bar in bars1:
    height = bar.get_height()
    ax.annotate(f'{height:.2f}',
                xy=(bar.get_x() + bar.get_width()/2, height),
                xytext=(0, 5), textcoords="offset points",
                ha='center', va='bottom', fontsize=11, fontweight='bold')

for bar in bars2:
    height = bar.get_height()
    ax.annotate(f'{height:.2f}',
                xy=(bar.get_x() + bar.get_width()/2, height),
                xytext=(0, 5), textcoords="offset points",
                ha='center', va='bottom', fontsize=11, fontweight='bold')

plt.tight_layout()
plt.savefig('time_comparison_bw.pdf', dpi=300, bbox_inches='tight')
plt.show()