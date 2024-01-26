import os

# Directory containing the mood board images
directory = 'C:/Users/bryan/Documents/GitHub/24-Blocks-OpenStorytelling/MoodBoard/'

# Base URL for the GitHub repository where the images are hosted
base_url = "https://github.com/BryanHarrisScripts/24-Blocks-OpenStorytelling/blob/main/MoodBoard/"

# Start of the markdown content for README.md
readme_content = "# Mood Board Collection\n\n| Image | Description |\n| --- | --- |\n"

# Iterate through each file in the directory and create markdown table rows
for filename in os.listdir(directory):
    if filename.endswith('.png'):
        title = filename.split(' - ')[0].replace('DALL·E 2024-01-26 ', '')
        image_url = base_url + filename.replace(' ', '%20')
        image_md = f"<img src=\"{image_url}\" width=\"200\" height=\"200\" alt=\"{title}\"/>"
        description = filename.split(' - ')[1].split('.')[0]
        readme_content += f"| {image_md} | **{title}** - {description} |\n"

# Write the markdown content to README.md
with open(os.path.join(directory, "README.md"), "w") as file:
    file.write(readme_content)

"README.md file created with the complete mood board collection."

