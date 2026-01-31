document.addEventListener('DOMContentLoaded', function() {
    const uploadForm = document.getElementById('upload-form');
    const fileInput = document.getElementById('pdf-file');
    const fileLabel = document.querySelector('.file-label .file-text');
    const extractBtn = document.getElementById('extract-btn');
    const loading = document.getElementById('loading');
    const errorMessage = document.getElementById('error-message');
    const resultsSection = document.getElementById('results-section');
    const extractedText = document.getElementById('extracted-text');
    const filenameDisplay = document.getElementById('filename-display');
    const methodDisplay = document.getElementById('method-display');
    const copyBtn = document.getElementById('copy-btn');

    // Update file label when file is selected
    fileInput.addEventListener('change', function() {
        if (this.files && this.files.length > 0) {
            fileLabel.textContent = this.files[0].name;
        } else {
            fileLabel.textContent = 'Choose PDF File';
        }
    });

    // Handle form submission
    uploadForm.addEventListener('submit', async function(e) {
        e.preventDefault();

        const file = fileInput.files[0];
        if (!file) {
            showError('Please select a PDF file');
            return;
        }

        // Validate file type
        if (!file.name.toLowerCase().endsWith('.pdf')) {
            showError('Please select a valid PDF file');
            return;
        }

        // Hide previous results and errors
        hideError();
        hideResults();

        // Show loading state
        showLoading();
        extractBtn.disabled = true;

        // Prepare form data
        const formData = new FormData();
        formData.append('file', file);
        
        const selectedMethod = document.querySelector('input[name="method"]:checked').value;
        formData.append('method', selectedMethod);

        try {
            const response = await fetch('/extract', {
                method: 'POST',
                body: formData
            });

            const data = await response.json();

            if (response.ok && data.success) {
                showResults(data.text, data.filename, data.method);
            } else {
                showError(data.error || 'An error occurred during extraction');
            }
        } catch (error) {
            showError('Network error: ' + error.message);
        } finally {
            hideLoading();
            extractBtn.disabled = false;
        }
    });

    // Copy to clipboard functionality
    copyBtn.addEventListener('click', function() {
        const text = extractedText.textContent;
        
        navigator.clipboard.writeText(text).then(function() {
            // Show success feedback
            const originalText = copyBtn.innerHTML;
            copyBtn.innerHTML = '<span>✓ Copied!</span>';
            copyBtn.style.background = '#10b981';
            
            setTimeout(function() {
                copyBtn.innerHTML = originalText;
                copyBtn.style.background = '';
            }, 2000);
        }).catch(function(err) {
            showError('Failed to copy text: ' + err.message);
        });
    });

    // Helper functions
    function showLoading() {
        loading.style.display = 'block';
    }

    function hideLoading() {
        loading.style.display = 'none';
    }

    function showError(message) {
        errorMessage.textContent = message;
        errorMessage.style.display = 'block';
    }

    function hideError() {
        errorMessage.style.display = 'none';
    }

    function showResults(text, filename, method) {
        extractedText.textContent = text;
        filenameDisplay.textContent = `File: ${filename}`;
        methodDisplay.textContent = `Method: ${method}`;
        resultsSection.style.display = 'block';
        
        // Scroll to results
        resultsSection.scrollIntoView({ behavior: 'smooth' });
    }

    function hideResults() {
        resultsSection.style.display = 'none';
    }
});
