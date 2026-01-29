# AI Video Generator (hack-a-thing-2)

Personalized video generation platform using AI-generated video clips.

### What We Built

We built an AI-powered video generation platform that allows users to create personalized videos from text prompts. The system includes both a Python API and a web interface, integrating with Replicate's text-to-video models (Zeroscope) to generate custom video content. The platform features a modular architecture that supports personalization and multiple AI providers.

### Who Did What

Isaac worked on the video generation system, signing up and working with Replicate as the AI API platform. Arsh worked on making the API work across multiple devices and integrating the system into a web interface.

### What We Learned

The majority of the project was invested in learning about how to work with APIs. We learned about authentication with API keys and that a budget is necessary for this project because AI generation is not free. This is especially important when considering the quality and speed of the video generation that we want for our project.

### How This Relates to Possible Project Ideas

Since our project is involved in personalized AI generated videos, we tried to work on specific video generation through text. Again, we want to emphasize how if we want to use APIs to try to AI generate videos, we need to consider how coming up with high quality videos may come with a high cost.

### What Didn't Work

The API had very large limitations with the video generating very low quality videos or just completely not showing the text prompt inputted. Another limitation was the speed as the video generation took minutes to work given a prompt. 

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
# Edit .env with your API keys (REPLICATE_API_KEY required)
```

## Usage

### Web Interface (Recommended)

Start the Flask web application:
```bash
python app.py
```

Then open your browser to: **http://localhost:5000**

Features:
- Simple web form to enter video prompts
- Real-time video generation
- View and download generated videos
- Clean, modern UI

### Python API

```python
from src.generators.video_generator import VideoGenerator

generator = VideoGenerator()
video = generator.generate(
    prompt="A serene mountain landscape at sunset",
    personalization_data={"user_name": "John"}
)
```

### Command Line Examples

```bash
# Basic generation
python examples/basic_generation.py

# Personalized videos
python examples/personalized_generation.py

# Async generation with status polling
python examples/async_generation.py
```

## Project Structure

- `app.py` - Flask web application
- `src/` - Main source code
  - `generators/` - Video generation modules
  - `personalization/` - User data and personalization logic
  - `utils/` - Helper functions
- `templates/` - HTML templates for web interface
- `static/` - CSS and JavaScript assets
- `examples/` - Example scripts
- `output/` - Generated videos

## Features

- **Web Interface** - Easy-to-use browser-based video generation
- **AI-Generated Video Clips** - Text-to-video using state-of-the-art models
- **Personalization Engine** - Custom content based on user data
- **Multiple AI Providers** - Support for Replicate, with extensible architecture
- **Modular Design** - Clean, maintainable codebase
- **Async Support** - Non-blocking generation for multiple videos

## API Keys

You'll need a Replicate API key:
1. Sign up at [replicate.com](https://replicate.com)
2. Get your API token from account settings
3. Add it to your `.env` file

Optional keys:
- `ANTHROPIC_API_KEY` - For AI-powered prompt enhancement
- `OPENAI_API_KEY` - For future integrations