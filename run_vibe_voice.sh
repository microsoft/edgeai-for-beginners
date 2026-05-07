#!/bin/bash

# VibeVoice Audio Generation Script
# This script clones VibeVoice, installs dependencies, and generates audio from podcast text

set -e  # Exit on error

echo "Step 1: Cloning VibeVoice repository..."
if [ ! -d "VibeVoice" ]; then
    git clone https://github.com/vibevoice-community/VibeVoice.git
else
    echo "VibeVoice directory already exists, skipping clone."
fi

echo "Step 2: Installing dependencies..."
cd VibeVoice/
uv pip install -e .

echo "Step 3: Generating audio from podcast text..."
uv run demo/inference_from_file.py \
    --model_path vibevoice/VibeVoice-7B \
    --txt_path ../src/02.Workflow-MultiAgent/03.Application/podcast.txt \
    --speaker_names Carter Alice

echo "Audio generation complete!"
