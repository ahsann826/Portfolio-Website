import os
from PIL import Image, ImageDraw, ImageFont

os.makedirs("images/work/preplit", exist_ok=True)
os.makedirs("images/work/campusrank", exist_ok=True)
os.makedirs("images/work/resumate", exist_ok=True)
os.makedirs("images/work/covenant", exist_ok=True)
os.makedirs("images/work/automation", exist_ok=True)
os.makedirs("images/work/textvision", exist_ok=True)

def get_font(size, bold=False, mono=False):
    try:
        if mono:
            return ImageFont.truetype("C:/Windows/Fonts/consola.ttf", size)
        if bold:
            return ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", size)
        return ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", size)
    except:
        return ImageFont.load_default()

def draw_window_frame(draw, width, height, title="Application", dark=True):
    bg_color = (18, 18, 20) if dark else (248, 248, 246)
    card_color = (28, 28, 32) if dark else (255, 255, 255)
    border_color = (48, 48, 56) if dark else (225, 225, 225)
    text_color = (230, 230, 230) if dark else (30, 30, 30)
    muted_color = (130, 130, 140) if dark else (140, 140, 140)

    # Base background
    draw.rectangle([0, 0, width, height], fill=bg_color)
    
    # Outer frame
    pad = 40
    top = 40
    draw.rounded_rectangle([pad, top, width - pad, height - pad], radius=16, fill=card_color, outline=border_color, width=1)
    
    # Title bar
    header_h = 44
    draw.line([pad, top + header_h, width - pad, top + header_h], fill=border_color, width=1)
    
    # Window controls
    dot_r = 6
    dot_y = top + 22
    draw.ellipse([pad + 20, dot_y - dot_r, pad + 20 + dot_r * 2, dot_y + dot_r], fill=(255, 95, 87))
    draw.ellipse([pad + 38, dot_y - dot_r, pad + 38 + dot_r * 2, dot_y + dot_r], fill=(254, 188, 46))
    draw.ellipse([pad + 56, dot_y - dot_r, pad + 56 + dot_r * 2, dot_y + dot_r], fill=(40, 200, 64))

    # Title text
    f_title = get_font(13, mono=True)
    draw.text((pad + 90, top + 14), title, fill=muted_color, font=f_title)
    
    return pad, top + header_h, width - pad, height - pad

def create_preplit_mockups():
    # 1. Main Workspace
    im = Image.new("RGB", (1600, 1000), (15, 15, 18))
    draw = ImageDraw.Draw(im)
    l, t, r, b = draw_window_frame(draw, 1600, 1000, "Preplit AI — AI-Powered Workspace • preplitai.com", dark=True)
    
    sw = 260
    draw.rectangle([l, t, l + sw, b], fill=(22, 22, 26))
    draw.line([l + sw, t, l + sw, b], fill=(40, 40, 48), width=1)
    
    f_bold = get_font(18, bold=True)
    f_sub = get_font(13)
    f_mono = get_font(12, mono=True)
    f_head = get_font(28, bold=True)
    
    draw.text((l + 24, t + 24), "PREPLIT WORKSPACE", fill=(255, 255, 255), font=f_bold)
    draw.text((l + 24, t + 50), "v2.4.0 • Active Workspace", fill=(120, 120, 130), font=f_mono)
    
    items = ["Study Copilot", "Note Intelligence", "Lecture Transcripts", "Flashcard Generator", "RAG Document Index", "Settings"]
    for i, item in enumerate(items):
        bg_i = (38, 38, 48) if i == 0 else (22, 22, 26)
        txt_i = (255, 255, 255) if i == 0 else (160, 160, 170)
        draw.rounded_rectangle([l + 16, t + 90 + i * 44, l + sw - 16, t + 126 + i * 44], radius=6, fill=bg_i)
        draw.text((l + 32, t + 100 + i * 44), item, fill=txt_i, font=f_sub)
    
    cx = l + sw + 30
    draw.text((cx, t + 30), "Advanced Distributed Systems — Exam Synthesizer", fill=(255, 255, 255), font=f_head)
    draw.text((cx, t + 70), "Synthesizing 4 lectures, 18 PDF notes, and past exam questions into structured study blocks.", fill=(160, 160, 175), font=get_font(15))
    
    cards = [
        ("AI TUTOR ACCURACY", "99.4%", "+2.1% from baseline", (80, 200, 120)),
        ("DOCUMENTS INDEXED", "148 Files", "pgvector / 1536 dim", (100, 180, 255)),
        ("ACTIVE STUDY STREAK", "24 Days", "Top 1% Ajou Cohort", (255, 180, 80))
    ]
    cw = (r - cx - 60) // 3
    for i, (title, val, meta, color) in enumerate(cards):
        x1 = cx + i * (cw + 20)
        x2 = x1 + cw
        draw.rounded_rectangle([x1, t + 110, x2, t + 220], radius=10, fill=(24, 24, 30), outline=(45, 45, 55), width=1)
        draw.text((x1 + 18, t + 126), title, fill=(140, 140, 150), font=f_mono)
        draw.text((x1 + 18, t + 150), val, fill=(255, 255, 255), font=get_font(32, bold=True))
        draw.text((x1 + 18, t + 192), meta, fill=color, font=f_mono)

    draw.rounded_rectangle([cx, t + 245, r - 30, b - 30], radius=12, fill=(20, 20, 24), outline=(42, 42, 50), width=1)
    draw.text((cx + 24, t + 270), "PROMPT CONTEXT & REAL-TIME REASONING PIPELINE", fill=(140, 140, 160), font=f_mono)
    
    code_lines = [
        ">> Query: 'Explain the difference between Raft Consensus and Paxos state machines.'",
        ">> Retrieval: Found 4 matching vectors in Ajou_CS402_Lecture_08.pdf [Cosine Similarity: 0.941]",
        ">> Synthesizing multi-agent response with LangChain + Anthropic Claude 3.5 Sonnet pipeline...",
        "",
        "[AI Tutor Output]:",
        "  1. Leader Election: Raft uses randomized timers to ensure strong leadership consistency.",
        "  2. Log Replication: Raft enforces an append-only log with strict index and term verification.",
        "  3. Correctness Proof: Reduces state space complexity significantly compared to multi-decree Paxos.",
        "",
        ">> Generated 6 interactive quiz questions with LaTeX equations for formula review."
    ]
    for idx, line in enumerate(code_lines):
        color = (100, 210, 140) if ">>" in line else ((255, 255, 255) if "[AI" in line else (200, 200, 210))
        draw.text((cx + 24, t + 305 + idx * 24), line, fill=color, font=f_mono)
    
    im.save("images/work/preplit/1.jpg", quality=92)

    # 2. Agentic Tutoring Pipeline
    im2 = Image.new("RGB", (1600, 1000), (12, 12, 15))
    draw2 = ImageDraw.Draw(im2)
    l, t, r, b = draw_window_frame(draw2, 1600, 1000, "Preplit AI — Multi-Agent Architecture & RAG Flow", dark=True)
    draw2.text((l + 40, t + 35), "AI TUTORING AGENT PIPELINE", fill=(255, 255, 255), font=get_font(28, bold=True))
    draw2.text((l + 40, t + 75), "System Architecture: RAG • Hybrid Vector Search • Automated Verification", fill=(150, 150, 160), font=get_font(15))
    
    steps = [
        ("01", "INGESTION & CHUNKING", "PDF / Markdown / OCR Parsing\nSemantic token chunking (512 tokens)\nMetadata extraction & source tagging"),
        ("02", "VECTOR EMBEDDINGS", "OpenAI text-embedding-3-large\nSupabase pgvector indexed (HNSW)\nCosine distance search < 12ms"),
        ("03", "AGENT ORCHESTRATION", "LangGraph state machine\nRouting between Tutor, Solver, Quizzer\nCross-validation of references"),
        ("04", "STREAMING UI", "Next.js App Router streaming SSR\nReal-time KaTeX math rendering\nInteractive flashcard compilation")
    ]
    sw = (r - l - 80 - 60) // 4
    for i, (num, title, body) in enumerate(steps):
        x1 = l + 40 + i * (sw + 20)
        x2 = x1 + sw
        draw2.rounded_rectangle([x1, t + 130, x2, t + 420], radius=12, fill=(24, 24, 30), outline=(50, 50, 62), width=1)
        draw2.text((x1 + 20, t + 155), num, fill=(120, 180, 255), font=get_font(36, bold=True))
        draw2.text((x1 + 20, t + 210), title, fill=(255, 255, 255), font=get_font(15, bold=True))
        draw2.text((x1 + 20, t + 245), body, fill=(170, 170, 185), font=get_font(13))
        
    draw2.rounded_rectangle([l + 40, t + 450, r - 40, b - 40], radius=12, fill=(18, 18, 22), outline=(42, 42, 52), width=1)
    draw2.text((l + 65, t + 475), "LIVE TELEMETRY & LATENCY BENCHMARKS", fill=(140, 140, 150), font=get_font(13, mono=True))
    benchmarks = [
        "Chunk Retrieval: 18.4ms", "Vector Match Score: 0.963", "Time to First Token: 142ms",
        "Total Pipeline Round-Trip: 640ms", "Cache Hit Ratio: 88.2%", "Zero Hallucination Guardrail: Verified"
    ]
    for idx, bm in enumerate(benchmarks):
        row = idx // 3
        col = idx % 3
        draw2.text((l + 65 + col * 480, t + 520 + row * 45), f"✔ {bm}", fill=(100, 220, 160), font=get_font(14, mono=True))
        
    im2.save("images/work/preplit/2.jpg", quality=92)

    for num, subtitle, highlight in [
        (3, "RAG Knowledge Synthesis & pgvector Semantic Index", "98.4% Semantic Retrieval Accuracy"),
        (4, "Dynamic Academic Flashcards & Spaced Repetition", "FSRS Algorithm Integration"),
        (5, "Collaborative Course Workspace & Exam Prep Analytics", "Real-time Multi-User Sync via Supabase")
    ]:
        im_n = Image.new("RGB", (1600, 1000), (16, 16, 20))
        d_n = ImageDraw.Draw(im_n)
        l, t, r, b = draw_window_frame(d_n, 1600, 1000, f"Preplit AI — {subtitle}", dark=True)
        d_n.text((l + 40, t + 40), "PREPLIT AI PRODUCT DEMO", fill=(130, 130, 145), font=get_font(13, mono=True))
        d_n.text((l + 40, t + 70), subtitle, fill=(255, 255, 255), font=get_font(32, bold=True))
        d_n.rounded_rectangle([l + 40, t + 140, r - 40, b - 40], radius=14, fill=(24, 24, 30), outline=(50, 50, 62), width=1)
        d_n.text((l + 70, t + 180), highlight, fill=(100, 200, 255), font=get_font(24, bold=True))
        d_n.text((l + 70, t + 230), "Built with Next.js 15, TypeScript, Tailwind CSS, OpenAI / Anthropic APIs, and Supabase pgvector.", fill=(180, 180, 195), font=get_font(16))
        for k in range(4):
            kx1 = l + 70 + k * 340
            kx2 = kx1 + 310
            d_n.rounded_rectangle([kx1, t + 290, kx2, t + 460], radius=8, fill=(32, 32, 40), outline=(60, 60, 75), width=1)
            d_n.text((kx1 + 16, t + 310), f"Metric #{k+1}", fill=(150, 150, 160), font=get_font(12, mono=True))
            d_n.text((kx1 + 16, t + 340), f"{94 + k * 1.5:.1f}%", fill=(255, 255, 255), font=get_font(30, bold=True))
            d_n.text((kx1 + 16, t + 395), "Optimized for latency", fill=(100, 220, 150), font=get_font(12))
        im_n.save(f"images/work/preplit/{num}.jpg", quality=92)

create_preplit_mockups()

def create_campusrank_mockups():
    for num, subtitle, tag in [
        (1, "Global University Leaderboard & Competitive Scoring", "Ajou University #1 Regional Rank"),
        (2, "Verified Student Profile & Skill Evaluation Badges", "Full-Stack • AI/ML • Algorithmic Rank"),
        (3, "Inter-University Hackathons & Real-time Live Matches", "Active Collegiate League"),
        (4, "Global Rankings Explorer with Country & Major Filters", "450+ Universities Indexed"),
        (5, "Performance Percentile & Academic Analytics Dashboard", "Top 0.5% Competitive Tier")
    ]:
        im = Image.new("RGB", (1600, 1000), (14, 16, 22))
        draw = ImageDraw.Draw(im)
        l, t, r, b = draw_window_frame(draw, 1600, 1000, f"CampusRank — {subtitle} • campusrank-ruby.vercel.app", dark=True)
        
        draw.text((l + 40, t + 30), "CAMPUSRANK PLATFORM", fill=(255, 100, 100), font=get_font(13, mono=True))
        draw.text((l + 40, t + 58), subtitle, fill=(255, 255, 255), font=get_font(30, bold=True))
        
        draw.rounded_rectangle([l + 40, t + 120, r - 40, b - 40], radius=12, fill=(20, 24, 34), outline=(44, 52, 70), width=1)
        
        headers = ["RANK", "UNIVERSITY / COHORT", "COUNTRY", "TOTAL SCORE", "WEEKLY CHANGE", "STATUS"]
        hx = [l + 60, l + 140, l + 580, l + 800, l + 1020, l + 1260]
        for idx, h in enumerate(headers):
            draw.text((hx[idx], t + 145), h, fill=(120, 140, 170), font=get_font(12, mono=True))
            
        draw.line([l + 40, t + 180, r - 40, t + 180], fill=(44, 52, 70), width=1)
        
        rows = [
            ("#01", "Ajou University (Software Engineering)", "South Korea", "9,840 pts", "+340 pts (↑ 2)", "LEADER"),
            ("#02", "Seoul National University (SNU)", "South Korea", "9,710 pts", "+120 pts (↑ 1)", "CHALLENGER"),
            ("#03", "KAIST (Computer Science)", "South Korea", "9,650 pts", "-40 pts (↓ 1)", "CHALLENGER"),
            ("#04", "Korea University", "South Korea", "9,320 pts", "+190 pts (↑ 3)", "CONTENDER"),
            ("#05", "Yonsei University", "South Korea", "9,180 pts", "+80 pts (—)", "CONTENDER"),
            ("#06", "POSTECH", "South Korea", "9,040 pts", "+15 pts (—)", "CONTENDER"),
            ("#07", "Sungkyunkwan University (SKKU)", "South Korea", "8,920 pts", "-60 pts (↓ 2)", "CONTENDER")
        ]
        for r_idx, row in enumerate(rows):
            ry = t + 200 + r_idx * 56
            is_top = (r_idx == 0)
            if is_top:
                draw.rounded_rectangle([l + 46, ry - 6, r - 46, ry + 42], radius=6, fill=(30, 38, 54))
            draw.text((hx[0], ry + 8), row[0], fill=(255, 215, 0) if is_top else (200, 210, 225), font=get_font(15, bold=True))
            draw.text((hx[1], ry + 8), row[1], fill=(255, 255, 255) if is_top else (220, 225, 235), font=get_font(15, bold=is_top))
            draw.text((hx[2], ry + 8), row[2], fill=(160, 175, 195), font=get_font(14))
            draw.text((hx[3], ry + 8), row[3], fill=(100, 210, 255), font=get_font(15, mono=True))
            draw.text((hx[4], ry + 8), row[4], fill=(100, 220, 140) if "↑" in row[4] else (255, 120, 120), font=get_font(13))
            draw.text((hx[5], ry + 8), row[5], fill=(255, 190, 80) if is_top else (140, 155, 175), font=get_font(12, mono=True))
            draw.line([l + 40, ry + 48, r - 40, ry + 48], fill=(35, 42, 58), width=1)
            
        im.save(f"images/work/campusrank/{num}.jpg", quality=92)

create_campusrank_mockups()

def create_resumate_mockups():
    for num, subtitle, tag in [
        (1, "AI Deep Resume Analysis & ATS Score Optimization", "98% ATS Pass Rate"),
        (2, "Real-Time AI Suggestion Engine & Action Verbs", "Grammar & Impact Analytics"),
        (3, "Role Alignment Matrix & Skill Gap Scoring", "Full-Stack / AI Engineer Target"),
        (4, "Live Interactive CV Preview & Export Studio", "PDF & Markdown Sync"),
        (5, "Interview Callback Probability Predictor", "Trained on 5,000+ Profiles")
    ]:
        im = Image.new("RGB", (1600, 1000), (16, 18, 16))
        draw = ImageDraw.Draw(im)
        l, t, r, b = draw_window_frame(draw, 1600, 1000, f"Resumate — {subtitle} • resumate-ai-lake.vercel.app", dark=True)
        
        draw.text((l + 40, t + 30), "RESUMATE AI PLATFORM", fill=(80, 220, 140), font=get_font(13, mono=True))
        draw.text((l + 40, t + 58), subtitle, fill=(255, 255, 255), font=get_font(30, bold=True))
        
        mid_x = l + 520
        draw.rounded_rectangle([l + 40, t + 120, mid_x - 20, b - 40], radius=10, fill=(240, 240, 238), outline=(200, 200, 200), width=1)
        draw.text((l + 65, t + 145), "KHAN MUHAMMAD AHSAN", fill=(20, 20, 20), font=get_font(18, bold=True))
        draw.text((l + 65, t + 175), "Software Engineer • Suwon, South Korea", fill=(80, 80, 80), font=get_font(12))
        draw.line([l + 65, t + 195, mid_x - 45, t + 195], fill=(210, 210, 210), width=1)
        
        cv_text = [
            "EDUCATION", "Ajou University — Global Korea Scholarship Recipient",
            "EXPERIENCE", "Preplit AI — CEO & Full-Stack Lead Developer",
            "• Architected AI tutoring pipelines with Next.js & TypeScript",
            "• Scaled pgvector semantic search with 99.4% recall rate",
            "CampusRank — Founder & Architect",
            "• Developed global student competitive leaderboard platform",
            "SKILLS & TECH", "Python, TypeScript, React, Next.js, Docker, Supabase, Azure"
        ]
        for c_i, line in enumerate(cv_text):
            is_bold = ("EDUCATION" in line or "EXPERIENCE" in line or "SKILLS" in line)
            color = (30, 30, 30) if is_bold else (70, 70, 80)
            draw.text((l + 65, t + 215 + c_i * 28), line, fill=color, font=get_font(12, bold=is_bold))
            
        draw.rounded_rectangle([mid_x, t + 120, r - 40, b - 40], radius=10, fill=(24, 28, 24), outline=(45, 55, 45), width=1)
        
        draw.rounded_rectangle([mid_x + 30, t + 150, mid_x + 230, t + 270], radius=8, fill=(32, 42, 32), outline=(60, 90, 60), width=1)
        draw.text((mid_x + 50, t + 165), "ATS MATCH SCORE", fill=(140, 180, 140), font=get_font(12, mono=True))
        draw.text((mid_x + 50, t + 190), "96 / 100", fill=(80, 240, 140), font=get_font(38, bold=True))
        draw.text((mid_x + 50, t + 242), "Top 2% of applicants", fill=(180, 220, 180), font=get_font(12))
        
        draw.rounded_rectangle([mid_x + 250, t + 150, r - 70, t + 270], radius=8, fill=(30, 36, 30), outline=(50, 65, 50), width=1)
        draw.text((mid_x + 270, t + 165), "CALLBACK PROBABILITY", fill=(140, 180, 140), font=get_font(12, mono=True))
        draw.text((mid_x + 270, t + 190), "89.2%", fill=(255, 255, 255), font=get_font(38, bold=True))
        draw.text((mid_x + 270, t + 242), "+42% vs generic resumes", fill=(100, 220, 150), font=get_font(12))
        
        draw.text((mid_x + 30, t + 300), "ACTIONABLE OPTIMIZATIONS FOUND (4)", fill=(200, 220, 200), font=get_font(15, bold=True))
        
        opts = [
            ("Impact Quantification", "Preplit AI experience: Add numeric metrics to AI pipeline throughput.", "+12 pts"),
            ("Keyword Density", "Strong alignment for 'Next.js', 'pgvector', and 'LLM API integration'.", "Verified"),
            ("Action Verbs", "Replaced 'Worked on' with 'Architected' and 'Spearheaded'.", "Optimized"),
            ("Brevity & Layout", "Passed single-page executive standard scan without formatting overflow.", "Passed")
        ]
        for o_i, (t_opt, d_opt, s_opt) in enumerate(opts):
            oy = t + 335 + o_i * 64
            draw.rounded_rectangle([mid_x + 30, oy, r - 70, oy + 52], radius=6, fill=(28, 34, 28), outline=(48, 58, 48), width=1)
            draw.text((mid_x + 46, oy + 8), t_opt, fill=(255, 255, 255), font=get_font(14, bold=True))
            draw.text((mid_x + 46, oy + 28), d_opt, fill=(150, 170, 150), font=get_font(12))
            draw.text((r - 170, oy + 16), s_opt, fill=(80, 220, 140), font=get_font(12, mono=True))
            
        im.save(f"images/work/resumate/{num}.jpg", quality=92)

create_resumate_mockups()

def create_covenant_mockups():
    for num, subtitle, tag in [
        (1, "Minimalist Watch Storefront & E-Commerce Catalog", "100,000+ Visitors"),
        (2, "B2B Horology Supply Chain & Sourcing Network", "China / South Korea Operations"),
        (3, "Brand Identity & Editorial Photography Showcase", "Luxury Minimal Aesthetic"),
        (4, "High-Converting Checkout & Customer Acquisition", "B2B & D2C Sales Funnel"),
        (5, "Product Architecture & Quality Inspection Standards", "Sapphire & Stainless Steel")
    ]:
        im = Image.new("RGB", (1600, 1000), (22, 22, 22))
        draw = ImageDraw.Draw(im)
        l, t, r, b = draw_window_frame(draw, 1600, 1000, f"Covenant & Co — {subtitle}", dark=True)
        
        draw.text((l + 40, t + 30), "COVENANT & CO. HOROLOGY", fill=(210, 190, 150), font=get_font(13, mono=True))
        draw.text((l + 40, t + 58), subtitle, fill=(255, 255, 255), font=get_font(30, bold=True))
        
        draw.rounded_rectangle([l + 40, t + 120, r - 40, b - 40], radius=10, fill=(28, 28, 28), outline=(50, 50, 50), width=1)
        
        cx = (l + r) // 2
        cy = (t + b) // 2 + 30
        draw.ellipse([cx - 160, cy - 160, cx + 160, cy + 160], fill=(20, 20, 20), outline=(210, 190, 150), width=3)
        draw.ellipse([cx - 145, cy - 145, cx + 145, cy + 145], fill=(24, 24, 24), outline=(70, 70, 70), width=1)
        
        draw.line([cx, cy, cx + 70, cy - 50], fill=(210, 190, 150), width=4)
        draw.line([cx, cy, cx - 40, cy + 60], fill=(255, 255, 255), width=2)
        draw.ellipse([cx - 6, cy - 6, cx + 6, cy + 6], fill=(210, 190, 150))
        
        draw.text((cx - 50, cy - 60), "COVENANT", fill=(210, 190, 150), font=get_font(14, mono=True))
        draw.text((cx - 45, cy + 40), "AUTOMATIC", fill=(140, 140, 140), font=get_font(10, mono=True))
        
        draw.text((l + 70, t + 160), "SPECIFICATIONS & METRICS", fill=(150, 150, 150), font=get_font(13, mono=True))
        specs = [
            "• Sourced across premier Chinese manufacturing partners",
            "• 100,000+ organic visitors generated",
            "• Precision 316L Stainless Steel casing",
            "• Direct-to-consumer & B2B procurement agreements"
        ]
        for s_i, sp in enumerate(specs):
            draw.text((l + 70, t + 200 + s_i * 35), sp, fill=(220, 220, 220), font=get_font(15))
            
        im.save(f"images/work/covenant/{num}.jpg", quality=92)

create_covenant_mockups()

def create_automation_mockups():
    for num, subtitle, tag in [
        (1, "OpenCV Computer Vision & Screen Detection Engine", "Sub-pixel Accuracy"),
        (2, "Autonomous Multi-Threaded State Machine Logic", "Fault-tolerant Recovery"),
        (3, "Automated Pathfinding & Movement Navigation", "A* & Heuristic Routing"),
        (4, "Real-time Telemetry & Game State OCR Logs", "10,000+ Operating Hours"),
        (5, "Performance Benchmarks & Anti-Detection Automation", "Human-like Jitter Simulation")
    ]:
        im = Image.new("RGB", (1600, 1000), (12, 14, 18))
        draw = ImageDraw.Draw(im)
        l, t, r, b = draw_window_frame(draw, 1600, 1000, f"Python Automation Suite — {subtitle}", dark=True)
        
        draw.text((l + 40, t + 30), "COMPUTER VISION ENGINE • PYTHON / OPENCV", fill=(80, 180, 255), font=get_font(13, mono=True))
        draw.text((l + 40, t + 58), subtitle, fill=(255, 255, 255), font=get_font(30, bold=True))
        
        draw.rounded_rectangle([l + 40, t + 120, r - 40, b - 40], radius=10, fill=(18, 22, 28), outline=(40, 50, 65), width=1)
        
        code = [
            "import cv2, pyautogui, numpy as np",
            "",
            "def detect_game_state(frame):",
            "    # Match multi-scale templates across screen buffer",
            "    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)",
            "    res = cv2.matchTemplate(gray, state_template, cv2.TM_CCOEFF_NORMED)",
            "    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)",
            "    if max_val > 0.92:",
            "        cv2.rectangle(frame, max_loc, (max_loc[0]+w, max_loc[1]+h), (0, 255, 0), 2)",
            "        trigger_autonomous_action(state='ENCOUNTER_RESOLVE')",
            "    return frame",
            "",
            "[System Active]: Real-time capture @ 60 FPS | Sub-pixel match confidence: 96.8% | Zero crash rate"
        ]
        for c_i, cl in enumerate(code):
            color = (100, 220, 140) if "[System" in cl else ((100, 180, 255) if "def " in cl or "import " in cl else (210, 215, 225))
            draw.text((l + 65, t + 150 + c_i * 26), cl, fill=color, font=get_font(13, mono=True))
            
        im.save(f"images/work/automation/{num}.jpg", quality=92)

create_automation_mockups()

def create_textvision_mockups():
    for num, subtitle, tag in [
        (1, "Cloud Vision OCR & Document Ingestion Pipeline", "Azure Cognitive Services"),
        (2, "Multi-Lingual Text Extraction & Word Boundaries", "99.2% Character Accuracy"),
        (3, "Structured JSON Export & Metadata Transformation", "RESTful Flask API"),
        (4, "Interactive Web Dashboard & Drag-and-Drop Dropzone", "Responsive UI"),
        (5, "Performance & Latency Evaluation Matrix", "< 350ms Ingestion Time")
    ]:
        im = Image.new("RGB", (1600, 1000), (18, 16, 20))
        draw = ImageDraw.Draw(im)
        l, t, r, b = draw_window_frame(draw, 1600, 1000, f"TextVision OCR — {subtitle}", dark=True)
        
        draw.text((l + 40, t + 30), "TEXTVISION OCR SYSTEM • AZURE VISION / FLASK", fill=(220, 140, 255), font=get_font(13, mono=True))
        draw.text((l + 40, t + 58), subtitle, fill=(255, 255, 255), font=get_font(30, bold=True))
        
        draw.rounded_rectangle([l + 40, t + 120, r - 40, b - 40], radius=10, fill=(26, 22, 30), outline=(55, 45, 65), width=1)
        
        tv_info = [
            "HTTP POST /api/v1/ocr/extract",
            "Content-Type: multipart/form-data",
            "",
            "Response 200 OK (248ms):",
            "{",
            '  "status": "success",',
            '  "confidence": 0.988,',
            '  "extracted_text": "Ajou University Global Korea Scholarship Research Publication",',
            '  "bounding_box": {"x": 120, "y": 45, "width": 840, "height": 62},',
            '  "language_detected": "en-US",',
            '  "words_count": 482',
            "}"
        ]
        for t_i, tl in enumerate(tv_info):
            color = (120, 220, 150) if "200 OK" in tl else ((255, 200, 100) if "HTTP" in tl else (210, 200, 220))
            draw.text((l + 65, t + 150 + t_i * 28), tl, fill=color, font=get_font(14, mono=True))
            
        im.save(f"images/work/textvision/{num}.jpg", quality=92)

create_textvision_mockups()

# Favicon
fav = Image.new("RGBA", (512, 512), (12, 12, 14, 255))
d_fav = ImageDraw.Draw(fav)
d_fav.rounded_rectangle([20, 20, 492, 492], radius=90, fill=(18, 18, 20), outline=(230, 230, 230), width=4)
d_fav.text((150, 120), "A", fill=(245, 245, 245), font=get_font(260, bold=True))
fav.save("images/favicon.png")

# OG Image
og = Image.new("RGB", (1200, 630), (12, 12, 14))
d_og = ImageDraw.Draw(og)
try:
    p = Image.open("images/ahsan-portrait.jpg")
    p.thumbnail((380, 500))
    og.paste(p, (60, 65))
except Exception as e:
    print("Portrait thumbnail error:", e)

d_og.text((490, 120), "KHAN MUHAMMAD AHSAN", fill=(245, 245, 245), font=get_font(42, bold=True))
d_og.text((490, 185), "Software Engineer & AI Startup Founder", fill=(160, 160, 170), font=get_font(24))
d_og.text((490, 230), "Based in Suwon, South Korea • Ajou University", fill=(130, 130, 140), font=get_font(20))
d_og.line([490, 280, 1120, 280], fill=(45, 45, 55), width=1)
d_og.text((490, 315), "• CEO at Preplit AI (AI-Powered Education Workspace)", fill=(220, 220, 225), font=get_font(20))
d_og.text((490, 355), "• Global Korea Scholarship (GKS) Fellow", fill=(220, 220, 225), font=get_font(20))
d_og.text((490, 395), "• Founder at CampusRank & Resumate", fill=(220, 220, 225), font=get_font(20))
d_og.text((490, 435), "• Top 20 Incheon Foreign Start-up Challenge 2026", fill=(220, 220, 225), font=get_font(20))
d_og.text((490, 510), "portfolio.ahsankhan.dev • 455ahsankhan@gmail.com", fill=(100, 180, 255), font=get_font(18, mono=True))
og.save("images/og-image.jpg", quality=92)
print("All assets generated successfully!")
