import matplotlib.pyplot as plt
import numpy as np

with open(r'C:\Users\Lucas\Documents\02631 3-Week-Project\trained_models\Logfile_for_6400x1600_e500.log') as f:
    lines = f.readlines()

saved = []
for x in lines:
    if x.startswith('400'):
        saved.append(x)

lines = None
loss = []
accuracy = []
val_loss = []
val_accuracy = []
for line in saved:
    words = line.split()
    for i, word in enumerate(words):
        if word == 'loss:':
            loss.append(float(words[i + 1]))
        elif word == 'accuracy:':
            accuracy.append(float(words[i + 1]))
        elif word == 'val_loss:':
            val_loss.append(float(words[i + 1]))
        elif word == 'val_accuracy:':
            val_accuracy.append(float(words[i + 1]))

saved = None

# Generate some sample data
degree = 100
# degree = int(100/7)
x = range(1, len(loss) + 1)[:]


# Fit a polynomial of degree 2 (a parabola) to the data

def get_polynomial(data):
    return np.poly1d(np.polyfit(x, data[:len(x)], degree))


# Plot the data and the fitted polynomial
# plt.scatter(x, y, color='b', label='Data')
# plt.plot(x, get_polynomial(loss)(x), label='Loss')
polynomial = get_polynomial(val_loss)(x)
# plt.plot(x, polynomial, label='Validation Loss')
# plt.plot(x, get_polynomial(np.array([1 - z for z in accuracy]))(x), label='Error')
polynomial1 = get_polynomial(np.array([1 - z for z in val_accuracy]))(x)
# plt.plot(x, polynomial1, label='Validation Error')
plt.plot(x, (polynomial+polynomial1), label='Thing')
print(np.argmin(polynomial+polynomial1))

plt.xlabel('Epochs')
plt.ylabel('Error')
plt.legend()
plt.grid()
plt.show()

# Plot loss
# fig, ax = plt.subplots()
# ax.plot(loss[:40], label='Training Loss')
# ax.plot(val_loss[:40], label='Validation Loss')
#
# # Add a title, axis labels, and a legend
# ax.set_title('Training and Validation Loss')
# ax.set_xlabel('Epoch')
# ax.set_ylabel('Loss')
# ax.legend()
# plt.grid()
#
# # Display the plot
# plt.show()

#
#
# # Create a figure and an axis
# fig, ax = plt.subplots()
# # Plot the training and validation errors
# ax.plot(accuracy, label='Training Accuracy')
# ax.plot(val_accuracy, label='Validation Accuracy')
#
# # Add a title, axis labels, and a legend
# ax.set_title('Training and Validation Accuracy')
# ax.set_xlabel('Epoch')
# ax.set_ylabel('Accuracy')
# ax.legend()
# plt.grid()
#
# # Display the plot
# plt.show()
#
# # combined
#
# # Create a figure and an axis
# fig, ax = plt.subplots()
# # Plot the training and validation errors
# ax.plot(loss, label='Training Loss')
# ax.plot(val_loss, label='Validation Loss')
# ax.plot(accuracy, label='Training Accuracy')
# ax.plot(val_accuracy, label='Validation Accuracy')
#
# # Add a title, axis labels, and a legend
# ax.set_title('Training and Validation Accuracy')
# ax.set_xlabel('Epoch')
# ax.set_ylabel('Error')
# ax.legend()
# plt.grid()
#
# # Display the plot
# plt.show()
