#!/usr/bin/env python3
"""
Automated Open Interpreter execution script
Runs Open Interpreter with the master prompt in non-interactive mode
"""

import subprocess
import sys
import time
from pathlib import Path

def main():
    print("="*60)
    print("🤖 Starting Automated Open Interpreter Execution")
    print("="*60)

    # Use the new execute-now prompt
    prompt_file = Path("OI_EXECUTE_NOW.md")
    if not prompt_file.exists():
        print("❌ OI_EXECUTE_NOW.md not found!")
        sys.exit(1)

    with open(prompt_file, 'r') as f:
        prompt = f.read()

    print(f"\n✅ Loaded prompt ({len(prompt)} characters)")
    print("\n🚀 Launching Open Interpreter...")
    print("⚙️  Flags: -y (auto-run), -v (verbose)")
    print("⏱️  Expected duration: ~30-60 minutes\n")

    # Run Open Interpreter with auto-run flag
    try:
        process = subprocess.Popen(
            ['interpreter', '-y', '-v'],  # -y for auto_run, -v for verbose
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,  # Combine stderr with stdout
            text=True,
            bufsize=1,
            universal_newlines=True
        )

        # Send the prompt and close stdin
        print("📤 Sending prompt to Open Interpreter...\n")
        print("="*60)

        # Write prompt and close stdin immediately
        process.stdin.write(prompt)
        process.stdin.close()

        # Stream output in real-time
        for line in process.stdout:
            print(line, end='', flush=True)

        # Wait for completion
        return_code = process.wait()

        print("\n" + "="*60)
        if return_code == 0:
            print("✅ Execution completed successfully!")
        else:
            print(f"⚠️  Process exited with code {return_code}")

        return return_code

    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user. Killing process...")
        process.kill()
        return 1
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == '__main__':
    exit_code = main()
    sys.exit(exit_code)
