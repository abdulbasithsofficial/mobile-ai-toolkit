#!/usr/bin/env python3
"""MobileAI-Toolkit — Termux setup checklists for AI CLI tools on Android. Installs nothing."""
import argparse
STEPS = {
 "coding": ["Install Termux from F-Droid (not Play Store).", "Run: pkg update && pkg upgrade", "Install: pkg install git python nodejs", "Clone the tool repo, then follow its own README for login/API key."],
 "chat": ["Install Termux from F-Droid.", "Run: pkg update && pkg upgrade", "Install: pkg install python", "Use a chat CLI that supports your own API key; never paste a key into a public chat."],
 "image": ["Install Termux from F-Droid.", "Run: pkg update && pkg upgrade", "Install: pkg install python", "Image tools often need more storage — check free space first with: df -h"],
}
def main():
    p = argparse.ArgumentParser(); p.add_argument("--list", action="store_true"); p.add_argument("--setup", default="")
    a = p.parse_args()
    if a.list: print("Categories: " + ", ".join(STEPS)); return
    if a.setup in STEPS:
        print(f"Termux setup for {a.setup}:")
        for i, s in enumerate(STEPS[a.setup], 1): print(f"{i}. {s}")
    else: print("Use --list, or --setup coding|chat|image")
if __name__ == "__main__": main()
