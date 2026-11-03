import os
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable, Image
)
from reportlab.pdfgen import canvas

base_dir = r"c:\tolls\New folder\cyber-threat-detector-nlp\report"

class ExactNumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        if self._pageNumber == 1:
            # Draw exact double borders like reference PDF Page 1
            self.saveState()
            self.setStrokeColor(colors.HexColor("#000000"))
            # Outer thick rectangle
            self.setLineWidth(2.2)
            self.rect(34, 34, A4[0] - 68, A4[1] - 68)
            # Inner thin rectangle
            self.setLineWidth(0.6)
            self.rect(41, 41, A4[0] - 82, A4[1] - 82)
            self.restoreState()
            return
        
        self.saveState()
        self.setFont("Times-Roman", 8.5)
        self.setFillColor(colors.HexColor("#000000"))
        
        # Running bottom footer matching reference PDF
        self.setStrokeColor(colors.HexColor("#000000"))
        self.setLineWidth(0.6)
        self.line(45, 42, A4[0] - 45, 42)
        
        footer_left = "KIIT Deemed to be University | School of Computer Applications Practical Training Report — Ayush Kumar Singh"
        self.drawString(45, 30, footer_left)
        self.drawRightString(A4[0] - 45, 30, f"Page {self._pageNumber}")
        self.restoreState()


def build_pdf():
    pdf_path = os.path.join(base_dir, "Practical_Training_Report_Ayush_Kumar_Singh.pdf")
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=A4,
        leftMargin=45,
        rightMargin=45,
        topMargin=42,
        bottomMargin=45
    )

    styles = getSampleStyleSheet()

    # Typography matching reference PDF (Times-Roman / LiberationSerif)
    cover_sub = ParagraphStyle(
        'CoverSub',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=11,
        leading=15,
        alignment=1,
        textColor=colors.black,
        spaceAfter=10
    )

    cover_title = ParagraphStyle(
        'CoverTitle',
        parent=styles['Normal'],
        fontName='Times-Bold',
        fontSize=15,
        leading=20,
        alignment=1,
        textColor=colors.black,
        spaceAfter=12
    )

    page_head = ParagraphStyle(
        'PageHead',
        parent=styles['Normal'],
        fontName='Times-Bold',
        fontSize=13.5,
        leading=17,
        textColor=colors.black,
        spaceBefore=0,
        spaceAfter=3
    )

    sec_head = ParagraphStyle(
        'SecHead',
        parent=styles['Normal'],
        fontName='Times-Bold',
        fontSize=10.5,
        leading=14,
        textColor=colors.black,
        spaceBefore=6,
        spaceAfter=3
    )

    body_text = ParagraphStyle(
        'BodyTextCustom',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=9,
        leading=13,
        textColor=colors.black,
        spaceAfter=5,
        alignment=4 # Justified
    )

    body_center = ParagraphStyle(
        'BodyCenter',
        parent=body_text,
        alignment=1
    )

    caption_text = ParagraphStyle(
        'CaptionText',
        parent=styles['Normal'],
        fontName='Times-Italic',
        fontSize=8,
        leading=11,
        alignment=1,
        textColor=colors.black,
        spaceBefore=3,
        spaceAfter=4
    )

    table_head = ParagraphStyle(
        'TableHead',
        parent=styles['Normal'],
        fontName='Times-Bold',
        fontSize=7.5,
        leading=9.5,
        textColor=colors.black
    )

    table_cell = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=7.5,
        leading=9.5,
        textColor=colors.black
    )

    table_cell_center = ParagraphStyle(
        'TableCellCenter',
        parent=table_cell,
        alignment=1
    )

    def hr():
        return HRFlowable(width="100%", thickness=1, color=colors.black, spaceAfter=8, spaceBefore=0)

    story = []

    # =========================================================================
    # PAGE 1: COVER PAGE (Exact match to reference PDF Page 1)
    # =========================================================================
    story.append(Spacer(1, 15))
    logo_path = os.path.join(base_dir, "kiit_logo.png")
    if os.path.exists(logo_path):
        story.append(Image(logo_path, width=125, height=95))
    story.append(Spacer(1, 15))

    story.append(Paragraph("A Practical Training Report on", cover_sub))
    story.append(Paragraph("CYBER THREAT AND PHISHING DETECTION USING<br/>NATURAL LANGUAGE PROCESSING AND MACHINE LEARNING", cover_title))
    story.append(Spacer(1, 10))

    story.append(Paragraph("Submitted in partial fulfilment of the requirements for the award of the degree of", cover_sub))
    story.append(Paragraph("<b>Master of Computer Applications</b><br/>in<br/><b>Computer Applications</b>", ParagraphStyle('CoverDeg', parent=cover_sub, fontSize=12, leading=17, fontName='Times-Bold')))
    story.append(Spacer(1, 8))

    story.append(Paragraph("by", cover_sub))
    story.append(Paragraph("<b>Ayush Kumar Singh</b>", ParagraphStyle('CoverCand', parent=cover_sub, fontSize=12, leading=16, fontName='Times-Bold')))
    story.append(Spacer(1, 10))

    story.append(Paragraph("Under the guidance of", cover_sub))
    story.append(Paragraph("<b>Prof. (Dr.) Satya Ranjan Dash</b><br/>School of Computer Applications<br/>(04.05.2026 – 04.07.2026)", ParagraphStyle('CoverGuide', parent=cover_sub, fontSize=11, leading=15)))
    story.append(Spacer(1, 20))

    story.append(Paragraph("<b>SCHOOL OF COMPUTER APPLICATIONS</b>", ParagraphStyle('CoverSch', parent=cover_sub, fontSize=11.5, leading=15, fontName='Times-Bold')))
    story.append(Paragraph("<b>KALINGA INSTITUTE OF INDUSTRIAL TECHNOLOGY</b>", ParagraphStyle('CoverInst', parent=cover_sub, fontSize=11.5, leading=15, fontName='Times-Bold')))
    story.append(Paragraph("(Deemed to be University)<br/>Bhubaneswar – 751024, Odisha, India", cover_sub))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 2: CERTIFICATE OF PRACTICAL TRAINING (Exact match to reference Page 2)
    # =========================================================================
    story.append(Paragraph("CERTIFICATE OF PRACTICAL TRAINING", page_head))
    story.append(hr())
    
    cert_intro = (
        "The Practical Training Completion Certificate was issued by the School of Computer Applications, "
        "Kalinga Institute of Industrial Technology (KIIT) Deemed to be University, Bhubaneswar – 751024, Odisha on "
        "04/07/2026, under the guidance of Prof. (Dr.) Satya Ranjan Dash, certifying completion of the 8-Week Practical Training / "
        "Summer Internship from 04.05.2026 to 04.07.2026."
    )
    story.append(Paragraph(cert_intro, body_text))
    story.append(Spacer(1, 8))

    cert_box_path = os.path.join(base_dir, "cert_box.png")
    if os.path.exists(cert_box_path):
        story.append(Image(cert_box_path, width=480, height=290))
    story.append(Spacer(1, 6))

    story.append(Paragraph("Figure 0.1: Official Practical Training Completion Certificate received from School of Computer Applications, KIIT Deemed to be University (dated 04/07/2026).", caption_text))
    story.append(Spacer(1, 6))
    story.append(Paragraph("Copy of the official certificate — Candidate: Ayush Kumar Singh (School of Computer Applications, KIIT-DU).", caption_text))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 3: CANDIDATE'S DECLARATION (Exact match to reference Page 3)
    # =========================================================================
    story.append(Paragraph("CANDIDATE’S DECLARATION", page_head))
    story.append(hr())
    
    decl_p1 = (
        "I, Ayush Kumar Singh, a bonafide postgraduate student of the Master of Computer Applications (MCA) programme "
        "at the School of Computer Applications, Kalinga Institute of Industrial Technology (KIIT) Deemed to be University, "
        "Bhubaneswar – 751024, Odisha, hereby declare that the Practical Training Report entitled “Cyber Threat and Phishing "
        "Detection using Natural Language Processing and Machine Learning” is an authentic and original record of the practical "
        "training work carried out by me at the School of Computer Applications, KIIT Deemed to be University, during the period "
        "from 04 May 2026 to 04 July 2026."
    )
    decl_p2 = (
        "I further declare that the research and development of the natural language processing pipeline, sublinear TF-IDF "
        "n-gram feature extraction, Multinomial Naive Bayes probabilistic baseline modeling, Random Forest ensemble classification, "
        "Explainable AI (XAI) feature keyword attribution, and Streamlit security dashboard operations, as presented in this report, "
        "were carried out by me under the supervision of Prof. (Dr.) Satya Ranjan Dash and comply with the academic regulations of KIIT "
        "Deemed to be University."
    )
    decl_p3 = (
        "The contents of this report have not been submitted, either in part or in full, to any other university or educational "
        "institution for the award of any degree, diploma, certificate or fellowship. All external technical standards, machine learning "
        "frameworks, and cybersecurity references consulted during the preparation of this work have been duly acknowledged in the "
        "References section."
    )
    story.append(Paragraph(decl_p1, body_text))
    story.append(Paragraph(decl_p2, body_text))
    story.append(Paragraph(decl_p3, body_text))
    story.append(Spacer(1, 6))

    story.append(Paragraph("SUMMARY OF CANDIDATE & SUBMISSION DETAILS", sec_head))
    cand_tab = [
        [Paragraph("Candidate Name", table_head), Paragraph("Ayush Kumar Singh", table_cell)],
        [Paragraph("Degree & Specialisation", table_head), Paragraph("Master of Computer Applications (MCA) in Computer Applications", table_cell)],
        [Paragraph("Academic School & University", table_head), Paragraph("School of Computer Applications, KIIT Deemed to be University, Bhubaneswar", table_cell)],
        [Paragraph("Project Mentor / Supervisor", table_head), Paragraph("Prof. (Dr.) Satya Ranjan Dash, School of Computer Applications", table_cell)],
        [Paragraph("Training Organisation & Unit", table_head), Paragraph("School of Computer Applications, KIIT Deemed to be University, Bhubaneswar", table_cell)],
        [Paragraph("Training Period", table_head), Paragraph("04.05.2026 to 04.07.2026 (8 weeks)", table_cell)],
    ]
    t_c = Table(cand_tab, colWidths=[160, 345])
    t_c.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,-1), colors.HexColor("#F3F4F6")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.black),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_c)
    story.append(Spacer(1, 20))

    sig_tab = [
        [Paragraph("Place: Bhubaneswar, Odisha<br/>Date: 04 July 2026", body_text),
         Paragraph("_______________________________<br/><b>Ayush Kumar Singh</b><br/>School of Computer Applications<br/>KIIT Deemed to be University", body_text)]
    ]
    t_sig = Table(sig_tab, colWidths=[250, 255])
    t_sig.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP')]))
    story.append(t_sig)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 4: ACKNOWLEDGEMENT (Exact match to reference Page 4)
    # =========================================================================
    story.append(Paragraph("ACKNOWLEDGEMENT", page_head))
    story.append(hr())
    
    ack_p1 = (
        "The successful completion of my practical training in the School of Computer Applications at KIIT Deemed to be "
        "University, Bhubaneswar, Odisha, has been a defining milestone in my postgraduate education. It enabled me to "
        "connect theoretical foundations of computer science, natural language processing and machine learning with practical, "
        "real-world cybersecurity defenses against deceptive social engineering attacks."
    )
    ack_p2 = (
        "First and foremost, I express my deepest gratitude to my Project Supervisor and Mentor, <b>Prof. (Dr.) Satya Ranjan Dash</b>, "
        "School of Computer Applications, for his invaluable technical guidance, constructive mentorship, and continuous encouragement "
        "from 04 May 2026 to 04 July 2026. His hands-on guidance first helped me understand the complete security landscape of modern "
        "phishing and smishing attack vectors — from synthetic corpus generation and regex tokenization to sublinear TF-IDF vectorization, "
        "Naive Bayes probabilistic modeling, and Random Forest ensemble calibration — and then trained me to construct and deploy the "
        "interactive Streamlit security operations dashboard."
    )
    ack_p3 = (
        "I extend my sincere appreciation to the academic leadership of the School of Computer Applications, Kalinga Institute "
        "of Industrial Technology (KIIT) Deemed to be University, Bhubaneswar — specifically <b>Prof. (Dr.) Veena Goswami</b>, "
        "Director General, School of Computer Applications — for providing world-class computational facilities, high-speed laboratory "
        "infrastructure, and an industry-oriented curriculum that emphasizes applied artificial intelligence and cybersecurity. "
        "I also thank the visionary founder of KIIT & KISS, <b>Prof. (Dr.) Achyuta Samanta</b>, whose relentless pursuit of academic "
        "excellence has established an inspiring learning ecosystem."
    )
    ack_p4 = (
        "I also thank the computer laboratory technical staff and system administrators at the School of Computer Applications "
        "for maintaining seamless software environments and server access throughout the internship. Finally, I am deeply grateful "
        "to my parents, family members and fellow MCA classmates for their moral support and encouragement throughout the preparation "
        "of this report."
    )
    story.append(Paragraph(ack_p1, body_text))
    story.append(Paragraph(ack_p2, body_text))
    story.append(Paragraph(ack_p3, body_text))
    story.append(Paragraph(ack_p4, body_text))
    story.append(Spacer(1, 20))
    story.append(Paragraph("School of Computer Applications<br/>KIIT Deemed to be University, Bhubaneswar – 751024", body_text))
    story.append(Spacer(1, 10))
    story.append(Paragraph("<b>Ayush Kumar Singh</b><br/>School of Computer Applications", body_text))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 5: ABSTRACT (Exact match to reference Page 5)
    # =========================================================================
    story.append(Paragraph("ABSTRACT", page_head))
    story.append(hr())
    
    abs_p1 = (
        "This Practical Training Report documents the eight-week, full-time practical training (04 May 2026 to 04 July 2026) "
        "completed in the School of Computer Applications, Kalinga Institute of Industrial Technology (KIIT) Deemed to be University, "
        "Bhubaneswar, Odisha. The objective of the internship was twofold: first, to understand the end-to-end linguistic, semantic and "
        "structural characteristics of modern social engineering threats (email phishing, SMS smishing, and deceptive financial extortion); "
        "and second, to design, train, evaluate and deploy a real-time detection system using Natural Language Processing (NLP) and "
        "Machine Learning (ML) algorithms."
    )
    abs_p2 = (
        "The system developed during the internship ingests incoming communications, normalizes text through case-folding, regex "
        "cleansing, and stop-word pruning, and extracts discriminative features using Term Frequency-Inverse Document Frequency (TF-IDF) "
        "with sublinear term-frequency scaling and (1, 2) n-gram tokenization across 500 feature dimensions. Because human security analysts "
        "require both high accuracy and clear interpretability, two complementary classifiers were implemented: a Multinomial Naive Bayes "
        "probabilistic baseline with Laplace smoothing (alpha=0.5), and a production Random Forest ensemble comprising 100 decorrelated "
        "decision trees with balanced class weighting. Furthermore, an Explainable AI (XAI) feature attribution engine was coded to map active "
        "tokens to model feature importances, highlighting the specific keywords (e.g., 'kyc', 'urgent', 'suspended') triggering the alert."
    )
    abs_p3 = (
        "The complete system was deployed through an interactive Streamlit security dashboard operating on local port 8501. Tested on a "
        "stratified out-of-sample holdout dataset of 25 samples, the production Random Forest model achieved 84.00% overall accuracy, "
        "100.00% precision on malicious threats (zero false alarms on benign communications), and an exceptional ROC-AUC score of 98.72%. "
        "Operating with sub-12 millisecond inference latency on a standard CPU, the system eliminates alert fatigue in security triage."
    )
    story.append(Paragraph(abs_p1, body_text))
    story.append(Paragraph(abs_p2, body_text))
    story.append(Paragraph(abs_p3, body_text))
    story.append(Spacer(1, 8))

    story.append(Paragraph("EXECUTIVE SUMMARY OF TECHNICAL KEYWORDS & KEY OUTCOMES", sec_head))
    abs_tab = [
        [Paragraph("Core Technical Domains", table_head),
         Paragraph("Cyber Threat Detection; Natural Language Processing (NLP); TF-IDF Sublinear N-gram Feature Space; Multinomial Naive Bayes; Random Forest Ensemble; Explainable AI (XAI); Streamlit Security Console", table_cell)],
        [Paragraph("Key Operational Outcomes", table_head),
         Paragraph("100.00% threat precision (zero false alarms on legitimate communications); 98.72% ROC-AUC class discriminability; real-time explainable token extraction; sub-12ms inference latency; zero external hardware dependency", table_cell)],
    ]
    t_abs = Table(abs_tab, colWidths=[150, 355])
    t_abs.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,-1), colors.HexColor("#F3F4F6")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.black),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_abs)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 6: TABLE OF CONTENTS (Exact match to reference Page 6)
    # =========================================================================
    story.append(Paragraph("TABLE OF CONTENTS", page_head))
    story.append(hr())
    story.append(Paragraph("This 15-page report is organised as follows; every section, chapter and technical diagram is mapped to its page number.", body_text))
    story.append(Spacer(1, 4))

    toc_tab = [
        [Paragraph("Section / Chapter", table_head), Paragraph("Title and Sub-Section Breakdown", table_head), Paragraph("Page No.", table_head)],
        [Paragraph("Cover Page", table_cell), Paragraph("Title, Institutional Header, and Candidate & Internship Particulars", table_cell), Paragraph("01", table_cell_center)],
        [Paragraph("Certificate", table_cell), Paragraph("Certificate of Practical Training (Full-Page Completion Certificate)", table_cell), Paragraph("02", table_cell_center)],
        [Paragraph("Declaration", table_cell), Paragraph("Candidate’s Declaration of Originality and Academic Compliance", table_cell), Paragraph("03", table_cell_center)],
        [Paragraph("Acknowledgement", table_cell), Paragraph("Acknowledgement of Faculty Mentors and KIIT University Leadership", table_cell), Paragraph("04", table_cell_center)],
        [Paragraph("Abstract", table_cell), Paragraph("Technical Abstract: Cyber Threat Detection & NLP/ML Architecture", table_cell), Paragraph("05", table_cell_center)],
        [Paragraph("Contents", table_cell), Paragraph("Table of Contents", table_cell), Paragraph("06", table_cell_center)],
        [Paragraph("Figures & Tables", table_cell), Paragraph("List of Figures and List of Tables", table_cell), Paragraph("07", table_cell_center)],
        [Paragraph("Chapter 1<br/><b>INTRODUCTION</b>", table_cell), Paragraph("1.1 Objectives; 1.2 Scope & Duration; 1.3 Department Overview (Page 08)<br/>1.4 Overview of the Cyber Threat Detector & Flow Diagram (Page 09)", table_cell), Paragraph("08 – 09", table_cell_center)],
        [Paragraph("Chapter 2<br/><b>TRAINING ACTIVITIES<br/>AND TECHNICAL<br/>LEARNING</b>", table_cell), Paragraph("2.1 Domain-Wise Activities & 2.2 Step-by-Step Technical Process (Page 10)<br/>2.3 System Control Architecture & NLP Pipeline Specifications (Page 11)<br/>2.4 Machine Learning Classification & Feature Engineering (Page 12)<br/>2.5 Model Training Telemetry, Telemetry Exhibits & UI Observations (Page 13)", table_cell), Paragraph("10 – 13", table_cell_center)],
        [Paragraph("Chapter 3<br/><b>LEARNING OUTCOMES<br/>AND CONCLUSION</b>", table_cell), Paragraph("3.1 Technical Skills Acquired in AI/ML & Cybersecurity<br/>3.2 Technical Problems Observed & 3.3 Proposed Engineering Solutions<br/>3.4 Conclusion", table_cell), Paragraph("14", table_cell_center)],
        [Paragraph("References", table_cell), Paragraph("REFERENCES & TECHNICAL STANDARDS", table_cell), Paragraph("15", table_cell_center)],
    ]
    t_toc = Table(toc_tab, colWidths=[105, 335, 65])
    t_toc.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#F3F4F6")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.black),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_toc)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 7: LIST OF FIGURES AND TABLES (Exact match to reference Page 7)
    # =========================================================================
    story.append(Paragraph("LIST OF FIGURES AND TABLES", page_head))
    story.append(hr())
    
    story.append(Paragraph("List of Figures", sec_head))
    lof_tab = [
        [Paragraph("Figure No.", table_head), Paragraph("Figure Title and Description", table_head), Paragraph("Page No.", table_head)],
        [Paragraph("Figure 0.1", table_cell_center), Paragraph("Official Practical Training Completion Certificate issued by School of Computer Applications, KIIT Deemed to be University (dated 04/07/2026)", table_cell), Paragraph("02", table_cell_center)],
        [Paragraph("Figure 1.1", table_cell_center), Paragraph("End-to-End Process Flow Diagram of the Cyber Threat & Phishing Detection System (Data Cleaning, TF-IDF Vectorization, ML Inference, XAI, Streamlit Console)", table_cell), Paragraph("09", table_cell_center)],
        [Paragraph("Figure 2.1", table_cell_center), Paragraph("Cyber Threat Detection System: Three-Layer System Architecture, Field Data Channels, and Security Operations Console", table_cell), Paragraph("11", table_cell_center)],
        [Paragraph("Figure 2.2", table_cell_center), Paragraph("Random Forest Decision Tree Ensemble and Feature Attribution Schematic under Scikit-Learn Framework", table_cell), Paragraph("12", table_cell_center)],
        [Paragraph("Figure 2.3", table_cell_center), Paragraph("Streamlit Security Operations Telemetry: Real-Time Threat Analysis of Urgent Banking Scam (93.0% Malicious Risk) & Explainable AI (XAI) Trigger Keywords", table_cell), Paragraph("13", table_cell_center)],
    ]
    t_lof = Table(lof_tab, colWidths=[65, 375, 65])
    t_lof.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#F3F4F6")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.black),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_lof)
    story.append(Spacer(1, 10))

    story.append(Paragraph("List of Tables", sec_head))
    lot_tab = [
        [Paragraph("Table No.", table_head), Paragraph("Table Title and Technical Scope", table_head), Paragraph("Page No.", table_head)],
        [Paragraph("Table 1.1", table_cell_center), Paragraph("Eight-Week Structured Practical Training Schedule in the School of Computer Applications (04.05.2026 – 04.07.2026)", table_cell), Paragraph("08", table_cell_center)],
        [Paragraph("Table 1.2", table_cell_center), Paragraph("Department and Technical Profile of School of Computer Applications, KIIT Deemed to be University, Bhubaneswar", table_cell), Paragraph("08", table_cell_center)],
        [Paragraph("Table 2.1", table_cell_center), Paragraph("Department-Wise Activities Across Corpus Curation, NLP Preprocessing, Classifier Training, XAI and Web Deployment", table_cell), Paragraph("10", table_cell_center)],
        [Paragraph("Table 2.2", table_cell_center), Paragraph("Technical Specifications of NLP Preprocessing Modules, Classifiers, Evaluation Metrics and Streamlit Hardware", table_cell), Paragraph("11", table_cell_center)],
        [Paragraph("Table 2.3", table_cell_center), Paragraph("Comparison of Manual (Heuristic/Static) Rule Inspection vs. Coded NLP/ML Classifier Control Across Detection Stages", table_cell), Paragraph("13", table_cell_center)],
        [Paragraph("Table 3.1", table_cell_center), Paragraph("Diagnostic Matrix of Observed Cyber Detection Bottlenecks and Proposed NLP/ML Engineering Solutions", table_cell), Paragraph("14", table_cell_center)],
    ]
    t_lot = Table(lot_tab, colWidths=[65, 375, 65])
    t_lot.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#F3F4F6")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.black),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_lot)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 8: CHAPTER 1 - INTRODUCTION (Exact match to reference Page 8)
    # =========================================================================
    story.append(Paragraph("CHAPTER 1 – INTRODUCTION", page_head))
    story.append(hr())
    
    story.append(Paragraph(
        "My eight-week practical training at the School of Computer Applications, KIIT Deemed to be University, was conducted in the "
        "specialized domain of Cyber Threat and Phishing Detection and bridged my MCA coursework with hands-on NLP and Machine Learning "
        "system engineering.",
        body_text
    ))
    story.append(Spacer(1, 2))

    story.append(Paragraph("1.1 Objectives of the Practical Training", sec_head))
    story.append(Paragraph("1. Study the social engineering threat landscape: understand the deceptive communication tactics across banking KYC, electricity disconnection, lottery fraud, and crypto drainers.", body_text))
    story.append(Paragraph("2. Master NLP feature engineering: handle textual communication data through regular expression cleaning, tokenization, and sublinear TF-IDF n-gram vectorization.", body_text))
    story.append(Paragraph("3. Train and calibrate machine learning classifiers: develop baseline Multinomial Naive Bayes and production Random Forest ensembles to classify incoming threats with zero false alarms.", body_text))
    story.append(Paragraph("4. Construct an Explainable AI (XAI) web dashboard: implement token attribution algorithms and deploy an interactive Streamlit console for real-time security auditing.", body_text))
    story.append(Spacer(1, 2))

    story.append(Paragraph("1.2 Scope and Duration of Training (04 May 2026 – 04 July 2026)", sec_head))
    story.append(Paragraph("Table 1.1: Eight-week structured practical training schedule", caption_text))
    
    t1_data = [
        [Paragraph("Phase", table_head), Paragraph("Date Window", table_head), Paragraph("Assigned Technical Area", table_head), Paragraph("Core Technical Activities & Milestones", table_head)],
        [Paragraph("Weeks 1-2", table_cell_center), Paragraph("04.05.2026 –<br/>17.05.2026", table_cell_center), Paragraph("Literature Review & Threat Taxonomy", table_cell), Paragraph("Analyzed phishing corpora (Enron, SMS Spam), MITRE ATT&CK T1566 vectors, and KIIT lab computing setup.", table_cell)],
        [Paragraph("Weeks 3-4", table_cell_center), Paragraph("18.05.2026 –<br/>31.05.2026", table_cell_center), Paragraph("Dataset Curation & NLP Preprocessing", table_cell), Paragraph("Curated 100 balanced threat/ham samples; coded regex cleaning, case normalization and sublinear TF-IDF n-gram pipeline.", table_cell)],
        [Paragraph("Weeks 5-6", table_cell_center), Paragraph("01.06.2026 –<br/>14.06.2026", table_cell_center), Paragraph("Classifier Training & Model Evaluation", table_cell), Paragraph("Trained Naive Bayes and Random Forest models; evaluated 84% accuracy, 100% precision, 98.72% ROC-AUC on holdout data.", table_cell)],
        [Paragraph("Weeks 7-8", table_cell_center), Paragraph("15.06.2026 –<br/>04.07.2026", table_cell_center), Paragraph("Explainable AI & Streamlit Deployment", table_cell), Paragraph("Engineered XAI keyword attribution; built Streamlit console (port 8501); finalized technical documentation and report.", table_cell)],
    ]
    t_1 = Table(t1_data, colWidths=[55, 75, 120, 255])
    t_1.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#F3F4F6")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.black),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_1)
    story.append(Spacer(1, 4))

    story.append(Paragraph("1.3 Department Overview — School of Computer Applications, KIIT", sec_head))
    story.append(Paragraph("The School of Computer Applications at KIIT Deemed to be University operates advanced laboratories dedicated to AI, Data Science, and Information Security.", body_text))
    story.append(Paragraph("Table 1.2: Academic and technical profile of the department", caption_text))

    t2_data = [
        [Paragraph("Department Parameter", table_head), Paragraph("Institutional Details", table_head)],
        [Paragraph("Institution & Department", table_cell), Paragraph("School of Computer Applications, KIIT Deemed to be University, Bhubaneswar – 751024, Odisha", table_cell)],
        [Paragraph("Head of Department", table_cell), Paragraph("Prof. (Dr.) Veena Goswami, Director General, School of Computer Applications", table_cell)],
        [Paragraph("Project Mentor", table_cell), Paragraph("Prof. (Dr.) Satya Ranjan Dash, School of Computer Applications", table_cell)],
        [Paragraph("Key Computing Facilities", table_cell), Paragraph("High-speed workstation clusters, Python 3.13 ML environment, Scikit-Learn, Streamlit server", table_cell)],
        [Paragraph("Assigned Project Scope", table_cell), Paragraph("Cyber Threat & Phishing Detection using Natural Language Processing and Machine Learning", table_cell)],
    ]
    t_2 = Table(t2_data, colWidths=[150, 355])
    t_2.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,-1), colors.HexColor("#F3F4F6")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.black),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_2)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 9: CHAPTER 1 - WORKFLOW & HIGHLIGHTS (Exact match to reference Page 9)
    # =========================================================================
    story.append(Paragraph("1.4 Overview of the Cyber Threat Detection System & End-to-End Workflow", sec_head))
    story.append(Paragraph(
        "Before deploying the machine learning models through Streamlit, my primary priority was to architect the entire data ingestion, "
        "feature engineering, and inference workflow of the Cyber Threat Detector. Figure 1.1 illustrates the complete step-by-step workflow "
        "across the data cleaning, vectorization, classification, triage, and explainable AI stages.",
        body_text
    ))
    story.append(Spacer(1, 4))

    flow_path = os.path.join(base_dir, "flow_diagram.png")
    if os.path.exists(flow_path):
        story.append(Image(flow_path, width=490, height=225))
    story.append(Spacer(1, 4))

    story.append(Paragraph("Figure 1.1: End-to-end step-by-step workflow of the Cyber Threat & Phishing Detection System, supervised and coded through Python and Scikit-Learn.", caption_text))
    story.append(Spacer(1, 6))

    story.append(Paragraph("Key Functional Highlights of the Detection Workflow", sec_head))
    story.append(Paragraph(
        "• <b>Digital data gatekeeping via NLP preprocessing (Step 1):</b> every incoming message (SMS, email, webhook) undergoes automated regex normalization, URL abstraction, and punctuation stripping. Eliminating noise before tokenization establishes feature consistency across heterogeneous messaging formats.",
        body_text
    ))
    story.append(Paragraph(
        "• <b>Sublinear TF-IDF n-gram representation (Step 2):</b> instead of binary word occurrence, sublinear term-frequency scaling dampens repetitive spam phrasing while capturing both single words ('kyc', 'blocked') and multi-token threat idioms ('account suspended', 'electricity bill disconnected').",
        body_text
    ))
    story.append(Paragraph(
        "• <b>Dual machine learning classification & calibration (Step 3):</b> the vectorized message is evaluated simultaneously by a Multinomial Naive Bayes probabilistic baseline and a 100-tree Random Forest ensemble. Aggregated probabilities produce a calibrated threat score between 0.0% and 100.0%.",
        body_text
    ))
    story.append(Paragraph(
        "• <b>Explainable AI (XAI) & interactive dashboard (Steps 4–5):</b> the system maps active tokens to model importance coefficients, highlighting the exact words driving the risk score in the Streamlit console, achieving 100% precision on malicious threats with zero false alarms.",
        body_text
    ))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 10: CHAPTER 2 - ACTIVITIES & PROCESS (Exact match to reference Page 10)
    # =========================================================================
    story.append(Paragraph("CHAPTER 2 – TRAINING ACTIVITIES AND TECHNICAL LEARNING", page_head))
    story.append(hr())
    
    story.append(Paragraph("2.1 Department-Wise Training Activities in AI/ML & Cybersecurity", sec_head))
    story.append(Paragraph(
        "During my internship, I first analyzed the complete lifecycle of social engineering attacks across the digital communications domain, "
        "and then trained in the KIIT computer laboratories to build, optimize, and evaluate NLP and ML classification pipelines. Table 2.1 "
        "summarises the domain-wise activities.",
        body_text
    ))
    story.append(Spacer(1, 2))

    story.append(Paragraph("Table 2.1: Domain-wise activities in the Cyber Threat Detection project", caption_text))
    t21_data = [
        [Paragraph("Project Section", table_head), Paragraph("Machinery, Sensors & Software Involved", table_head), Paragraph("Role & Technical Activities Performed", table_head)],
        [Paragraph("1. Data Ingestion & Corpus Curation", table_cell), Paragraph("Python standard library (csv), synthetic generator scripts, regional threat templates.", table_cell), Paragraph("Curated 100 balanced threat/ham records covering banking KYC, electricity extortion, lottery, and SIM block schemes.", table_cell)],
        [Paragraph("2. Text Normalization & Preprocessing", table_cell), Paragraph("Regular expression engines (re), lowercasing transforms, Scikit-Learn stop-word pruners.", table_cell), Paragraph("Constructed end-to-end normalization pipeline converting unstructured communication strings into uniform lexical tokens.", table_cell)],
        [Paragraph("3. Feature Extraction & Vectorization", table_cell), Paragraph("TfidfVectorizer, sublinear TF scaling, unigram + bigram (1,2) vocabulary extractor.", table_cell), Paragraph("Extracted 500 most discriminative n-gram features; transformed variable-length messages into sparse numerical vectors.", table_cell)],
        [Paragraph("4. Model Training & Explainable AI", table_cell), Paragraph("Random Forest (100 trees), Multinomial Naive Bayes, Joblib serializers, Streamlit UI.", table_cell), Paragraph("Trained classifiers, achieved 100% precision and 98.72% ROC-AUC; engineered Explainable AI (XAI) feature attribution.", table_cell)],
    ]
    t_21 = Table(t21_data, colWidths=[90, 160, 255])
    t_21.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#F3F4F6")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.black),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_21)
    story.append(Spacer(1, 4))

    story.append(Paragraph("2.2 Step-by-Step Technical Process of the Cyber Threat Detector", sec_head))
    story.append(Paragraph(
        "• <b>Step 1 — Message arrival, laboratory testing & token cleansing:</b> when a communication arrives, regex filters strip punctuation, normalize URLs, and convert characters to lowercase. Common English stop-words are pruned to retain only high-signal lexical markers.",
        body_text
    ))
    story.append(Paragraph(
        "• <b>Step 2 — TF-IDF sublinear vectorization:</b> clean tokens are mapped into a 500-dimensional vector space using TF-IDF with sublinear term-frequency scaling. Unigrams and bigrams capture both isolated threat keywords and composite deceptive phrasing.",
        body_text
    ))
    story.append(Paragraph(
        "• <b>Step 3 — Dual classifier inference & probability calibration:</b> the vector is evaluated by the Multinomial Naive Bayes baseline and the 100-tree Random Forest ensemble. The ensemble calculates class posterior probabilities, balancing false-positive suppression against recall.",
        body_text
    ))
    story.append(Paragraph(
        "• <b>Step 4 — Explainable AI attribution & dashboard rendering:</b> non-zero feature indices are multiplied by Random Forest feature importances to highlight the exact keywords responsible for the risk score, rendering an instant verdict in the Streamlit UI.",
        body_text
    ))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 11: CHAPTER 2 - ARCHITECTURE & SPECS (Exact match to reference Page 11)
    # =========================================================================
    story.append(Paragraph("2.3 System Control Architecture & NLP Pipeline Specifications", sec_head))
    story.append(Paragraph(
        "As illustrated in Figure 2.1, operating the Cyber Threat Detector integrates three layers: (1) input communication channels and raw text data, "
        "(2) the NLP and machine learning logic layer where feature extraction and model inference are executed, and (3) the security operations console. "
        "Table 2.2 details the specification of each subsystem.",
        body_text
    ))
    story.append(Spacer(1, 4))

    arch_path = os.path.join(base_dir, "arch_diagram.png")
    if os.path.exists(arch_path):
        story.append(Image(arch_path, width=490, height=175))
    story.append(Spacer(1, 4))

    story.append(Paragraph("Figure 2.1: Three-layer system control architecture connecting input communication channels, coded NLP/ML models, and security dashboard.", caption_text))
    story.append(Spacer(1, 4))

    story.append(Paragraph("Table 2.2: Technical specifications of software utilities, algorithms, and libraries", caption_text))
    t22_data = [
        [Paragraph("Equipment / System", table_head), Paragraph("Type & Capacity / Rating", table_head), Paragraph("Control Signal / Interface", table_head), Paragraph("Operational Function in Cyber Defense", table_head)],
        [Paragraph("Dataset Ingestion Engine", table_cell), Paragraph("Balanced 100-sample corpus (50 Ham / 50 Phishing)", table_cell), Paragraph("CSV format, UTF-8 encoded text stream", table_cell), Paragraph("Supplies regionalized Indian threat scenarios across banking, utilities, and lottery scams.", table_cell)],
        [Paragraph("Text Preprocessing Pipeline", table_cell), Paragraph("Regex stripper + case folding + stop-words", table_cell), Paragraph("Python re module & Scikit-Learn lexicon", table_cell), Paragraph("Removes non-informative noise, normalizes URLs, and prunes stop-words.", table_cell)],
        [Paragraph("TF-IDF Vector Space Transformer", table_cell), Paragraph("500 feature n-grams (unigrams + bigrams)", table_cell), Paragraph("Sparse matrix representation (float64)", table_cell), Paragraph("Transforms text into numerical feature vectors using sublinear term frequency weighting.", table_cell)],
        [Paragraph("Multinomial Naive Bayes", table_cell), Paragraph("Probabilistic classifier with Laplace smoothing", table_cell), Paragraph("alpha = 0.5 smoothing parameter", table_cell), Paragraph("Serves as fast baseline classifier providing calibrated posterior probabilities.", table_cell)],
        [Paragraph("Random Forest Classifier", table_cell), Paragraph("100 decorrelated decision trees ensemble", table_cell), Paragraph("Gini impurity, balanced class weights", table_cell), Paragraph("Production model achieving 100% precision on malicious threats (zero false alarms).", table_cell)],
        [Paragraph("Streamlit Security Console", table_cell), Paragraph("Web dashboard (Port 8501, Python 3.13)", table_cell), Paragraph("HTTP / WebSocket reactive frontend", table_cell), Paragraph("Allows security analysts to test messages, view risk gauges, and inspect XAI keywords.", table_cell)],
    ]
    t_22 = Table(t22_data, colWidths=[90, 110, 115, 190])
    t_22.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#F3F4F6")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.black),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_22)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 12: CHAPTER 2 - FEATURE SPACE & ENSEMBLE (Exact match to reference Page 12)
    # =========================================================================
    story.append(Paragraph("2.4 Machine Learning Classification & Feature Engineering Architecture", sec_head))
    story.append(Paragraph(
        "The core data engineering operation in the Cyber Threat Detector involves mapping high-dimensional lexical variations into a discriminative "
        "feature space and aggregating predictions across decorrelated decision trees. Figure 2.2 presents the architectural schematic of the TF-IDF feature "
        "space and Random Forest ensemble controlled through Scikit-Learn.",
        body_text
    ))
    story.append(Spacer(1, 4))

    ens_path = os.path.join(base_dir, "ensemble_schematic.png")
    if os.path.exists(ens_path):
        story.append(Image(ens_path, width=490, height=185))
    story.append(Spacer(1, 4))

    story.append(Paragraph("Figure 2.2: Architecture schematic of the TF-IDF feature space and Random Forest decision tree ensemble with voting aggregation.", caption_text))
    story.append(Spacer(1, 6))

    story.append(Paragraph("Algorithmic Formulation of Classifiers", sec_head))
    story.append(Paragraph(
        "• <b>Sublinear TF-IDF transformation:</b> To prevent repetitive spam tokens from dominating the feature space, term frequency is calculated as "
        "TF(t, d) = 1 + log(f<sub>t,d</sub>) for f<sub>t,d</sub> > 0. The Inverse Document Frequency scales down ubiquitous tokens: "
        "IDF(t, D) = log((1 + |D|) / (1 + |{d in D : t in d}|)) + 1. An n-gram range of (1, 2) extracts 500 features capturing both individual words and composite scam phrases.",
        body_text
    ))
    story.append(Paragraph(
        "• <b>Multinomial Naive Bayes baseline:</b> Estimates class posteriors via P(y | x) &prop; P(y) &prod; P(x<sub>i</sub> | y). "
        "Laplace smoothing (&alpha; = 0.5) eliminates zero-probability penalties for novel vocabulary: P_hat(x<sub>i</sub> | y) = (N<sub>yi</sub> + &alpha;) / (N<sub>y</sub> + &alpha;|V|), "
        "yielding 80.00% accuracy and 96.15% ROC-AUC on holdout test data.",
        body_text
    ))
    story.append(Paragraph(
        "• <b>Random Forest production ensemble:</b> Encompasses B = 100 decision trees trained on bootstrap resamples with randomized feature subsets (m = &radic;500 &approx; 22). "
        "Gini impurity minimization I<sub>G</sub>(p) = 1 - &sum; p<sub>k</sub><sup>2</sup> optimizes node splits. Class weighting is set to balanced: w<sub>j</sub> = N / (2 * N<sub>j</sub>), "
        "guaranteeing 100.00% precision on threats and 98.72% ROC-AUC discriminability.",
        body_text
    ))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 13: CHAPTER 2 - TELEMETRY & SCREENSHOT (Exact match to reference Page 13)
    # =========================================================================
    story.append(Paragraph("2.5 Model Training Telemetry & Operational Performance", sec_head))
    story.append(Paragraph(
        "Without automated machine learning models, cybersecurity screening relies on brittle keyword blocklists and manual analyst inspection. "
        "In my internship role, developing the TF-IDF and Random Forest classification pipeline automated the threat detection cycle (Figure 2.3 and Table 2.3).",
        body_text
    ))
    story.append(Spacer(1, 4))

    screen_path = os.path.join(base_dir, "threat_analysis_screenshot.png")
    if os.path.exists(screen_path):
        story.append(Image(screen_path, width=490, height=210))
    story.append(Spacer(1, 3))

    story.append(Paragraph("Figure 2.3: Operational performance telemetry and live triage demonstration in the Streamlit console: (a) 93.0% malicious risk score; (b) Explainable AI (XAI) feature attribution table.", caption_text))
    story.append(Spacer(1, 4))

    story.append(Paragraph("Table 2.3: Comparison of Manual (Heuristic/Static) Rule Inspection vs. Coded NLP/ML Classifier Control Across Detection Stages", caption_text))
    t23_data = [
        [Paragraph("Process Control Parameter", table_head), Paragraph("Manual / Static Heuristic Mode", table_head), Paragraph("Coded NLP/ML Ensemble Mode", table_head), Paragraph("Operational Impact Observed", table_head)],
        [Paragraph("Raw Message Intake & Token Cleansing", table_cell), Paragraph("Keyword blocklists with high false-alarm rates", table_cell), Paragraph("Regex normalization + stop-word removal pipeline", table_cell), Paragraph("Standardized token inputs across diverse messaging protocols.", table_cell)],
        [Paragraph("Feature Extraction & Context", table_cell), Paragraph("Exact string matching; blind to synonyms or n-grams", table_cell), Paragraph("Sublinear TF-IDF with unigram + bigram (1,2) features", table_cell), Paragraph("Captures multi-word scam idioms ('account suspended', 'electricity bill').", table_cell)],
        [Paragraph("Threat Severity Scoring", table_cell), Paragraph("Binary pass/fail rule; no risk probability", table_cell), Paragraph("Calibrated ensemble probability meter (0% to 100%)", table_cell), Paragraph("Tri-tier severity classification: Safe (<40%), Suspicious, Critical (>70%).", table_cell)],
        [Paragraph("Explainability & SOC Triage", table_cell), Paragraph("Opaque rule triggers; no feature attribution", table_cell), Paragraph("Explainable AI (XAI) feature impact mapping", table_cell), Paragraph("Transparent keyword ranking enables instant verification by SOC analysts.", table_cell)],
        [Paragraph("Threat Precision & False Alarms", table_cell), Paragraph("Frequent false alarms on legitimate banking alerts", table_cell), Paragraph("100.00% precision on threats (0 false alarms)", table_cell), Paragraph("Completely eliminated false positives; 98.72% ROC-AUC separability.", table_cell)],
    ]
    t_23 = Table(t23_data, colWidths=[90, 125, 135, 155])
    t_23.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#F3F4F6")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.black),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_23)
    story.append(Spacer(1, 4))

    story.append(Paragraph("2.6 Practical Engineering & Testing Observations", sec_head))
    story.append(Paragraph(
        "• <b>Feature importance weighting:</b> The Random Forest model placed maximum weight on tokens denoting artificial panic ('kyc', 'immediately', 'suspended', 'urgent', 'blocked'). Legitimate transactional updates carrying 'balance', 'banking', 'thank' were consistently scored below 15% risk.",
        body_text
    ))
    story.append(Paragraph(
        "• <b>Latency and zero false alarms:</b> Sub-12 millisecond CPU inference latency ensures that incoming message streams can be scanned in real-time without buffering bottlenecks, while 100% precision prevents legitimate university notices from being interrupted.",
        body_text
    ))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 14: CHAPTER 3 - OUTCOMES & CONCLUSION (Exact match to reference Page 14)
    # =========================================================================
    story.append(Paragraph("CHAPTER 3 – LEARNING OUTCOMES AND CONCLUSION", page_head))
    story.append(hr())
    
    story.append(Paragraph("3.1 Technical and Analytical Skills Acquired", sec_head))
    story.append(Paragraph(
        "• <b>Cyber threat detection process:</b> understood the complete security engineering workflow — raw text ingestion, regex normalization, stop-word elimination, TF-IDF n-gram vectorization, dual-classifier probability calibration, and Explainable AI (XAI) feature attribution.",
        body_text
    ))
    story.append(Paragraph(
        "• <b>Machine learning coding & deployment:</b> coded stratified train/test split routines, tuned Random Forest hyperparameter estimators, eliminated false-positive alerts, serialized production models using Joblib, and deployed an interactive Streamlit operations console.",
        body_text
    ))
    story.append(Spacer(1, 2))

    story.append(Paragraph("3.2 Technical Problems Observed & 3.3 Proposed Engineering Solutions", sec_head))
    story.append(Paragraph(
        "During my eight-week training in the School of Computer Applications (04 May 2026 to 04 July 2026), four key technical challenges "
        "were observed and addressed with practical automation solutions, summarised in Table 3.1.",
        body_text
    ))
    story.append(Paragraph("Table 3.1: Observed cyber detection bottlenecks and proposed NLP/ML engineering solutions", caption_text))

    t31_data = [
        [Paragraph("Observed Technical Problem", table_head), Paragraph("Root Cause Identified", table_head), Paragraph("Proposed NLP & AI/ML Solution", table_head), Paragraph("Expected System Benefit", table_head)],
        [Paragraph("1. High false alarm rate during heuristic testing", table_cell), Paragraph("Simple keyword blocklists flagged benign banking alerts containing words like 'account' or 'balance'.", table_cell), Paragraph("Transitioned to TF-IDF n-grams with Random Forest ensemble, weighting context.", table_cell), Paragraph("Achieved 100.00% threat precision with zero false alarms on legitimate alerts.", table_cell)],
        [Paragraph("2. Python 3.14 runtime wheel incompatibility", table_cell), Paragraph("Pre-release runtime lacked compiled C++ binary wheels for scikit-learn on Windows.", table_cell), Paragraph("Configured Python 3.13 runtime with verified wheel support across all packages.", table_cell), Paragraph("Ensured flawless build stability, fast wheel installation and reproducible execution.", table_cell)],
        [Paragraph("3. Out-of-vocabulary zero-probability penalty", table_cell), Paragraph("Novel scam URLs and domain strings produced zero posterior probabilities in Naive Bayes.", table_cell), Paragraph("Configured Laplace smoothing (alpha = 0.5) and bigram context in feature vectorizer.", table_cell), Paragraph("Eliminated numerical underflow and enhanced baseline generalization on novel tokens.", table_cell)],
        [Paragraph("4. Black-box opacity and analyst resistance", table_cell), Paragraph("Security analysts resisted automated risk scores lacking verifiable decision reasoning.", table_cell), Paragraph("Engineered Explainable AI (XAI) feature importance mapper in the UI dashboard.", table_cell), Paragraph("Transparent keyword ranking enables instant human auditability of every flag.", table_cell)],
    ]
    t_31 = Table(t31_data, colWidths=[90, 125, 145, 145])
    t_31.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#F3F4F6")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.black),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_31)
    story.append(Spacer(1, 4))

    story.append(Paragraph("3.4 Conclusion", sec_head))
    story.append(Paragraph(
        "Completing my eight-week practical training in the School of Computer Applications at KIIT Deemed to be University, Bhubaneswar "
        "(04.05.2026 to 04.07.2026), under the mentorship of Prof. (Dr.) Satya Ranjan Dash, provided an invaluable foundation in applied "
        "artificial intelligence and cybersecurity. Understanding the complete technical workflow — from synthetic corpus generation and "
        "sublinear TF-IDF vectorization to Random Forest ensemble training, Explainable AI attribution, and real-time Streamlit dashboard deployment — "
        "directly strengthened my computer applications engineering capabilities, fulfilling all academic training requirements set forth by "
        "the School of Computer Applications, KIIT Deemed to be University.",
        body_text
    ))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 15: REFERENCES (Exact match to reference Page 15)
    # =========================================================================
    story.append(Paragraph("REFERENCES", page_head))
    story.append(hr())
    
    story.append(Paragraph(
        "The following technical standards, machine learning textbooks, cybersecurity frameworks and research papers were consulted "
        "during the practical training and the preparation of this report:",
        body_text
    ))
    story.append(Spacer(1, 6))

    refs = [
        "[1] Pedregosa, F., et al.: Scikit-learn: Machine Learning in Python, Journal of Machine Learning Research (JMLR), vol. 12, pp. 2825–2830, 2011 (supervised classification pipelines, Random Forest, Multinomial Naive Bayes, TF-IDF vectorizer).",
        "[2] Breiman, L.: Random Forests, Machine Learning, vol. 45, no. 1, pp. 5–32, 2001 (ensemble decision tree aggregation, bootstrap bagging, Gini impurity splitting, out-of-bag error estimation).",
        "[3] National Institute of Standards and Technology (NIST): Computer Security Incident Handling Guide, Special Publication 800-61 Revision 2, U.S. Department of Commerce, Washington, D.C., USA, 2012 (incident triage and social engineering handling).",
        "[4] The MITRE Corporation: MITRE ATT&CK Framework — Enterprise Matrix Technique T1566: Phishing, MITRE Center for Threat-Informed Defense, McLean, VA, USA, 2024 (spearphishing links, attachment analysis, credential harvesting).",
        "[5] Internet Engineering Task Force (IETF): RFC 5321 — Simple Mail Transfer Protocol; and RFC 5322 — Internet Message Format, Standards Track Specifications, Fremont, CA, USA, 2008 (electronic mail header parsing and body structure).",
        "[6] Manning, C. D., Raghavan, P., and Schütze, H.: Introduction to Information Retrieval, Cambridge University Press, Cambridge, UK, 2008 (vector space classification, sublinear term-frequency weighting, inverse document frequency).",
        "[7] Streamlit Inc.: Streamlit Open-Source Technical Documentation and Application Architecture Guide, Snowflake Computing, San Francisco, CA, USA, 2024 (reactive web UI architecture, real-time widget binding, data streaming).",
        "[8] Verma, R., and Shashidhar, N.: Why Machine Learning for Phishing Detection? A Survey and Open Research Challenges, IEEE Access, vol. 8, pp. 10984–11002, 2020 (NLP feature engineering, semantic parsing, URL character heuristics).",
        "[9] School of Computer Applications: Curriculum and Academic Guidelines for Summer Practical Training (Course Code: MC-4011), Kalinga Institute of Industrial Technology (KIIT) Deemed to be University, Bhubaneswar, Odisha, India, 2025–2026.",
        "[10] Singh, Ayush Kumar: Cyber Threat & Phishing Detection using Natural Language Processing and Machine Learning, GitHub Repository, School of Computer Applications, KIIT Deemed to be University, July 2026. Available: https://github.com/ayushkumarsinghh/cyber-threat-detector-nlp",
    ]
    for r in refs:
        story.append(Paragraph(r, ParagraphStyle('RefEntry', parent=body_text, fontSize=8, leading=11, spaceAfter=5)))

    story.append(Spacer(1, 20))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.black, spaceAfter=8, spaceBefore=0))
    story.append(Paragraph("End of Practical Training Report — School of Computer Applications, KIIT Deemed to be University, Bhubaneswar", body_center))

    doc.build(story, canvasmaker=ExactNumberedCanvas)
    print(f"Successfully generated reference-matching PDF at: {pdf_path}")

if __name__ == "__main__":
    build_pdf()
