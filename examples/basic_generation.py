#!/usr/bin/env python3
"""
Basic example of generating an AI video.
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.generators.video_generator import VideoGenerator
from src.config import config

def main():
    # Validate configuration
    try:
        config.validate()
    except ValueError as e:
        print(f"Configuration error: {e}")
        print("Please set up your .env file with the required API keys.")
        return

    # Create video generator
    generator = VideoGenerator(provider="replicate", model="zeroscope")

    # Generate a simple video
    prompt = "A majestic eagle soaring over snow-capped mountains at golden hour"

    print("Starting video generation...")
    print(f"Prompt: {prompt}")
    print("-" * 60)

    video_path = generator.generate(prompt)

    print("-" * 60)
    print(f"Video generated successfully: {video_path}")

if __name__ == "__main__":
    main()
