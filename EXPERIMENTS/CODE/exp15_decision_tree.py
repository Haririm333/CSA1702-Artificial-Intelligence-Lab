import math
from collections import Counter

dataset = [
    {'Outlook': 'Sunny', 'Temperature': 'Hot', 'Humidity': 'High', 'Wind': 'Weak', 'Play': 'No'},
    {'Outlook': 'Sunny', 'Temperature': 'Hot', 'Humidity': 'High', 'Wind': 'Strong', 'Play': 'No'},
    {'Outlook': 'Overcast', 'Temperature': 'Hot', 'Humidity': 'High', 'Wind': 'Weak', 'Play': 'Yes'},
    {'Outlook': 'Rain', 'Temperature': 'Mild', 'Humidity': 'High', 'Wind': 'Weak', 'Play': 'Yes'},
    {'Outlook': 'Rain', 'Temperature': 'Cool', 'Humidity': 'Normal', 'Wind': 'Weak', 'Play': 'Yes'},
    {'Outlook': 'Rain', 'Temperature': 'Cool', 'Humidity': 'Normal', 'Wind': 'Strong', 'Play': 'No'},
    {'Outlook': 'Overcast', 'Temperature': 'Cool', 'Humidity': 'Normal', 'Wind': 'Strong', 'Play': 'Yes'},
    {'Outlook': 'Sunny', 'Temperature': 'Mild', 'Humidity': 'High', 'Wind': 'Weak', 'Play': 'No'},
    {'Outlook': 'Sunny', 'Temperature': 'Cool', 'Humidity': 'Normal', 'Wind': 'Weak', 'Play': 'Yes'},
    {'Outlook': 'Rain', 'Temperature': 'Mild', 'Humidity': 'Normal', 'Wind': 'Weak', 'Play': 'Yes'},
    {'Outlook': 'Sunny', 'Temperature': 'Mild', 'Humidity': 'Normal', 'Wind': 'Strong', 'Play': 'Yes'},
    {'Outlook': 'Overcast', 'Temperature': 'Mild', 'Humidity': 'High', 'Wind': 'Strong', 'Play': 'Yes'},
    {'Outlook': 'Overcast', 'Temperature': 'Hot', 'Humidity': 'Normal', 'Wind': 'Weak', 'Play': 'Yes'},
    {'Outlook': 'Rain', 'Temperature': 'Mild', 'Humidity': 'High', 'Wind': 'Strong', 'Play': 'No'}
]

target_attribute = 'Play'
features = ['Outlook', 'Temperature', 'Humidity', 'Wind']

def entropy(rows):
    labels = [row[target_attribute] for row in rows]
    total = len(labels)
    if total == 0:
        return 0
    counts = Counter(labels)
    ent = 0
    for count in counts.values():
        p = count / total
        ent -= p * math.log2(p)
    return ent

def info_gain(rows, feature):
    total_entropy = entropy(rows)
    total_count = len(rows)
    splits = {}
    for row in rows:
        val = row[feature]
        splits.setdefault(val, []).append(row)

    weighted_entropy = sum((len(sub) / total_count) * entropy(sub) for sub in splits.values())
    return total_entropy - weighted_entropy

def build_tree(rows, available_features):
    labels = [row[target_attribute] for row in rows]
    if len(set(labels)) == 1:
        return labels[0]

    if not available_features:
        return Counter(labels).most_common(1)[0][0]

    best_feature = max(available_features, key=lambda f: info_gain(rows, f))
    tree = {best_feature: {}}
    remaining_features = [f for f in available_features if f != best_feature]

    feature_values = set(row[best_feature] for row in rows)
    for val in feature_values:
        sub_rows = [row for row in rows if row[best_feature] == val]
        tree[best_feature][val] = build_tree(sub_rows, remaining_features)

    return tree

def print_tree(tree, indent=""):
    for key, val in tree.items():
        if isinstance(val, dict):
            for sub_key, sub_val in val.items():
                if isinstance(sub_val, dict):
                    print(f"{indent}[{key} = {sub_key}]:")
                    print_tree(sub_val, indent + "  ")
                else:
                    print(f"{indent}[{key} = {sub_key}] -> Play: {sub_val}")

decision_tree = build_tree(dataset, features)
print("Decision Tree (ID3):")
print_tree(decision_tree)
