document.addEventListener('DOMContentLoaded', function() {
    // Elements
    const uploadForm = document.getElementById('upload-form');
    const fileInput = document.getElementById('pdf-file');
    const loading = document.getElementById('loading');
    const loadingText = document.getElementById('loading-text');
    const errorMessage = document.getElementById('error-message');
    
    // Progress elements
    const progressContainer = document.getElementById('progress-container');
    const progressFill = document.getElementById('progress-fill');
    const progressMessage = document.getElementById('progress-message');
    const progressPercentage = document.getElementById('progress-percentage');
    const progressDetails = document.getElementById('progress-details');
    const progressEta = document.getElementById('progress-eta');
    
    // Toolbar buttons
    const openFileBtn = document.getElementById('open-file-btn');
    const extractTextBtn = document.getElementById('extract-text-btn');
    const extractImagesBtn = document.getElementById('extract-images-btn');
    const quickOpenBtn = document.getElementById('quick-open-btn');
    
    // Sidebar buttons
    const textOptions = document.getElementById('text-options');
    const imageOptions = document.getElementById('image-options');
    const sidebarTools = document.querySelectorAll('.tool-item');
    
    // Results sections
    const textResultsSection = document.getElementById('text-results-section');
    const imageResultsSection = document.getElementById('image-results-section');
    
    // Text results elements
    const extractedText = document.getElementById('extracted-text');
    const filenameDisplay = document.getElementById('filename-display');
    const methodDisplay = document.getElementById('method-display');
    const ocrDisplay = document.getElementById('ocr-display');
    const copyBtn = document.getElementById('copy-btn');
    
    // Image results elements
    const imageFilenameDisplay = document.getElementById('image-filename-display');
    const totalImagesEl = document.getElementById('total-images');
    const processedImagesEl = document.getElementById('processed-images');
    const skippedImagesEl = document.getElementById('skipped-images');
    const productsList = document.getElementById('products-list');
    const downloadExcelBtn = document.getElementById('download-excel-btn');

    let currentMode = 'text'; // Default mode
    let progressInterval = null;
    let currentTaskId = null;
    let excelFileName = null;

    // Sidebar tool switching
    sidebarTools.forEach(tool => {
        tool.addEventListener('click', function() {
            // Update active tool
            sidebarTools.forEach(t => t.classList.remove('active'));
            this.classList.add('active');
            
            // Get selected tool
            const toolType = this.dataset.tool;
            
            // Show/hide appropriate options
            if (toolType === 'text-extract') {
                currentMode = 'text';
                textOptions.style.display = 'block';
                imageOptions.style.display = 'none';
            } else if (toolType === 'image-extract') {
                currentMode = 'image';
                textOptions.style.display = 'none';
                imageOptions.style.display = 'block';
            } else if (toolType === 'metadata') {
                currentMode = 'metadata';
                textOptions.style.display = 'none';
                imageOptions.style.display = 'none';
            }
            
            // Hide results
            hideAllResults();
        });
    });

    // Open file button - triggers file selection
    if (openFileBtn) {
        openFileBtn.addEventListener('click', function() {
            fileInput.click();
        });
    }

    // Quick open button - triggers file selection
    if (quickOpenBtn) {
        quickOpenBtn.addEventListener('click', function() {
            fileInput.click();
        });
    }

    // Extract text button - triggers file selection with text mode
    if (extractTextBtn) {
        extractTextBtn.addEventListener('click', function() {
            currentMode = 'text';
            // Update sidebar to show text tool as active
            sidebarTools.forEach(t => t.classList.remove('active'));
            const textTool = document.querySelector('[data-tool="text-extract"]');
            if (textTool) textTool.classList.add('active');
            textOptions.style.display = 'block';
            imageOptions.style.display = 'none';
            fileInput.click();
        });
    }

    // Extract images button - triggers file selection with image mode
    if (extractImagesBtn) {
        extractImagesBtn.addEventListener('click', function() {
            currentMode = 'image';
            // Update sidebar to show image tool as active
            sidebarTools.forEach(t => t.classList.remove('active'));
            const imageTool = document.querySelector('[data-tool="image-extract"]');
            if (imageTool) imageTool.classList.add('active');
            textOptions.style.display = 'none';
            imageOptions.style.display = 'block';
            fileInput.click();
        });
    }

    // Handle file selection - automatically submit when file is chosen
    fileInput.addEventListener('change', function() {
        if (this.files && this.files.length > 0) {
            // Show work area
            const welcomeScreen = document.getElementById('welcome-screen');
            const workArea = document.getElementById('work-area');
            if (welcomeScreen) welcomeScreen.style.display = 'none';
            if (workArea) workArea.style.display = 'block';
            
            // Auto-submit the form
            uploadForm.dispatchEvent(new Event('submit'));
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
        hideAllResults();
        hideProgress();

        // Show loading state
        if (currentMode === 'text') {
            loadingText.textContent = 'Extracting text from PDF...';
        } else {
            loadingText.textContent = 'Starting AI analysis... This may take several minutes.';
        }
        showLoading();

        // Prepare form data
        const formData = new FormData();
        formData.append('file', file);

        try {
            let response;
            
            if (currentMode === 'text') {
                // Text extraction
                const selectedMethod = document.querySelector('input[name="method"]:checked').value;
                const useOcr = document.querySelector('input[name="use_ocr"]').checked;
                formData.append('method', selectedMethod);
                formData.append('use_ocr', useOcr);
                
                response = await fetch('/extract', {
                    method: 'POST',
                    body: formData
                });

                const data = await response.json();

                if (response.ok && data.success) {
                    showTextResults(data.text, data.filename, data.method, data.ocr_used);
                } else {
                    showError(data.error || 'An error occurred during extraction');
                }
            } else {
                // Image extraction with progress tracking
                hideLoading();
                showProgress();
                
                // Generate task ID
                currentTaskId = 'images_' + Date.now();
                
                // Start progress polling
                startProgressPolling(currentTaskId);
                
                response = await fetch('/extract-images', {
                    method: 'POST',
                    body: formData
                });

                const data = await response.json();
                
                // Stop progress polling
                stopProgressPolling();
                hideProgress();

                if (response.ok && data.success) {
                    excelFileName = data.excel_file;
                    showImageResults(data);
                } else {
                    showError(data.error || 'An error occurred during image extraction');
                }
            }
        } catch (error) {
            stopProgressPolling();
            showError('Network error: ' + error.message);
        } finally {
            hideLoading();
            hideProgress();
        }
    });

    // Progress polling
    function startProgressPolling(taskId) {
        progressInterval = setInterval(async () => {
            try {
                const response = await fetch(`/progress/${taskId}`);
                if (response.ok) {
                    const data = await response.json();
                    updateProgressBar(data);
                }
            } catch (error) {
                console.error('Progress polling error:', error);
            }
        }, 1000); // Poll every second
    }

    function stopProgressPolling() {
        if (progressInterval) {
            clearInterval(progressInterval);
            progressInterval = null;
        }
    }

    function updateProgressBar(data) {
        progressFill.style.width = data.percentage + '%';
        progressPercentage.textContent = data.percentage + '%';
        progressMessage.textContent = data.message;
        progressDetails.textContent = `Processing ${data.current} of ${data.total}`;
        
        if (data.eta_seconds) {
            const minutes = Math.floor(data.eta_seconds / 60);
            const seconds = data.eta_seconds % 60;
            progressEta.textContent = `Est. ${minutes}m ${seconds}s remaining`;
        } else {
            progressEta.textContent = 'Calculating time...';
        }
    }

    // Copy to clipboard functionality
    if (copyBtn) {
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
    }

    // Download Excel functionality
    if (downloadExcelBtn) {
        downloadExcelBtn.addEventListener('click', function() {
            if (excelFileName) {
                // Properly encode filename to handle special characters
                const encodedFilename = encodeURIComponent(excelFileName);
                window.location.href = `/download-excel/${encodedFilename}`;
            }
        });
    }

    // Helper functions
    function showLoading() {
        loading.style.display = 'block';
    }

    function hideLoading() {
        loading.style.display = 'none';
    }

    function showProgress() {
        progressContainer.style.display = 'block';
    }

    function hideProgress() {
        progressContainer.style.display = 'none';
    }

    function showError(message) {
        errorMessage.textContent = message;
        errorMessage.style.display = 'block';
    }

    function hideError() {
        errorMessage.style.display = 'none';
    }

    function showTextResults(text, filename, method, ocrUsed) {
        extractedText.textContent = text;
        filenameDisplay.textContent = `File: ${filename}`;
        methodDisplay.textContent = `Method: ${method}`;
        ocrDisplay.textContent = ocrUsed ? '✓ OCR Enabled' : '';
        ocrDisplay.style.color = '#10b981';
        ocrDisplay.style.fontWeight = '600';
        textResultsSection.style.display = 'block';
        
        // Scroll to results
        textResultsSection.scrollIntoView({ behavior: 'smooth' });
    }

    function showImageResults(data) {
        // Update summary stats
        totalImagesEl.textContent = data.total_images;
        processedImagesEl.textContent = data.processed;
        skippedImagesEl.textContent = data.skipped;
        imageFilenameDisplay.textContent = `File: ${data.filename}`;
        
        // Show/hide download button
        if (data.excel_file) {
            downloadExcelBtn.style.display = 'block';
        }
        
        // Clear and populate products list
        productsList.innerHTML = '';
        
        if (data.results && data.results.length > 0) {
            data.results.forEach(product => {
                const productItem = document.createElement('div');
                productItem.className = 'product-item';
                
                // Get icon based on category
                const icon = getCategoryIcon(product.category);
                
                productItem.innerHTML = `
                    <div class="product-icon">${icon}</div>
                    <div class="product-info">
                        <div class="product-sku">SKU: ${product.sku}</div>
                        <div class="product-category">${product.category}</div>
                        ${product.description ? `<div class="product-description" style="font-size: 0.85rem; color: #888; margin-top: 5px;">${product.description}</div>` : ''}
                    </div>
                    <div class="product-page">Page ${product.page}</div>
                `;
                
                productsList.appendChild(productItem);
            });
        } else {
            productsList.innerHTML = '<p style="color: #999; text-align: center; padding: 20px;">No products with SKU were found in the PDF.</p>';
        }
        
        // Show results section
        imageResultsSection.style.display = 'block';
        
        // Scroll to results
        imageResultsSection.scrollIntoView({ behavior: 'smooth' });
    }

    function getCategoryIcon(category) {
        const icons = {
            'Gate': '🚪',
            'Door': '🚪',
            'Fence': '🔲',
            'Handrail': '🛡️',
            'Window Protection': '🪟',
            'Unknown': '❓'
        };
        return icons[category] || '📦';
    }

    function hideAllResults() {
        textResultsSection.style.display = 'none';
        imageResultsSection.style.display = 'none';
    }
});
