import matplotlib.pyplot as plt
import numpy as np

# Training and validation data
loss = np.array([0.5220, 0.3425, 0.2853, 0.2544, 0.2345, 0.2311, 0.2063, 0.2067, 0.2075, 0.1912])
accuracy = np.array([0.7486, 0.8589, 0.8897, 0.8995, 0.9111, 0.9127, 0.9223, 0.9222, 0.9212, 0.9309])
val_loss = np.array([0.3292, 0.2907, 0.2296, 0.2046, 0.2621, 0.1821, 0.1889, 0.2095, 0.1963, 0.1667])
val_accuracy = np.array([0.8687, 0.8838, 0.9119, 0.9225, 0.9062, 0.9381, 0.9300, 0.9181, 0.9344, 0.9381])

# Plot loss
fig, ax = plt.subplots()
ax.plot(loss, label='Training Loss')
ax.plot(val_loss, label='Validation Loss')

# Add a title, axis labels, and a legend
ax.set_title('Training and Validation Loss')
ax.set_xlabel('Epoch')
ax.set_ylabel('Loss')
ax.legend()
plt.grid()

# Display the plot
plt.show()



# Create a figure and an axis
fig, ax = plt.subplots()
# Plot the training and validation errors
ax.plot(accuracy, label='Training Accuracy')
ax.plot(val_accuracy, label='Validation Accuracy')

# Add a title, axis labels, and a legend
ax.set_title('Training and Validation Accuracy')
ax.set_xlabel('Epoch')
ax.set_ylabel('Accuracy')
ax.legend()
plt.grid()

# Display the plot
plt.show()

# combined

# Create a figure and an axis
fig, ax = plt.subplots()
# Plot the training and validation errors
ax.plot(loss, label='Training Loss')
ax.plot(val_loss, label='Validation Loss')
ax.plot(accuracy, label='Training Accuracy')
ax.plot(val_accuracy, label='Validation Accuracy')

# Add a title, axis labels, and a legend
ax.set_title('Training and Validation Accuracy')
ax.set_xlabel('Epoch')
ax.set_ylabel('Error')
ax.legend()
plt.grid()

# Display the plot
plt.show()