import json
import sys

def update_plugin(name, version):
    for plugin in data:
        if plugin['InternalName'] == name:
            plugin['AssemblyVersion'] = version
            plugin['DownloadLinkInstall'] = f'https://github.com/UnstableFlipPhone/{name}/releases/download/{version}/latest.zip'
            plugin['DownloadLinkUpdate'] = f'https://github.com/UnstableFlipPhone/{name}/releases/download/{version}/latest.zip'

if __name__ == '__main__':
    name = sys.argv[1]  # Get the plugin name from the command line
    version = sys.argv[2]  # Get the version from the command line

    # Read the existing JSON file
    with open('pluginmaster.json', 'r') as f:
        data = json.load(f)

    # Update the plugin
    update_plugin(name, version)

    # Write the updated JSON back to the file
    with open('pluginmaster.json', 'w') as f:
        json.dump(data, f, indent=2)
