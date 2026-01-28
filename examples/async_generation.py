#!/usr/bin/env python3
"""
Example of async video generation with status polling.
"""

import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.generators.video_generator import VideoGenerator
from src.config import config

def main():
    # Validate configuration
    try:
        config.validate()
    except ValueError as e:
        print(f"Configuration error: {e}")
        return

    generator = VideoGenerator(provider="replicate", model="zeroscope")

    prompt = "A time-lapse of a bustling city street transitioning from day to night"

    print("Starting async video generation...")
    print(f"Prompt: {prompt}")

    # Start async generation
    job_id = generator.generate_async(prompt)
    print(f"Job started with ID: {job_id}")
    print("-" * 60)

    # Poll for completion
    while True:
        status = generator.get_status(job_id)

        print(f"Status: {status['status']}")

        if status['status'] == 'succeeded':
            print("Video generation complete!")
            print(f"Output URL: {status['output']}")
            break
        elif status['status'] == 'failed':
            print(f"Generation failed: {status['error']}")
            break

        time.sleep(5)  # Wait 5 seconds before checking again

if __name__ == "__main__":
    main()
