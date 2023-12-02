import json
import requests
import os

# Define a list of plugins with their repository names and internal names
plugins = [
    {"repo_name": "UnstablePlugin", "internal_name": "UnstablePlugin"},
    {"repo_name": "EasySolver", "internal_name": "EasySolver"},
    # Add more plugins here as needed
]

def update_download_count(data, repo_name, internal_name):
    # Fetch the download count from the GitHub API for the specific release
    release_url = f'https://api.github.com/repos/UnstableFlipPhone/{repo_name}/releases/latest'
    response = requests.get(release_url)
    if response.status_code == 200:
        release_data = response.json()
        download_count = release_data['assets'][0]['download_count']
    else:
        download_count = 0

    # Get the previous download count from the JSON file
    previous_download_count = None
    for plugin in data:
        if plugin['InternalName'] == internal_name:
            previous_download_count = plugin.get('DownloadCount', None)
            break

    # Update the download count for the specified plugin
    for plugin in data:
        if plugin['InternalName'] == internal_name:
            plugin['DownloadCount'] = str(download_count)

    # Check if the download count has changed, and exit successfully if it hasn't
    if previous_download_count is not None and previous_download_count == str(download_count):
        print(f"Download count for {internal_name} hasn't changed. Exiting without updating.")
        os._exit(0)

if __name__ == '__main__':
    # Read the existing JSON file
    with open('pluginmaster.json', 'r') as f:
        data = json.load(f)

    # Update the download counts for each plugin
    for plugin_info in plugins:
        update_download_count(data, plugin_info["repo_name"], plugin_info["internal_name"])

    # Write the updated JSON back to the file
    with open('pluginmaster.json', 'w') as f:
        json.dump(data, f, indent=2)
