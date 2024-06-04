#!/bin/bash

# Define the directory where the virtual environment and tool will be installed
INSTALL_DIR="$HOME/favhashgen"

# Create the installation directory if it doesn't exist
mkdir -p "$INSTALL_DIR"

# Create a Python virtual environment in the installation directory
python3 -m venv "$INSTALL_DIR/venv"

# Activate the virtual environment
source "$INSTALL_DIR/venv/bin/activate"

# Install the required Python packages
pip install -r requirements.txt

# Deactivate the virtual environment
deactivate

# Create a symbolic link to the script in /usr/local/bin for easy access
sudo ln -sf "$INSTALL_DIR/favhashgen.py" /usr/local/bin/favhashgen

# Make the script executable
chmod +x "$INSTALL_DIR/favhashgen.py"

echo "Setup complete. You can now run the tool using the command 'favhashgen'"
