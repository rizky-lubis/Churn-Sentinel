import os

html_content = r"""<!DOCTYPE html>
<html lang="en" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Churn Sentinel AI | Enterprise Predictor</title>
    <script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet">
    
    <script>
        tailwind.config = {
            darkMode: "class",
            theme: {
                extend: {
                    colors: {
                        navy: { 900: '#0F172A', 800: '#1E293B', 700: '#334155', 600: '#475569' },
                        cyan: { 400: '#22D3EE', 500: '#06B6D4', 600: '#0891B2' },
                        emerald: { 400: '#34D399', 500: '#10B981', 600: '#059669' },
                        rose: { 400: '#FB7185', 500: '#EF4444', 600: '#E11D48' },
                        amber: { 400: '#FBBF24', 500: '#F59E0B' },
                        slate: { 300: '#CBD5E1', 400: '#94A3B8', 500: '#64748B' }
                    },
                    fontFamily: {
                        sans: ['Inter', 'sans-serif'],
                        mono: ['JetBrains Mono', 'monospace']
                    }
                }
            }
        }
    </script>
    <style>
        body { background-color: #0F172A; color: #F8FAFC; font-family: 'Inter', sans-serif; }
        .glass-panel {
            background: rgba(30, 41, 59, 0.6);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid rgba(71, 85, 105, 0.4);
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        }
        .input-field {
            background: rgba(15, 23, 42, 0.6);
            border: 1px solid rgba(71, 85, 105, 0.6);
            color: #F8FAFC;
            transition: all 0.2s;
            font-size: 0.875rem;
        }
        .input-field:focus {
            outline: none;
            border-color: #06B6D4;
            box-shadow: 0 0 0 1px #06B6D4;
        }
        .material-symbols-outlined { font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24; }
        .material-symbols-outlined.filled { font-variation-settings: 'FILL' 1; }
        
        .btn-primary {
            background: linear-gradient(135deg, #0891B2 0%, #06B6D4 100%);
            box-shadow: 0 0 12px rgba(6, 182, 212, 0.2);
            transition: all 0.2s;
        }
        .btn-primary:hover {
            box-shadow: 0 0 16px rgba(6, 182, 212, 0.4);
            transform: translateY(-1px);
        }
        
        ::-webkit-scrollbar { width: 6px; height: 6px; }
        ::-webkit-scrollbar-track { background: #0F172A; }
        ::-webkit-scrollbar-thumb { background: #334155; border-radius: 4px; }
        ::-webkit-scrollbar-thumb:hover { background: #475569; }
        
        /* Metric Card styling */
        .metric-card {
            background: linear-gradient(180deg, rgba(30, 41, 59, 0.8) 0%, rgba(15, 23, 42, 0.4) 100%);
            border: 1px solid rgba(71, 85, 105, 0.3);
            border-top: 1px solid rgba(100, 116, 139, 0.3);
        }
    </style>
</head>
<body class="min-h-screen flex overflow-hidden">

<!-- Sidebar -->
<aside class="w-64 bg-navy-900 border-r border-navy-700 flex-shrink-0 flex flex-col hidden md:flex">
    <div class="h-16 flex items-center px-6 border-b border-navy-700">
        <span class="material-symbols-outlined text-cyan-500 mr-2 filled">hexagon</span>
        <span class="font-semibold text-slate-300 tracking-wide text-sm">CHURN SENTINEL</span>
    </div>
    <div class="p-4 flex-1 space-y-2">
        <p class="text-xs font-semibold text-slate-500 uppercase tracking-wider mb-4 px-2">Analytics Core</p>
        
        <button onclick="switchTab('dashboard')" id="nav-dashboard" class="w-full flex items-center px-3 py-2 rounded-lg text-sm transition-colors text-slate-400 hover:text-slate-200 hover:bg-navy-800">
            <span class="material-symbols-outlined text-[18px] mr-3">dashboard</span>
            Overview
        </button>
        <button onclick="switchTab('prediction')" id="nav-prediction" class="w-full flex items-center px-3 py-2 rounded-lg text-sm transition-colors bg-navy-800 text-cyan-400 font-medium">
            <span class="material-symbols-outlined text-[18px] mr-3">model_training</span>
            Risk Analysis
        </button>
        <button onclick="switchTab('insights')" id="nav-insights" class="w-full flex items-center px-3 py-2 rounded-lg text-sm transition-colors text-slate-400 hover:text-slate-200 hover:bg-navy-800">
            <span class="material-symbols-outlined text-[18px] mr-3">insights</span>
            Drivers & Trends
        </button>
    </div>
    <div class="p-4 border-t border-navy-700">
        <div class="flex items-center">
            <div class="w-8 h-8 rounded bg-navy-700 flex items-center justify-center text-xs font-mono font-bold text-slate-300 border border-navy-600">A1</div>
            <div class="ml-3">
                <p class="text-xs font-medium text-slate-300">Analyst Unit 01</p>
                <p class="text-[10px] text-slate-500 font-mono">System Active</p>
            </div>
        </div>
    </div>
</aside>

<!-- Main Area -->
<div class="flex-1 flex flex-col h-screen overflow-hidden bg-navy-900 relative">
    <!-- Subtle background glows -->
    <div class="absolute top-[-10%] left-[-10%] w-[40%] h-[40%] rounded-full bg-cyan-900/20 blur-[120px] pointer-events-none"></div>
    <div class="absolute bottom-[-10%] right-[-10%] w-[30%] h-[30%] rounded-full bg-navy-700/30 blur-[100px] pointer-events-none"></div>

    <!-- Topbar -->
    <header class="h-16 border-b border-navy-700 flex items-center justify-between px-6 bg-navy-900/80 backdrop-blur-md z-10">
        <div class="flex items-center md:hidden">
            <span class="material-symbols-outlined text-slate-400">menu</span>
            <span class="ml-3 font-semibold text-slate-300 text-sm">CHURN SENTINEL</span>
        </div>
        <div class="hidden md:flex items-center text-sm font-mono text-slate-400">
            <span class="w-2 h-2 rounded-full bg-emerald-500 mr-2 shadow-[0_0_8px_rgba(16,185,129,0.6)]"></span>
            SVM Core Connected
        </div>
        <div class="flex items-center gap-4">
            <button class="text-slate-400 hover:text-slate-200 transition-colors">
                <span class="material-symbols-outlined text-[20px]">notifications</span>
            </button>
            <button class="text-slate-400 hover:text-slate-200 transition-colors">
                <span class="material-symbols-outlined text-[20px]">settings</span>
            </button>
        </div>
    </header>

    <!-- Scrollable Content -->
    <main class="flex-1 overflow-y-auto p-6 lg:p-8 z-10">
        
        <!-- ========================================== -->
        <!-- DASHBOARD TAB                              -->
        <!-- ========================================== -->
        <div id="view-dashboard" class="hidden space-y-6 max-w-7xl mx-auto animate-in fade-in duration-300">
            <div class="flex justify-between items-end mb-6">
                <div>
                    <h1 class="text-2xl font-semibold text-slate-100">Enterprise Overview</h1>
                    <p class="text-sm text-slate-400 mt-1">Real-time metrics and retention history.</p>
                </div>
                <button class="text-xs font-mono bg-navy-800 text-slate-300 border border-navy-700 px-3 py-1.5 rounded hover:bg-navy-700 transition-colors flex items-center gap-2">
                    <span class="material-symbols-outlined text-[14px]">download</span> Export Report
                </button>
            </div>

            <!-- KPIs -->
            <div class="grid grid-cols-1 md:grid-cols-4 gap-4">
                <div class="metric-card rounded-xl p-5">
                    <p class="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-2">Total Customers</p>
                    <p class="text-2xl font-mono text-slate-100">7,043</p>
                    <p class="text-xs text-emerald-400 mt-2 flex items-center"><span class="material-symbols-outlined text-[12px] mr-1">arrow_upward</span> +1.2% this month</p>
                </div>
                <div class="metric-card rounded-xl p-5">
                    <p class="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-2">Global Churn Rate</p>
                    <p class="text-2xl font-mono text-rose-400">26.5%</p>
                    <p class="text-xs text-rose-400 mt-2 flex items-center"><span class="material-symbols-outlined text-[12px] mr-1">arrow_upward</span> +0.4% this month</p>
                </div>
                <div class="metric-card rounded-xl p-5">
                    <p class="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-2">Monthly Revenue</p>
                    <p class="text-2xl font-mono text-slate-100">$456,200</p>
                    <p class="text-xs text-emerald-400 mt-2 flex items-center"><span class="material-symbols-outlined text-[12px] mr-1">arrow_upward</span> +3.1% this month</p>
                </div>
                <div class="metric-card rounded-xl p-5">
                    <p class="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-2">Retention Success</p>
                    <p class="text-2xl font-mono text-cyan-400">68.2%</p>
                    <p class="text-xs text-slate-400 mt-2 flex items-center"><span class="material-symbols-outlined text-[12px] mr-1">horizontal_rule</span> Steady</p>
                </div>
            </div>

            <!-- Trend Chart Mock -->
            <div class="glass-panel rounded-2xl p-6 border border-navy-700">
                <h3 class="text-sm font-semibold text-slate-300 mb-6">Predicted Churn Volume (Last 30 Days)</h3>
                <div class="h-40 flex items-end gap-2 md:gap-4 opacity-80">
                    <!-- CSS Mock Bars -->
                    <div class="flex-1 bg-navy-700 hover:bg-cyan-900 transition-colors rounded-t-sm" style="height: 30%"></div>
                    <div class="flex-1 bg-navy-700 hover:bg-cyan-900 transition-colors rounded-t-sm" style="height: 50%"></div>
                    <div class="flex-1 bg-navy-700 hover:bg-cyan-900 transition-colors rounded-t-sm" style="height: 40%"></div>
                    <div class="flex-1 bg-navy-700 hover:bg-cyan-900 transition-colors rounded-t-sm" style="height: 60%"></div>
                    <div class="flex-1 bg-navy-700 hover:bg-cyan-900 transition-colors rounded-t-sm" style="height: 45%"></div>
                    <div class="flex-1 bg-navy-700 hover:bg-cyan-900 transition-colors rounded-t-sm" style="height: 70%"></div>
                    <div class="flex-1 bg-rose-900/50 hover:bg-rose-800 transition-colors rounded-t-sm border border-rose-500/30" style="height: 90%"></div>
                    <div class="flex-1 bg-navy-700 hover:bg-cyan-900 transition-colors rounded-t-sm" style="height: 65%"></div>
                    <div class="flex-1 bg-navy-700 hover:bg-cyan-900 transition-colors rounded-t-sm" style="height: 55%"></div>
                    <div class="flex-1 bg-navy-700 hover:bg-cyan-900 transition-colors rounded-t-sm" style="height: 40%"></div>
                    <div class="flex-1 bg-navy-700 hover:bg-cyan-900 transition-colors rounded-t-sm" style="height: 30%"></div>
                    <div class="flex-1 bg-navy-700 hover:bg-cyan-900 transition-colors rounded-t-sm" style="height: 50%"></div>
                </div>
                <div class="flex justify-between text-[10px] font-mono text-slate-500 mt-3">
                    <span>Oct 01</span>
                    <span>Oct 15</span>
                    <span>Oct 30</span>
                </div>
            </div>

            <!-- History Table -->
            <div class="glass-panel rounded-2xl p-6 border border-navy-700">
                <div class="flex justify-between items-center mb-6">
                    <h3 class="text-sm font-semibold text-slate-300">Recent Predictions & Actions</h3>
                    <div class="flex gap-2">
                        <button onclick="clearHistory()" class="text-xs text-rose-400 hover:text-rose-300 transition-colors flex items-center">
                            <span class="material-symbols-outlined text-[14px] mr-1">delete</span> Clear Logs
                        </button>
                    </div>
                </div>
                <div class="overflow-x-auto">
                    <table class="w-full text-left border-collapse text-sm">
                        <thead>
                            <tr class="border-b border-navy-700">
                                <th class="pb-3 text-xs font-semibold text-slate-500 uppercase">Timestamp</th>
                                <th class="pb-3 text-xs font-semibold text-slate-500 uppercase">Customer ID</th>
                                <th class="pb-3 text-xs font-semibold text-slate-500 uppercase">Risk Level</th>
                                <th class="pb-3 text-xs font-semibold text-slate-500 uppercase text-right">Action State</th>
                            </tr>
                        </thead>
                        <tbody id="history-table-body">
                            <!-- JS populated -->
                        </tbody>
                    </table>
                    <div id="empty-history" class="text-center py-10">
                        <p class="text-sm text-slate-500">No predictions yet. Run your first customer risk analysis.</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- ========================================== -->
        <!-- PREDICTION TAB (ACTIVE)                    -->
        <!-- ========================================== -->
        <div id="view-prediction" class="space-y-6 max-w-7xl mx-auto animate-in fade-in duration-300 block">
            
            <div class="flex justify-between items-end mb-6">
                <div>
                    <h1 class="text-2xl font-semibold text-slate-100">Analyze Customer Risk</h1>
                    <p class="text-sm text-slate-400 mt-1">Run SVM model inference on customer features to predict churn probability.</p>
                </div>
                <div class="flex bg-navy-800 rounded p-1 border border-navy-700">
                    <button onclick="toggleInputMode('manual')" id="tab-manual" class="px-4 py-1.5 rounded bg-navy-700 text-cyan-400 text-xs font-medium transition-all shadow-sm">
                        Single Input
                    </button>
                    <button onclick="toggleInputMode('csv')" id="tab-csv" class="px-4 py-1.5 rounded text-slate-400 hover:text-slate-200 text-xs font-medium transition-all">
                        Batch CSV
                    </button>
                </div>
            </div>

            <div class="grid grid-cols-1 xl:grid-cols-3 gap-6">
                <!-- Left: Form -->
                <div class="xl:col-span-2 space-y-6">
                    
                    <!-- MANUAL FORM -->
                    <div id="form-manual" class="glass-panel rounded-2xl p-6 border border-navy-700 animate-in fade-in">
                        <h3 class="text-sm font-semibold text-slate-300 mb-6 flex items-center">
                            <span class="material-symbols-outlined text-[18px] mr-2 text-cyan-500">tune</span> Feature Parameters
                        </h3>
                        <form id="churn-form" class="grid grid-cols-1 md:grid-cols-2 gap-4">
                            <div class="md:col-span-2 mb-2">
                                <label class="block text-xs font-medium text-slate-400 mb-1.5">Customer Identifier</label>
                                <input id="customerName" name="customerName" type="text" class="input-field w-full rounded-lg px-3 py-2.5 font-mono text-cyan-100" placeholder="e.g. CUST-8921" required>
                            </div>
                            
                            <div>
                                <label class="block text-xs font-medium text-slate-400 mb-1.5">Tenure (Months)</label>
                                <input id="tenure" name="tenure" type="number" class="input-field w-full rounded-lg px-3 py-2 font-mono" placeholder="12">
                            </div>
                            <div>
                                <label class="block text-xs font-medium text-slate-400 mb-1.5">Monthly Charges (Rp)</label>
                                <input id="MonthlyCharges" name="MonthlyCharges" type="number" class="input-field w-full rounded-lg px-3 py-2 font-mono" placeholder="150000">
                            </div>
                            <div class="md:col-span-2">
                                <label class="block text-xs font-medium text-slate-400 mb-1.5">Total Charges (Rp)</label>
                                <input id="TotalCharges" name="TotalCharges" type="number" class="input-field w-full rounded-lg px-3 py-2 font-mono" placeholder="1800000">
                            </div>

                            <hr class="md:col-span-2 border-navy-700 my-2">

                            <div>
                                <label class="block text-xs font-medium text-slate-400 mb-1.5">Gender</label>
                                <select id="gender" name="gender" class="input-field w-full rounded-lg px-3 py-2"><option value="Male">Male</option><option value="Female">Female</option></select>
                            </div>
                            <div>
                                <label class="block text-xs font-medium text-slate-400 mb-1.5">Senior Citizen</label>
                                <select id="SeniorCitizen" name="SeniorCitizen" class="input-field w-full rounded-lg px-3 py-2"><option value="0">No</option><option value="1">Yes</option></select>
                            </div>
                            <div>
                                <label class="block text-xs font-medium text-slate-400 mb-1.5">Partner</label>
                                <select id="Partner" name="Partner" class="input-field w-full rounded-lg px-3 py-2"><option value="No">No</option><option value="Yes">Yes</option></select>
                            </div>
                            <div>
                                <label class="block text-xs font-medium text-slate-400 mb-1.5">Dependents</label>
                                <select id="Dependents" name="Dependents" class="input-field w-full rounded-lg px-3 py-2"><option value="No">No</option><option value="Yes">Yes</option></select>
                            </div>
                            
                            <hr class="md:col-span-2 border-navy-700 my-2">

                            <div>
                                <label class="block text-xs font-medium text-slate-400 mb-1.5">Internet Service</label>
                                <select id="InternetService" name="InternetService" class="input-field w-full rounded-lg px-3 py-2"><option value="Fiber optic">Fiber optic</option><option value="DSL">DSL</option><option value="No">No</option></select>
                            </div>
                            <div>
                                <label class="block text-xs font-medium text-slate-400 mb-1.5">Contract</label>
                                <select id="Contract" name="Contract" class="input-field w-full rounded-lg px-3 py-2"><option value="Month-to-month">Month-to-month</option><option value="One year">One year</option><option value="Two year">Two year</option></select>
                            </div>
                            
                            <div>
                                <label class="block text-xs font-medium text-slate-400 mb-1.5">Phone Service</label>
                                <select id="PhoneService" name="PhoneService" class="input-field w-full rounded-lg px-3 py-2"><option value="Yes">Yes</option><option value="No">No</option></select>
                            </div>
                            <div>
                                <label class="block text-xs font-medium text-slate-400 mb-1.5">Multiple Lines</label>
                                <select id="MultipleLines" name="MultipleLines" class="input-field w-full rounded-lg px-3 py-2"><option value="No">No</option><option value="Yes">Yes</option><option value="No phone service">No phone service</option></select>
                            </div>
                            <div>
                                <label class="block text-xs font-medium text-slate-400 mb-1.5">Online Security</label>
                                <select id="OnlineSecurity" name="OnlineSecurity" class="input-field w-full rounded-lg px-3 py-2"><option value="No">No</option><option value="Yes">Yes</option><option value="No internet service">No internet service</option></select>
                            </div>
                            <div>
                                <label class="block text-xs font-medium text-slate-400 mb-1.5">Online Backup</label>
                                <select id="OnlineBackup" name="OnlineBackup" class="input-field w-full rounded-lg px-3 py-2"><option value="No">No</option><option value="Yes">Yes</option><option value="No internet service">No internet service</option></select>
                            </div>
                            <div>
                                <label class="block text-xs font-medium text-slate-400 mb-1.5">Device Protection</label>
                                <select id="DeviceProtection" name="DeviceProtection" class="input-field w-full rounded-lg px-3 py-2"><option value="No">No</option><option value="Yes">Yes</option><option value="No internet service">No internet service</option></select>
                            </div>
                            <div>
                                <label class="block text-xs font-medium text-slate-400 mb-1.5">Tech Support</label>
                                <select id="TechSupport" name="TechSupport" class="input-field w-full rounded-lg px-3 py-2"><option value="No">No</option><option value="Yes">Yes</option><option value="No internet service">No internet service</option></select>
                            </div>
                            <div>
                                <label class="block text-xs font-medium text-slate-400 mb-1.5">Streaming TV</label>
                                <select id="StreamingTV" name="StreamingTV" class="input-field w-full rounded-lg px-3 py-2"><option value="No">No</option><option value="Yes">Yes</option><option value="No internet service">No internet service</option></select>
                            </div>
                            <div>
                                <label class="block text-xs font-medium text-slate-400 mb-1.5">Streaming Movies</label>
                                <select id="StreamingMovies" name="StreamingMovies" class="input-field w-full rounded-lg px-3 py-2"><option value="No">No</option><option value="Yes">Yes</option><option value="No internet service">No internet service</option></select>
                            </div>
                            
                            <hr class="md:col-span-2 border-navy-700 my-2">
                            
                            <div>
                                <label class="block text-xs font-medium text-slate-400 mb-1.5">Paperless Billing</label>
                                <select id="PaperlessBilling" name="PaperlessBilling" class="input-field w-full rounded-lg px-3 py-2"><option value="Yes">Yes</option><option value="No">No</option></select>
                            </div>
                            <div>
                                <label class="block text-xs font-medium text-slate-400 mb-1.5">Payment Method</label>
                                <select id="PaymentMethod" name="PaymentMethod" class="input-field w-full rounded-lg px-3 py-2"><option value="Electronic check">Electronic check</option><option value="Mailed check">Mailed check</option><option value="Bank transfer (automatic)">Bank transfer (auto)</option><option value="Credit card (automatic)">Credit card (auto)</option></select>
                            </div>
                        </form>
                        
                        <div class="mt-6">
                            <button id="analyze-btn" class="w-full btn-primary text-white font-semibold py-3 rounded-lg flex justify-center items-center gap-2">
                                <span class="material-symbols-outlined text-[18px]">bolt</span> Execute Inference
                                <div id="loader" class="hidden">
                                    <svg class="animate-spin h-4 w-4 text-white" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
                                </div>
                            </button>
                        </div>
                    </div>

                    <!-- CSV FORM -->
                    <div id="form-csv" class="glass-panel rounded-2xl p-6 border border-navy-700 hidden animate-in fade-in">
                        <h3 class="text-sm font-semibold text-slate-300 mb-6 flex items-center">
                            <span class="material-symbols-outlined text-[18px] mr-2 text-cyan-500">upload_file</span> Batch Processing
                        </h3>
                        <div class="border-2 border-dashed border-navy-600 rounded-xl p-10 text-center hover:border-cyan-500/50 transition-colors bg-navy-900/50 relative">
                            <input type="file" id="csv-file" accept=".csv" class="absolute inset-0 w-full h-full opacity-0 cursor-pointer z-10" onchange="updateFileName(this)">
                            <span class="material-symbols-outlined text-[48px] text-slate-600 mb-4">cloud_upload</span>
                            <h4 class="text-sm font-semibold text-slate-300 mb-1">Drag & Drop CSV File</h4>
                            <p class="text-xs text-slate-500 mb-4">Or click to browse from directory.</p>
                            <p id="file-name-display" class="text-cyan-400 font-mono text-xs hidden">No file selected.</p>
                        </div>
                        <div class="mt-6">
                            <button id="process-csv-btn" class="w-full btn-primary text-white font-semibold py-3 rounded-lg flex justify-center items-center gap-2">
                                <span class="material-symbols-outlined text-[18px]">psychology</span> Process Batch Pipeline
                                <div id="loader-csv" class="hidden">
                                    <svg class="animate-spin h-4 w-4 text-white" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
                                </div>
                            </button>
                        </div>
                        <div id="csv-progress-container" class="hidden mt-4">
                            <div class="flex justify-between text-xs font-mono mb-1 text-slate-400"><span>Processing...</span><span id="csv-progress-text" class="text-cyan-400">0 / 0</span></div>
                            <div class="w-full bg-navy-800 rounded-full h-1.5 overflow-hidden">
                                <div id="csv-progress-bar" class="bg-cyan-500 h-1.5 rounded-full w-0 transition-all duration-200"></div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Right: Output & Model Info -->
                <div class="space-y-6">
                    
                    <!-- EMPTY STATE -->
                    <div id="result-empty" class="glass-panel rounded-2xl p-6 border border-navy-700 h-48 flex flex-col items-center justify-center text-center">
                        <span class="material-symbols-outlined text-slate-600 text-4xl mb-3">analytics</span>
                        <p class="text-sm text-slate-400">No predictions yet.<br>Run your first customer risk analysis.</p>
                    </div>

                    <!-- RESULT STATE -->
                    <div id="results-container" class="hidden space-y-6 animate-in slide-in-from-bottom-4 duration-500">
                        
                        <!-- Main Result Box -->
                        <div id="result-churn" class="hidden glass-panel rounded-2xl p-6 border-t-4 border-t-rose-500 relative overflow-hidden bg-rose-900/10">
                            <div class="flex flex-col items-center text-center">
                                <div class="w-24 h-24 rounded-full border-4 border-rose-500/30 flex items-center justify-center mb-4 relative">
                                    <!-- Fake radial gauge -->
                                    <svg class="absolute inset-0 w-full h-full -rotate-90" viewBox="0 0 36 36">
                                        <path class="text-rose-500" stroke-dasharray="85, 100" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" fill="none" stroke="currentColor" stroke-width="3" />
                                    </svg>
                                    <span class="text-2xl font-mono font-bold text-rose-400">85%</span>
                                </div>
                                <h2 class="text-lg font-semibold text-rose-400 mb-1">High churn risk detected</h2>
                                <p class="text-xs text-rose-300/70 font-mono">Confidence Level: High</p>
                            </div>
                        </div>

                        <div id="result-no-churn" class="hidden glass-panel rounded-2xl p-6 border-t-4 border-t-emerald-500 relative overflow-hidden bg-emerald-900/10">
                            <div class="flex flex-col items-center text-center">
                                <div class="w-24 h-24 rounded-full border-4 border-emerald-500/30 flex items-center justify-center mb-4 relative">
                                    <svg class="absolute inset-0 w-full h-full -rotate-90" viewBox="0 0 36 36">
                                        <path class="text-emerald-500" stroke-dasharray="15, 100" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" fill="none" stroke="currentColor" stroke-width="3" />
                                    </svg>
                                    <span class="text-2xl font-mono font-bold text-emerald-400">15%</span>
                                </div>
                                <h2 class="text-lg font-semibold text-emerald-400 mb-1">Likely to stay</h2>
                                <p class="text-xs text-emerald-300/70 font-mono">Confidence Level: High</p>
                            </div>
                        </div>

                        <!-- Explainability -->
                        <div id="explainability-card" class="glass-panel rounded-xl p-5 border border-navy-700">
                            <h3 class="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-4">Why this prediction?</h3>
                            <div class="space-y-3" id="explainability-bars">
                                <!-- JS Populated -->
                            </div>
                        </div>

                        <!-- Decision Support -->
                        <div id="decision-card" class="hidden glass-panel rounded-xl p-5 border border-cyan-500/30 bg-cyan-900/10">
                            <h3 class="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-2">Recommended action</h3>
                            <p id="decision-text" class="text-sm text-cyan-100 mb-4 font-medium">Offer 20% retention discount</p>
                            <button id="decision-btn" class="w-full bg-cyan-500/20 text-cyan-400 border border-cyan-500/50 py-2 rounded text-xs font-semibold hover:bg-cyan-500/30 transition-colors">
                                Send retention offer
                            </button>
                            <button class="w-full mt-2 text-slate-400 hover:text-slate-200 text-xs py-1 transition-colors">
                                Schedule follow-up call
                            </button>
                        </div>

                        <!-- Model Info -->
                        <div class="glass-panel rounded-xl p-5 border border-navy-700">
                            <h3 class="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-3">Model Information</h3>
                            <div class="space-y-2 text-xs font-mono text-slate-300">
                                <div class="flex justify-between"><span>Algorithm</span> <span class="text-slate-100">SVM</span></div>
                                <div class="flex justify-between"><span>Accuracy</span> <span class="text-emerald-400">92.4%</span></div>
                                <div class="flex justify-between"><span>Precision</span> <span class="text-slate-100">90.1%</span></div>
                                <div class="flex justify-between"><span>Recall</span> <span class="text-slate-100">88.7%</span></div>
                                <div class="flex justify-between"><span>F1 Score</span> <span class="text-slate-100">89.3%</span></div>
                            </div>
                        </div>

                    </div>
                </div>
            </div>
        </div>

        <!-- ========================================== -->
        <!-- INSIGHTS TAB (HIDDEN)                      -->
        <!-- ========================================== -->
        <div id="view-insights" class="hidden space-y-6 max-w-7xl mx-auto animate-in fade-in duration-300">
            <div class="mb-6">
                <h1 class="text-2xl font-semibold text-slate-100">Drivers & Trends</h1>
                <p class="text-sm text-slate-400 mt-1">Global feature importance and segment analysis.</p>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div class="glass-panel rounded-2xl p-6 border border-navy-700">
                    <h3 class="text-sm font-semibold text-slate-300 mb-4">Top Churn Drivers</h3>
                    <div class="space-y-4">
                        <div>
                            <div class="flex justify-between text-xs mb-1 text-slate-300"><span>Month-to-month contract</span> <span class="text-rose-400">+32%</span></div>
                            <div class="w-full bg-navy-800 rounded-full h-1.5"><div class="bg-rose-500 h-1.5 rounded-full" style="width: 80%"></div></div>
                        </div>
                        <div>
                            <div class="flex justify-between text-xs mb-1 text-slate-300"><span>No tech support</span> <span class="text-rose-400">+21%</span></div>
                            <div class="w-full bg-navy-800 rounded-full h-1.5"><div class="bg-rose-500 h-1.5 rounded-full" style="width: 60%"></div></div>
                        </div>
                        <div>
                            <div class="flex justify-between text-xs mb-1 text-slate-300"><span>High monthly charges</span> <span class="text-rose-400">+18%</span></div>
                            <div class="w-full bg-navy-800 rounded-full h-1.5"><div class="bg-rose-500 h-1.5 rounded-full" style="width: 45%"></div></div>
                        </div>
                    </div>
                </div>
                <div class="glass-panel rounded-2xl p-6 border border-navy-700">
                    <h3 class="text-sm font-semibold text-slate-300 mb-4">Retention Drivers</h3>
                    <div class="space-y-4">
                        <div>
                            <div class="flex justify-between text-xs mb-1 text-slate-300"><span>Two year contract</span> <span class="text-emerald-400">-40%</span></div>
                            <div class="w-full bg-navy-800 rounded-full h-1.5"><div class="bg-emerald-500 h-1.5 rounded-full" style="width: 90%"></div></div>
                        </div>
                        <div>
                            <div class="flex justify-between text-xs mb-1 text-slate-300"><span>Online security</span> <span class="text-emerald-400">-25%</span></div>
                            <div class="w-full bg-navy-800 rounded-full h-1.5"><div class="bg-emerald-500 h-1.5 rounded-full" style="width: 65%"></div></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

    </main>
</div>

<script>
    // Tab Switching Logic
    function switchTab(tabId) {
        ['dashboard', 'prediction', 'insights'].forEach(id => {
            document.getElementById('view-' + id).classList.add('hidden');
            const nav = document.getElementById('nav-' + id);
            if(nav) {
                nav.className = nav.className.replace('bg-navy-800 text-cyan-400 font-medium', 'text-slate-400 hover:text-slate-200 hover:bg-navy-800');
            }
        });
        document.getElementById('view-' + tabId).classList.remove('hidden');
        const activeNav = document.getElementById('nav-' + tabId);
        if(activeNav) {
            activeNav.className = activeNav.className.replace('text-slate-400 hover:text-slate-200 hover:bg-navy-800', 'bg-navy-800 text-cyan-400 font-medium');
        }
    }

    function toggleInputMode(mode) {
        const tabManual = document.getElementById('tab-manual');
        const tabCsv = document.getElementById('tab-csv');
        const formManual = document.getElementById('form-manual');
        const formCsv = document.getElementById('form-csv');
        
        document.getElementById('results-container').classList.add('hidden');
        document.getElementById('result-empty').classList.remove('hidden');

        if(mode === 'manual') {
            tabManual.className = "px-4 py-1.5 rounded bg-navy-700 text-cyan-400 text-xs font-medium transition-all shadow-sm";
            tabCsv.className = "px-4 py-1.5 rounded text-slate-400 hover:text-slate-200 text-xs font-medium transition-all";
            formManual.classList.remove('hidden');
            formCsv.classList.add('hidden');
        } else {
            tabCsv.className = "px-4 py-1.5 rounded bg-navy-700 text-cyan-400 text-xs font-medium transition-all shadow-sm";
            tabManual.className = "px-4 py-1.5 rounded text-slate-400 hover:text-slate-200 text-xs font-medium transition-all";
            formCsv.classList.remove('hidden');
            formManual.classList.add('hidden');
        }
    }

    function updateFileName(input) {
        const display = document.getElementById('file-name-display');
        if(input.files && input.files[0]) {
            display.textContent = input.files[0].name;
            display.classList.remove('hidden');
        } else {
            display.classList.add('hidden');
        }
    }

    // History Logic
    function loadHistory() {
        const history = JSON.parse(localStorage.getItem('churnHistory') || '[]');
        const tbody = document.getElementById('history-table-body');
        const emptyMsg = document.getElementById('empty-history');
        
        if(!tbody) return;
        tbody.innerHTML = '';
        
        if (history.length === 0) {
            if(emptyMsg) emptyMsg.classList.remove('hidden');
        } else {
            if(emptyMsg) emptyMsg.classList.add('hidden');
            history.slice().reverse().forEach((item, index) => {
                const realIndex = history.length - 1 - index;
                const isChurn = item.prediction === 'Churn';
                const statusHtml = isChurn 
                    ? `<span class="bg-rose-900/30 text-rose-400 px-2 py-0.5 rounded text-[10px] font-mono border border-rose-500/20">High Risk</span>`
                    : `<span class="bg-emerald-900/30 text-emerald-400 px-2 py-0.5 rounded text-[10px] font-mono border border-emerald-500/20">Safe</span>`;
                
                let actionBtn = '';
                if (isChurn) {
                    if (item.promoSent) {
                        actionBtn = `<span class="text-xs font-mono text-slate-500 flex items-center justify-end"><span class="material-symbols-outlined text-[14px] mr-1">done_all</span> Completed</span>`;
                    } else {
                        actionBtn = `<button id="history-btn-${realIndex}" onclick="sendPromoHistory(${realIndex}, '${item.name.replace(/'/g, "\\'")}', '${item.promo ? item.promo.replace(/'/g, "\\'") : "Offer retention discount"}')" class="text-xs font-mono text-cyan-400 hover:text-cyan-300 transition-colors flex items-center justify-end w-full">Execute <span class="material-symbols-outlined text-[14px] ml-1">arrow_forward</span></button>`;
                    }
                } else {
                    actionBtn = `<span class="text-xs font-mono text-slate-600 italic block text-right">None req.</span>`;
                }

                tbody.innerHTML += `
                    <tr class="border-b border-navy-700/50 hover:bg-navy-800/50 transition-colors">
                        <td class="py-3 text-xs text-slate-400 font-mono">${item.time}</td>
                        <td class="py-3 text-sm font-medium text-slate-200">${item.name}</td>
                        <td class="py-3">${statusHtml}</td>
                        <td class="py-3">${actionBtn}</td>
                    </tr>
                `;
            });
        }
    }

    function sendPromoHistory(index, name, promoName) {
        const history = JSON.parse(localStorage.getItem('churnHistory') || '[]');
        if (history[index]) {
            history[index].promoSent = true;
            localStorage.setItem('churnHistory', JSON.stringify(history));
            loadHistory();
        }
        alert(`Action executed: Offer sent to ${name}.`);
    }

    function clearHistory() {
        if(confirm('Clear all logs?')) {
            localStorage.removeItem('churnHistory');
            loadHistory();
        }
    }

    document.addEventListener('DOMContentLoaded', loadHistory);

    // Predict Logic
    document.getElementById('analyze-btn').addEventListener('click', async () => {
        const form = document.getElementById('churn-form');
        const loader = document.getElementById('loader');
        const resultEmpty = document.getElementById('result-empty');
        const resultsContainer = document.getElementById('results-container');
        const resultChurn = document.getElementById('result-churn');
        const resultNoChurn = document.getElementById('result-no-churn');
        const decisionCard = document.getElementById('decision-card');
        const decisionText = document.getElementById('decision-text');
        const explainBars = document.getElementById('explainability-bars');

        if(!form.checkValidity()) {
            form.reportValidity();
            return;
        }

        const fd = new FormData(form);
        const map = {
            "gender": (v) => v === "Male" ? 1 : 0,
            "SeniorCitizen": (v) => parseInt(v),
            "Partner": (v) => v === "Yes" ? 1 : 0,
            "Dependents": (v) => v === "Yes" ? 1 : 0,
            "PhoneService": (v) => v === "Yes" ? 1 : 0,
            "MultipleLines": (v) => v === "Yes" ? 2 : (v === "No" ? 0 : 1),
            "InternetService": (v) => v === "Fiber optic" ? 1 : (v === "DSL" ? 0 : 2),
            "OnlineSecurity": (v) => v === "Yes" ? 2 : (v === "No" ? 0 : 1),
            "OnlineBackup": (v) => v === "Yes" ? 2 : (v === "No" ? 0 : 1),
            "DeviceProtection": (v) => v === "Yes" ? 2 : (v === "No" ? 0 : 1),
            "TechSupport": (v) => v === "Yes" ? 2 : (v === "No" ? 0 : 1),
            "StreamingTV": (v) => v === "Yes" ? 2 : (v === "No" ? 0 : 1),
            "StreamingMovies": (v) => v === "Yes" ? 2 : (v === "No" ? 0 : 1),
            "Contract": (v) => v === "Two year" ? 2 : (v === "One year" ? 1 : 0),
            "PaperlessBilling": (v) => v === "Yes" ? 1 : 0,
            "PaymentMethod": (v) => {
                if (v === "Electronic check") return 2;
                if (v === "Mailed check") return 3;
                if (v === "Bank transfer (automatic)") return 0;
                return 1; 
            }
        };

        const monthlyRp = parseFloat(fd.get('MonthlyCharges') || 0);
        const features = [
            map.gender(fd.get('gender')),
            map.SeniorCitizen(fd.get('SeniorCitizen')),
            map.Partner(fd.get('Partner')),
            map.Dependents(fd.get('Dependents')),
            parseFloat(fd.get('tenure') || 0),
            map.PhoneService(fd.get('PhoneService')),
            map.MultipleLines(fd.get('MultipleLines')),
            map.InternetService(fd.get('InternetService')),
            map.OnlineSecurity(fd.get('OnlineSecurity')),
            map.OnlineBackup(getVal(fd, 'OnlineBackup')),
            map.DeviceProtection(getVal(fd, 'DeviceProtection')),
            map.TechSupport(getVal(fd, 'TechSupport')),
            map.StreamingTV(getVal(fd, 'StreamingTV')),
            map.StreamingMovies(getVal(fd, 'StreamingMovies')),
            map.Contract(getVal(fd, 'Contract')),
            map.PaperlessBilling(getVal(fd, 'PaperlessBilling')),
            map.PaymentMethod(getVal(fd, 'PaymentMethod')),
            monthlyRp / 15000,
            parseFloat(fd.get('TotalCharges') || 0) / 15000
        ];

        function getVal(fd, name) { return fd.get(name); }

        loader.classList.remove('hidden');
        resultEmpty.classList.add('hidden');
        resultsContainer.classList.add('hidden');
        resultChurn.classList.add('hidden');
        resultNoChurn.classList.add('hidden');
        decisionCard.classList.add('hidden');

        try {
            const response = await fetch('/predict', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ features: features })
            });

            if (!response.ok) throw new Error(`Server error`);
            const result = await response.json();
            
            resultsContainer.classList.remove('hidden');
            
            const contract = fd.get('Contract');
            const techSupport = fd.get('TechSupport');
            const tenure = parseFloat(fd.get('tenure') || 0);
            
            let promoSaran = "Offer 20% retention discount";
            
            // Explainability Logic Generator
            let reasonsHtml = '';
            if (contract === "Month-to-month") {
                promoSaran = "Offer 1-year contract upgrade (30% off)";
                reasonsHtml += `<div><div class="flex justify-between text-xs mb-1 text-slate-300"><span>Month-to-month contract</span> <span class="text-rose-400">+32%</span></div><div class="w-full bg-navy-800 rounded-full h-1.5"><div class="bg-rose-500 h-1.5 rounded-full" style="width: 80%"></div></div></div>`;
            }
            if (techSupport === "No") {
                if(promoSaran === "Offer 20% retention discount") promoSaran = "Offer free priority tech support (2 months)";
                reasonsHtml += `<div><div class="flex justify-between text-xs mb-1 text-slate-300"><span>No tech support</span> <span class="text-rose-400">+21%</span></div><div class="w-full bg-navy-800 rounded-full h-1.5"><div class="bg-rose-500 h-1.5 rounded-full" style="width: 60%"></div></div></div>`;
            }
            if (tenure < 6) {
                reasonsHtml += `<div><div class="flex justify-between text-xs mb-1 text-slate-300"><span>Low tenure (< 6 mos)</span> <span class="text-rose-400">+14%</span></div><div class="w-full bg-navy-800 rounded-full h-1.5"><div class="bg-rose-500 h-1.5 rounded-full" style="width: 40%"></div></div></div>`;
            }
            if (monthlyRp > 1200000) {
                reasonsHtml += `<div><div class="flex justify-between text-xs mb-1 text-slate-300"><span>High monthly charges</span> <span class="text-rose-400">+18%</span></div><div class="w-full bg-navy-800 rounded-full h-1.5"><div class="bg-rose-500 h-1.5 rounded-full" style="width: 50%"></div></div></div>`;
            }
            if(reasonsHtml === '') {
                reasonsHtml = `<p class="text-xs text-slate-500 italic">No strong negative drivers detected.</p>`;
            }
            explainBars.innerHTML = reasonsHtml;

            if (result.prediction === "Churn") {
                resultChurn.classList.remove('hidden');
                decisionCard.classList.remove('hidden');
                decisionText.textContent = promoSaran;
            } else {
                resultNoChurn.classList.remove('hidden');
            }
            
            const customerName = fd.get('customerName').trim() || 'Unknown';
            const now = new Date();
            const timeString = now.toLocaleDateString('en-US') + ' ' + now.toLocaleTimeString('en-US');
            
            const history = JSON.parse(localStorage.getItem('churnHistory') || '[]');
            history.push({
                name: customerName,
                prediction: result.prediction,
                time: timeString,
                promo: promoSaran
            });
            localStorage.setItem('churnHistory', JSON.stringify(history));
            loadHistory();
            
        } catch (e) {
            console.error(e);
            alert('Inference failed.');
        } finally {
            loader.classList.add('hidden');
        }
    });

    // CSV Logic
    document.getElementById('process-csv-btn').addEventListener('click', async () => {
        const fileInput = document.getElementById('csv-file');
        if(!fileInput.files || fileInput.files.length === 0) return alert('Select CSV file.');

        const file = fileInput.files[0];
        const loader = document.getElementById('loader-csv');
        const progressContainer = document.getElementById('csv-progress-container');
        const progressBar = document.getElementById('csv-progress-bar');
        const progressText = document.getElementById('csv-progress-text');
        const btn = document.getElementById('process-csv-btn');

        loader.classList.remove('hidden');
        progressContainer.classList.remove('hidden');
        btn.disabled = true;

        const reader = new FileReader();
        reader.onload = async function(e) {
            const lines = e.target.result.split('\n').filter(l => l.trim().length > 0);
            if(lines.length < 2) { alert('Invalid CSV'); reset(); return; }

            const headers = lines[0].split(',').map(h => h.trim().replace(/["']/g, ''));
            const cIdIndex = headers.findIndex(h => h.toLowerCase() === 'customerid');
            const totalData = lines.length - 1;
            let processed = 0;
            const history = JSON.parse(localStorage.getItem('churnHistory') || '[]');

            const map = {
                "gender": (v) => v === "Male" ? 1 : 0,
                "SeniorCitizen": (v) => parseInt(v || 0),
                "Partner": (v) => v === "Yes" ? 1 : 0,
                "Dependents": (v) => v === "Yes" ? 1 : 0,
                "PhoneService": (v) => v === "Yes" ? 1 : 0,
                "MultipleLines": (v) => v === "Yes" ? 2 : (v === "No" ? 0 : 1),
                "InternetService": (v) => v === "Fiber optic" ? 1 : (v === "DSL" ? 0 : 2),
                "OnlineSecurity": (v) => v === "Yes" ? 2 : (v === "No" ? 0 : 1),
                "OnlineBackup": (v) => v === "Yes" ? 2 : (v === "No" ? 0 : 1),
                "DeviceProtection": (v) => v === "Yes" ? 2 : (v === "No" ? 0 : 1),
                "TechSupport": (v) => v === "Yes" ? 2 : (v === "No" ? 0 : 1),
                "StreamingTV": (v) => v === "Yes" ? 2 : (v === "No" ? 0 : 1),
                "StreamingMovies": (v) => v === "Yes" ? 2 : (v === "No" ? 0 : 1),
                "Contract": (v) => v === "Two year" ? 2 : (v === "One year" ? 1 : 0),
                "PaperlessBilling": (v) => v === "Yes" ? 1 : 0,
                "PaymentMethod": (v) => {
                    if (v === "Electronic check") return 2;
                    if (v === "Mailed check") return 3;
                    if (v === "Bank transfer (automatic)") return 0;
                    return 1;
                }
            };

            for(let i = 1; i < lines.length; i++) {
                const row = lines[i].split(',').map(item => item.trim().replace(/["']/g, ''));
                const getVal = (name) => { const idx = headers.findIndex(h => h.toLowerCase() === name.toLowerCase()); return idx !== -1 ? row[idx] : ""; };
                const customerID = cIdIndex !== -1 ? row[cIdIndex] : `Batch-${i}`;
                
                try {
                    const features = [
                        map.gender(getVal('gender')), map.SeniorCitizen(getVal('SeniorCitizen')), map.Partner(getVal('Partner')), map.Dependents(getVal('Dependents')),
                        parseFloat(getVal('tenure') || 0), map.PhoneService(getVal('PhoneService')), map.MultipleLines(getVal('MultipleLines')), map.InternetService(getVal('InternetService')),
                        map.OnlineSecurity(getVal('OnlineSecurity')), map.OnlineBackup(getVal('OnlineBackup')), map.DeviceProtection(getVal('DeviceProtection')), map.TechSupport(getVal('TechSupport')),
                        map.StreamingTV(getVal('StreamingTV')), map.StreamingMovies(getVal('StreamingMovies')), map.Contract(getVal('Contract')), map.PaperlessBilling(getVal('PaperlessBilling')),
                        map.PaymentMethod(getVal('PaymentMethod')), parseFloat(getVal('MonthlyCharges') || 0) / 15000, parseFloat(getVal('TotalCharges') || 0) / 15000
                    ];

                    const response = await fetch('/predict', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ features: features }) });
                    if(response.ok) {
                        const result = await response.json();
                        const now = new Date();
                        let promoSaran = "Offer 20% retention discount";
                        const contract = getVal('Contract');
                        if (contract === "Month-to-month") promoSaran = "Offer 1-year contract upgrade (30% off)";
                        
                        history.push({
                            name: customerID, prediction: result.prediction,
                            time: now.toLocaleDateString('en-US') + ' ' + now.toLocaleTimeString('en-US'),
                            promo: promoSaran
                        });
                    }
                } catch(err) {}
                processed++;
                progressBar.style.width = Math.floor((processed/totalData) * 100) + '%';
                progressText.innerText = `${processed} / ${totalData}`;
            }

            localStorage.setItem('churnHistory', JSON.stringify(history));
            loadHistory(); 
            reset();
            switchTab('dashboard'); 
        };
        reader.readAsText(file);

        function reset() {
            loader.classList.add('hidden');
            progressContainer.classList.add('hidden');
            btn.disabled = false;
            progressBar.style.width = '0%';
            fileInput.value = '';
            document.getElementById('file-name-display').classList.add('hidden');
        }
    });

    document.getElementById('decision-btn')?.addEventListener('click', function() {
        alert("Action sent to retention team queue.");
        // Normally we'd mark the latest prediction as completed, but for demo:
        this.innerHTML = "Action Executed";
        this.classList.add("opacity-50", "cursor-not-allowed");
    });
</script>
</body>
</html>
"""

with open('c:/Users/mhdri/Documents/Churn-Deteksi/Prediksi.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Redesign applied successfully.")
