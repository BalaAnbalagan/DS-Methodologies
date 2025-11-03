"""
AI Critique Helper for DS Methodology Notebooks
Automatically get ChatGPT critiques within Jupyter/Colab notebooks
"""

from openai import OpenAI
import os
from IPython.display import display, Markdown, HTML
import json
from datetime import datetime

class AICritiqueHelper:
    """Helper class for getting AI critiques in notebooks"""

    def __init__(self, api_key=None, model="gpt-4"):
        """
        Initialize the critique helper

        Args:
            api_key: OpenAI API key (defaults to OPENAI_API_KEY env var)
            model: Model to use (gpt-4, gpt-4-turbo, gpt-3.5-turbo)
        """
        self.api_key = api_key or os.environ.get("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OpenAI API key not found. Set OPENAI_API_KEY environment variable or pass api_key parameter")

        self.client = OpenAI(api_key=self.api_key)
        self.model = model
        self.critique_history = []

    def critique_phase(self, methodology, phase_name, code, output, save_to_file=True):
        """
        Get AI critique for a methodology phase

        Args:
            methodology: "CRISP-DM", "KDD", or "SEMMA"
            phase_name: e.g., "Business Understanding", "Selection", "Sample"
            code: Your code as string
            output: Your results/outputs as string
            save_to_file: Save critique to markdown file

        Returns:
            Formatted critique
        """

        print(f"🤖 Requesting critique from {self.model}...")
        print(f"   Methodology: {methodology}")
        print(f"   Phase: {phase_name}")
        print(f"   Code length: {len(code)} chars")
        print(f"   Output length: {len(output)} chars\n")

        # Build expert persona
        system_prompt = self._get_expert_persona(methodology)

        # Build critique request
        user_prompt = f"""Please critique my {phase_name} phase implementation for a {methodology} project.

**My Code:**
```python
{code}
```

**Output/Results:**
```
{output}
```

**Please provide a structured critique:**

## ✅ What You Did Well
[Specific strengths - be detailed]

## ⚠️ Critical Issues (if any)
[List with severity: 🔴 High / 🟡 Medium / 🟢 Low]

## 💡 Specific Improvements (5-10 actionable items)
1. [Specific change]
2. [Specific change]
...

## 📚 Best Practices for This Phase
[What should always be done in {phase_name}]

## ✓ Ready to Proceed?
[Yes/No and why. What must be fixed before next phase?]

Be thorough, specific, and actionable. Focus on both technical rigor and business value."""

        # Call API
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.7,
                max_tokens=2500
            )

            critique = response.choices[0].message.content

            # Save to history
            critique_record = {
                "timestamp": datetime.now().isoformat(),
                "methodology": methodology,
                "phase": phase_name,
                "model": self.model,
                "code": code,
                "output": output,
                "critique": critique
            }
            self.critique_history.append(critique_record)

            # Display in notebook
            self._display_critique(critique, phase_name)

            # Save to file
            if save_to_file:
                self._save_critique_to_file(critique_record, methodology, phase_name)

            return critique

        except Exception as e:
            print(f"❌ Error getting critique: {str(e)}")
            print(f"   Check your API key and internet connection")
            return None

    def second_pass_critique(self, methodology, phase_name, initial_critique, improved_code, improved_output):
        """
        Get second-pass critique after improvements

        Args:
            methodology: CRISP-DM, KDD, or SEMMA
            phase_name: Phase name
            initial_critique: The first critique you received
            improved_code: Your improved code
            improved_output: New results after improvements

        Returns:
            Second-pass critique
        """

        print(f"🔄 Requesting SECOND-PASS critique from {self.model}...")

        system_prompt = f"""You are a {methodology} expert reviewing REVISED work after your initial critique.
Be thorough but encouraging. Verify that your suggestions were implemented correctly."""

        user_prompt = f"""I've revised my {phase_name} implementation based on your previous feedback.

**Your Previous Critique:**
{initial_critique}

**My Improved Code:**
```python
{improved_code}
```

**New Results:**
```
{improved_output}
```

**Please assess the improvements:**

## ✓ Successfully Implemented Suggestions
[Which of your previous suggestions were addressed well?]

## ⚠️ Still Needs Work
[What's still missing or incorrectly implemented?]

## 🆕 New Issues (if any)
[Any problems introduced by the changes?]

## 📊 Overall Assessment
- Technical quality: [Score 1-10]
- Business alignment: [Score 1-10]
- Production readiness: [Yes/No]

## 🚀 Final Recommendation
[Ready to proceed to next phase? If not, what's blocking?]"""

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.7,
                max_tokens=2000
            )

            second_critique = response.choices[0].message.content

            # Display
            self._display_critique(second_critique, f"{phase_name} (Second Pass)", color="green")

            return second_critique

        except Exception as e:
            print(f"❌ Error getting second-pass critique: {str(e)}")
            return None

    def _get_expert_persona(self, methodology):
        """Build expert persona prompt based on methodology"""

        personas = {
            "CRISP-DM": """You are a world-renowned CRISP-DM methodology expert who has:
- Led 50+ enterprise data science projects following CRISP-DM
- Written award-winning books: "Mastering CRISP-DM" and "Business-Driven Data Science"
- Trained over 10,000 data scientists at Fortune 500 companies
- Published 30+ peer-reviewed papers on methodology best practices
- Consulted for IBM, SAS, Microsoft on data mining standards

You provide detailed, actionable critiques that improve both technical rigor and business value.""",

            "KDD": """You are a world-renowned KDD (Knowledge Discovery in Databases) expert who has:
- Pioneered KDD research at top universities for 25+ years
- Published 100+ papers in KDD conferences and journals
- Developed novel algorithms for rare-event detection and anomaly analysis
- Consulted on fraud detection systems at major financial institutions
- Served as program chair for ACM SIGKDD conferences

You provide rigorous, research-backed critiques focused on knowledge extraction and pattern discovery.""",

            "SEMMA": """You are a world-renowned SEMMA methodology expert who has:
- Worked at SAS Institute designing SEMMA framework
- Implemented 200+ analytics projects using SAS Enterprise Miner
- Written definitive guides on rapid prototyping with SEMMA
- Trained corporate clients on agile data mining approaches
- Specialized in marketing analytics and campaign optimization

You provide practical, speed-focused critiques that balance rigor with iteration velocity."""
        }

        return personas.get(methodology, personas["CRISP-DM"])

    def _display_critique(self, critique, phase_name, color="blue"):
        """Display critique beautifully in notebook"""

        color_map = {
            "blue": "#2196F3",
            "green": "#4CAF50",
            "orange": "#FF9800"
        }

        html = f"""
        <div style="border-left: 4px solid {color_map.get(color, '#2196F3')};
                    padding: 15px;
                    margin: 20px 0;
                    background-color: #f5f5f5;
                    border-radius: 5px;">
            <h3 style="color: {color_map.get(color, '#2196F3')}; margin-top: 0;">
                🤖 AI Critique: {phase_name}
            </h3>
            <div style="background: white; padding: 15px; border-radius: 5px; font-family: monospace; white-space: pre-wrap;">
{critique}
            </div>
        </div>
        """
        display(HTML(html))

    def _save_critique_to_file(self, critique_record, methodology, phase_name):
        """Save critique to markdown file"""

        # Create critiques directory if needed
        critique_dir = f"critiques/{phase_name.lower().replace(' ', '_')}"
        os.makedirs(critique_dir, exist_ok=True)

        # Generate filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{critique_dir}/critique_{timestamp}.md"

        # Write markdown file
        with open(filename, 'w') as f:
            f.write(f"# AI Critique: {phase_name}\n\n")
            f.write(f"**Methodology:** {methodology}\n")
            f.write(f"**Model:** {critique_record['model']}\n")
            f.write(f"**Timestamp:** {critique_record['timestamp']}\n\n")
            f.write(f"---\n\n")
            f.write(f"## Code Submitted\n\n```python\n{critique_record['code']}\n```\n\n")
            f.write(f"## Output/Results\n\n```\n{critique_record['output']}\n```\n\n")
            f.write(f"## Critique\n\n{critique_record['critique']}\n")

        print(f"💾 Critique saved to: {filename}")

    def save_all_critiques_json(self, filename="critiques/all_critiques.json"):
        """Save all critiques to JSON file"""

        os.makedirs(os.path.dirname(filename), exist_ok=True)

        with open(filename, 'w') as f:
            json.dump(self.critique_history, f, indent=2)

        print(f"💾 All critiques saved to: {filename}")


# Example usage in notebook
def example_usage():
    """
    Example of how to use in a Jupyter notebook cell:

    ```python
    # Initialize helper (do this once at the start of notebook)
    from ai_critique_helper import AICritiqueHelper

    ai_helper = AICritiqueHelper(model="gpt-4")

    # After running Phase 1 code, get critique
    code = '''
    project_charter = {
        'stakeholders': ['VP Customer Success'],
        'business_objectives': ['Reduce churn'],
        ...
    }
    '''

    output = str(project_charter)

    critique = ai_helper.critique_phase(
        methodology="CRISP-DM",
        phase_name="Business Understanding",
        code=code,
        output=output
    )

    # Make improvements based on critique...

    # Get second-pass critique
    improved_code = '''
    # Improved version with more stakeholders
    project_charter = {
        'stakeholders': ['VP Customer Success', 'CFO', 'Data Engineering'],
        ...
    }
    '''

    second_critique = ai_helper.second_pass_critique(
        methodology="CRISP-DM",
        phase_name="Business Understanding",
        initial_critique=critique,
        improved_code=improved_code,
        improved_output=str(new_project_charter)
    )
    ```
    """
    pass


if __name__ == "__main__":
    print("AI Critique Helper for DS Methodology Notebooks")
    print("=" * 60)
    print("\nThis module provides automated ChatGPT critiques for:")
    print("  - CRISP-DM phases")
    print("  - KDD phases")
    print("  - SEMMA phases")
    print("\nUsage: from ai_critique_helper import AICritiqueHelper")
