import csv
import os
import random
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

random.seed(42)

data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)
filepath = os.path.join(data_dir, 'students_scores.csv')

if not os.path.exists(filepath):
    names = ['Aisha', 'Daniyar', 'Zarina', 'Arman', 'Gulnur',
             'Bekzat', 'Saltanat', 'Nursultan', 'Madina', 'Yerlan',
             'Aizat', 'Timur', 'Moldir', 'Azat', 'Diana',
             'Sanzhar', 'Ainur', 'Marat', 'Kamila', 'Dauren']
    genders = ['Female', 'Male', 'Female', 'Male', 'Female',
               'Male', 'Female', 'Male', 'Female', 'Male',
               'Female', 'Male', 'Female', 'Male', 'Female',
               'Male', 'Female', 'Male', 'Female', 'Male']
    groups = ['SE-101', 'SE-101', 'SE-102', 'SE-102', 'SE-103',
              'SE-103', 'SE-101', 'SE-102', 'SE-103', 'SE-101',
              'SE-102', 'SE-103', 'SE-101', 'SE-102', 'SE-103',
              'SE-101', 'SE-102', 'SE-103', 'SE-101', 'SE-102']
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['student_id', 'name', 'gender', 'group',
                         'math_score', 'python_score', 'english_score'])
        for i, name in enumerate(names):
            writer.writerow([i + 1, name, genders[i], groups[i],
                             random.randint(45, 100),
                             random.randint(40, 100),
                             random.randint(50, 100)])
    print(f"Dataset created: {os.path.abspath(filepath)}")
else:
    print(f"Dataset already exists: {os.path.abspath(filepath)}")

print("\n" + "=" * 55)
print("  TASK 1: File Setup with OS Module")
print("=" * 55)

if not os.path.exists(filepath):
    print("Error: File not found!")
    exit()

abs_path = os.path.abspath(filepath)
print(f"File found:    {abs_path}")
print(f"Absolute path: {abs_path}")

print("\n" + "=" * 55)
print("  TASK 2: Reading CSV with the csv Module")
print("=" * 55)

with open(filepath, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    print(f"Fields: {reader.fieldnames}\n")
    rows = list(reader)
    for idx, row in enumerate(rows[:5], start=1):
        print(f"Row {idx}: {dict(row)}")

print(f"\nTotal students: {len(rows)}")

print("\n" + "=" * 55)
print("  TASK 3: Data Analysis with Pandas")
print("=" * 55)

print("\n--- 3a: Load and Inspect ---")
df = pd.read_csv(filepath)
print(df.head())
print(f"\nShape: {df.shape}")
print("\nData types:")
print(df.dtypes)

print("\n--- 3b: Descriptive Statistics ---")
print(df.describe())
score_cols = ['math_score', 'python_score', 'english_score']
print("\nMean:  ", df[score_cols].mean().round(2).to_dict())
print("Median:", df[score_cols].median().to_dict())
print("Std:   ", df[score_cols].std().round(2).to_dict())

print("\n--- 3c: Average Score Column ---")
df['average_score'] = df[score_cols].mean(axis=1).round(2)
print(df[['name', 'group', 'average_score']].to_string(index=False))

print("\n--- 3d: Filtering ---")
high_scorers = df[df['average_score'] >= 75]
print(f"\nStudents with average_score >= 75 ({len(high_scorers)} students):")
print(high_scorers[['name', 'group', 'average_score']].to_string(index=False))

group_101 = df[df['group'] == 'SE-101']
print(f"\nStudents in SE-101 ({len(group_101)} students):")
print(group_101[['name', 'group', 'average_score']].to_string(index=False))

print("\n--- 3e: Group Analysis ---")
group_means = df.groupby('group')[score_cols].mean().round(2)
print("\nMean scores by group:")
print(group_means)
gender_means = df.groupby('gender')['average_score'].mean().round(2)
print("\nMean average_score by gender:")
print(gender_means)

print("\n" + "=" * 55)
print("  TASK 4: Data Visualization")
print("=" * 55)

group_avg = df.groupby('group')['average_score'].mean()
plt.figure(figsize=(8, 5))
plt.bar(group_avg.index, group_avg.values, color=['#3498DB', '#E74C3C', '#2ECC71'])
plt.title('Average Score by Study Group')
plt.xlabel('Study Group')
plt.ylabel('Average Score')
plt.ylim(0, 100)
plt.tight_layout()
plt.savefig(os.path.join(data_dir, 'bar_group_avg.png'), dpi=150, bbox_inches='tight')
plt.show()
print("Saved: bar_group_avg.png")

plt.figure(figsize=(8, 5))
plt.hist(df['python_score'], bins=10, color='#9B59B6', edgecolor='white')
plt.title('Distribution of Python Scores')
plt.xlabel('Python Score')
plt.ylabel('Number of Students')
plt.tight_layout()
plt.savefig(os.path.join(data_dir, 'hist_python_scores.png'), dpi=150, bbox_inches='tight')
plt.show()
print("Saved: hist_python_scores.png")

plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='gender', y='average_score',
            hue='gender', palette='Set2', legend=False)
plt.title('Score Distribution by Gender')
plt.xlabel('Gender')
plt.ylabel('Average Score')
plt.tight_layout()
plt.savefig(os.path.join(data_dir, 'box_gender_scores.png'), dpi=150, bbox_inches='tight')
plt.show()
print("Saved: box_gender_scores.png")

plt.figure(figsize=(8, 6))
corr = df[score_cols + ['average_score']].corr()
sns.heatmap(corr, annot=True, cmap='Blues', fmt='.2f')
plt.title('Correlation Matrix of Student Scores')
plt.tight_layout()
plt.savefig(os.path.join(data_dir, 'heatmap_correlation.png'), dpi=150, bbox_inches='tight')
plt.show()
print("Saved: heatmap_correlation.png")

print("\n" + "=" * 55)
print("  BONUS 1: Summary Report CSV")
print("=" * 55)


def assign_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 75:
        return 'B'
    elif score >= 60:
        return 'C'
    else:
        return 'F'


df['grade'] = df['average_score'].apply(assign_grade)
summary = df[['name', 'group', 'average_score', 'grade']]
summary_path = os.path.join(data_dir, 'summary_report.csv')
summary.to_csv(summary_path, index=False)
print(f"Saved: {os.path.abspath(summary_path)}")
print(summary.to_string(index=False))

print("\n" + "=" * 55)
print("  BONUS 2: Scatter Plot — Math vs Python")
print("=" * 55)

plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='math_score', y='python_score',
                hue='gender', palette='Set1', s=100)
plt.title('Math Score vs Python Score by Gender')
plt.xlabel('Math Score')
plt.ylabel('Python Score')
plt.legend(title='Gender')
plt.tight_layout()
plt.savefig(os.path.join(data_dir, 'scatter_math_vs_python.png'), dpi=150, bbox_inches='tight')
plt.show()
print("Saved: scatter_math_vs_python.png")

print("\n" + "=" * 55)
print("  BONUS 3: Top 3 Students")
print("=" * 55)

top3 = df.nlargest(3, 'average_score')[['name', 'group', 'average_score']]
print("\nTop 3 students by average score:")
for rank, (_, row) in enumerate(top3.iterrows(), start=1):
    print(f"  {rank}. {row['name']:<12} | Group: {row['group']} | Score: {row['average_score']}")

print("\n" + "=" * 55)
print("  All tasks completed successfully!")
print("=" * 55)
