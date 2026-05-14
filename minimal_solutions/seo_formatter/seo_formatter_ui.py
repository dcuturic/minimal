from fasthtml.common import *

def render_seo_formatter_ui():
    return Div(
        # Hero Section
        Div(
            H2("SEO Formatter", cls="text-3xl font-bold text-white mb-2 tracking-tight"),
            P("Formatiere SEO-Daten für eine optimale Darstellung und analysiere Ziel-Keywords.", cls="text-gray-400 text-sm"),
            cls="mb-8"
        ),
        
        # Main Layout: Form (Left) & Result (Right)
        Div(
            # Form Section
            Div(
                Form(
                    # Topic
                    Div(
                        Label("Thema oder Rohtext (Topic)", cls="block text-xs font-medium text-gray-400 mb-1 uppercase tracking-wider"),
                        Textarea(
                            name="topic", 
                            placeholder="Gib hier den Text oder das Thema ein...", 
                            cls="w-full bg-[#0a0a0f] border border-gray-800 rounded-lg px-4 py-3 text-white placeholder-gray-600 focus:outline-none focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500 transition-all shadow-inner min-h-[120px]",
                            required=True
                        ),
                        cls="mb-5"
                    ),
                    # Target
                    Div(
                        Label("Ziel (Target)", cls="block text-xs font-medium text-gray-400 mb-1 uppercase tracking-wider"),
                        Input(
                            type="text",
                            name="target",
                            placeholder="z.B. Google, Bing, Social Media",
                            cls="w-full bg-[#0a0a0f] border border-gray-800 rounded-lg px-4 py-3 text-white focus:outline-none focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500 transition-all shadow-inner",
                            required=True
                        ),
                        cls="mb-5"
                    ),
                    # Options
                    Div(
                        Label("Optionen", cls="block text-xs font-medium text-gray-400 mb-1 uppercase tracking-wider"),
                        Input(
                            type="text",
                            name="options",
                            placeholder="z.B. bold_keywords, clean_html (kommagetrennt)",
                            cls="w-full bg-[#0a0a0f] border border-gray-800 rounded-lg px-4 py-3 text-white focus:outline-none focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500 transition-all shadow-inner"
                        ),
                        cls="mb-8"
                    ),
                    
                    # Submit Button
                    Button(
                        "SEO-Daten formatieren", 
                        type="submit", 
                        cls="w-full bg-indigo-600 hover:bg-indigo-500 text-white font-medium py-3 px-4 rounded-lg transition-all shadow-[0_0_15px_rgba(79,70,229,0.3)] hover:shadow-[0_0_25px_rgba(79,70,229,0.5)] flex justify-center items-center gap-2"
                    ),
                    id="seo-formatter-form"
                ),
                cls="bg-[#12121a] p-6 rounded-2xl border border-gray-800/50 shadow-xl"
            ),
            
            # Result Section
            Div(
                # Loading State (hidden by default)
                Div(
                    Div(cls="w-8 h-8 border-2 border-indigo-500 border-t-transparent rounded-full animate-spin mb-4"),
                    P("Formatiere Daten...", cls="text-gray-400 text-sm font-medium tracking-wide animate-pulse"),
                    id="loading-indicator",
                    cls="flex-col items-center justify-center absolute inset-0 bg-[#12121a]/90 backdrop-blur-sm z-10 rounded-2xl",
                    style="display: none;"
                ),
                
                # Result Area
                Div(
                    # Empty State (Initial)
                    Div(
                        NotStr('<svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1" stroke-linecap="round" stroke-linejoin="round" class="text-gray-700 mb-4"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>'),
                        P("Fülle das Formular aus, um", cls="text-gray-400 mb-1 font-medium"),
                        P("die formatierten SEO-Daten zu sehen.", cls="text-gray-500 text-sm"),
                        cls="flex flex-col items-center justify-center h-full min-h-[300px] text-center",
                        id="empty-state"
                    ),
                    # Error State (hidden by default)
                    Div(
                        P("Ein Fehler ist aufgetreten.", id="error-message", cls="text-red-400 text-center"),
                        cls="flex flex-col items-center justify-center h-full min-h-[300px] text-center hidden",
                        id="error-state"
                    ),
                    # Data Area
                    Div(
                        id="formatted-result",
                        cls="hidden h-full flex flex-col"
                    ),
                    id="result-area",
                    cls="h-full min-h-[300px] flex flex-col"
                ),
                cls="bg-[#12121a] p-6 rounded-2xl border border-gray-800/50 shadow-xl relative"
            ),
            cls="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-12"
        ),

        # API Documentation Box
        Div(
            H3("API-Schnittstelle", cls="text-xl font-bold text-white mb-4"),
            P("Du kannst den SEO Formatter auch per API ansprechen. Hier ist ein Beispiel für Request und Response:", cls="text-gray-400 mb-4"),
            Div(
                Div(
                    H4("Request", cls="text-sm font-semibold text-gray-300 mb-2 uppercase tracking-wider"),
                    Pre(
                        Code(
                            """POST /api/minimal-solutions/seo_formatter
Content-Type: application/json

{
  "topic": "Dein Text oder Thema...",
  "target": "Google",
  "options": ["bold_keywords", "clean_html"]
}""",
                            cls="text-sm text-indigo-300"
                        ),
                        cls="bg-[#0a0a0f] p-4 rounded-xl border border-gray-800 overflow-x-auto mb-4"
                    ),
                    cls="flex-1"
                ),
                Div(
                    H4("Response", cls="text-sm font-semibold text-gray-300 mb-2 uppercase tracking-wider"),
                    Pre(
                        Code(
                            """{
  "status": "success",
  "data": {
    "formatted_content": "<p>Dein formattierter SEO Text...</p>",
    "metadata": {
      "target": "Google"
    }
  }
}""",
                            cls="text-sm text-green-300"
                        ),
                        cls="bg-[#0a0a0f] p-4 rounded-xl border border-gray-800 overflow-x-auto"
                    ),
                    cls="flex-1"
                ),
                cls="flex flex-col lg:flex-row gap-4"
            ),
            cls="bg-[#12121a] p-6 rounded-2xl border border-gray-800/50 shadow-xl"
        ),
        
        # JavaScript for API Integration
        Script(r"""
            document.addEventListener('DOMContentLoaded', function() {
                const form = document.getElementById('seo-formatter-form');
                const loadingIndicator = document.getElementById('loading-indicator');
                const emptyState = document.getElementById('empty-state');
                const errorState = document.getElementById('error-state');
                const errorMessage = document.getElementById('error-message');
                const formattedResult = document.getElementById('formatted-result');
                const resultArea = document.getElementById('result-area');
                
                if(form) {
                    form.addEventListener('submit', async function(e) {
                        e.preventDefault();
                        
                        const topic = form.querySelector('[name="topic"]').value;
                        const target = form.querySelector('[name="target"]').value;
                        const optionsStr = form.querySelector('[name="options"]').value;
                        
                        let options = [];
                        if (optionsStr) {
                            options = optionsStr.split(',').map(o => o.trim()).filter(o => o);
                        }
                        
                        // Show loading
                        loadingIndicator.style.display = 'flex';
                        resultArea.style.opacity = '0.5';
                        emptyState.classList.add('hidden');
                        errorState.classList.add('hidden');
                        formattedResult.classList.add('hidden');
                        
                        try {
                            const response = await fetch('/api/minimal-solutions/seo_formatter', {
                                method: 'POST',
                                headers: {
                                    'Content-Type': 'application/json'
                                },
                                body: JSON.stringify({
                                    topic: topic,
                                    target: target,
                                    options: options
                                })
                            });
                            
                            const data = await response.json();
                            
                            if(!response.ok || data.status === 'error') {
                                if (typeof window.showErrorPanel === 'function') {
                                    window.showErrorPanel(data.status || 'Error', data.message || 'Ein Fehler ist aufgetreten.', '');
                                } else {
                                    errorState.classList.remove('hidden');
                                    errorMessage.textContent = data.message || 'Ein Fehler ist aufgetreten.';
                                }
                                return;
                            }
                            
                            // Formatted content logic
                            const outputData = data.data || data.formatted_text || data;
                            const isString = typeof outputData === 'string';
                            const resultText = isString ? outputData : JSON.stringify(outputData, null, 2);
                            
                            let html = `
                                <div class="bg-[#1a1a24] p-4 rounded-xl border border-gray-800 h-full flex flex-col relative group flex-1">
                                    <h4 class="text-indigo-400 font-medium mb-3 text-sm uppercase tracking-wider">Ergebnis</h4>
                                    <pre class="text-white text-sm whitespace-pre-wrap flex-1 overflow-y-auto font-mono" id="result-text"></pre>
                                    <div class="absolute top-4 right-4 flex gap-2">
                                        <button type="button" class="text-gray-400 hover:text-white bg-gray-800/80 hover:bg-indigo-600 p-2 rounded-lg transition-all copy-btn" title="Kopieren">
                                            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
                                        </button>
                                        <button type="button" class="text-gray-400 hover:text-white bg-gray-800/80 hover:bg-indigo-600 p-2 rounded-lg transition-all download-btn" title="Herunterladen">
                                            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
                                        </button>
                                    </div>
                                </div>
                            `;
                            
                            formattedResult.innerHTML = html;
                            formattedResult.classList.remove('hidden');
                            
                            // Safe text insertion
                            document.getElementById('result-text').textContent = resultText;
                            
                            // Copy button logic
                            formattedResult.querySelector('.copy-btn').addEventListener('click', function() {
                                if (typeof window.copyTextFromElement === 'function') {
                                    window.copyTextFromElement(document.getElementById('result-text'), this);
                                } else {
                                    navigator.clipboard.writeText(resultText).then(() => {
                                        const original = this.innerHTML;
                                        this.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>';
                                        setTimeout(() => this.innerHTML = original, 2000);
                                    });
                                }
                            });

                            // Download button logic
                            formattedResult.querySelector('.download-btn').addEventListener('click', function() {
                                const ext = isString ? 'txt' : 'json';
                                if (typeof window.triggerDownload === 'function') {
                                    window.triggerDownload(resultText, ext, 'seo_formatted_data', this);
                                } else {
                                    const mimeType = isString ? 'text/plain' : 'application/json';
                                    const blob = new Blob([resultText], { type: mimeType });
                                    const url = URL.createObjectURL(blob);
                                    const a = document.createElement('a');
                                    a.href = url;
                                    a.download = `seo_formatted_data.${ext}`;
                                    document.body.appendChild(a);
                                    a.click();
                                    document.body.removeChild(a);
                                    URL.revokeObjectURL(url);
                                }
                            });
                            
                        } catch (err) {
                            if (typeof window.showErrorPanel === 'function') {
                                window.showErrorPanel('Network Error', 'Verbindung zur API fehlgeschlagen.', err.message);
                            } else {
                                errorState.classList.remove('hidden');
                                errorMessage.textContent = 'Verbindung zur API fehlgeschlagen.';
                            }
                        } finally {
                            loadingIndicator.style.display = 'none';
                            resultArea.style.opacity = '1';
                        }
                    });
                }
            });
        """),
        cls="max-w-5xl mx-auto"
    )
