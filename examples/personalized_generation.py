#!/usr/bin/env python3
"""
Example of generating personalized AI videos.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.generators.video_generator import VideoGenerator
from src.personalization.prompt_builder import AIPromptBuilder
from src.config import config

def main():
    # Validate configuration
    try:
        config.validate()
    except ValueError as e:
        print(f"Configuration error: {e}")
        print("Please set up your .env file with the required API keys.")
        return

    # Example user data
    user_data = {
        "name": "Sarah",
        "favorite_color": "purple",
        "hobby": "hiking",
        "location": "mountains"
    }

    # Build personalized prompt using AI
    prompt_builder = AIPromptBuilder()

    base_template = """Create a personalized nature video for {name} who loves
    {hobby} in the {location} and their favorite color is {favorite_color}"""

    personalized_prompt = prompt_builder.build_prompt(base_template, user_data)

    print("Personalized prompt generated:")
    print(f"  {personalized_prompt}")
    print("-" * 60)

    # Generate the video
    generator = VideoGenerator(provider="replicate", model="zeroscope")

    print("Starting video generation...")
    video_path = generator.generate(personalized_prompt)

    print("-" * 60)
    print(f"Personalized video generated: {video_path}")

if __name__ == "__main__":
    main()
