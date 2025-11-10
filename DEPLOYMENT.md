# Deployment Guide

## Overview

This guide covers deploying the Dynasec Visibility website to production environments with proper security configurations.

## Deployment Options

### 1. GitHub Pages (Recommended for Static Site)

**Pros:**
- Free hosting
- Automatic HTTPS
- Integrated with Git workflow
- Custom domain support

**Setup:**

1. **Enable GitHub Pages**
   ```
   Repository Settings → Pages
   Source: Deploy from a branch
   Branch: main or gh-pages
   ```

2. **Configure Custom Domain (Optional)**
   - Add CNAME file with your domain
   - Configure DNS settings:
     ```
     Type: CNAME
     Name: www
     Value: username.github.io
     ```

3. **Enforce HTTPS**
   - Enable "Enforce HTTPS" in repository settings

**Limitations:**
- Firebase authentication requires additional configuration
- No server-side processing

### 2. Firebase Hosting (Recommended for Full Features)

**Pros:**
- Integrated with Firebase Authentication
- Custom domain support
- Automatic SSL/TLS
- CDN distribution
- Server-side functions support

**Setup:**

1. **Install Firebase CLI**
   ```bash
   npm install -g firebase-tools
   ```

2. **Login to Firebase**
   ```bash
   firebase login
   ```

3. **Initialize Firebase Hosting**
   ```bash
   firebase init hosting
   ```

4. **Configure firebase.json**
   ```json
   {
     "hosting": {
       "public": ".",
       "ignore": [
         "firebase.json",
         "**/.*",
         "**/node_modules/**",
         "**/*.py",
         "**/*.md"
       ],
       "headers": [
         {
           "source": "**/*.html",
           "headers": [
             {
               "key": "Content-Security-Policy",
               "value": "default-src 'self'; script-src 'self' 'unsafe-inline' https://www.gstatic.com; style-src 'self' 'unsafe-inline'; connect-src 'self' https://*.firebaseapp.com https://*.googleapis.com;"
             },
             {
               "key": "X-Frame-Options",
               "value": "DENY"
             },
             {
               "key": "X-Content-Type-Options",
               "value": "nosniff"
             },
             {
               "key": "Strict-Transport-Security",
               "value": "max-age=31536000; includeSubDomains"
             }
           ]
         }
       ],
       "redirects": [
         {
           "source": "/old-page",
           "destination": "/new-page",
           "type": 301
         }
       ]
     }
   }
   ```

5. **Deploy**
   ```bash
   firebase deploy --only hosting
   ```

**Reference:** [Firebase Hosting Documentation](https://firebase.google.com/docs/hosting)

### 3. Netlify

**Pros:**
- Easy deployment
- Automatic HTTPS
- Form handling
- Continuous deployment

**Setup:**

1. **Connect Repository**
   - Login to Netlify
   - New site from Git
   - Select repository

2. **Configure Build Settings**
   ```
   Build command: (leave empty for static site)
   Publish directory: .
   ```

3. **Add Custom Headers** (netlify.toml)
   ```toml
   [[headers]]
     for = "/*"
     [headers.values]
       Content-Security-Policy = "default-src 'self'; script-src 'self' 'unsafe-inline' https://www.gstatic.com;"
       X-Frame-Options = "DENY"
       X-Content-Type-Options = "nosniff"
       Strict-Transport-Security = "max-age=31536000; includeSubDomains"
   ```

### 4. Vercel

**Pros:**
- Fast deployment
- Edge network
- Serverless functions
- Preview deployments

**Setup:**

1. **Install Vercel CLI**
   ```bash
   npm i -g vercel
   ```

2. **Deploy**
   ```bash
   vercel
   ```

3. **Configure vercel.json**
   ```json
   {
     "headers": [
       {
         "source": "/(.*)",
         "headers": [
           {
             "key": "Content-Security-Policy",
             "value": "default-src 'self'; script-src 'self' 'unsafe-inline' https://www.gstatic.com;"
           },
           {
             "key": "X-Frame-Options",
             "value": "DENY"
           }
         ]
       }
     ]
   }
   ```

## Pre-Deployment Checklist

### Security

- [ ] Remove all hardcoded credentials
- [ ] Configure environment variables
- [ ] Update Firebase configuration
- [ ] Set up Firebase Security Rules
- [ ] Enable Firebase App Check
- [ ] Configure CSP headers
- [ ] Enable HTTPS enforcement
- [ ] Set up CORS properly

### Firebase Configuration

1. **Update firebase-config.js**
   - Use production Firebase project
   - Update all configuration values

2. **Configure Security Rules**

   **Firestore Rules:**
   ```javascript
   rules_version = '2';
   service cloud.firestore {
     match /databases/{database}/documents {
       match /{document=**} {
         allow read, write: if request.auth != null;
       }
     }
   }
   ```

   **Storage Rules:**
   ```javascript
   rules_version = '2';
   service firebase.storage {
     match /b/{bucket}/o {
       match /{allPaths=**} {
         allow read: if true;
         allow write: if request.auth != null;
       }
     }
   }
   ```

3. **Enable Authentication Methods**
   - Email/Password
   - Google (optional)
   - Configure authorized domains

4. **Set Up Firebase App Check**
   ```javascript
   // Add to your HTML files
   <script src="https://www.gstatic.com/firebasejs/10.7.1/firebase-app-check-compat.js"></script>
   <script>
     const appCheck = firebase.appCheck();
     appCheck.activate(RECAPTCHA_SITE_KEY);
   </script>
   ```

### Performance

- [ ] Optimize images (compress, use WebP)
- [ ] Minify CSS and JavaScript
- [ ] Enable caching headers
- [ ] Use CDN for static assets
- [ ] Lazy load images

### SEO

- [ ] Add meta descriptions to all pages
- [ ] Create sitemap.xml (already exists)
- [ ] Create robots.txt (already exists)
- [ ] Add Open Graph tags
- [ ] Add Twitter Card tags
- [ ] Configure canonical URLs

### Testing

- [ ] Test all authentication flows
- [ ] Verify payment links work
- [ ] Test on multiple browsers
- [ ] Test responsive design
- [ ] Run Lighthouse audit
- [ ] Check accessibility (WAVE, axe)

## Environment Variables

For production, set these environment variables:

### Firebase (if using server-side)
```bash
FIREBASE_API_KEY=your_production_api_key
FIREBASE_AUTH_DOMAIN=your-project.firebaseapp.com
FIREBASE_PROJECT_ID=your-project-id
```

### GitHub Bot (if deploying scripts)
```bash
GITHUB_TOKEN=your_production_token
GITHUB_REPO_OWNER=hochster71
GITHUB_REPO_NAME=dynasec-visibility
```

## DNS Configuration

### For Custom Domain

1. **Add DNS Records**
   ```
   Type: A
   Name: @
   Value: GitHub/Firebase/Netlify IP addresses

   Type: CNAME
   Name: www
   Value: username.github.io (or Firebase/Netlify domain)
   ```

2. **Add CNAME File**
   ```bash
   echo "yourdomain.com" > CNAME
   ```

## SSL/TLS Configuration

All recommended hosting providers (GitHub Pages, Firebase, Netlify, Vercel) provide automatic SSL/TLS certificates.

**Verify HTTPS:**
- Test at https://www.ssllabs.com/ssltest/
- Ensure HSTS header is set
- Check for mixed content warnings

## Monitoring & Analytics

### Firebase Analytics

Already configured in firebase-config.js:
```javascript
if (typeof firebase.analytics === 'function') {
  firebase.analytics();
}
```

### Google Analytics (Optional)

Add to all HTML pages:
```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

### Error Tracking

Consider adding error tracking:
- Sentry
- LogRocket
- Rollbar

## Post-Deployment

### 1. Verify Deployment

- [ ] Visit website and check all pages
- [ ] Test authentication
- [ ] Verify payment links
- [ ] Check mobile responsiveness
- [ ] Test all forms

### 2. Security Audit

```bash
# Run security headers check
curl -I https://yourdomain.com

# Check SSL configuration
openssl s_client -connect yourdomain.com:443

# Lighthouse audit
lighthouse https://yourdomain.com --view
```

### 3. Performance Testing

- Run Lighthouse audit
- Test with GTmetrix
- Check WebPageTest
- Monitor Core Web Vitals

### 4. Setup Monitoring

- Configure uptime monitoring (UptimeRobot, Pingdom)
- Set up Firebase monitoring
- Enable error logging
- Configure performance monitoring

## Rollback Procedure

### GitHub Pages
```bash
git revert HEAD
git push origin main
```

### Firebase Hosting
```bash
firebase hosting:channel:deploy preview
# Test preview
firebase hosting:rollback  # If issues found
```

### Netlify/Vercel
- Use dashboard to rollback to previous deployment

## Troubleshooting

### Common Issues

1. **Firebase Authentication Not Working**
   - Check authorized domains in Firebase Console
   - Verify firebase-config.js has correct values
   - Check browser console for errors

2. **CSP Blocking Resources**
   - Update CSP headers to allow required domains
   - Check browser console for CSP violations

3. **CORS Errors**
   - Configure CORS in Firebase hosting
   - Check Firebase Security Rules

4. **Payment Links Not Working**
   - Verify Stripe links are correct
   - Check for mixed content (HTTP/HTTPS)

## Support & Maintenance

### Regular Tasks

- Update dependencies monthly
- Review Firebase usage
- Monitor error logs
- Check security advisories
- Update content as needed

### Security Updates

1. Monitor Firebase SDK releases
2. Update Python dependencies
3. Review OWASP Top 10
4. Conduct security audits quarterly

## References

- [Firebase Hosting Guide](https://firebase.google.com/docs/hosting)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [Netlify Documentation](https://docs.netlify.com/)
- [Vercel Documentation](https://vercel.com/docs)
- [OWASP Secure Headers](https://owasp.org/www-project-secure-headers/)

---

**Last Updated:** 2025-11-09
