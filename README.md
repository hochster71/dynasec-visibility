# Dynasec Visibility

Corporate website for Dynasec AI Solutions - A comprehensive platform showcasing AI-powered security and intelligence solutions.

## 🔒 Security

This project has been updated with modern security best practices:

- **No hardcoded credentials**: All sensitive data uses environment variables
- **Updated dependencies**: Using latest Firebase SDK (v10+) with modular architecture
- **Security headers**: CSP and other security headers implemented
- **Input validation**: Proper sanitization and validation on all forms
- **HTTPS enforcement**: Redirects and security policies for secure connections

### Security Best Practices Implemented

1. **Authentication**: Firebase Authentication with proper security rules
2. **Environment Variables**: Sensitive configuration in `.env` (never committed)
3. **Content Security Policy**: XSS protection via CSP headers
4. **Modern APIs**: Using Bearer token authentication for GitHub API
5. **Error Handling**: Comprehensive error handling without exposing internals

## 🚀 Quick Start

### Prerequisites

- Modern web browser (Chrome, Firefox, Safari, Edge)
- Python 3.8+ (for upload bot)
- Firebase account (for authentication features)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/hochster71/dynasec-visibility.git
cd dynasec-visibility
```

2. Configure environment variables:
```bash
cp .env.example .env
# Edit .env with your actual values
```

3. For local development, serve the files:
```bash
# Python 3
python3 -m http.server 8000

# Then visit http://localhost:8000
```

## 📁 Project Structure

- `index.html` - Main landing page
- `login.html` - Firebase authentication login
- `dashboard*.html` - Protected dashboard pages
- `store.html` - Product catalog with Stripe integration
- `firebase-config.js` - Firebase initialization (update with your config)
- `github_auto_upload_bot.py` - Automated GitHub file uploader

## 🔧 Configuration

### Firebase Setup

1. Create a Firebase project at https://console.firebase.google.com
2. Enable Authentication (Email/Password)
3. Update `firebase-config.js` with your project credentials
4. Configure security rules in Firebase Console

**Important**: While Firebase config is public in web apps, always configure proper security rules in Firebase Console to restrict access.

Reference: [Firebase Security Best Practices](https://firebase.google.com/docs/rules/basics)

### GitHub Upload Bot

The upload bot uses environment variables for security:

```bash
export GITHUB_TOKEN="your_token_here"
python github_auto_upload_bot.py
```

See `.env.example` for all configuration options.

## 🛡️ Security Considerations

### Firebase API Keys
Firebase API keys for web apps are safe to be public, but you MUST configure security rules:
- Reference: https://firebase.google.com/docs/projects/api-keys
- Always test your security rules
- Use Firebase App Check for additional protection

### Passwords
- NEVER hardcode passwords in client-side JavaScript
- Use Firebase Authentication or other secure auth providers
- Implement proper session management

### HTTPS
- Always use HTTPS in production
- Configure HSTS headers
- Redirect HTTP to HTTPS

## 📝 Recent Updates

### Security Enhancements (2025)
- ✅ Removed hardcoded credentials from all files
- ✅ Implemented environment variable configuration
- ✅ Updated Firebase SDK to v10+ (modular)
- ✅ Added comprehensive error handling
- ✅ Implemented CSP headers for XSS protection
- ✅ Added input validation and sanitization
- ✅ Fixed file naming issues (.py.py → .py)
- ✅ Added .gitignore for sensitive files
- ✅ Documented all security practices

## 📚 References

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [MDN Web Security](https://developer.mozilla.org/en-US/docs/Web/Security)
- [Firebase Security Documentation](https://firebase.google.com/docs/rules)
- [GitHub API Documentation](https://docs.github.com/en/rest)

## 📄 License

© 2025 Dynasec AI Solutions — Commanded by LCDR Michael Hoch, USN (Ret.). All Rights Reserved.

## 🤝 Contributing

When contributing, ensure:
1. No hardcoded credentials or secrets
2. Follow security best practices
3. Test all changes locally
4. Update documentation as needed
