/**
 * Firebase Configuration
 * 
 * Security Note:
 * Firebase API keys for web apps are designed to be public. They identify your 
 * Firebase project but don't grant access to your data. Access is controlled by
 * Firebase Security Rules configured in the Firebase Console.
 * 
 * IMPORTANT: Always configure proper security rules in Firebase Console:
 * - Authentication rules
 * - Firestore/Database rules  
 * - Storage rules
 * 
 * References:
 * - Firebase API Keys: https://firebase.google.com/docs/projects/api-keys
 * - Security Rules: https://firebase.google.com/docs/rules/basics
 * - Web Setup: https://firebase.google.com/docs/web/setup
 * 
 * This configuration is for the PRODUCTION environment.
 * Update these values with your own Firebase project credentials.
 */

const firebaseConfig = {
  apiKey: "AIzaSyDEezpF_02kkxk3R96Zh1ez3SuT4E2QUg8",
  authDomain: "dynasec-cic.firebaseapp.com",
  projectId: "dynasec-cic",
  storageBucket: "dynasec-cic.appspot.com",
  messagingSenderId: "517529086063",
  appId: "1:517529086063:web:70c6ca5ec15655d480f9be",
  measurementId: "G-2LNDQHW8T7"
};

// Initialize Firebase (using compat API for backward compatibility)
// Note: For new projects, consider using the modular SDK:
// https://firebase.google.com/docs/web/modular-upgrade
if (typeof firebase !== 'undefined') {
  firebase.initializeApp(firebaseConfig);
  
  // Optional: Initialize Analytics if needed
  if (typeof firebase.analytics === 'function') {
    firebase.analytics();
  }
} else {
  console.error('Firebase SDK not loaded. Please include Firebase scripts before this file.');
}

