import os

true_classification_path = r'C:\Users\Lucas\Pictures\02461 Pictures\Testing'
ai_classified_path = r'C:\Users\Lucas\Pictures\02461 Pictures\AI_Test'

males = []
females = []
for subfolder in ['male', 'female']:
    for filename in os.listdir(os.path.join(true_classification_path, subfolder)):
        if subfolder.startswith('m'):
            males.append(filename)
        else:
            females.append(filename)
ai_males = []
ai_females = []
for subfolder in ['male', 'female']:
    for filename in os.listdir(os.path.join(ai_classified_path, subfolder)):
        if subfolder.startswith('m'):
            ai_males.append(filename)
        else:
            ai_females.append(filename)

should_have_been_sorted_to_male = []
for file in males:
    if file in ai_males:
        continue

    should_have_been_sorted_to_male.append(file)

should_have_been_sorted_to_female = []
for file in females:
    if file in ai_females:
        continue

    should_have_been_sorted_to_female.append(file)

accuracy = (len(should_have_been_sorted_to_female) + len(should_have_been_sorted_to_male)) / (len(males) + len(
    females)) - 1
print('accuracy', str(round(abs(accuracy * 100), 2)) + '%')
