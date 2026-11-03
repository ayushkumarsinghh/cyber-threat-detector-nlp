import os
from PIL import Image, ImageDraw, ImageFont

base_dir = r"c:\tolls\New folder\cyber-threat-detector-nlp\report"

# -------------------------------------------------------------------------
# 1. Figure 0.1: Certificate Box Image (Like page 2 in reference PDF)
# -------------------------------------------------------------------------
def create_certificate_image():
    w, h = 1800, 1100
    img = Image.new("RGB", (w, h), "#FFFFFF")
    draw = ImageDraw.Draw(img)

    # Outer and inner border
    draw.rectangle([(20, 20), (w - 20, h - 20)], outline="#000000", width=4)
    draw.rectangle([(32, 32), (w - 32, h - 32)], outline="#000000", width=1)

    # University header
    draw.text((w // 2, 80), "SCHOOL OF COMPUTER APPLICATIONS", fill="#000000", anchor="mm", font_size=36)
    draw.text((w // 2, 130), "KALINGA INSTITUTE OF INDUSTRIAL TECHNOLOGY (KIIT)", fill="#000000", anchor="mm", font_size=42)
    draw.text((w // 2, 175), "Deemed to be University U/S 3 of UGC Act, 1956 | Bhubaneswar - 751024, Odisha", fill="#444444", anchor="mm", font_size=26)
    draw.line([(80, 210), (w - 80, 210)], fill="#000000", width=2)

    draw.text((w // 2, 270), "PRACTICAL TRAINING COMPLETION CERTIFICATE", fill="#1E3A8A", anchor="mm", font_size=38)
    draw.text((w - 120, 330), "Date: 04/07/2026", fill="#000000", anchor="rm", font_size=28)

    body_text = (
        "This is to certify that Mr. Ayush Kumar Singh, a student of the School of Computer Applications,\n"
        "KIIT Deemed to be University, Bhubaneswar - 751024, has successfully undergone and completed his\n"
        "8-Week Practical Training / Summer Internship titled:\n\n"
        "\"CYBER THREAT AND PHISHING DETECTION USING NLP AND MACHINE LEARNING\"\n\n"
        "commencing from 04.05.2026 to 04.07.2026 under the mentorship of Prof. (Dr.) Satya Ranjan Dash.\n"
        "During this training period, his conduct was exemplary, and he demonstrated outstanding technical\n"
        "aptitude in Machine Learning, Cybersecurity, Image Processing, and Natural Language Processing."
    )
    draw.multiline_text((w // 2, 530), body_text, fill="#000000", anchor="mm", align="center", spacing=14, font_size=30)

    # Signatures
    draw.line([(150, 920), (550, 920)], fill="#000000", width=2)
    draw.text((350, 950), "Prof. (Dr.) Satya Ranjan Dash", fill="#000000", anchor="mm", font_size=28)
    draw.text((350, 985), "Project Supervisor & Mentor", fill="#444444", anchor="mm", font_size=24)
    draw.text((350, 1020), "School of Computer Applications", fill="#444444", anchor="mm", font_size=22)

    # Official Seal circle
    draw.ellipse([(800, 840), (1000, 1040)], outline="#1E3A8A", width=3)
    draw.text((900, 920), "KIIT - SCA", fill="#1E3A8A", anchor="mm", font_size=26)
    draw.text((900, 960), "OFFICIAL SEAL", fill="#1E3A8A", anchor="mm", font_size=20)

    draw.line([(w - 550, 920), (w - 150, 920)], fill="#000000", width=2)
    draw.text((w - 350, 950), "Prof. (Dr.) Veena Goswami", fill="#000000", anchor="mm", font_size=28)
    draw.text((w - 350, 985), "Director General", fill="#444444", anchor="mm", font_size=24)
    draw.text((w - 350, 1020), "School of Computer Applications", fill="#444444", anchor="mm", font_size=22)

    cert_path = os.path.join(base_dir, "cert_box.png")
    img.save(cert_path, "PNG", dpi=(300, 300))
    print(f"Saved certificate image: {cert_path}")


# -------------------------------------------------------------------------
# 2. Figure 1.1: Process Flow Diagram (Like page 9 in reference PDF)
# -------------------------------------------------------------------------
def create_flow_diagram():
    w, h = 1800, 820
    img = Image.new("RGB", (w, h), "#FFFFFF")
    draw = ImageDraw.Draw(img)

    draw.rectangle([(10, 10), (w - 10, h - 10)], outline="#CBD5E1", width=1)
    draw.text((w // 2, 40), "End-to-End Workflow of the Cyber Threat & Phishing Detection System", fill="#000000", anchor="mm", font_size=32)

    # Row 1: 3 boxes
    # Box 1: Raw input & Preprocessing
    draw.rectangle([(60, 90), (560, 280)], outline="#000000", width=2, fill="#F8FAFC")
    draw.rectangle([(60, 90), (560, 135)], fill="#1E293B")
    draw.text((310, 112), "STEP 1: RAW INCOMING DATA", fill="#FFFFFF", anchor="mm", font_size=22)
    t1 = "Incoming SMS, Email or Message\nToken Extraction & URL Regex Parsing\nCase Normalization & Punctuation Stripping\nStop-word Elimination Pipeline"
    draw.multiline_text((310, 205), t1, fill="#000000", anchor="mm", align="center", spacing=8, font_size=20)

    # Arrow 1 -> 2
    draw.line([(560, 185), (660, 185)], fill="#000000", width=3)
    draw.polygon([(660, 185), (645, 175), (645, 195)], fill="#000000")
    draw.text((610, 165), "Clean Tokens", fill="#475569", anchor="mm", font_size=18)

    # Box 2: TF-IDF Vectorization
    draw.rectangle([(660, 90), (1160, 280)], outline="#000000", width=2, fill="#F8FAFC")
    draw.rectangle([(660, 90), (1160, 135)], fill="#1E293B")
    draw.text((910, 112), "STEP 2: TF-IDF N-GRAM EXTRACTION", fill="#FFFFFF", anchor="mm", font_size=22)
    t2 = "Sublinear Term Frequency Scaling\nInverse Document Frequency (IDF) Scoring\nUnigrams + Bigrams (1,2) Context\n500 Most Informative Features"
    draw.multiline_text((910, 205), t2, fill="#000000", anchor="mm", align="center", spacing=8, font_size=20)

    # Arrow 2 -> 3
    draw.line([(1160, 185), (1260, 185)], fill="#000000", width=3)
    draw.polygon([(1260, 185), (1245, 175), (1245, 195)], fill="#000000")
    draw.text((1210, 165), "Vectors", fill="#475569", anchor="mm", font_size=18)

    # Box 3: Dual ML Classifier
    draw.rectangle([(1260, 90), (1740, 280)], outline="#000000", width=2, fill="#F8FAFC")
    draw.rectangle([(1260, 90), (1740, 135)], fill="#1E293B")
    draw.text((1500, 112), "STEP 3: CLASSIFIER INFERENCE", fill="#FFFFFF", anchor="mm", font_size=22)
    t3 = "Multinomial Naive Bayes (Baseline)\nRandom Forest (100 Decision Trees)\nEnsemble Probability Calibration\nBalanced Class Weight Adjustment"
    draw.multiline_text((1500, 205), t3, fill="#000000", anchor="mm", align="center", spacing=8, font_size=20)

    # Down arrow from Box 3 to Box 4
    draw.line([(1500, 280), (1500, 390)], fill="#000000", width=3)
    draw.polygon([(1500, 390), (1490, 375), (1510, 375)], fill="#000000")
    draw.text((1560, 335), "Probabilities", fill="#475569", anchor="mm", font_size=18)

    # Row 2: 3 boxes
    # Box 4: Multi-Tier Risk Verdict
    draw.rectangle([(1260, 390), (1740, 580)], outline="#000000", width=2, fill="#F8FAFC")
    draw.rectangle([(1260, 390), (1740, 435)], fill="#1E293B")
    draw.text((1500, 412), "STEP 4: SEVERITY TRIAGE", fill="#FFFFFF", anchor="mm", font_size=22)
    t4 = "Safe / Benign: < 40% Risk\nSuspicious Threat: 40% - 69% Risk\nCritical Phishing: >= 70% Risk\n100% Precision (Zero False Alarms)"
    draw.multiline_text((1500, 505), t4, fill="#000000", anchor="mm", align="center", spacing=8, font_size=20)

    # Arrow 4 -> 5
    draw.line([(1260, 485), (1160, 485)], fill="#000000", width=3)
    draw.polygon([(1160, 485), (1175, 475), (1175, 495)], fill="#000000")
    draw.text((1210, 465), "Verdict", fill="#475569", anchor="mm", font_size=18)

    # Box 5: Explainable AI Attribution
    draw.rectangle([(660, 390), (1160, 580)], outline="#000000", width=2, fill="#F8FAFC")
    draw.rectangle([(660, 390), (1160, 435)], fill="#1E293B")
    draw.text((910, 412), "STEP 5: EXPLAINABLE AI (XAI)", fill="#FFFFFF", anchor="mm", font_size=22)
    t5 = "Feature Impact = TF-IDF * RF-Importance\nTop Suspicious Token Identification\nHighlights: 'kyc', 'urgent', 'suspended'\nTransparent Auditing for SOC Analysts"
    draw.multiline_text((910, 505), t5, fill="#000000", anchor="mm", align="center", spacing=8, font_size=20)

    # Arrow 5 -> Control Console
    draw.line([(660, 485), (560, 485)], fill="#000000", width=3)
    draw.polygon([(560, 485), (575, 475), (575, 495)], fill="#000000")
    draw.text((610, 465), "Dashboard", fill="#475569", anchor="mm", font_size=18)

    # Box 6: Streamlit Console
    draw.rectangle([(60, 390), (560, 580)], outline="#000000", width=2, fill="#F8FAFC")
    draw.rectangle([(60, 390), (560, 435)], fill="#1E293B")
    draw.text((310, 412), "OPERATIONAL WEB CONSOLE", fill="#FFFFFF", anchor="mm", font_size=22)
    t6 = "Streamlit Reactive Web App (Port 8501)\n1-Click Quick Attack Simulation Presets\nReal-Time Gauge & Confidence Metrics\nZero GPU / External Hardware Dependency"
    draw.multiline_text((310, 505), t6, fill="#000000", anchor="mm", align="center", spacing=8, font_size=20)

    # Bottom summary box
    draw.rectangle([(60, 630), (1740, 770)], outline="#1E3A8A", width=2, fill="#EFF6FF")
    summary_text = (
        "CORE CYBERSECURITY WORKFLOW:\n"
        "Raw Message -> Token Cleaning -> Sublinear TF-IDF -> Random Forest Evaluation -> Multi-Threshold Risk Meter -> Explainable AI Inspection"
    )
    draw.multiline_text((w // 2, 700), summary_text, fill="#1E3A8A", anchor="mm", align="center", spacing=10, font_size=24)

    flow_path = os.path.join(base_dir, "flow_diagram.png")
    img.save(flow_path, "PNG", dpi=(300, 300))
    print(f"Saved flow diagram: {flow_path}")


# -------------------------------------------------------------------------
# 3. Figure 2.1: Three-Layer Architecture Block Diagram (Like page 11)
# -------------------------------------------------------------------------
def create_architecture_diagram():
    w, h = 1800, 650
    img = Image.new("RGB", (w, h), "#FFFFFF")
    draw = ImageDraw.Draw(img)

    draw.rectangle([(10, 10), (w - 10, h - 10)], outline="#CBD5E1", width=1)
    draw.text((w // 2, 40), "Simplified Three-Layer Cyber Threat Detection Architecture", fill="#000000", anchor="mm", font_size=30)

    # Layer 1: Ingestion & Text Inputs
    draw.rectangle([(60, 100), (560, 560)], outline="#000000", width=2, fill="#F8FAFC")
    draw.rectangle([(60, 100), (560, 155)], fill="#0F172A")
    draw.text((310, 127), "1. INPUTS & DATA CHANNELS", fill="#FFFFFF", anchor="mm", font_size=22)
    t1 = "SMS Communications\nEmail Ingestion (RFC 5322)\nInstant Messaging Chats\nSynthetic Benchmark Corpus\nRegional Scam Templates\n(KYC, Lottery, SIM, Bills)"
    draw.multiline_text((310, 350), t1, fill="#000000", anchor="mm", align="center", spacing=16, font_size=24)

    # Arrow 1 -> 2
    draw.line([(560, 330), (660, 330)], fill="#000000", width=3)
    draw.polygon([(660, 330), (645, 320), (645, 340)], fill="#000000")
    draw.text((610, 305), "Raw Text", fill="#475569", anchor="mm", font_size=18)

    # Layer 2: NLP & Machine Learning Engine
    draw.rectangle([(660, 100), (1160, 560)], outline="#000000", width=2, fill="#F8FAFC")
    draw.rectangle([(660, 100), (1160, 155)], fill="#0F172A")
    draw.text((910, 127), "2. NLP & CLASSIFIER LOGIC", fill="#FFFFFF", anchor="mm", font_size=22)
    t2 = "Regex Cleaning & Stopwords\nSublinear TF-IDF (1,2 n-grams)\nMultinomial Naive Bayes (a=0.5)\nRandom Forest (100 Trees)\nProbability Calibration\nExplainable AI (XAI) Mapper"
    draw.multiline_text((910, 350), t2, fill="#000000", anchor="mm", align="center", spacing=16, font_size=24)

    # Arrow 2 -> 3
    draw.line([(1160, 330), (1260, 330)], fill="#000000", width=3)
    draw.polygon([(1260, 330), (1245, 320), (1245, 340)], fill="#000000")
    draw.text((1210, 305), "Triage Data", fill="#475569", anchor="mm", font_size=18)

    # Layer 3: Security Console & Outputs
    draw.rectangle([(1260, 100), (1740, 560)], outline="#000000", width=2, fill="#F8FAFC")
    draw.rectangle([(1260, 100), (1740, 155)], fill="#0F172A")
    draw.text((1500, 127), "3. SECURITY DASHBOARD & APIS", fill="#FFFFFF", anchor="mm", font_size=22)
    t3 = "Streamlit UI Operations Console\nReal-Time Risk Meter (0-100%)\nSeverity Cards (Safe/Threat)\nXAI Trigger Keyword Table\nModel Performance Telemetry\nREST API Ready Integration"
    draw.multiline_text((1500, 350), t3, fill="#000000", anchor="mm", align="center", spacing=16, font_size=24)

    arch_path = os.path.join(base_dir, "arch_diagram.png")
    img.save(arch_path, "PNG", dpi=(300, 300))
    print(f"Saved architecture diagram: {arch_path}")


# -------------------------------------------------------------------------
# 4. Figure 2.2: P&ID / Ensemble Classifier Schematic (Like page 12)
# -------------------------------------------------------------------------
def create_ensemble_schematic():
    w, h = 1800, 680
    img = Image.new("RGB", (w, h), "#FFFFFF")
    draw = ImageDraw.Draw(img)

    draw.rectangle([(10, 10), (w - 10, h - 10)], outline="#CBD5E1", width=1)
    draw.text((w // 2, 40), "Random Forest Decision Tree Ensemble & Feature Attribution Schematic", fill="#000000", anchor="mm", font_size=30)

    # Top Central Block: Vectorizer
    draw.rectangle([(500, 90), (1300, 210)], outline="#000000", width=2, fill="#F1F5F9")
    draw.rectangle([(500, 90), (1300, 135)], fill="#1E293B")
    draw.text((900, 112), "TF-IDF FEATURE VECTOR (500 DIMENSIONS)", fill="#FFFFFF", anchor="mm", font_size=22)
    draw.text((900, 172), "Sublinear TF: 1 + log(f) | IDF: log((1+|D|)/(1+|d|)) + 1 | Unigram + Bigram Context", fill="#000000", anchor="mm", font_size=21)

    # 3 Trees in parallel
    tree_x = [300, 900, 1500]
    tree_names = ["DECISION TREE 1", "DECISION TREE b (Bootstrap Sample)", "DECISION TREE 100"]

    for i, tx in enumerate(tree_x):
        # Line from vectorizer to tree
        draw.line([(900, 210), (tx, 270)], fill="#000000", width=2)
        draw.polygon([(tx, 270), (tx - 8, 255), (tx + 8, 255)], fill="#000000")

        # Tree Box
        draw.rectangle([(tx - 200, 270), (tx + 200, 440)], outline="#000000", width=2, fill="#F8FAFC")
        draw.rectangle([(tx - 200, 270), (tx + 200, 310)], fill="#334155")
        draw.text((tx, 290), tree_names[i], fill="#FFFFFF", anchor="mm", font_size=18)
        tt = "Random Feature Subset (m=22)\nGini Impurity Minimization\nLeaf Node Probability: P_b(y|x)"
        draw.multiline_text((tx, 375), tt, fill="#000000", anchor="mm", align="center", spacing=8, font_size=19)

        # Line from tree to voting block
        draw.line([(tx, 440), (900, 500)], fill="#000000", width=2)
        draw.polygon([(900, 500), (900 - 8, 485), (900 + 8, 485)], fill="#000000")

    # Bottom voting block
    draw.rectangle([(400, 500), (1400, 620)], outline="#000000", width=2, fill="#EFF6FF")
    draw.rectangle([(400, 500), (1400, 545)], fill="#1E3A8A")
    draw.text((900, 522), "ENSEMBLE PROBABILITY AGGREGATION & SOFT VOTING", fill="#FFFFFF", anchor="mm", font_size=22)
    draw.text((900, 582), "P(y = Malicious | x) = (1 / 100) * Sum[ P_b(y | x) ] -> High Precision Threat Output", fill="#1E3A8A", anchor="mm", font_size=21)

    ens_path = os.path.join(base_dir, "ensemble_schematic.png")
    img.save(ens_path, "PNG", dpi=(300, 300))
    print(f"Saved ensemble schematic: {ens_path}")

if __name__ == "__main__":
    create_certificate_image()
    create_flow_diagram()
    create_architecture_diagram()
    create_ensemble_schematic()
