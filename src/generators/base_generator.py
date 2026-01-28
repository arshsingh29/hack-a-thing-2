from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
from pathlib import Path

class BaseVideoGenerator(ABC):
    """Abstract base class for video generators."""

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self.config = config or {}

    @abstractmethod
    def generate(self, prompt: str, **kwargs) -> Path:
        """
        Generate a video based on the prompt.

        Args:
            prompt: Text description of the video to generate
            **kwargs: Additional parameters for generation

        Returns:
            Path to the generated video file
        """
        pass

    @abstractmethod
    def get_status(self, job_id: str) -> Dict[str, Any]:
        """
        Check the status of a video generation job.

        Args:
            job_id: Unique identifier for the generation job

        Returns:
            Dictionary with status information
        """
        pass
