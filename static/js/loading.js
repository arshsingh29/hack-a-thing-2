document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('videoForm');
    const loadingState = document.getElementById('loadingState');
    const generateBtn = document.getElementById('generateBtn');
    const promptTextarea = document.getElementById('prompt');
    const charCount = document.getElementById('charCount');

    // Character counter
    if (promptTextarea && charCount) {
        promptTextarea.addEventListener('input', function() {
            charCount.textContent = this.value.length;
        });
    }

    // Form submission handler
    if (form && loadingState && generateBtn) {
        form.addEventListener('submit', function(e) {
            const prompt = promptTextarea.value.trim();

            // Client-side validation
            if (!prompt) {
                e.preventDefault();
                alert('Please provide a video prompt');
                return;
            }

            if (prompt.length > 500) {
                e.preventDefault();
                alert('Prompt is too long (max 500 characters)');
                return;
            }

            // Show loading state
            form.style.display = 'none';
            loadingState.style.display = 'block';
            generateBtn.disabled = true;
        });
    }
});
