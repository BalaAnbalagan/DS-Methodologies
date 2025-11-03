"""
Example: ChatGPT API Integration for Notebook Critiques
"""

from openai import OpenAI
import os

# Initialize OpenAI client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def get_ai_critique(phase_name, code_content, output_content, methodology="CRISP-DM"):
    """
    Get AI critique for a specific methodology phase

    Args:
        phase_name: e.g., "Business Understanding"
        code_content: The code you wrote for this phase
        output_content: The results/outputs from running the code
        methodology: CRISP-DM, KDD, or SEMMA

    Returns:
        AI critique and suggestions
    """

    # Build the expert persona prompt
    system_prompt = f"""You are a world-renowned {methodology} methodology expert who has:
- Led data science projects at Fortune 500 companies for 20+ years
- Written award-winning books on {methodology} best practices
- Trained thousands of data scientists globally
- Published research papers on methodology optimization

You provide detailed, actionable critiques that improve both technical rigor and business value."""

    user_prompt = f"""Please critique my {phase_name} phase implementation for a {methodology} project.

**My Code:**
```python
{code_content}
```

**Output/Results:**
```
{output_content}
```

**Please provide:**
1. What I did well (be specific)
2. Critical gaps or mistakes (with severity: High/Medium/Low)
3. 5-10 specific, actionable improvements
4. Best practices I should follow for this phase
5. What I should validate before moving to the next phase

Focus on both technical correctness and business alignment."""

    # Call OpenAI API
    response = client.chat.completions.create(
        model="gpt-4",  # or "gpt-4-turbo" or "gpt-3.5-turbo"
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.7,
        max_tokens=2000
    )

    return response.choices[0].message.content


def get_second_pass_critique(phase_name, initial_code, initial_critique, improved_code, improved_output):
    """
    Second-pass critique after improvements
    """

    system_prompt = """You are reviewing a REVISED implementation after your initial critique.
Be thorough but encouraging. Focus on whether your previous suggestions were implemented correctly."""

    user_prompt = f"""I've revised my {phase_name} implementation based on your feedback.

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

**Please assess:**
1. Which of your suggestions did I implement successfully?
2. What still needs improvement?
3. Any new issues introduced by the changes?
4. Is this now production-ready, or what's still missing?
5. Final score: Ready to proceed? (Yes/No and why)"""

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.7,
        max_tokens=1500
    )

    return response.choices[0].message.content


# Example usage in notebook:
if __name__ == "__main__":
    # Example code from Business Understanding phase
    code = """
project_charter = {
    'stakeholders': ['VP Customer Success', 'Retention Analytics Lead'],
    'business_objectives': ['Quantify churn risk', 'Prioritize outreach campaigns'],
    'constraints': ['Data refresh monthly', 'Model must be explainable'],
    'milestones': {
        'kickoff': 'Define outcomes and KPIs',
        'baseline_model': 'First iteration with classical ML',
        'deployment_candidate': 'Pipeline validated in UAT'
    }
}
"""

    output = """
{'stakeholders': ['VP Customer Success', 'Retention Analytics Lead'],
 'business_objectives': ['Quantify churn risk', 'Prioritize outreach campaigns'],
 'constraints': ['Data refresh monthly', 'Model must be explainable']}
"""

    # Get critique
    print("🤖 Getting AI critique from ChatGPT...")
    critique = get_ai_critique(
        phase_name="Business Understanding",
        code_content=code,
        output_content=output,
        methodology="CRISP-DM"
    )

    print("\n" + "="*80)
    print("AI CRITIQUE:")
    print("="*80)
    print(critique)
