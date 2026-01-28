import replicate
import requests
from pathlib import Path
from typing import Dict, Any, Optional
from ..config import config
from .base_generator import BaseVideoGenerator

class ReplicateVideoGenerator(BaseVideoGenerator):
    """Video generator using Replicate's text-to-video models."""

    # Available models
    MODELS = {
        "stable-video-diffusion": "stability-ai/stable-video-diffusion:3f0457e4619daac51203dedb472816fd4af51f3149fa7a9e0b5ffcf1b8172438",
        "zeroscope": "anotherjesse/zeroscope-v2-xl:9f747673945c62801b13b84701c783929c0ee784e4748ec062204894dda1a351",
    }

    def __init__(self, model_name: str = "zeroscope", config_dict: Optional[Dict[str, Any]] = None):
        super().__init__(config_dict)
        self.model_name = model_name
        self.model_version = self.MODELS.get(model_name)

        if not self.model_version:
            raise ValueError(f"Unknown model: {model_name}. Available: {list(self.MODELS.keys())}")

        # Set up Replicate client
        if not config.REPLICATE_API_KEY:
            raise ValueError("REPLICATE_API_KEY not set in environment")

        self.client = replicate.Client(api_token=config.REPLICATE_API_KEY)

    def generate(self, prompt: str, duration: Optional[int] = None, **kwargs) -> Path:
        """
        Generate a video using Replicate's text-to-video models.

        Args:
            prompt: Text description of the video
            duration: Video duration in seconds (model-dependent)
            **kwargs: Additional model-specific parameters

        Returns:
            Path to the downloaded video file
        """
        print(f"Generating video with prompt: '{prompt}'")
        print(f"Using model: {self.model_name}")

        # Prepare input parameters
        input_params = {
            "prompt": prompt,
            **kwargs
        }

        # Run the model
        output = self.client.run(
            self.model_version,
            input=input_params
        )

        # Download the generated video
        video_url = output if isinstance(output, str) else output[0]
        return self._download_video(video_url, prompt)

    def generate_async(self, prompt: str, **kwargs) -> str:
        """
        Start an async video generation job.

        Returns:
            Job ID for tracking
        """
        input_params = {
            "prompt": prompt,
            **kwargs
        }

        prediction = self.client.predictions.create(
            version=self.model_version,
            input=input_params
        )

        return prediction.id

    def get_status(self, job_id: str) -> Dict[str, Any]:
        """
        Check the status of a video generation job.

        Args:
            job_id: Prediction ID from generate_async

        Returns:
            Dictionary with status, output URL if ready, etc.
        """
        prediction = self.client.predictions.get(job_id)

        return {
            "status": prediction.status,
            "output": prediction.output,
            "error": prediction.error,
            "logs": prediction.logs
        }

    def _download_video(self, url: str, prompt: str) -> Path:
        """Download video from URL to output directory."""
        config.OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

        # Create a safe filename from the prompt
        safe_name = "".join(c if c.isalnum() or c in (' ', '-', '_') else '_' for c in prompt)
        safe_name = safe_name[:50]  # Limit length

        output_path = config.OUTPUT_DIR / f"{safe_name}.mp4"

        # Make filename unique if it exists
        counter = 1
        while output_path.exists():
            output_path = config.OUTPUT_DIR / f"{safe_name}_{counter}.mp4"
            counter += 1

        print(f"Downloading video to: {output_path}")

        response = requests.get(url, stream=True)
        response.raise_for_status()

        with open(output_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        print(f"Video saved successfully!")
        return output_path
