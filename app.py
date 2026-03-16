from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import time
from datetime import datetime, timedelta
from Utilities.until import load_accounts
from Api.Account import get_garena_token, get_major_login
from Api.InGame import get_player_personal_show, get_player_stats, search_account_by_keyword


accounts = load_accounts()


app = Flask(__name__)
# Enable CORS for all origins on all routes
CORS(app)


@app.route('/', methods=['GET'])
def home():
    return """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
    <title>JuTt X Hacker | Free Fire API</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&family=Poppins:wght@600;700;800&display=swap" rel="stylesheet">
    
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Poppins', sans-serif;
            background: #000000;
            color: #e5e7eb;
            overflow-x: hidden;
        }

        /* Animated Background */
        .bg-container {
            position: fixed;
            inset: 0;
            background: linear-gradient(135deg, #0f172a 0%, #000000 50%, #0f172a 100%);
            z-index: -10;
        }

        .bg-glow-1 {
            position: absolute;
            top: 0;
            left: 25%;
            width: 400px;
            height: 400px;
            background: radial-gradient(circle, rgba(0, 217, 255, 0.3) 0%, transparent 70%);
            border-radius: 50%;
            filter: blur(80px);
            animation: pulse 4s ease-in-out infinite;
        }

        .bg-glow-2 {
            position: absolute;
            bottom: 0;
            right: 25%;
            width: 400px;
            height: 400px;
            background: radial-gradient(circle, rgba(34, 197, 94, 0.3) 0%, transparent 70%);
            border-radius: 50%;
            filter: blur(80px);
            animation: pulse 4s ease-in-out infinite 1s;
        }

        @keyframes pulse {
            0%, 100% { opacity: 0.5; }
            50% { opacity: 1; }
        }

        @keyframes slideDown {
            from {
                opacity: 0;
                transform: translateY(-20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }

        /* Header */
        header {
            border-bottom: 1px solid rgba(0, 217, 255, 0.3);
            background: rgba(0, 0, 0, 0.5);
            backdrop-filter: blur(10px);
            position: sticky;
            top: 0;
            z-index: 50;
            animation: slideDown 0.6s ease-out;
        }

        .header-container {
            max-width: 1280px;
            margin: 0 auto;
            padding: 1rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 1rem;
        }

        .header-left {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            min-width: 0;
        }

        .logo {
            width: 40px;
            height: 40px;
            background: linear-gradient(135deg, #00d9ff 0%, #22c55e 100%);
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            font-size: 16px;
            color: #000;
            flex-shrink: 0;
        }

        .brand-info h1 {
            font-size: 1.125rem;
            background: linear-gradient(90deg, #00d9ff 0%, #22c55e 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            font-weight: 800;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }

        .brand-info p {
            font-size: 0.65rem;
            color: #22c55e;
            margin-top: 2px;
            white-space: nowrap;
        }

        .header-right {
            display: flex;
            gap: 0.5rem;
            flex-shrink: 0;
        }

        .icon-btn {
            width: 36px;
            height: 36px;
            border: 1px solid rgba(0, 217, 255, 0.3);
            background: transparent;
            border-radius: 6px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.3s ease;
            color: #00d9ff;
            font-size: 16px;
            flex-shrink: 0;
        }

        .icon-btn:hover {
            background: rgba(0, 217, 255, 0.2);
            border-color: #00d9ff;
            transform: scale(1.05);
        }

        .icon-btn.whatsapp {
            color: #22c55e;
            border-color: rgba(34, 197, 94, 0.3);
        }

        .icon-btn.whatsapp:hover {
            background: rgba(34, 197, 94, 0.2);
            border-color: #22c55e;
        }

        .icon-btn.email {
            color: #fbbf24;
            border-color: rgba(251, 191, 36, 0.3);
        }

        .icon-btn.email:hover {
            background: rgba(251, 191, 36, 0.2);
            border-color: #fbbf24;
        }

        /* Main Content */
        main {
            max-width: 1280px;
            margin: 0 auto;
            padding: 1.5rem 1rem;
        }

        /* Hero Section */
        .hero {
            text-align: center;
            margin-bottom: 2rem;
            animation: fadeIn 0.8s ease-out 0.2s both;
        }

        .hero h2 {
            font-size: clamp(1.5rem, 5vw, 3rem);
            margin-bottom: 0.75rem;
            background: linear-gradient(90deg, #00d9ff 0%, #22c55e 50%, #00d9ff 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            font-weight: 800;
        }

        .hero p {
            font-size: clamp(0.875rem, 3vw, 1.125rem);
            color: #9ca3af;
            margin-bottom: 1.5rem;
        }

        /* API Documentation Grid */
        .api-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 0.75rem;
            margin-bottom: 2rem;
        }

        .api-card {
            background: rgba(30, 30, 46, 0.5);
            border: 1px solid rgba(0, 217, 255, 0.3);
            border-radius: 8px;
            padding: 1rem;
            text-align: center;
            transition: all 0.3s ease;
            animation: fadeIn 0.8s ease-out 0.3s both;
        }

        .api-card:hover {
            border-color: #00d9ff;
            background: rgba(0, 217, 255, 0.1);
            transform: translateY(-3px);
        }

        .api-card.green {
            border-color: rgba(34, 197, 94, 0.3);
        }

        .api-card.green:hover {
            border-color: #22c55e;
            background: rgba(34, 197, 94, 0.1);
        }

        .api-card.yellow {
            border-color: rgba(251, 191, 36, 0.3);
        }

        .api-card.yellow:hover {
            border-color: #fbbf24;
            background: rgba(251, 191, 36, 0.1);
        }

        .api-icon {
            font-size: 1.75rem;
            margin-bottom: 0.5rem;
        }

        .api-card h3 {
            font-weight: 700;
            margin-bottom: 0.25rem;
            font-size: 0.95rem;
        }

        .api-card p {
            font-size: 0.75rem;
            color: #9ca3af;
            font-family: 'JetBrains Mono', monospace;
        }

        /* Tabs */
        .tabs {
            display: flex;
            gap: 0.5rem;
            margin-bottom: 1.5rem;
            border-bottom: 1px solid rgba(0, 217, 255, 0.3);
            padding-bottom: 0.75rem;
            overflow-x: auto;
            animation: fadeIn 0.8s ease-out 0.4s both;
            -webkit-overflow-scrolling: touch;
        }

        .tab-btn {
            padding: 0.5rem 1rem;
            border-radius: 6px;
            font-weight: 600;
            border: 1px solid #475569;
            background: transparent;
            color: #9ca3af;
            cursor: pointer;
            transition: all 0.3s ease;
            white-space: nowrap;
            font-size: 0.85rem;
        }

        .tab-btn.active {
            background: rgba(0, 217, 255, 0.2);
            border-color: #00d9ff;
            color: #00d9ff;
        }

        .tab-btn.active.green {
            background: rgba(34, 197, 94, 0.2);
            border-color: #22c55e;
            color: #22c55e;
        }

        .tab-btn.active.yellow {
            background: rgba(251, 191, 36, 0.2);
            border-color: #fbbf24;
            color: #fbbf24;
        }

        .tab-btn:hover {
            border-color: #00d9ff;
            color: #e5e7eb;
        }

        /* Content Grid */
        .content-grid {
            display: grid;
            grid-template-columns: 1fr 2fr;
            gap: 1.5rem;
            animation: fadeIn 0.8s ease-out 0.5s both;
        }

        @media (max-width: 1024px) {
            .content-grid {
                grid-template-columns: 1fr;
            }
        }

        /* Control Panel */
        .control-panel {
            background: rgba(30, 30, 46, 0.5);
            border: 1px solid #1e293b;
            border-radius: 8px;
            padding: 1.25rem;
            height: fit-content;
            position: sticky;
            top: 100px;
        }

        @media (max-width: 1024px) {
            .control-panel {
                position: static;
                top: auto;
            }
        }

        .control-panel h3 {
            font-size: 1rem;
            color: #00d9ff;
            margin-bottom: 1rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .form-group {
            margin-bottom: 0.75rem;
        }

        .form-group label {
            display: block;
            font-size: 0.8rem;
            color: #9ca3af;
            margin-bottom: 0.35rem;
        }

        .form-group input,
        .form-group select {
            width: 100%;
            background: #1e293b;
            border: 1px solid #475569;
            border-radius: 6px;
            padding: 0.6rem;
            color: #e5e7eb;
            font-size: 0.85rem;
            font-family: 'JetBrains Mono', monospace;
            transition: all 0.3s ease;
        }

        .form-group input:focus,
        .form-group select:focus {
            outline: none;
            border-color: #00d9ff;
            background: #0f172a;
        }

        .fetch-btn {
            width: 100%;
            background: linear-gradient(135deg, #00d9ff 0%, #22c55e 100%);
            color: #000;
            border: none;
            border-radius: 6px;
            padding: 0.75rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.3s ease;
            font-size: 0.95rem;
        }

        .fetch-btn:hover:not(:disabled) {
            transform: translateY(-2px);
            box-shadow: 0 10px 30px rgba(0, 217, 255, 0.3);
        }

        .fetch-btn:disabled {
            opacity: 0.6;
            cursor: not-allowed;
        }

        .error-msg {
            color: #ef4444;
            font-size: 0.8rem;
            background: rgba(239, 68, 68, 0.1);
            border: 1px solid rgba(239, 68, 68, 0.3);
            border-radius: 6px;
            padding: 0.6rem;
            margin-top: 0.75rem;
            display: none;
        }

        .error-msg.show {
            display: block;
        }

        /* Results Panel */
        .results-panel {
            background: rgba(30, 30, 46, 0.5);
            border: 1px solid rgba(0, 217, 255, 0.3);
            border-radius: 8px;
            padding: 1.5rem;
        }

        .results-panel.green {
            border-color: rgba(34, 197, 94, 0.3);
        }

        .results-panel.yellow {
            border-color: rgba(251, 191, 36, 0.3);
        }

        .results-panel h3 {
            font-size: 1.15rem;
            margin-bottom: 1rem;
            color: #00d9ff;
        }

        .results-panel.green h3 {
            color: #22c55e;
        }

        .results-panel.yellow h3 {
            color: #fbbf24;
        }

        .stat-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
            gap: 0.75rem;
            margin-bottom: 1rem;
        }

        .stat-box {
            background: rgba(15, 23, 42, 0.5);
            border: 1px solid #1e293b;
            border-radius: 6px;
            padding: 0.75rem;
        }

        .stat-label {
            font-size: 0.75rem;
            color: #9ca3af;
            margin-bottom: 0.35rem;
            font-weight: 600;
        }

        .stat-value {
            font-size: 1.25rem;
            font-weight: 700;
            color: #00d9ff;
            font-family: 'JetBrains Mono', monospace;
            word-break: break-word;
        }

        .stat-box.level .stat-value {
            color: #22c55e;
        }

        .stat-box.rank .stat-value {
            color: #fbbf24;
        }

        .stat-box.points .stat-value {
            color: #a855f7;
        }

        .stat-box.cs .stat-value {
            color: #06b6d4;
        }

        .stat-box.liked .stat-value {
            color: #ec4899;
        }

        .section-title {
            font-size: 0.95rem;
            font-weight: 700;
            color: #00d9ff;
            margin-top: 1.25rem;
            margin-bottom: 0.75rem;
            padding-bottom: 0.5rem;
            border-bottom: 1px solid rgba(0, 217, 255, 0.2);
        }

        .clan-info {
            background: rgba(15, 23, 42, 0.5);
            border: 1px solid #1e293b;
            border-radius: 6px;
            padding: 0.75rem;
            margin-top: 0.75rem;
        }

        .clan-label {
            font-size: 0.75rem;
            color: #9ca3af;
            margin-bottom: 0.35rem;
        }

        .clan-value {
            font-weight: 700;
            color: #ec4899;
            font-size: 0.95rem;
            word-break: break-word;
        }

        .placeholder-text {
            color: #9ca3af;
            text-align: center;
            padding: 1.5rem;
            font-size: 0.9rem;
        }

        .search-results {
            max-height: 500px;
            overflow-y: auto;
            display: flex;
            flex-direction: column;
            gap: 0.6rem;
        }

        .search-result-item {
            background: rgba(15, 23, 42, 0.5);
            border: 1px solid #1e293b;
            border-radius: 6px;
            padding: 0.75rem;
            transition: all 0.3s ease;
            cursor: pointer;
        }

        .search-result-item:hover {
            border-color: #fbbf24;
            background: rgba(251, 191, 36, 0.05);
        }

        .search-result-name {
            font-weight: 700;
            color: #fbbf24;
            margin-bottom: 0.35rem;
            font-size: 0.9rem;
            word-break: break-word;
        }

        .search-result-info {
            font-size: 0.75rem;
            color: #9ca3af;
            display: flex;
            flex-direction: column;
            gap: 0.25rem;
        }

        .info-row {
            display: flex;
            justify-content: space-between;
            gap: 0.5rem;
        }

        /* Footer */
        footer {
            border-top: 1px solid rgba(0, 217, 255, 0.3);
            background: rgba(0, 0, 0, 0.5);
            backdrop-filter: blur(10px);
            margin-top: 2rem;
            padding: 1.5rem 1rem;
            text-align: center;
            color: #9ca3af;
            font-size: 0.8rem;
        }

        footer p {
            margin: 0.35rem 0;
        }

        footer .brand {
            color: #00d9ff;
            font-weight: 700;
        }

        /* Loading spinner */
        .spinner {
            display: inline-block;
            width: 14px;
            height: 14px;
            border: 2px solid rgba(0, 217, 255, 0.3);
            border-top-color: #00d9ff;
            border-radius: 50%;
            animation: spin 0.8s linear infinite;
            margin-right: 0.5rem;
        }

        @keyframes spin {
            to { transform: rotate(360deg); }
        }

        /* Scrollbar styling */
        ::-webkit-scrollbar {
            width: 6px;
            height: 6px;
        }

        ::-webkit-scrollbar-track {
            background: rgba(0, 217, 255, 0.05);
        }

        ::-webkit-scrollbar-thumb {
            background: rgba(0, 217, 255, 0.3);
            border-radius: 3px;
        }

        ::-webkit-scrollbar-thumb:hover {
            background: rgba(0, 217, 255, 0.5);
        }

        @media (max-width: 640px) {
            main {
                padding: 1rem 0.75rem;
            }

            .header-container {
                padding: 0.75rem;
            }

            .control-panel {
                padding: 1rem;
            }

            .results-panel {
                padding: 1rem;
            }

            .stat-grid {
                grid-template-columns: repeat(2, 1fr);
            }

            .api-grid {
                grid-template-columns: 1fr;
            }

            .tabs {
                gap: 0.35rem;
            }

            .tab-btn {
                padding: 0.4rem 0.8rem;
                font-size: 0.75rem;
            }

            .hero h2 {
                font-size: 1.5rem;
            }

            .hero p {
                font-size: 0.85rem;
            }
        }
    </style>
</head>
<body>
    <div class="bg-container">
        <div class="bg-glow-1"></div>
        <div class="bg-glow-2"></div>
    </div>

    <!-- Header -->
    <header>
        <div class="header-container">
            <div class="header-left">
                <div class="logo">JX</div>
                <div class="brand-info">
                    <h1>JuTt X Hacker</h1>
                    <p>Matric Fail Hacker</p>
                </div>
            </div>
            <div class="header-right">
                <a href="https://youtube.com/@matricfailhacker" target="_blank" class="icon-btn" title="YouTube">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/>
                    </svg>
                </a>
                <a href="https://whatsapp.com/channel/0029Vb5czH6IXnllDW2uNs1i" target="_blank" class="icon-btn whatsapp" title="WhatsApp">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8zm3.5-9c.83 0 1.5-.67 1.5-1.5S16.33 8 15.5 8 14 8.67 14 9.5s.67 1.5 1.5 1.5zm-7 0c.83 0 1.5-.67 1.5-1.5S9.33 8 8.5 8 7 8.67 7 9.5 7.67 11 8.5 11zm3.5 6.5c2.33 0 4.31-1.46 5.11-3.5H6.89c.8 2.04 2.78 3.5 5.11 3.5z"/>
                    </svg>
                </a>
                <a href="mailto:Juttxhacker12@gmail.com" class="icon-btn email" title="Email">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <rect x="2" y="4" width="20" height="16" rx="2"/>
                        <path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>
                    </svg>
                </a>
            </div>
        </div>
    </header>

    <!-- Main Content -->
    <main>
        <!-- Hero Section -->
        <div class="hero">
            <h2>Free Fire Player Stats API</h2>
            <p>Access real-time player statistics, personal profiles, and search accounts across Free Fire servers</p>

            <!-- API Documentation Grid -->
            <div class="api-grid">
                <div class="api-card">
                    <div class="api-icon">⌘</div>
                    <h3>Personal Stats</h3>
                    <p>/get_player_personal_show</p>
                </div>
                <div class="api-card green">
                    <div class="api-icon">⚡</div>
                    <h3>Match Stats</h3>
                    <p>/get_player_stats</p>
                </div>
                <div class="api-card yellow">
                    <div class="api-icon">🔍</div>
                    <h3>Search Accounts</h3>
                    <p>/get_search_account_by_keyword</p>
                </div>
            </div>
        </div>

        <!-- Tabs -->
        <div class="tabs">
            <button class="tab-btn active" data-tab="personal">Personal Stats</button>
            <button class="tab-btn green" data-tab="matchstats">Match Stats</button>
            <button class="tab-btn yellow" data-tab="search">Search Accounts</button>
        </div>

        <!-- Content Grid -->
        <div class="content-grid">
            <!-- Control Panel -->
            <div class="control-panel">
                <h3>⌘ API Controls</h3>

                <!-- Server Selection -->
                <div class="form-group">
                    <label>Server</label>
                    <select id="server">
                        <option value="pk">Pakistan (PK)</option>
                        <option value="sg">Singapore (SG)</option>
                        <option value="in">India (IN)</option>
                        <option value="bd">Bangladesh (BD)</option>
                    </select>
                </div>

                <!-- UID Input (for personal & match stats) -->
                <div class="form-group" id="uid-group">
                    <label>Player UID</label>
                    <input type="text" id="uid" placeholder="Enter UID" value="11647508073">
                </div>

                <!-- Search Keyword (for search tab) -->
                <div class="form-group" id="keyword-group" style="display: none;">
                    <label>Player Name</label>
                    <input type="text" id="keyword" placeholder="Enter keyword" value="juTt">
                </div>

                <!-- Game Mode (for match stats) -->
                <div class="form-group" id="gamemode-group" style="display: none;">
                    <label>Game Mode</label>
                    <select id="gamemode">
                        <option value="br">Battle Royale (BR)</option>
                        <option value="cs">Clash Squad (CS)</option>
                    </select>
                </div>

                <!-- Match Mode (for match stats) -->
                <div class="form-group" id="matchmode-group" style="display: none;">
                    <label>Match Mode</label>
                    <select id="matchmode">
                        <option value="RANKED">Ranked</option>
                        <option value="UNRANKED">Unranked</option>
                    </select>
                    <small style="font-size: 0.7rem; color: #9ca3af; margin-top: 0.25rem; display: block;">Note: Unranked uses NORMAL mode in API</small>
                </div>

                <!-- Fetch Button -->
                <button class="fetch-btn" id="fetchBtn">Fetch Data</button>

                <!-- Error Message -->
                <div class="error-msg" id="errorMsg"></div>
            </div>

            <!-- Results Panel -->
            <div class="results-panel" id="resultsPanel">
                <h3 id="resultsTitle">Personal Stats</h3>
                <div id="resultsContent" class="placeholder-text">
                    Enter UID and click "Fetch Data" to see personal stats
                </div>
            </div>
        </div>
    </main>

    <!-- Footer -->
    <footer>
        <p>Built by <span class="brand">JuTt X Hacker</span> | Powered by Free Fire API</p>
        <p>© 2026 Matric Fail Hacker. All rights reserved.</p>
    </footer>

    <script>
        const API_BASE = "https://ff-infobyjxh.vercel.app";

        // DOM Elements
        const tabBtns = document.querySelectorAll('.tab-btn');
        const uidGroup = document.getElementById('uid-group');
        const keywordGroup = document.getElementById('keyword-group');
        const gamemodeGroup = document.getElementById('gamemode-group');
        const matchmodeGroup = document.getElementById('matchmode-group');
        const fetchBtn = document.getElementById('fetchBtn');
        const resultsPanel = document.getElementById('resultsPanel');
        const resultsTitle = document.getElementById('resultsTitle');
        const resultsContent = document.getElementById('resultsContent');
        const errorMsg = document.getElementById('errorMsg');
        const serverSelect = document.getElementById('server');
        const uidInput = document.getElementById('uid');
        const keywordInput = document.getElementById('keyword');
        const gamemodeSelect = document.getElementById('gamemode');
        const matchmodeSelect = document.getElementById('matchmode');

        let currentTab = 'personal';

        // Tab switching
        tabBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                tabBtns.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                currentTab = btn.dataset.tab;

                // Update form groups visibility
                if (currentTab === 'personal') {
                    uidGroup.style.display = 'block';
                    keywordGroup.style.display = 'none';
                    gamemodeGroup.style.display = 'none';
                    matchmodeGroup.style.display = 'none';
                    resultsTitle.textContent = 'Personal Stats';
                    resultsPanel.classList.remove('green', 'yellow');
                } else if (currentTab === 'matchstats') {
                    uidGroup.style.display = 'block';
                    keywordGroup.style.display = 'none';
                    gamemodeGroup.style.display = 'block';
                    matchmodeGroup.style.display = 'block';
                    resultsTitle.textContent = 'Match Statistics';
                    resultsPanel.classList.remove('yellow');
                    resultsPanel.classList.add('green');
                } else if (currentTab === 'search') {
                    uidGroup.style.display = 'none';
                    keywordGroup.style.display = 'block';
                    gamemodeGroup.style.display = 'none';
                    matchmodeGroup.style.display = 'none';
                    resultsTitle.textContent = 'Search Results';
                    resultsPanel.classList.remove('green');
                    resultsPanel.classList.add('yellow');
                }

                resultsContent.innerHTML = '<div class="placeholder-text">Ready to fetch data...</div>';
                errorMsg.classList.remove('show');
            });
        });

        // Fetch functions
        async function fetchPersonalStats() {
            const uid = uidInput.value;
            const server = serverSelect.value;

            if (!uid) {
                showError('Please enter a UID');
                return;
            }

            setLoading(true);
            try {
                const response = await fetch(`${API_BASE}/get_player_personal_show?server=${server}&uid=${uid}`);
                const data = await response.json();

                if (data.basicinfo) {
                    const basic = data.basicinfo;
                    const profile = data.profileinfo || {};
                    const clan = data.clanbasicinfo || {};
                    const social = data.socialinfo || {};
                    const pet = data.petinfo || {};
                    const credit = data.creditscoreinfo || {};

                    let html = `
                        <div class="stat-grid">
                            <div class="stat-box">
                                <div class="stat-label">Nickname</div>
                                <div class="stat-value" style="font-size: 0.9rem; color: #00d9ff;">${basic.nickname || 'N/A'}</div>
                            </div>
                            <div class="stat-box level">
                                <div class="stat-label">Level</div>
                                <div class="stat-value">${basic.level || 0}</div>
                            </div>
                            <div class="stat-box rank">
                                <div class="stat-label">BR Rank</div>
                                <div class="stat-value">#${basic.rank || 0}</div>
                            </div>
                            <div class="stat-box points">
                                <div class="stat-label">BR Points</div>
                                <div class="stat-value">${basic.rankingpoints || 0}</div>
                            </div>
                            <div class="stat-box cs">
                                <div class="stat-label">CS Rank</div>
                                <div class="stat-value">#${basic.csrank || 0}</div>
                            </div>
                            <div class="stat-box liked">
                                <div class="stat-label">Liked</div>
                                <div class="stat-value">${basic.liked || 0}</div>
                            </div>
                        </div>

                        <div class="section-title">📊 Detailed Stats</div>
                        <div class="stat-grid">
                            <div class="stat-box">
                                <div class="stat-label">Max BR Rank</div>
                                <div class="stat-value">#${basic.maxrank || 0}</div>
                            </div>
                            <div class="stat-box">
                                <div class="stat-label">Max CS Rank</div>
                                <div class="stat-value">#${basic.csmaxrank || 0}</div>
                            </div>
                            <div class="stat-box">
                                <div class="stat-label">CS Points</div>
                                <div class="stat-value">${basic.csrankingpoints || 0}</div>
                            </div>
                            <div class="stat-box">
                                <div class="stat-label">Badges</div>
                                <div class="stat-value">${basic.badgecnt || 0}</div>
                            </div>
                            <div class="stat-box">
                                <div class="stat-label">Hippo Rank</div>
                                <div class="stat-value">${basic.hipporank || 0}</div>
                            </div>
                            <div class="stat-box">
                                <div class="stat-label">Season</div>
                                <div class="stat-value">${basic.seasonid || 0}</div>
                            </div>
                        </div>
                    `;

                    if (clan.clanname) {
                        html += `
                            <div class="section-title">🏢 Guild Information</div>
                            <div class="stat-grid">
                                <div class="stat-box">
                                    <div class="stat-label">Guild Name</div>
                                    <div class="stat-value" style="font-size: 0.9rem; color: #ec4899;">${clan.clanname}</div>
                                </div>
                                <div class="stat-box">
                                    <div class="stat-label">Guild Level</div>
                                    <div class="stat-value">${clan.clanlevel || 0}</div>
                                </div>
                                <div class="stat-box">
                                    <div class="stat-label">Members</div>
                                    <div class="stat-value">${clan.membernum || 0}/${clan.capacity || 0}</div>
                                </div>
                            </div>
                        `;
                    }

                    if (social.signature) {
                        html += `
                            <div class="section-title">✍️ About</div>
                            <div class="clan-info">
                                <div class="clan-value">${social.signature}</div>
                            </div>
                        `;
                    }

                    if (pet.id) {
                        html += `
                            <div class="section-title">🐾 Pet Info</div>
                            <div class="stat-grid">
                                <div class="stat-box">
                                    <div class="stat-label">Pet Level</div>
                                    <div class="stat-value">${pet.level || 0}</div>
                                </div>
                                <div class="stat-box">
                                    <div class="stat-label">Pet Exp</div>
                                    <div class="stat-value">${pet.exp || 0}</div>
                                </div>
                            </div>
                        `;
                    }

                    if (credit.creditscore) {
                        html += `
                            <div class="section-title">⭐ Credit Score</div>
                            <div class="stat-grid">
                                <div class="stat-box">
                                    <div class="stat-label">Score</div>
                                    <div class="stat-value">${credit.creditscore}</div>
                                </div>
                            </div>
                        `;
                    }

                    resultsContent.innerHTML = html;
                    errorMsg.classList.remove('show');
                } else {
                    showError('No data found for this UID');
                }
            } catch (err) {
                showError('Failed to fetch personal stats: ' + err.message);
            } finally {
                setLoading(false);
            }
        }

        async function fetchPlayerStats() {
            const uid = uidInput.value;
            const server = serverSelect.value;
            const gamemode = gamemodeSelect.value;
            let matchmode = matchmodeSelect.value;

            if (!uid) {
                showError('Please enter a UID');
                return;
            }

            // Convert Unranked to NORMAL for API
            if (matchmode === 'UNRANKED') {
                matchmode = 'NORMAL';
            }

            setLoading(true);
            try {
                const response = await fetch(
                    `${API_BASE}/get_player_stats?server=${server}&uid=${uid}&matchmode=${matchmode}&gamemode=${gamemode}`
                );
                const data = await response.json();

                if (data.success && data.data) {
                    const stats = data.data;
                    let html = '';

                    if (stats.solostats) {
                        const solo = stats.solostats;
                        const detailed = solo.detailedstats || {};
                        html += `
                            <div class="section-title">🎯 Solo Stats</div>
                            <div class="stat-grid">
                                <div class="stat-box">
                                    <div class="stat-label">Kills</div>
                                    <div class="stat-value">${solo.kills || 0}</div>
                                </div>
                                <div class="stat-box">
                                    <div class="stat-label">Games</div>
                                    <div class="stat-value">${solo.gamesplayed || 0}</div>
                                </div>
                                <div class="stat-box">
                                    <div class="stat-label">K/D</div>
                                    <div class="stat-value">${solo.gamesplayed ? (solo.kills / solo.gamesplayed).toFixed(2) : '0'}</div>
                                </div>
                                <div class="stat-box">
                                    <div class="stat-label">Damage</div>
                                    <div class="stat-value">${detailed.damage || 0}</div>
                                </div>
                                <div class="stat-box">
                                    <div class="stat-label">Headshots</div>
                                    <div class="stat-value">${detailed.headshots || 0}</div>
                                </div>
                                <div class="stat-box">
                                    <div class="stat-label">Distance</div>
                                    <div class="stat-value">${(detailed.distancetravelled / 1000 || 0).toFixed(1)}km</div>
                                </div>
                            </div>
                        `;
                    }

                    if (stats.duostats) {
                        const duo = stats.duostats;
                        const detailed = duo.detailedstats || {};
                        html += `
                            <div class="section-title">👥 Duo Stats</div>
                            <div class="stat-grid">
                                <div class="stat-box">
                                    <div class="stat-label">Kills</div>
                                    <div class="stat-value">${duo.kills || 0}</div>
                                </div>
                                <div class="stat-box">
                                    <div class="stat-label">Games</div>
                                    <div class="stat-value">${duo.gamesplayed || 0}</div>
                                </div>
                                <div class="stat-box">
                                    <div class="stat-label">K/D</div>
                                    <div class="stat-value">${duo.gamesplayed ? (duo.kills / duo.gamesplayed).toFixed(2) : '0'}</div>
                                </div>
                                <div class="stat-box">
                                    <div class="stat-label">Damage</div>
                                    <div class="stat-value">${detailed.damage || 0}</div>
                                </div>
                                <div class="stat-box">
                                    <div class="stat-label">Knockdowns</div>
                                    <div class="stat-value">${detailed.knockdown || 0}</div>
                                </div>
                                <div class="stat-box">
                                    <div class="stat-label">Pickups</div>
                                    <div class="stat-value">${detailed.pickups || 0}</div>
                                </div>
                            </div>
                        `;
                    }

                    if (stats.quadstats) {
                        const quad = stats.quadstats;
                        const detailed = quad.detailedstats || {};
                        html += `
                            <div class="section-title">👨‍👩‍👧‍👦 Squad Stats</div>
                            <div class="stat-grid">
                                <div class="stat-box">
                                    <div class="stat-label">Kills</div>
                                    <div class="stat-value">${quad.kills || 0}</div>
                                </div>
                                <div class="stat-box">
                                    <div class="stat-label">Wins</div>
                                    <div class="stat-value">${quad.wins || 0}</div>
                                </div>
                                <div class="stat-box">
                                    <div class="stat-label">Games</div>
                                    <div class="stat-value">${quad.gamesplayed || 0}</div>
                                </div>
                                <div class="stat-box">
                                    <div class="stat-label">Win Rate</div>
                                    <div class="stat-value">${quad.gamesplayed ? ((quad.wins / quad.gamesplayed) * 100).toFixed(1) : '0'}%</div>
                                </div>
                                <div class="stat-box">
                                    <div class="stat-label">Damage</div>
                                    <div class="stat-value">${detailed.damage || 0}</div>
                                </div>
                                <div class="stat-box">
                                    <div class="stat-label">Revives</div>
                                    <div class="stat-value">${detailed.revives || 0}</div>
                                </div>
                            </div>
                        `;
                    }

                    if (stats.csstats) {
                        const cs = stats.csstats;
                        const detailed = cs.detailedstats || {};
                        html += `
                            <div class="section-title">🎮 Clash Squad Stats</div>
                            <div class="stat-grid">
                                <div class="stat-box">
                                    <div class="stat-label">Kills</div>
                                    <div class="stat-value">${cs.kills || 0}</div>
                                </div>
                                <div class="stat-box">
                                    <div class="stat-label">Wins</div>
                                    <div class="stat-value">${cs.wins || 0}</div>
                                </div>
                                <div class="stat-box">
                                    <div class="stat-label">Games</div>
                                    <div class="stat-value">${cs.gamesplayed || 0}</div>
                                </div>
                                <div class="stat-box">
                                    <div class="stat-label">Win Rate</div>
                                    <div class="stat-value">${cs.gamesplayed ? ((cs.wins / cs.gamesplayed) * 100).toFixed(1) : '0'}%</div>
                                </div>
                                <div class="stat-box">
                                    <div class="stat-label">Damage</div>
                                    <div class="stat-value">${detailed.damage || 0}</div>
                                </div>
                                <div class="stat-box">
                                    <div class="stat-label">Headshots</div>
                                    <div class="stat-value">${detailed.headshotkills || 0}</div>
                                </div>
                            </div>
                            <div class="stat-grid">
                                <div class="stat-box">
                                    <div class="stat-label">Assists</div>
                                    <div class="stat-value">${detailed.assists || 0}</div>
                                </div>
                                <div class="stat-box">
                                    <div class="stat-label">Knockdowns</div>
                                    <div class="stat-value">${detailed.knockdowns || 0}</div>
                                </div>
                                <div class="stat-box">
                                    <div class="stat-label">Revivals</div>
                                    <div class="stat-value">${detailed.revivals || 0}</div>
                                </div>
                                <div class="stat-box">
                                    <div class="stat-label">MVP Count</div>
                                    <div class="stat-value">${detailed.mvpcount || 0}</div>
                                </div>
                                <div class="stat-box">
                                    <div class="stat-label">Double Kills</div>
                                    <div class="stat-value">${detailed.doublekills || 0}</div>
                                </div>
                                <div class="stat-box">
                                    <div class="stat-label">Triple Kills</div>
                                    <div class="stat-value">${detailed.triplekills || 0}</div>
                                </div>
                            </div>
                            <div class="stat-grid">
                                <div class="stat-box">
                                    <div class="stat-label">Rating Points</div>
                                    <div class="stat-value">${(detailed.ratingpoints || 0).toFixed(0)}</div>
                                </div>
                                <div class="stat-box">
                                    <div class="stat-label">Max Damage</div>
                                    <div class="stat-value">${detailed.onegamemostdamage || 0}</div>
                                </div>
                                <div class="stat-box">
                                    <div class="stat-label">Max Kills</div>
                                    <div class="stat-value">${detailed.onegamemostkills || 0}</div>
                                </div>
                                <div class="stat-box">
                                    <div class="stat-label">Streak Wins</div>
                                    <div class="stat-value">${detailed.streakwins || 0}</div>
                                </div>
                                <div class="stat-box">
                                    <div class="stat-label">Hit Count</div>
                                    <div class="stat-value">${detailed.hitcount || 0}</div>
                                </div>
                                <div class="stat-box">
                                    <div class="stat-label">Headshot %</div>
                                    <div class="stat-value">${detailed.hitcount ? ((detailed.headshotcount / detailed.hitcount) * 100).toFixed(1) : '0'}%</div>
                                </div>
                            </div>
                        `;
                    }

                    resultsContent.innerHTML = html || '<div class="placeholder-text">No stats available</div>';
                    errorMsg.classList.remove('show');
                } else {
                    showError('No stats data found');
                }
            } catch (err) {
                showError('Failed to fetch match stats: ' + err.message);
            } finally {
                setLoading(false);
            }
        }

        async function searchAccounts() {
            const keyword = keywordInput.value;
            const server = serverSelect.value;

            if (!keyword) {
                showError('Please enter a keyword');
                return;
            }

            setLoading(true);
            try {
                const response = await fetch(
                    `${API_BASE}/get_search_account_by_keyword?server=${server}&keyword=${keyword}`
                );
                const data = await response.json();

                if (data.infos && data.infos.length > 0) {
                    let html = '<div class="search-results">';
                    data.infos.forEach(player => {
                        html += `
                            <div class="search-result-item">
                                <div class="search-result-name">${player.nickname || 'Unknown'}</div>
                                <div class="search-result-info">
                                    <div class="info-row">
                                        <span>UID: ${player.accountid}</span>
                                        <span>Lvl ${player.level}</span>
                                    </div>
                                    <div class="info-row">
                                        <span>BR Rank: #${player.rank}</span>
                                        <span>CS Rank: #${player.csrank}</span>
                                    </div>
                                    <div class="info-row">
                                        <span>Liked: ${player.liked}</span>
                                        <span>Last Login: ${new Date(player.lastloginat * 1000).toLocaleDateString()}</span>
                                    </div>
                                </div>
                            </div>
                        `;
                    });
                    html += '</div>';
                    resultsContent.innerHTML = html;
                    errorMsg.classList.remove('show');
                } else {
                    resultsContent.innerHTML = '<div class="placeholder-text">No players found</div>';
                }
            } catch (err) {
                showError('Failed to search accounts: ' + err.message);
            } finally {
                setLoading(false);
            }
        }

        // Helper functions
        function setLoading(isLoading) {
            if (isLoading) {
                fetchBtn.innerHTML = '<span class="spinner"></span>Loading...';
                fetchBtn.disabled = true;
            } else {
                fetchBtn.innerHTML = 'Fetch Data';
                fetchBtn.disabled = false;
            }
        }

        function showError(message) {
            errorMsg.textContent = message;
            errorMsg.classList.add('show');
        }

        // Fetch button click handler
        fetchBtn.addEventListener('click', () => {
            if (currentTab === 'personal') {
                fetchPersonalStats();
            } else if (currentTab === 'matchstats') {
                fetchPlayerStats();
            } else if (currentTab === 'search') {
                searchAccounts();
            }
        });

        // Enter key support
        uidInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter' && currentTab !== 'search') {
                fetchBtn.click();
            }
        });

        keywordInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter' && currentTab === 'search') {
                fetchBtn.click();
            }
        });
    </script>
</body>
</html>
    """

@app.route('/get_search_account_by_keyword', methods=['GET'])
def get_search_account_by_keyword():
    try:
        # Get request parameters
        region = request.args.get('server', 'IND').upper()
        search_term = request.args.get('keyword')
        
        # Validate keyword parameter
        if not search_term:
            return json.dumps({"error": "Keyword parameter is required"}, indent=2), 400, {'Content-Type': 'application/json; charset=utf-8'}
        
        # Enforce minimum keyword length
        if len(search_term.strip()) < 3:
            return json.dumps({"error": "Keyword must be at least 3 characters long"}, indent=2), 400, {'Content-Type': 'application/json; charset=utf-8'}
        
        # Validate server exists in accounts
        if region not in accounts:
            return json.dumps({"error": f"Invalid server: {region}"}, indent=2), 400, {'Content-Type': 'application/json; charset=utf-8'}
        
        # Authenticate with Garena
        auth_response = get_garena_token(accounts[region]['uid'], accounts[region]['password'])
        if not auth_response or 'access_token' not in auth_response:
            return json.dumps({"error": "Authentication failed"}, indent=2), 401, {'Content-Type': 'application/json; charset=utf-8'}
        
        # Get major login credentials
        login_response = get_major_login(auth_response["access_token"], auth_response["open_id"])
        if not login_response or 'token' not in login_response:
            return json.dumps({"error": "Major login failed"}, indent=2), 401, {'Content-Type': 'application/json; charset=utf-8'}
        
        # Search for accounts
        search_results = search_account_by_keyword(login_response["serverUrl"], login_response["token"], search_term)
        
        # Return formatted response
        formatted_response = json.dumps(search_results, indent=2, ensure_ascii=False)
        return formatted_response, 200, {'Content-Type': 'application/json; charset=utf-8'}
        
    except KeyError as e:
        return json.dumps({"error": f"Missing configuration: {str(e)}"}, indent=2), 500, {'Content-Type': 'application/json; charset=utf-8'}
    except Exception as e:
        return json.dumps({"error": f"Internal server error: {str(e)}"}, indent=2), 500, {'Content-Type': 'application/json; charset=utf-8'}

@app.route('/get_player_stats', methods=['GET'])
def get_player_stat():
    try:
        # Get and validate parameters
        server = request.args.get('server', 'IND').upper()
        uid = request.args.get('uid')
        gamemode = request.args.get('gamemode', 'br').lower()
        matchmode = request.args.get('matchmode', 'CAREER').upper()

        # Validate required parameters
        if not uid:
            return jsonify({
                "success": False,
                "error": "Missing required parameter",
                "message": "UID parameter is required"
            }), 400

        if not uid.isdigit():
            return jsonify({
                "success": False,
                "error": "Invalid UID",
                "message": "UID must be a numeric value"
            }), 400

        # Validate server
        if server not in accounts:
            return jsonify({
                "success": False,
                "error": "Invalid server",
                "message": f"Server '{server}' not found. Available servers: {list(accounts.keys())}"
            }), 400

        # Validate gamemode
        if gamemode not in ['br', 'cs']:
            return jsonify({
                "success": False,
                "error": "Invalid gamemode",
                "message": "Gamemode must be 'br' or 'cs'"
            }), 400

        # Validate matchmode
        if matchmode not in ['CAREER', 'NORMAL', 'RANKED']:
            return jsonify({
                "success": False,
                "error": "Invalid matchmode",
                "message": "Matchmode must be 'CAREER', 'NORMAL', or 'RANKED'"
            }), 400

        # Step 1: Get Garena token
        try:
            garena_token_result = get_garena_token(accounts[server]['uid'], accounts[server]['password'])
            
            if not garena_token_result or 'access_token' not in garena_token_result:
                return jsonify({
                    "success": False,
                    "error": "Garena authentication failed",
                    "message": "Failed to obtain Garena access token"
                }), 401
                
        except Exception as e:
            return jsonify({
                "success": False,
                "error": "Garena authentication error",
                "message": f"Failed to authenticate with Garena: {str(e)}"
            }), 502

        # Step 2: Get Major login
        try:
            major_login_result = get_major_login(garena_token_result["access_token"], garena_token_result["open_id"])
            
            if not major_login_result or 'token' not in major_login_result:
                return jsonify({
                    "success": False,
                    "error": "Major login failed",
                    "message": "Failed to obtain Major login token"
                }), 401
                
        except Exception as e:
            return jsonify({
                "success": False,
                "error": "Major login error",
                "message": f"Failed to login to Major: {str(e)}"
            }), 502

        # Step 3: Get player stats
        try:
            player_stats = get_player_stats(
                major_login_result["token"], 
                major_login_result["serverUrl"], 
                gamemode, 
                uid, 
                matchmode
            )
            
            if not player_stats:
                return jsonify({
                    "success": False,
                    "error": "No stats data",
                    "message": "No player statistics found for the given parameters"
                }), 404

            # Return formatted JSON response
            return jsonify({
                "success": True,
                "data": player_stats,
                "metadata": {
                    "server": server,
                    "uid": uid,
                    "gamemode": gamemode,
                    "matchmode": matchmode
                }
            }), 200
            
        except ValueError as e:
            return jsonify({
                "success": False,
                "error": "Invalid request parameters",
                "message": str(e)
            }), 400
        except ConnectionError as e:
            return jsonify({
                "success": False,
                "error": "Connection error",
                "message": str(e)
            }), 503
        except ProtobufError as e:
            return jsonify({
                "success": False,
                "error": "Data processing error",
                "message": str(e)
            }), 500
        except APIError as e:
            return jsonify({
                "success": False,
                "error": "External API error",
                "message": str(e)
            }), 502
        except Exception as e:
            return jsonify({
                "success": False,
                "error": "Stats retrieval error",
                "message": f"Failed to retrieve player stats: {str(e)}"
            }), 500

    except Exception as e:
        # Catch any unexpected errors
        return jsonify({
            "success": False,
            "error": "Internal server error",
            "message": "An unexpected error occurred while processing your request"
        }), 500

@app.route('/get_player_personal_show', methods=['GET'])
def get_account_info():
    try:
        # Get parameters with defaults
        server = request.args.get('server', 'IND').upper()
        uid = request.args.get('uid')
        need_gallery_info = request.args.get('need_gallery_info', False)
        call_sign_src = request.args.get('call_sign_src', 7)
        
        # Validate UID parameter - must be integer
        if not uid:
            response = {
                "status": "error",
                "error": "Missing UID",
                "message": "Empty 'uid' parameter. Please provide a valid 'uid'.",
                "code": "MISSING_UID"
            }
            return jsonify(response), 400, {'Content-Type': 'application/json; charset=utf-8'}
        
        # Check if UID is a valid integer
        try:
            uid_int = int(uid)
            # Additional validation for UID range if needed
            if uid_int <= 0:
                response = {
                    "status": "error",
                    "error": "Invalid UID",
                    "message": "UID must be a positive integer.",
                    "code": "INVALID_UID_RANGE"
                }
                return jsonify(response), 400, {'Content-Type': 'application/json; charset=utf-8'}
        except (ValueError, TypeError):
            response = {
                "status": "error",
                "error": "Invalid UID",
                "message": "UID must be a valid integer.",
                "code": "INVALID_UID_FORMAT"
            }
            return jsonify(response), 400, {'Content-Type': 'application/json; charset=utf-8'}
        
        # Validate server parameter
        if server not in accounts:
            response = {
                "status": "error",
                "error": "Invalid Server",
                "message": f"Server '{server}' not found. Available servers: {list(accounts.keys())}",
                "available_servers": list(accounts.keys()),
                "code": "SERVER_NOT_FOUND"
            }
            return jsonify(response), 400, {'Content-Type': 'application/json; charset=utf-8'}
        
        # Validate need_gallery_info parameter
        try:
            if isinstance(need_gallery_info, str):
                if need_gallery_info.lower() in ['true', '1', 'yes']:
                    need_gallery_info = True
                elif need_gallery_info.lower() in ['false', '0', 'no']:
                    need_gallery_info = False
                else:
                    raise ValueError("Invalid boolean value")
            need_gallery_info = bool(need_gallery_info)
        except (ValueError, TypeError):
            response = {
                "status": "error",
                "error": "Invalid Parameter",
                "message": "need_gallery_info must be a boolean value (true/false, 1/0).",
                "code": "INVALID_GALLERY_PARAM"
            }
            return jsonify(response), 400, {'Content-Type': 'application/json; charset=utf-8'}
        
        # Validate call_sign_src parameter
        try:
            call_sign_src_int = int(call_sign_src)
            if call_sign_src_int < 0:
                response = {
                    "status": "error",
                    "error": "Invalid Parameter",
                    "message": "call_sign_src must be a non-negative integer.",
                    "code": "INVALID_CALL_SIGN_SRC"
                }
                return jsonify(response), 400, {'Content-Type': 'application/json; charset=utf-8'}
        except (ValueError, TypeError):
            response = {
                "status": "error",
                "error": "Invalid Parameter",
                "message": "call_sign_src must be a valid integer.",
                "code": "INVALID_CALL_SIGN_FORMAT"
            }
            return jsonify(response), 400, {'Content-Type': 'application/json; charset=utf-8'}
        
        # Check if server account credentials exist
        if 'uid' not in accounts[server] or 'password' not in accounts[server]:
            response = {
                "status": "error",
                "error": "Server Configuration Error",
                "message": f"Server '{server}' is missing required credentials.",
                "code": "SERVER_CONFIG_ERROR"
            }
            return jsonify(response), 500, {'Content-Type': 'application/json; charset=utf-8'}
        
        # Step 1: Get Garena token
        garena_token_result = get_garena_token(accounts[server]['uid'], accounts[server]['password'])
        if not garena_token_result or 'access_token' not in garena_token_result or 'open_id' not in garena_token_result:
            response = {
                "status": "error",
                "error": "Authentication Failed",
                "message": "Failed to obtain Garena token. Invalid credentials or service unavailable.",
                "code": "GARENA_AUTH_FAILED"
            }
            return jsonify(response), 401, {'Content-Type': 'application/json; charset=utf-8'}
        
        # Step 2: Get major login
        major_login_result = get_major_login(garena_token_result["access_token"], garena_token_result["open_id"])
        if not major_login_result or 'serverUrl' not in major_login_result or 'token' not in major_login_result:
            response = {
                "status": "error",
                "error": "Login Failed",
                "message": "Failed to perform major login. Service unavailable.",
                "code": "MAJOR_LOGIN_FAILED"
            }
            return jsonify(response), 401, {'Content-Type': 'application/json; charset=utf-8'}
        
        # Step 3: Get player personal show data
        player_personal_show_result = get_player_personal_show(
            major_login_result["serverUrl"], 
            major_login_result["token"], 
            uid_int, 
            need_gallery_info, 
            call_sign_src_int
        )

        if not player_personal_show_result:
            response = {
                "status": "error",
                "error": "Data Not Found",
                "message": f"No player data found for UID: {uid_int}",
                "code": "PLAYER_DATA_NOT_FOUND"
            }
            return jsonify(response), 404, {'Content-Type': 'application/json; charset=utf-8'}
        
        # Success response
        formatted_json = json.dumps(player_personal_show_result, indent=2, ensure_ascii=False)
        return formatted_json, 200, {'Content-Type': 'application/json; charset=utf-8'}
    
    except Exception as e:
        # Log the unexpected error for debugging
        print(f"Unexpected error in get_player_personal_show: {str(e)}")
        print(f"Error type: {type(e).__name__}")
        import traceback
        print(f"Traceback: {traceback.format_exc()}")
        
        response = {
            "status": "error",
            "error": "Internal Server Error",
            "message": "An unexpected error occurred while processing your request.",
            "code": "INTERNAL_SERVER_ERROR"
        }
        return jsonify(response), 500, {'Content-Type': 'application/json; charset=utf-8'}



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)