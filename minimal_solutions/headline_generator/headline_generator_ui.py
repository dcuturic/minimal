from fasthtml.common import *

def render_headline_generator_ui():
    return Div(
        # Hero Section
        Div(
            H2("Headline Generator", cls="text-3xl font-bold text-white mb-2 tracking-tight"),
            P("Erstelle ansprechende und klickstarke Headlines für deine Artikel, Ads oder Posts.", cls="text-gray-400 text-sm"),
            cls="mb-8"
        ),
        
        # Main Layout: Form (Left) & Result (Right)
        Div(
            # Form Section
            Div(
                Form(
                    # Topic
                    Div(
                        Label("Thema oder Keyword", cls="block text-xs font-medium text-gray-400 mb-1 uppercase tracking-wider"),
                        Input(
                            type="text", 
                            name="topic", 
                            placeholder="z.B. Künstliche Intelligenz im Marketing", 
                            cls="w-full bg-[#0a0a0f] border border-gray-800 rounded-lg px-4 py-3 text-white placeholder-gray-600 focus:outline-none focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500 transition-all shadow-inner",
                            required=True
                        ),
                        cls="mb-5"
                    ),
                    # Style
                    Div(
                        Label("Stil", cls="block text-xs font-medium text-gray-400 mb-1 uppercase tracking-wider"),
                        Select(
                            Option("Informativ", value="informative"),
                            Option("Clickbait", value="clickbait"),
                            Option("Humorvoll", value="humorous"),
                            Option("Provokativ", value="provocative"),
                            Option("Professionell", value="professional"),
                            name="style",
                            cls="w-full bg-[#0a0a0f] border border-gray-800 rounded-lg px-4 py-3 text-white focus:outline-none focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500 transition-all appearance-none shadow-inner"
                        ),
                        cls="mb-5"
                    ),
                    # Count
                    Div(
                        Label("Anzahl", cls="block text-xs font-medium text-gray-400 mb-1 uppercase tracking-wider"),
                        Input(
                            type="number",
                            name="count",
                            value="3",
                            min="1",
                            max="10",
                            cls="w-full bg-[#0a0a0f] border border-gray-800 rounded-lg px-4 py-3 text-white focus:outline-none focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500 transition-all shadow-inner"
                        ),
                        cls="mb-8"
                    ),
                    
                    # Submit Button
                    Button(
                        "Headlines generieren", 
                        type="submit", 
                        cls="w-full bg-indigo-600 hover:bg-indigo-500 text-white font-medium py-3 px-4 rounded-lg transition-all shadow-[0_0_15px_rgba(79,70,229,0.3)] hover:shadow-[0_0_25px_rgba(79,70,229,0.5)] flex justify-center items-center gap-2"
                    ),
                    id="headline-form"
                ),
                cls="bg-[#12121a] p-6 rounded-2xl border border-gray-800/50 shadow-xl"
            ),
            
            # Result Section
            Div(
                # Loading State (hidden by default)
                Div(
                    Div(cls="w-8 h-8 border-2 border-indigo-500 border-t-transparent rounded-full animate-spin mb-4"),
                    P("Generiere kreative Headlines...", cls="text-gray-400 text-sm font-medium tracking-wide animate-pulse"),
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
                        P("passende Headlines zu erhalten.", cls="text-gray-500 text-sm"),
                        cls="flex flex-col items-center justify-center h-full min-h-[300px] text-center"
                    ),
                    id="result-area",
                    cls="h-full min-h-[300px]"
                ),
                cls="bg-[#12121a] p-6 rounded-2xl border border-gray-800/50 shadow-xl relative"
            ),
            cls="grid grid-cols-1 lg:grid-cols-2 gap-6"
        ),
        
        # JavaScript for API Integration
        Script(r"""
            document.addEventListener('DOMContentLoaded', function() {
                const form = document.getElementById('headline-form');
                const resultArea = document.getElementById('result-area');
                const loadingIndicator = document.getElementById('loading-indicator');
                
                if(form) {
                    form.addEventListener('submit', async function(e) {
                        e.preventDefault();
                        
                        const topic = form.querySelector('input[name="topic"]').value;
                        const style = form.querySelector('select[name="style"]').value;
                        const count = form.querySelector('input[name="count"]').value;
                        
                        // Show loading
                        loadingIndicator.style.display = 'flex';
                        resultArea.style.opacity = '0.5';
                        
                        try {
                            const response = await fetch('/api/minimal-solutions/headline_generator', {
                                method: 'POST',
                                headers: {
                                    'Content-Type': 'application/json'
                                },
                                body: JSON.stringify({
                                    topic: topic,
                                    style: style,
                                    count: parseInt(count)
                                })
                            });
                            
                            const data = await response.json();
                            
                            if(!response.ok || data.status === 'error') {
                                if (typeof showErrorPanel === 'function') {
                                    showErrorPanel('API Error', data.message || 'Ein Fehler ist aufgetreten.');
                                } else {
                                    alert(data.message || 'Ein Fehler ist aufgetreten.');
                                }
                                return;
                            }
                            
                            // Show results
                            const headlines = data.data.headlines || [];
                            
                            let html = '<div class="space-y-4">';
                            headlines.forEach((hl, index) => {
                                html += `
                                    <div class="bg-[#1a1a24] p-4 rounded-xl border border-gray-800 flex justify-between items-center group hover:border-indigo-500/50 transition-colors">
                                        <p class="text-white font-medium text-lg flex-1 pr-4" id="hl-text-${index}"></p>
                                        <button type="button" class="text-gray-400 hover:text-white bg-gray-800/50 hover:bg-indigo-600 p-2 rounded-lg transition-all copy-btn" data-index="${index}" title="Kopieren">
                                            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
                                        </button>
                                    </div>
                                `;
                            });
                            html += '</div>';
                            
                            if (headlines.length > 0) {
                                html += `
                                    <div class="mt-6 flex justify-end">
                                        <button type="button" id="copy-all-btn" class="text-sm text-indigo-400 hover:text-indigo-300 flex items-center gap-2 transition-colors">
                                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
                                            Alle kopieren
                                        </button>
                                    </div>
                                `;
                            }
                            
                            resultArea.innerHTML = html;
                            
                            // Now safely set text and add event listeners
                            headlines.forEach((hl, index) => {
                                document.getElementById(`hl-text-${index}`).textContent = hl;
                            });
                            
                            document.querySelectorAll('.copy-btn').forEach(btn => {
                                btn.addEventListener('click', function() {
                                    const idx = this.getAttribute('data-index');
                                    navigator.clipboard.writeText(headlines[idx]).then(() => {
                                        const original = this.innerHTML;
                                        this.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>';
                                        setTimeout(() => this.innerHTML = original, 2000);
                                    });
                                });
                            });
                            
                            const copyAllBtn = document.getElementById('copy-all-btn');
                            if (copyAllBtn) {
                                copyAllBtn.addEventListener('click', function() {
                                    navigator.clipboard.writeText(headlines.join('\\n')).then(() => {
                                        const original = this.innerHTML;
                                        this.innerHTML = 'Kopiert!';
                                        setTimeout(() => this.innerHTML = original, 2000);
                                    });
                                });
                            }
                            
                        } catch (err) {
                            if (typeof showErrorPanel === 'function') {
                                showErrorPanel('Netzwerkfehler', 'Verbindung zur API fehlgeschlagen.');
                            } else {
                                alert('Verbindung zur API fehlgeschlagen.');
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
