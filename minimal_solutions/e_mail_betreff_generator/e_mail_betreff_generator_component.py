from fasthtml.common import *

def render_e_mail_betreff_generator_ui():
    return Div(
        # Hero Section
        Div(
            H2("E-Mail Betreff Generator", cls="text-3xl font-bold text-white mb-2 tracking-tight"),
            P("Erstelle ansprechende und klickstarke Betreffzeilen für deine E-Mail-Kampagnen.", cls="text-gray-400 text-sm"),
            cls="mb-8"
        ),
        
        # Main Layout: Form (Left) & Result (Right)
        Div(
            # Form Section
            Div(
                Form(
                    # Topic
                    Div(
                        Label("Thema der E-Mail", cls="block text-xs font-medium text-gray-400 mb-1 uppercase tracking-wider"),
                        Input(
                            type="text", 
                            name="topic", 
                            placeholder="z.B. Black Friday Sale", 
                            cls="w-full bg-[#0a0a0f] border border-gray-800 rounded-lg px-4 py-3 text-white placeholder-gray-600 focus:outline-none focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500 transition-all shadow-inner",
                            required=True
                        ),
                        cls="mb-5"
                    ),
                    # Audience
                    Div(
                        Label("Zielgruppe", cls="block text-xs font-medium text-gray-400 mb-1 uppercase tracking-wider"),
                        Input(
                            type="text", 
                            name="audience", 
                            placeholder="z.B. Bestandskunden, B2B-Leads", 
                            cls="w-full bg-[#0a0a0f] border border-gray-800 rounded-lg px-4 py-3 text-white placeholder-gray-600 focus:outline-none focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500 transition-all shadow-inner",
                            required=True
                        ),
                        cls="mb-5"
                    ),
                    # Tone
                    Div(
                        Label("Tonalität", cls="block text-xs font-medium text-gray-400 mb-1 uppercase tracking-wider"),
                        Select(
                            Option("Dringend (Urgency)", value="urgent"),
                            Option("Neugierig (Curiosity)", value="curious"),
                            Option("Persönlich", value="personal"),
                            Option("Professionell", value="professional"),
                            Option("Humorvoll", value="humorous"),
                            Option("Kurz & Prägnant", value="short"),
                            name="tone",
                            cls="w-full bg-[#0a0a0f] border border-gray-800 rounded-lg px-4 py-3 text-white focus:outline-none focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500 transition-all appearance-none shadow-inner"
                        ),
                        cls="mb-8"
                    ),
                    
                    # Submit Button
                    Button(
                        "Betreffzeilen generieren", 
                        type="submit", 
                        cls="w-full bg-indigo-600 hover:bg-indigo-500 text-white font-medium py-3 px-4 rounded-lg transition-all shadow-[0_0_15px_rgba(79,70,229,0.3)] hover:shadow-[0_0_25px_rgba(79,70,229,0.5)] flex justify-center items-center gap-2"
                    ),
                    id="email-subject-form"
                ),
                cls="bg-[#12121a] p-6 rounded-2xl border border-gray-800/50 shadow-xl"
            ),
            
            # Result Section
            Div(
                # Loading State (hidden by default)
                Div(
                    Div(cls="w-8 h-8 border-2 border-indigo-500 border-t-transparent rounded-full animate-spin mb-4"),
                    P("Generiere Betreffzeilen...", cls="text-gray-400 text-sm font-medium tracking-wide animate-pulse"),
                    id="loading-indicator",
                    cls="flex-col items-center justify-center absolute inset-0 bg-[#12121a]/90 backdrop-blur-sm z-10 rounded-2xl",
                    style="display: none;"
                ),
                
                # Result Area
                Div(
                    # Empty State (Initial)
                    Div(
                        NotStr('<svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1" stroke-linecap="round" stroke-linejoin="round" class="text-gray-700 mb-4"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>'),
                        P("Fülle das Formular aus, um", cls="text-gray-400 mb-1 font-medium"),
                        P("Betreffzeilen zu erhalten.", cls="text-gray-500 text-sm"),
                        cls="flex flex-col items-center justify-center h-full min-h-[300px] text-center"
                    ),
                    id="result-area",
                    cls="h-full min-h-[300px]"
                ),
                cls="bg-[#12121a] p-6 rounded-2xl border border-gray-800/50 shadow-xl relative"
            ),
            cls="grid grid-cols-1 lg:grid-cols-2 gap-6"
        ),
        
        # API Documentation Box
        Div(
            H3("API Dokumentation", cls="text-xl font-bold text-white mb-4"),
            P("Diese Minimal-Lösung kann auch über eine REST-API angesprochen werden.", cls="text-gray-400 mb-4"),
            
            # API Details
            Div(
                # Endpoint
                Div(
                    H4("Endpoint", cls="text-sm font-medium text-gray-500 uppercase tracking-wider mb-2"),
                    Code("POST /api/minimal-solutions/e_mail_betreff_generator", cls="block bg-[#0a0a0f] text-indigo-400 p-3 rounded-lg border border-gray-800 font-mono text-sm"),
                    cls="mb-6"
                ),
                
                # Request Example
                Div(
                    H4("Request Example", cls="text-sm font-medium text-gray-500 uppercase tracking-wider mb-2"),
                    Pre(
                        Code('''{
    "topic": "Black Friday Sale",
    "audience": "Bestandskunden",
    "tone": "urgent"
}''', cls="block bg-[#0a0a0f] text-green-400 p-4 rounded-lg border border-gray-800 font-mono text-sm overflow-x-auto"),
                    ),
                    cls="mb-6"
                ),
                
                # Response Example
                Div(
                    H4("Response Example", cls="text-sm font-medium text-gray-500 uppercase tracking-wider mb-2"),
                    Pre(
                        Code('''{
    "status": "success",
    "data": {
        "subjects": [
            "🚨 Black Friday: Exklusiv für Bestandskunden",
            "Nur heute: VIP-Sale für dich",
            "Dein Early-Access: Black Friday"
        ]
    }
}''', cls="block bg-[#0a0a0f] text-blue-400 p-4 rounded-lg border border-gray-800 font-mono text-sm overflow-x-auto"),
                    ),
                ),
                cls="bg-[#12121a] p-6 rounded-2xl border border-gray-800/50"
            ),
            cls="mt-12 mb-8"
        ),
        
        # JavaScript for API Integration
        Script(r"""
            document.addEventListener('DOMContentLoaded', function() {
                const form = document.getElementById('email-subject-form');
                const resultArea = document.getElementById('result-area');
                const loadingIndicator = document.getElementById('loading-indicator');
                
                if(form) {
                    form.addEventListener('submit', async function(e) {
                        e.preventDefault();
                        
                        const topic = form.querySelector('input[name="topic"]').value;
                        const audience = form.querySelector('input[name="audience"]').value;
                        const tone = form.querySelector('select[name="tone"]').value;
                        
                        // Show loading
                        loadingIndicator.style.display = 'flex';
                        resultArea.style.opacity = '0.5';
                        
                        try {
                            const response = await fetch('/api/minimal-solutions/e_mail_betreff_generator', {
                                method: 'POST',
                                headers: {
                                    'Content-Type': 'application/json'
                                },
                                body: JSON.stringify({
                                    topic: topic,
                                    audience: audience,
                                    tone: tone
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
                            const subjects = data.data.subjects || [];
                            
                            let html = '<div class="space-y-4">';
                            subjects.forEach((subj, index) => {
                                html += `
                                    <div class="bg-[#1a1a24] p-4 rounded-xl border border-gray-800 flex justify-between items-center group hover:border-indigo-500/50 transition-colors">
                                        <p class="text-white font-medium text-lg flex-1 pr-4" id="subj-text-${index}"></p>
                                        <button type="button" class="text-gray-400 hover:text-white bg-gray-800/50 hover:bg-indigo-600 p-2 rounded-lg transition-all copy-btn" data-index="${index}" title="Kopieren">
                                            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
                                        </button>
                                    </div>
                                `;
                            });
                            html += '</div>';
                            
                            if (subjects.length > 0) {
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
                            subjects.forEach((subj, index) => {
                                document.getElementById(`subj-text-${index}`).textContent = subj;
                            });
                            
                            document.querySelectorAll('.copy-btn').forEach(btn => {
                                btn.addEventListener('click', function() {
                                    const idx = this.getAttribute('data-index');
                                    navigator.clipboard.writeText(subjects[idx]).then(() => {
                                        const original = this.innerHTML;
                                        this.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>';
                                        setTimeout(() => this.innerHTML = original, 2000);
                                    });
                                });
                            });
                            
                            const copyAllBtn = document.getElementById('copy-all-btn');
                            if (copyAllBtn) {
                                copyAllBtn.addEventListener('click', function() {
                                    navigator.clipboard.writeText(subjects.join('\\n')).then(() => {
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
