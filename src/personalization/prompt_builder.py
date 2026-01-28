from typing import Dict, Any, Optional
from anthropic import Anthropic
from ..config import config

class AIPromptBuilder:
    """
    Uses AI to build personalized video prompts based on user data.
    """

    def __init__(self):
        if config.ANTHROPIC_API_KEY:
            self.client = Anthropic(api_key=config.ANTHROPIC_API_KEY)
            self.use_ai = True
        else:
            self.use_ai = False
            print("Warning: ANTHROPIC_API_KEY not set. AI prompt building disabled.")

    def build_prompt(
        self,
        template: str,
        user_data: Dict[str, Any],
        context: Optional[str] = None
    ) -> str:
        """
        Build a personalized video prompt using AI.

        Args:
            template: Base template or description of desired video
            user_data: User-specific data for personalization
            context: Additional context for prompt generation

        Returns:
            AI-generated personalized prompt
        """
        if not self.use_ai:
            return self._simple_substitution(template, user_data)

        system_prompt = """You are a video prompt generator. Create detailed,
        visually descriptive prompts for AI video generation based on user data.
        Keep prompts concise but vivid (2-3 sentences max). Focus on visual
        elements, mood, and style."""

        user_message = f"""Template: {template}

User Data: {user_data}
{f'Context: {context}' if context else ''}

Generate a personalized video prompt:"""

        message = self.client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=200,
            messages=[{"role": "user", "content": user_message}],
            system=system_prompt
        )

        return message.content[0].text.strip()

    def _simple_substitution(self, template: str, user_data: Dict[str, Any]) -> str:
        """Fallback method for simple template substitution."""
        result = template
        for key, value in user_data.items():
            placeholder = f"{{{key}}}"
            result = result.replace(placeholder, str(value))
        return result
