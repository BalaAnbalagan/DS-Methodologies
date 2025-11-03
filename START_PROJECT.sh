#!/bin/bash

# DS Methodologies Project - Open Interpreter Startup Script

echo "========================================"
echo "DS Methodologies Automated Generation"
echo "========================================"
echo ""

# Step 1: Activate virtual environment
echo "Step 1: Activating virtual environment..."
source venv/bin/activate

# Step 2: Check Open Interpreter installation
echo "Step 2: Checking Open Interpreter..."
if ! command -v interpreter &> /dev/null; then
    echo "⚠️  Open Interpreter not found in PATH"
    echo "Installing Open Interpreter..."
    cd open-interpreter && pip install -e . && cd ..
fi

# Step 3: Check API key
echo "Step 3: Checking API configuration..."
if [ ! -f ".env" ]; then
    echo "❌ .env file not found! Please create it with your OpenAI API key."
    exit 1
fi

echo "✅ Environment ready!"
echo ""
echo "========================================"
echo "📋 NEXT STEPS:"
echo "========================================"
echo ""
echo "1. Open the file: OI_PROJECT_PROMPT.md"
echo "2. Copy the ENTIRE contents"
echo "3. Run: interpreter"
echo "4. Paste the prompt when prompted"
echo "5. Let it run for ~90 minutes"
echo ""
echo "Or run automatically:"
echo "  interpreter < OI_PROJECT_PROMPT.md"
echo ""
echo "========================================"
