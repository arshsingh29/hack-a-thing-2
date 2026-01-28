from typing import Dict, Any, Optional
from pathlib import Path
from .replicate_generator import ReplicateVideoGenerator

class VideoGenerator:
    """
    Main video generator class that handles AI video generation
    with personalization support.
    """

    def __init__(self, provider: str = "replicate", model: str = "zeroscope"):
        """
        Initialize the video generator.

        Args:
            provider: AI provider to use ('replicate', etc.)
            model: Specific model to use
        """
        self.provider = provider

        if provider == "replicate":
            self.generator = ReplicateVideoGenerator(model_name=model)
        else:
            raise ValueError(f"Unknown provider: {provider}")

    def generate(
        self,
        prompt: str,
        personalization_data: Optional[Dict[str, Any]] = None,
        **kwargs
    ) -> Path:
        """
        Generate a personalized video.

        Args:
            prompt: Base prompt for video generation
            personalization_data: User-specific data for personalization
            **kwargs: Additional generation parameters

        Returns:
            Path to the generated video file
        """
        # Apply personalization to the prompt
        personalized_prompt = self._personalize_prompt(prompt, personalization_data)

        # Generate the video
        return self.generator.generate(personalized_prompt, **kwargs)

    def generate_async(
        self,
        prompt: str,
        personalization_data: Optional[Dict[str, Any]] = None,
        **kwargs
    ) -> str:
        """
        Start async video generation.

        Returns:
            Job ID for tracking
        """
        personalized_prompt = self._personalize_prompt(prompt, personalization_data)
        return self.generator.generate_async(personalized_prompt, **kwargs)

    def get_status(self, job_id: str) -> Dict[str, Any]:
        """Get the status of an async generation job."""
        return self.generator.get_status(job_id)

    def _personalize_prompt(
        self,
        prompt: str,
        personalization_data: Optional[Dict[str, Any]]
    ) -> str:
        """
        Apply personalization to the video prompt.

        Args:
            prompt: Base prompt
            personalization_data: User data for personalization

        Returns:
            Personalized prompt
        """
        if not personalization_data:
            return prompt

        # Simple template substitution
        personalized = prompt
        for key, value in personalization_data.items():
            placeholder = f"{{{key}}}"
            if placeholder in personalized:
                personalized = personalized.replace(placeholder, str(value))

        return personalized
