# AI Video Generator (hack-a-thing-2)

Personalized video generation platform using AI-generated video clips.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure your API keys:
```bash
cp .env.example .env
# Edit .env with your API keys
```

## Project Structure

- `src/` - Main source code
  - `generators/` - Video generation modules
  - `personalization/` - User data and personalization logic
  - `utils/` - Helper functions
- `examples/` - Example scripts
- `output/` - Generated videos

## Usage

```python
from src.generators.video_generator import VideoGenerator

generator = VideoGenerator()
video = generator.generate(
    prompt="A serene mountain landscape at sunset",
    personalization_data={"user_name": "John"}
)
```

## Features

- AI-generated video clips using text-to-video models
- Personalization engine for custom content
- Modular architecture for easy extension
- Support for multiple AI providers
