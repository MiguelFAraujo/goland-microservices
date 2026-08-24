#!/usr/bin/env python3
# AI Code Review using Ollama

import argparse
import ollama

def review_code(diff_text, model='llama3.2:latest'):
    prompt = f"""You are a senior ${LANGUAGE} engineer reviewing code for:
- Performance optimization
- Security vulnerabilities
- Best practices and idiomatic ${LANGUAGE}
- Memory safety and resource management
- Testability and maintainability

Review the following diff and provide:
1. Critical issues (security, crashes, data loss)
2. Performance concerns
3. Best practice violations
4. Suggested improvements with code snippets

Diff:
{diff_text}"""

    response = ollama.chat(model=model, messages=[{
        'role': 'user',
        'content': prompt
    }])
    return response['message']['content']

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--diff-file', required=True)
    parser.add_argument('--output', default='review.md')
    parser.add_argument('--model', default='llama3.2:latest')
    args = parser.parse_args()

    with open(args.diff_file, 'r') as f:
        diff = f.read()

    if not diff.strip():
        with open(args.output, 'w') as f:
            f.write("# AI Code Review\n\nNo changes to review.")
        return

    print(f"Reviewing diff with {args.model}...")
    review = review_code(diff, args.model)

    with open(args.output, 'w') as f:
        f.write(f"# AI Code Review (Ollama {args.model})\n\n")
        f.write(review)

    print(f"Review saved to {args.output}")

if __name__ == '__main__':
    main()
