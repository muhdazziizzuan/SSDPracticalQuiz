// Main application JavaScript file
// This file demonstrates security-conscious JavaScript practices

(function() {
    'use strict';
    
    // Secure form validation
    function validateSearchForm() {
        const form = document.querySelector('form');
        const searchInput = document.querySelector('input[name="search_term"]');
        
        if (!form || !searchInput) {
            return;
        }
        
        form.addEventListener('submit', function(event) {
            const value = searchInput.value.trim();
            
            // Basic XSS prevention
            if (containsScriptTags(value)) {
                event.preventDefault();
                showError('Invalid input detected. Script tags are not allowed.');
                return false;
            }
            
            // SQL injection pattern detection
            if (containsSQLInjection(value)) {
                event.preventDefault();
                showError('SQL injection patterns are not allowed.');
                return false;
            }
            
            // Length validation
            if (value.length > 100) {
                event.preventDefault();
                showError('Search term is too long.');
                return false;
            }
        });
    }
    
    // Security helper functions
    function containsScriptTags(input) {
        const scriptPattern = /<script[^>]*>.*?<\/script>/gi;
        return scriptPattern.test(input);
    }
    
    function containsSQLInjection(input) {
        const sqlPatterns = [
            /('|(\-\-)|(;)|(\||\|)|(\*|\*))/i,
            /(union|select|insert|delete|update|drop|create|alter|exec|execute)/i
        ];
        
        return sqlPatterns.some(pattern => pattern.test(input));
    }
    
    function showError(message) {
        // Safely display error message without using innerHTML
        const errorDiv = document.createElement('div');
        errorDiv.className = 'error-message';
        errorDiv.style.color = 'red';
        errorDiv.style.marginTop = '10px';
        errorDiv.textContent = message; // Use textContent instead of innerHTML for security
        
        const form = document.querySelector('form');
        if (form) {
            // Remove existing error messages
            const existingErrors = form.querySelectorAll('.error-message');
            existingErrors.forEach(error => error.remove());
            
            form.appendChild(errorDiv);
        }
    }
    
    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', validateSearchForm);
    } else {
        validateSearchForm();
    }
    
})();