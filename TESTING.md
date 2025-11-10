# Testing Guide

This guide provides comprehensive testing procedures for the Dynasec Visibility project.

## Table of Contents

- [Local Testing](#local-testing)
- [Security Testing](#security-testing)
- [Functional Testing](#functional-testing)
- [Performance Testing](#performance-testing)
- [Accessibility Testing](#accessibility-testing)
- [Browser Compatibility](#browser-compatibility)
- [Mobile Testing](#mobile-testing)

## Local Testing

### Setup Test Environment

1. **Start Local Server**
   ```bash
   python3 -m http.server 8000
   ```

2. **Access Test URLs**
   - Main site: http://localhost:8000
   - Login: http://localhost:8000/login.html
   - Dashboard: http://localhost:8000/dashboard.html
   - Store: http://localhost:8000/store.html

### Python Script Testing

1. **Syntax Check**
   ```bash
   python3 -m py_compile github_auto_upload_bot.py
   ```

2. **Dry Run** (without actual upload)
   ```bash
   export GITHUB_TOKEN="test_token"
   export FILE_PATH="/path/to/test/file"
   python3 github_auto_upload_bot.py
   ```

3. **Dependency Check**
   ```bash
   pip install -r requirements.txt
   python3 -c "import requests; print(requests.__version__)"
   ```

## Security Testing

### 1. Input Validation Testing

**Test Cases for Login Form:**

| Test Case | Input | Expected Result |
|-----------|-------|-----------------|
| Valid email | user@example.com | Accepted |
| Invalid email | notanemail | Error: "Please enter a valid email address" |
| Empty email | (empty) | Error: "Please enter both email and password" |
| Short password | "12345" | Error: "Password must be at least 6 characters" |
| XSS attempt | `<script>alert('xss')</script>` | Input sanitized, no script execution |

**Manual Testing:**
```javascript
// Open browser console on login.html
// Test email validation
validateEmail("test@example.com")  // Should return true
validateEmail("invalid")           // Should return false

// Test input sanitization
sanitizeInput("<script>alert('xss')</script>")  // Should remove < >
```

### 2. Content Security Policy (CSP) Testing

**Test CSP Headers:**

1. **Open Browser DevTools** (F12)
2. **Check Console** for CSP violations
3. **Expected**: No CSP errors
4. **If violations exist**: Update CSP in meta tag

**Verify CSP:**
```bash
curl -I http://localhost:8000/login.html | grep -i content-security
```

**Online Tools:**
- https://csp-evaluator.withgoogle.com/
- https://observatory.mozilla.org/

### 3. Authentication Testing

**Firebase Authentication Test Cases:**

| Test Case | Expected Result |
|-----------|-----------------|
| Valid credentials | Successful login, redirect to dashboard |
| Invalid email | Error: "Invalid email or password" |
| Invalid password | Error: "Invalid email or password" |
| Non-existent user | Error: "Invalid email or password" |
| Too many attempts | Error: "Too many failed attempts. Please try again later" |
| Already logged in | Auto-redirect to dashboard |
| Logout | Return to login page, session cleared |

**Manual Test:**
```javascript
// In browser console on login page
firebase.auth().onAuthStateChanged(function(user) {
  console.log('User state:', user ? user.email : 'Not logged in');
});
```

### 4. Security Headers Testing

**Test Security Headers:**
```bash
curl -I https://yourdomain.com | grep -E "X-Frame-Options|X-Content-Type-Options|Strict-Transport-Security"
```

**Expected Headers:**
- `Content-Security-Policy`: Present with proper directives
- `X-Frame-Options`: DENY or SAMEORIGIN
- `X-Content-Type-Options`: nosniff
- `Strict-Transport-Security`: max-age=31536000; includeSubDomains (HTTPS only)

**Online Tools:**
- https://securityheaders.com/
- https://observatory.mozilla.org/

### 5. CodeQL Security Scan

Already run and passed with 0 alerts:
- JavaScript: ✅ No alerts
- Python: ✅ No alerts

### 6. Dependency Vulnerability Scan

**Python Dependencies:**
```bash
pip install safety
safety check -r requirements.txt
```

**Expected**: No known vulnerabilities in requests>=2.31.0

## Functional Testing

### 1. Navigation Testing

**Test all links work:**
- [ ] Home page loads
- [ ] All navigation links work
- [ ] Store links to Stripe work
- [ ] Catalog page displays correctly
- [ ] Dashboard requires authentication
- [ ] Login page accessible
- [ ] All product pages load

### 2. Form Testing

**Login Form:**
- [ ] Email input accepts valid emails
- [ ] Password input is masked
- [ ] Submit button works
- [ ] Enter key submits form
- [ ] Loading state displays during submission
- [ ] Error messages display correctly
- [ ] Success redirects to dashboard

**Protected Dashboard Form:**
- [ ] Login form displays when not authenticated
- [ ] Logout button works when authenticated
- [ ] Authentication persists on page reload

### 3. Firebase Integration Testing

**Test Firebase Services:**

1. **Authentication**
   ```javascript
   // Test sign in
   firebase.auth().signInWithEmailAndPassword("test@example.com", "password")
     .then(user => console.log("Signed in:", user.email))
     .catch(error => console.error("Error:", error));
   
   // Test sign out
   firebase.auth().signOut()
     .then(() => console.log("Signed out"))
     .catch(error => console.error("Error:", error));
   ```

2. **Analytics** (if enabled)
   ```javascript
   firebase.analytics().logEvent('page_view', {page: 'test'});
   ```

### 4. Payment Link Testing

**Verify Stripe Links:**
- [ ] All Stripe links are valid (https://buy.stripe.com/...)
- [ ] Links open in new tab (rel="noopener noreferrer")
- [ ] Links go to correct products
- [ ] Prices match product descriptions

**Test Process:**
1. Click each payment link
2. Verify correct product loads in Stripe
3. Check price matches
4. **DO NOT** complete payment in testing

## Performance Testing

### 1. Page Load Time

**Test with Lighthouse:**
```bash
lighthouse http://localhost:8000 --view
```

**Target Metrics:**
- Performance: >90
- Accessibility: >90
- Best Practices: >90
- SEO: >90

### 2. Image Optimization

**Check Image Sizes:**
```bash
ls -lh *.png *.jpg | awk '{print $9, $5}'
```

**Recommendations:**
- Compress images (use TinyPNG, ImageOptim)
- Consider WebP format
- Implement lazy loading for large images

### 3. Network Performance

**Test in DevTools:**
1. Open Network tab (F12)
2. Reload page
3. Check:
   - Total transfer size
   - Number of requests
   - Load time

**Targets:**
- Total size: <2MB
- Requests: <20
- Load time: <3s

## Accessibility Testing

### 1. Automated Testing

**Use axe DevTools:**
1. Install axe DevTools browser extension
2. Run scan on each page
3. Fix all violations

**Online Tool:**
- https://wave.webaim.org/

### 2. Keyboard Navigation

**Test keyboard-only navigation:**
- [ ] Tab through all interactive elements
- [ ] Enter key submits forms
- [ ] Focus indicators visible
- [ ] No keyboard traps
- [ ] Logical tab order

### 3. Screen Reader Testing

**Test with screen reader:**
- Windows: NVDA (free)
- macOS: VoiceOver (built-in)
- Linux: Orca

**Check:**
- [ ] All images have alt text
- [ ] Forms have proper labels
- [ ] Headings are in logical order
- [ ] Links are descriptive

### 4. Color Contrast

**Check contrast ratios:**
- Tool: https://webaim.org/resources/contrastchecker/

**Requirements:**
- Normal text: 4.5:1 minimum
- Large text: 3:1 minimum
- UI components: 3:1 minimum

## Browser Compatibility

### Desktop Browsers

Test on latest versions:
- [ ] Chrome (Windows, macOS, Linux)
- [ ] Firefox (Windows, macOS, Linux)
- [ ] Safari (macOS)
- [ ] Edge (Windows)

### Features to Test

- [ ] Layout renders correctly
- [ ] CSS animations work
- [ ] JavaScript functions work
- [ ] Firebase auth works
- [ ] Forms submit correctly
- [ ] Responsive design works

### Browser DevTools Testing

**Chrome DevTools:**
1. Open DevTools (F12)
2. Test in Device Mode
3. Check Console for errors
4. Verify Network requests
5. Check Application > Local Storage

## Mobile Testing

### Responsive Design

**Test at breakpoints:**
- [ ] 320px (iPhone SE)
- [ ] 375px (iPhone X)
- [ ] 414px (iPhone Plus)
- [ ] 768px (iPad)
- [ ] 1024px (iPad Pro)

**Chrome DevTools Device Mode:**
1. Open DevTools (F12)
2. Click device icon (Ctrl+Shift+M)
3. Test each device size

### Mobile Browsers

**Test on actual devices:**
- [ ] iOS Safari (latest)
- [ ] Android Chrome (latest)
- [ ] Android Firefox (latest)

### Touch Interactions

- [ ] Buttons are large enough (44x44px minimum)
- [ ] Links are tappable
- [ ] Form inputs are usable
- [ ] No hover-only interactions

### Mobile-Specific Issues

- [ ] No horizontal scrolling
- [ ] Text is readable without zooming
- [ ] Images fit within viewport
- [ ] Loading states show on slow networks

## Regression Testing

### After Code Changes

**Test checklist:**
- [ ] All pages still load
- [ ] Authentication still works
- [ ] No console errors
- [ ] No CSP violations
- [ ] Payment links work
- [ ] Responsive design intact

### Automated Testing (Future)

Consider implementing:
- Jest for JavaScript unit tests
- Pytest for Python tests
- Cypress for E2E testing
- GitHub Actions for CI/CD

## Test Reporting

### Document Test Results

**Template:**
```markdown
## Test Report - [Date]

### Environment
- Browser: Chrome 120
- OS: Windows 11
- Screen: 1920x1080

### Tests Performed
- [x] Login functionality - PASS
- [x] Payment links - PASS
- [ ] Mobile responsive - FAIL (Issue #123)

### Issues Found
1. [Issue description]
   - Severity: High/Medium/Low
   - Steps to reproduce
   - Expected vs actual result
   - Screenshot/video

### Recommendations
- [List of improvements]
```

## Continuous Testing

### Regular Testing Schedule

- **Daily**: Automated tests (when implemented)
- **Weekly**: Manual smoke tests
- **Monthly**: Full regression testing
- **Quarterly**: Security audit
- **Annually**: Comprehensive review

## Testing Tools Reference

### Security
- [OWASP ZAP](https://www.zaproxy.org/) - Security scanner
- [Snyk](https://snyk.io/) - Dependency vulnerability scanning
- [Safety](https://pypi.org/project/safety/) - Python dependency checker

### Performance
- [Lighthouse](https://developers.google.com/web/tools/lighthouse)
- [WebPageTest](https://www.webpagetest.org/)
- [GTmetrix](https://gtmetrix.com/)

### Accessibility
- [axe DevTools](https://www.deque.com/axe/devtools/)
- [WAVE](https://wave.webaim.org/)
- [Lighthouse Accessibility Audit](https://developers.google.com/web/tools/lighthouse)

### Browser Testing
- [BrowserStack](https://www.browserstack.com/)
- [LambdaTest](https://www.lambdatest.com/)

## Conclusion

Regular testing ensures:
- Security vulnerabilities are caught early
- User experience remains optimal
- Performance stays fast
- Accessibility is maintained
- Cross-browser compatibility is preserved

---

**Last Updated**: 2025-11-09
