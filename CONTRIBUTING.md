# Contributing to Dynasec Visibility

Thank you for your interest in contributing to Dynasec Visibility! This document provides guidelines and best practices for contributing to this project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Security Guidelines](#security-guidelines)
- [Submitting Changes](#submitting-changes)
- [Testing](#testing)

## Code of Conduct

### Our Standards

- Be respectful and inclusive
- Focus on constructive feedback
- Prioritize security and quality
- Maintain professional communication

## Getting Started

### Prerequisites

- Git
- Python 3.8 or higher
- Modern web browser
- Code editor (VS Code, Sublime, etc.)
- Firebase account (for authentication features)

### Development Setup

1. **Fork and Clone**
   ```bash
   git clone https://github.com/YOUR_USERNAME/dynasec-visibility.git
   cd dynasec-visibility
   ```

2. **Set up Environment Variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

3. **Install Python Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start Local Development Server**
   ```bash
   python3 -m http.server 8000
   # Visit http://localhost:8000
   ```

## Coding Standards

### HTML

- Use HTML5 semantic elements (`<header>`, `<nav>`, `<main>`, `<footer>`)
- Include proper DOCTYPE: `<!DOCTYPE html>`
- Use `lang` attribute: `<html lang="en">`
- Include meta tags:
  - `charset="UTF-8"`
  - `viewport` for responsive design
  - `description` for SEO
  - CSP headers for security

**Example:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Page description">
  <meta http-equiv="Content-Security-Policy" content="...">
  <title>Page Title</title>
</head>
<body>
  <!-- Content -->
</body>
</html>
```

### CSS

- Use consistent indentation (2 spaces)
- Group related properties
- Use meaningful class names
- Implement responsive design (mobile-first)
- Avoid inline styles when possible

**Example:**
```css
.container {
  /* Layout */
  display: flex;
  flex-direction: column;
  
  /* Sizing */
  max-width: 1200px;
  padding: 2rem;
  
  /* Colors */
  background: #0d1117;
  color: #f8fafc;
}

@media (max-width: 768px) {
  .container {
    padding: 1rem;
  }
}
```

### JavaScript

- Use modern ES6+ syntax
- Add comments for complex logic
- Implement proper error handling
- Validate user input
- Follow security best practices

**Example:**
```javascript
/**
 * Validate email format
 * @param {string} email - Email address to validate
 * @returns {boolean} - True if valid
 */
function validateEmail(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}
```

### Python

- Follow PEP 8 style guide
- Use type hints
- Add docstrings to functions
- Implement proper error handling
- Use environment variables for configuration

**Example:**
```python
def upload_file() -> int:
    """
    Upload file to GitHub repository.
    
    Returns:
        int: Exit code (0 for success, 1 for failure)
    """
    try:
        # Implementation
        return 0
    except Exception as e:
        print(f"Error: {e}")
        return 1
```

## Security Guidelines

### Critical Rules

1. **NEVER commit secrets or credentials**
   - Use environment variables
   - Add sensitive files to `.gitignore`
   - Use `.env.example` for documentation

2. **Validate all user input**
   - Client-side validation
   - Sanitize input to prevent XSS
   - Check data types and formats

3. **Use secure headers**
   - Content Security Policy (CSP)
   - X-Content-Type-Options
   - X-Frame-Options

4. **Keep dependencies updated**
   - Regularly update Firebase SDK
   - Update Python packages
   - Monitor security advisories

5. **Proper error handling**
   - Don't expose internal errors to users
   - Log errors securely
   - Provide user-friendly messages

### Security Checklist

Before submitting:
- [ ] No hardcoded credentials
- [ ] All user input validated
- [ ] CSP headers implemented
- [ ] HTTPS enforced (production)
- [ ] Error messages are user-friendly
- [ ] Dependencies are up-to-date
- [ ] Security documentation updated

## Submitting Changes

### Branch Naming

Use descriptive branch names:
- `feature/add-new-page`
- `fix/security-vulnerability`
- `update/firebase-sdk`
- `docs/improve-readme`

### Commit Messages

Write clear, descriptive commit messages:

**Good:**
```
Add CSP headers to login page

- Implement Content Security Policy
- Prevent XSS attacks
- Allow Firebase and Stripe domains
```

**Bad:**
```
fix stuff
```

### Pull Request Process

1. **Create Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make Changes**
   - Follow coding standards
   - Add comments where needed
   - Update documentation

3. **Test Changes**
   - Test locally
   - Verify security
   - Check responsive design

4. **Commit Changes**
   ```bash
   git add .
   git commit -m "Descriptive message"
   ```

5. **Push to GitHub**
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create Pull Request**
   - Provide clear description
   - Reference related issues
   - Include screenshots if UI changes
   - List security considerations

### Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Security fix
- [ ] Documentation update

## Testing
- [ ] Tested locally
- [ ] Tested on mobile
- [ ] Security validated

## Security Considerations
- List any security implications
- Document new environment variables
- Note any dependency changes

## Screenshots (if applicable)
Add screenshots for UI changes
```

## Testing

### Local Testing

1. **Visual Testing**
   - Test on multiple browsers (Chrome, Firefox, Safari)
   - Test responsive design on different screen sizes
   - Verify all links work

2. **Security Testing**
   - Verify CSP headers
   - Test authentication flows
   - Check for XSS vulnerabilities
   - Validate input handling

3. **Functionality Testing**
   - Test all forms
   - Verify Firebase authentication
   - Check Stripe payment links
   - Test error handling

### Browser Testing

Minimum browser support:
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

### Mobile Testing

Test on:
- iOS Safari
- Android Chrome
- Various screen sizes (320px to 1920px)

## Documentation

### When to Update Documentation

- Adding new features
- Changing configuration
- Modifying security settings
- Updating dependencies

### Documentation Standards

- Use clear, concise language
- Include code examples
- Add references to external documentation
- Keep README.md up-to-date

## Questions or Issues?

- Check existing issues on GitHub
- Review SECURITY.md for security concerns
- Create a new issue with detailed description

## References

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [MDN Web Docs](https://developer.mozilla.org/)
- [Firebase Documentation](https://firebase.google.com/docs)
- [PEP 8 Style Guide](https://pep8.org/)

## License

By contributing, you agree that your contributions will be licensed under the same license as the project.

---

**Thank you for contributing to Dynasec Visibility!**
