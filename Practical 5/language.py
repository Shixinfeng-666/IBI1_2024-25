#  Define a dictionary to store programming languages and user percentages
#  Print the original dictionary
#  Create a bar plot using matplotlibExtract languages and their percentages
#  Add title and labels of the bars
#  Display the bar plot
#  Print the percentage of developers who use a specified language


lang_data = {
    'JavaScript': 62.3,
    'HTML': 52.9,
    'Python': 51,
    'SQL': 51,
    'TypeScript': 38.5
}  # Define a dictionary to store programming languages and their user percentages

# Print the original dictionary
print("Original dictionary:")
print(lang_data)

# Create a bar plot using matplotlib
import matplotlib.pyplot as plt

# Extract languages and their corresponding user percentages to set as X/Y axis
languages = list(lang_data.keys())
users = list(lang_data.values())

# Create the bar plot 
p1 = plt.bar(languages, users, color='blue')
# Add title and labels with set properties
plt.title('Programming Language Popularity', fontsize=16)
plt.xlabel('Language', fontsize=14, color='red')
plt.ylabel('Users in %', color='blue', fontsize=14)
# (Here's a try to see whether the order influences or not.-- It shows not)
plt.show()

the_language = 'Python' # use 'Python' users as an example
if the_language in lang_data:
    print('The percentage of Python user is',lang_data ['Python'], '%')
else:
    print(f'{the_language} is not in the dictionary')

the_language = 'Pycharm'
if the_language in lang_data:
    print('The percentage of Python user is',lang_data ['Python'], '%')
else:
    print(f'{the_language} is not in the dictionary')
