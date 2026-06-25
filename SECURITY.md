# Security Policy

## Reporting a Vulnerability

If you discover a security vulnerability in this project, please do **not** open a public GitHub issue.

Instead, contact the maintainer directly:

- **GitHub**: [@Youssef-Mohamed-Albiely](https://github.com/Youssef-Mohamed-Albiely)

Please include:
- A description of the vulnerability
- Steps to reproduce
- Potential impact

You will receive a response within 48 hours.

## Security Best Practices for Deployment

- Always use environment variables for secrets — never hardcode API keys
- Enable Telegram's `secret_token` webhook parameter to verify requests come from Telegram
- Run the server behind HTTPS only (Telegram requires it for webhooks)
- Rotate your `ACCESS_TOKEN` if you suspect it has been compromised via [@BotFather](https://t.me/BotFather)
- Monitor LangSmith traces for unusual usage patterns
