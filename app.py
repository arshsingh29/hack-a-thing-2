from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
from pathlib import Path
import os

from src.generators.video_generator import VideoGenerator
from src.config import config

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'dev-secret-key-change-in-production')

# Configuration
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max request


@app.route('/')
def index():
    """Home page with video generation form."""
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    """Process video generation request."""
    prompt = request.form.get('prompt', '').strip()

    # Validation
    if not prompt:
        flash('Please provide a video prompt', 'error')
        return redirect(url_for('index'))

    if len(prompt) > 500:
        flash('Prompt too long (max 500 characters)', 'error')
        return redirect(url_for('index'))

    try:
        # Validate configuration
        config.validate()

        # Create generator and generate video
        generator = VideoGenerator(provider="replicate", model="zeroscope")
        video_path = generator.generate(prompt)

        # Redirect to result page
        return redirect(url_for('result', filename=video_path.name, prompt=prompt))

    except ValueError as e:
        flash(f'Configuration error: {str(e)}', 'error')
        return redirect(url_for('index'))
    except Exception as e:
        flash(f'Generation failed: {str(e)}', 'error')
        return redirect(url_for('index'))


@app.route('/result/<filename>')
def result(filename):
    """Display the generated video."""
    prompt = request.args.get('prompt', 'Generated video')

    # Verify file exists
    video_path = config.OUTPUT_DIR / filename
    if not video_path.exists():
        flash('Video not found', 'error')
        return redirect(url_for('index'))

    return render_template('result.html', filename=filename, prompt=prompt)


@app.route('/output/<filename>')
def serve_video(filename):
    """Serve video file for viewing in browser."""
    return send_from_directory(config.OUTPUT_DIR, filename)


@app.route('/download/<filename>')
def download_video(filename):
    """Force download of video file."""
    return send_from_directory(config.OUTPUT_DIR, filename, as_attachment=True)


if __name__ == '__main__':
    try:
        config.validate()
        print(f"✓ Configuration valid")
        print(f"✓ Output directory: {config.OUTPUT_DIR}")
        print(f"✓ Starting Flask server on http://0.0.0.0:8080")
        print(f"✓ Access at: http://localhost:8080")
    except ValueError as e:
        print(f"✗ Configuration error: {e}")
        print("Please set up your .env file with REPLICATE_API_KEY")
        exit(1)

    app.run(debug=True, host='0.0.0.0', port=8080)
