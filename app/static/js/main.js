function copyTextFromElement(element, btn) {
    const text = element.innerText || element.textContent;
    navigator.clipboard.writeText(text).then(() => {
        showCopySuccess(btn, false);
    }).catch(err => {
        console.error('Failed to copy text: ', err);
    });
}

function copyCode(btn) {
    const pre = btn.parentElement.nextElementSibling;
    const text = pre.innerText || pre.textContent;
    navigator.clipboard.writeText(text).then(() => {
        showCopySuccess(btn, true);
    }).catch(err => {
        console.error('Failed to copy text: ', err);
    });
}

function showCopySuccess(btn, hasText) {
    const originalHTML = btn.innerHTML;
    if (hasText) {
        btn.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#00ffd5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-right: 4px;"><polyline points="20 6 9 17 4 12"></polyline></svg><span style="color: #00ffd5;">Copied!</span>`;
    } else {
        btn.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#00ffd5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>`;
    }
    
    setTimeout(() => {
        btn.innerHTML = originalHTML;
    }, 2000);
}

function copyFromSelector(selector, btn) {
    const el = document.querySelector(selector);
    if (!el) return;
    const text = el.innerText || el.textContent || el.value;
    navigator.clipboard.writeText(text).then(() => {
        showCopySuccess(btn, true);
    }).catch(err => {
        console.error('Failed to copy text: ', err);
    });
}

function downloadFromSelector(selector, format, filename, btn) {
    const el = document.querySelector(selector);
    if (!el) return;
    const text = el.innerText || el.textContent || el.value;
    triggerDownload(text, format, filename, btn);
}

function downloadCode(btn, format, defaultFilename) {
    // Navigate up to the code-header, then to the next element (the pre block)
    const header = btn.closest('.code-header') || btn.parentElement;
    const pre = header.nextElementSibling;
    if (!pre) return;
    const text = pre.innerText || pre.textContent;
    triggerDownload(text, format, defaultFilename, btn);
}

function triggerDownload(content, format, filename, btn) {
    let mimeType = 'text/plain';
    let ext = format.toLowerCase();
    
    switch(ext) {
        case 'json': mimeType = 'application/json'; break;
        case 'xml': mimeType = 'application/xml'; break;
        case 'csv': mimeType = 'text/csv'; break;
        case 'svg': mimeType = 'image/svg+xml'; break;
        case 'text':
        case 'txt': 
            mimeType = 'text/plain'; 
            ext = 'txt';
            break;
        default:
            mimeType = 'text/plain';
            break;
    }
    
    const fullFilename = `${filename}.${ext}`;
    const blob = new Blob([content], { type: mimeType });
    const url = URL.createObjectURL(blob);
    
    const a = document.createElement('a');
    a.href = url;
    a.download = fullFilename;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
    
    if (btn) {
        showDownloadSuccess(btn);
    }
}

function showDownloadSuccess(btn) {
    const originalHTML = btn.innerHTML;
    btn.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#00ffd5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-right: 4px;"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg><span style="color: #00ffd5;">Downloaded!</span>`;
    
    setTimeout(() => {
        btn.innerHTML = originalHTML;
    }, 2000);
}

// --- Loading State Utilities ---

// Add loading state to a button
function setButtonLoading(btn, isLoading) {
    if (!btn) return;
    if (isLoading) {
        if (!btn.dataset.originalText) {
            btn.dataset.originalText = btn.innerHTML;
        }
        btn.classList.add('loading');
        btn.disabled = true;
    } else {
        btn.classList.remove('loading');
        btn.disabled = false;
        if (btn.dataset.originalText) {
            btn.innerHTML = btn.dataset.originalText;
            delete btn.dataset.originalText;
        }
    }
}

// Show a spinner loader in a container
function showLoader(containerId) {
    const container = document.getElementById(containerId);
    if (!container) return;
    if (!container.dataset.originalContent) {
        container.dataset.originalContent = container.innerHTML;
    }
    container.innerHTML = '<div class="loader-container"><div class="loader"></div></div>';
}

// Hide the spinner loader and restore content
function hideLoader(containerId) {
    const container = document.getElementById(containerId);
    if (!container || !container.dataset.originalContent) return;
    container.innerHTML = container.dataset.originalContent;
    delete container.dataset.originalContent;
}

// Apply skeleton loader to a container
function showSkeleton(containerId, lines = 3) {
    const container = document.getElementById(containerId);
    if (!container) return;
    if (!container.dataset.originalContent) {
        container.dataset.originalContent = container.innerHTML;
    }
    
    let skeletons = '';
    for (let i = 0; i < lines; i++) {
        const width = 70 + Math.random() * 30; // Random width between 70% and 100%
        skeletons += `<div class="skeleton" style="width: ${width}%; margin-bottom: 0.8rem; height: 1.2rem;"></div>`;
    }
    container.innerHTML = `<div class="skeleton-container" style="width: 100%; padding: 1rem 0;">${skeletons}</div>`;
}

// Hide skeleton loader (same as hideLoader but kept for clarity)
function hideSkeleton(containerId) {
    hideLoader(containerId);
}

// --- Error Panel ---
function showErrorPanel(code, message, details) {
    const panel = document.getElementById('global-error-panel');
    if (!panel) return;
    
    const codeEl = document.getElementById('error-panel-code');
    if (code) {
        codeEl.textContent = `(${code})`;
    } else {
        codeEl.textContent = '';
    }
    
    document.getElementById('error-panel-message').textContent = message || 'An unexpected error occurred.';
    
    const detailsContainer = panel.querySelector('.error-details-container');
    const detailsEl = document.getElementById('error-panel-details');
    
    if (details) {
        let detailsText = typeof details === 'object' ? JSON.stringify(details, null, 2) : details;
        detailsEl.textContent = detailsText;
        detailsContainer.style.display = 'block';
    } else {
        detailsEl.textContent = '';
        detailsContainer.style.display = 'none';
    }
    
    panel.classList.add('show');
    
    // Auto-hide after 8 seconds if no details
    if (!details) {
        setTimeout(hideErrorPanel, 8000);
    }
}

function hideErrorPanel() {
    const panel = document.getElementById('global-error-panel');
    if (panel) {
        panel.classList.remove('show');
    }
}

function copyErrorDetails(btn) {
    const details = document.getElementById('error-panel-details').textContent;
    navigator.clipboard.writeText(details).then(() => {
        const originalHTML = btn.innerHTML;
        btn.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#00ffd5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-right: 4px;"><polyline points="20 6 9 17 4 12"></polyline></svg><span style="color: #00ffd5;">Copied!</span>`;
        setTimeout(() => {
            btn.innerHTML = originalHTML;
        }, 2000);
    }).catch(err => {
        console.error('Failed to copy error details: ', err);
    });
}

// Helper for API requests with automatic button loading state and error handling
async function fetchWithLoading(url, options = {}, btnElement = null) {
    if (btnElement) {
        setButtonLoading(btnElement, true);
    }
    
    try {
        const response = await fetch(url, options);
        if (!response.ok) {
            let errorData;
            try {
                errorData = await response.clone().json();
            } catch (e) {
                errorData = { error: { message: response.statusText } };
            }
            
            const code = errorData.error?.code || errorData.error?.type || response.status;
            const message = errorData.error?.message || `HTTP Error ${response.status}`;
            const details = errorData.error?.details || errorData.error || errorData;
            
            showErrorPanel(code, message, details);
        }
        return response;
    } catch (error) {
        showErrorPanel('Network Error', error.message, error.stack);
        throw error;
    } finally {
        if (btnElement) {
            setButtonLoading(btnElement, false);
        }
    }
}
