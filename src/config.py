import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Configuration management for the video generator."""

    # API Keys
    REPLICATE_API_KEY = os.getenv("REPLICATE_API_KEY")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

    # Paths
    PROJECT_ROOT = Path(__file__).parent.parent
    OUTPUT_DIR = Path(os.getenv("OUTPUT_DIR", "./output"))

    # Video Settings
    DEFAULT_VIDEO_DURATION = int(os.getenv("DEFAULT_VIDEO_DURATION", "5"))
    DEFAULT_VIDEO_RESOLUTION = os.getenv("DEFAULT_VIDEO_RESOLUTION", "1024x576")

    @classmethod
    def validate(cls):
        """Validate that required configuration is present."""
        if not cls.REPLICATE_API_KEY:
            raise ValueError("REPLICATE_API_KEY not found in environment")

        cls.OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

        return True

config = Config()
