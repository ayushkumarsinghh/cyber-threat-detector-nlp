# PRACTICAL TRAINING REPORT (MC-4011)

---

# CYBER THREAT AND PHISHING DETECTION USING NATURAL LANGUAGE PROCESSING AND MACHINE LEARNING

**A Practical Training Report submitted in partial fulfillment of the requirements for the Summer Internship Program**

**Academic Session: 2025 - 2026**

---

### Submitted By:
**Name:** AYUSH KUMAR SINGH  
**Program:** Master of Computer Applications / Bachelor of Computer Applications  
**School:** School of Computer Applications  
**Institution:** Kalinga Institute of Industrial Technology (KIIT) Deemed to be University  
**Campus:** Bhubaneswar, Odisha - 751024, India  

---

### Under the Supervision and Mentorship of:
**Faculty Mentors & Project Supervisors**  
School of Computer Applications  
KIIT Deemed to be University, Bhubaneswar  

---

**July 2026**

--- [PAGE BREAK: PAGE 1 OF 15] ---

## CERTIFICATE OF PRACTICAL TRAINING

### SCHOOL OF COMPUTER APPLICATIONS
**KALINGA INSTITUTE OF INDUSTRIAL TECHNOLOGY (KIIT)**  
*Deemed to be University U/S 3 of UGC Act, 1956*  
**Bhubaneswar - 751024, Odisha, India**

---

This is to certify that **AYUSH KUMAR SINGH**, a bonafide student of the **School of Computer Applications, KIIT Deemed to be University**, has successfully undergone and completed his 8-Week Practical Training / Summer Internship titled:

### "CYBER THREAT AND PHISHING DETECTION USING NATURAL LANGUAGE PROCESSING AND MACHINE LEARNING"

commencing from **04th May 2026 to 04th July 2026** at the School of Computer Applications, KIIT Deemed to be University.

The practical training encompassed rigorous conceptual study, experimental design, and practical software engineering in the specialized domains of **Artificial Intelligence, Machine Learning, Cybersecurity, Image Processing, and Natural Language Processing (NLP)**.

He has completed this project work under our guidance and supervision. To the best of our knowledge, the results, models, and documentation presented in this report represent authentic and original work carried out by the candidate and have not been submitted elsewhere for the award of any other degree, diploma, or fellowship.

We commend his diligence, technical aptitude, and problem-solving abilities demonstrated throughout the internship tenure.

---

**Date:** 04th July 2026  
**Place:** Bhubaneswar, Odisha  

---

```
____________________________                    ____________________________
Project Supervisor / Mentor                     Prof. (Dr.) Veena Goswami
School of Computer Applications                 Director General
KIIT Deemed to be University                    School of Computer Applications
Bhubaneswar, Odisha                             KIIT Deemed to be University
```

--- [PAGE BREAK: PAGE 2 OF 15] ---

## CANDIDATE'S DECLARATION

I, **AYUSH KUMAR SINGH**, hereby declare that the practical training report entitled **"CYBER THREAT AND PHISHING DETECTION USING NATURAL LANGUAGE PROCESSING AND MACHINE LEARNING"** submitted to the **School of Computer Applications, KIIT Deemed to be University, Bhubaneswar**, is an authentic record of independent technical and practical work carried out by me during the period from **04th May 2026 to 04th July 2026**.

I further declare that this report has been prepared by me under the academic mentorship of the faculty members of the School of Computer Applications, KIIT Deemed to be University. The matter embodied in this report has not been submitted by me or any other individual for the award of any other academic degree, diploma, or certificate in this or any other university or institution.

All literature, software libraries, algorithms, and technical standards referred to in the execution of this work have been duly cited and acknowledged in the references section.

---

**Signature of the Candidate:** _______________________________  
**Name of the Candidate:** AYUSH KUMAR SINGH  
**Date:** 04th July 2026  
**Place:** Bhubaneswar, Odisha  

---

### CANDIDATE & TRAINING PROFILE

| Academic Attribute | Details |
| :--- | :--- |
| Candidate Name | Ayush Kumar Singh |
| Department | School of Computer Applications |
| University | Kalinga Institute of Industrial Technology (KIIT) Deemed to be University |
| Internship Program | 8-Week Practical Training / Summer Internship (2026) |
| Internship Duration | 04.05.2026 to 04.07.2026 (8 Weeks) |
| Course / Subject Code | MC-4011 (Practical Training / Summer Internship) |
| Academic Session | 2025 - 2026 |
| Target Domain | Artificial Intelligence, Machine Learning, NLP & Cybersecurity |
| Repository URL | https://github.com/ayushkumarsinghh/cyber-threat-detector-nlp |

--- [PAGE BREAK: PAGE 3 OF 15] ---

## ACKNOWLEDGEMENT

The satisfaction and technical accomplishment that accompany the successful completion of an 8-week practical training project would be incomplete without expressing my sincere gratitude to all the individuals who provided guidance, mentorship, and encouragement throughout this journey.

First and foremost, I express my deepest veneration and profound gratitude to the visionary founder of KIIT & KISS, **Prof. (Dr.) Achyuta Samanta**, whose relentless pursuit of academic excellence, world-class infrastructure, and inspiring leadership have established an environment where technical innovation and practical research thrive.

I convey my respectful and heartfelt gratitude to **Prof. (Dr.) Veena Goswami**, Director General, School of Computer Applications, KIIT Deemed to be University, for her constant encouragement, strategic academic leadership, and for granting the necessary computing facilities and administrative support to undertake this rigorous summer training program.

I am immensely indebted to my **Project Supervisors and Faculty Mentors** in the School of Computer Applications for their insightful technical suggestions, thorough code reviews, and structured academic direction. Their constructive critiques on natural language feature extraction, machine learning evaluation methodologies, and model calibration were pivotal to the success of this cyber threat detection system.

I extend my appreciation to the technical and administrative staff of the computer laboratories at the School of Computer Applications for maintaining robust high-speed development servers, network connectivity, and computational infrastructure throughout the 8-week internship period.

Finally, I express my sincere appreciation to my parents, family members, and peer student colleagues whose steadfast moral support, patience, and motivation sustained my focus throughout the preparation of this project and report.

---

**AYUSH KUMAR SINGH**  
School of Computer Applications  
KIIT Deemed to be University, Bhubaneswar  
Date: 04th July 2026  

--- [PAGE BREAK: PAGE 4 OF 15] ---

## ABSTRACT

Digital communications, including electronic mail (email), short message service (SMS), and instant messaging networks, have become the primary attack surface for malicious cyber actors. Social engineering vectors such as deceptive phishing, smishing, financial extortion, and impersonation fraud account for over 80% of unauthorized access incidents globally. Traditional static security countermeasures, including rule-based keyword blocklists and domain blacklisting, suffer from high latency, susceptibility to adversarial evasion (e.g., typographical manipulation), and inability to assess contextual semantic intent.

This practical training report documents the design, mathematical formulation, implementation, and deployment of **CyberShield NLP**, an end-to-end Machine Learning and Natural Language Processing system for real-time cyber threat detection and explainable triage. Developed during an 8-week summer internship (04.05.2026 to 04.07.2026) at the School of Computer Applications, KIIT Deemed to be University, the project delivers:

1. **Balanced Security Corpus Generation**: A curated dataset of 100 domain-authentic samples spanning critical legitimate communications (banking transaction alerts, academic updates, salary credits) and adversarial threat vectors (urgent KYC suspension scams, SIM deactivation frauds, electricity disconnection extortion, and crypto asset drainers).
2. **Feature Engineering Pipeline**: A Term Frequency-Inverse Document Frequency (TF-IDF) vectorizer extracting unigram and bigram token sequences with sublinear term-frequency scaling and stop-word elimination.
3. **Dual Machine Learning Classification**: Comparative training of a baseline Multinomial Naive Bayes classifier ($80.00\%$ accuracy, $96.15\%$ ROC-AUC) against a production Random Forest ensemble ($84.00\%$ accuracy, $100.00\%$ precision on malicious threats, $98.72\%$ ROC-AUC).
4. **Explainable AI (XAI) Attribution**: Transparent token-level contribution scoring that identifies high-risk lexical indicators (e.g., 'kyc', 'urgent', 'suspended', 'immediately') responsible for the classified risk score.
5. **Operational Web Console**: An interactive Streamlit dashboard enabling real-time multi-channel communication testing, scenario simulation, and visual threat telemetry without requiring specialized GPU hardware.

### EXECUTIVE PROJECT SUMMARY TABLE

| Dimension | Specification |
| :--- | :--- |
| Project Title | Cyber Threat & Phishing Detection using NLP and Machine Learning |
| Candidate | Ayush Kumar Singh (KIIT School of Computer Applications) |
| Core Technologies | Python 3.13, Scikit-Learn, Pandas, NumPy, Streamlit, Joblib |
| Feature Extraction | TF-IDF (Unigram + Bigram, 500 features, Sublinear TF) |
| Best Performing Model | Random Forest Classifier (100 Estimators, Gini Index) |
| Threat Precision | 100.00% (Zero False Alarms on Benign Communications) |
| ROC-AUC Score | 98.72% Discrimination Capability |
| Inference Latency | < 12 milliseconds per input message on standard CPU |

--- [PAGE BREAK: PAGE 5 OF 15] ---

## TABLE OF CONTENTS

- **Title Page** ............................................................................................ Page 1
- **Certificate of Practical Training** ................................................................. Page 2
- **Candidate's Declaration & Profile** ............................................................. Page 3
- **Acknowledgement** .................................................................................. Page 4
- **Abstract & Executive Summary** ................................................................. Page 5
- **Table of Contents** .................................................................................... Page 6
- **List of Figures and Tables** ....................................................................... Page 7

---

### CHAPTER 1: INTRODUCTION & TRAINING OBJECTIVES ................................... Page 8
- 1.1 Background & Threat Landscape Formulation ............................................. Page 8
- 1.2 Objectives of the 8-Week Practical Training ................................................ Page 8
- 1.3 8-Week Training Schedule & Milestones (Weekly Roadmap) ............................. Page 8
- 1.4 Attack Vector Taxonomy (Phishing, Smishing, Extortion) ................................ Page 9
- 1.5 High-Level System Architecture & Flowchart ............................................... Page 9

---

### CHAPTER 2: TECHNICAL METHODOLOGY & IMPLEMENTATION .......................... Page 10
- 2.1 Dataset Construction & Threat Categorization ............................................ Page 10
- 2.2 Text Normalization & Preprocessing Pipeline ............................................. Page 10
- 2.3 Feature Engineering: TF-IDF Vector Space Model ........................................ Page 11
- 2.4 Mathematical Formulation of Classifiers .................................................... Page 11
  - 2.4.1 Multinomial Naive Bayes (Baseline) ................................................... Page 11
  - 2.4.2 Random Forest Classifier (Production Ensemble) .................................... Page 12
- 2.5 Explainable AI (XAI) & Keyword Impact Attribution .................................... Page 12
- 2.6 Empirical Evaluation Telemetry & Confusion Matrix ..................................... Page 13
- 2.7 Interactive Security Dashboard Architecture .............................................. Page 13

---

### CHAPTER 3: LEARNING OUTCOMES & CONCLUSION ...................................... Page 14
- 3.1 Practical Skills & Technical Competencies Acquired ..................................... Page 14
- 3.2 Problem-Solution Diagnostic Matrix ........................................................ Page 14
- 3.3 System Limitations & Future Research Directions ........................................ Page 14
- 3.4 Concluding Remarks ............................................................................. Page 14

---

### REFERENCES & TECHNICAL STANDARDS .................................................... Page 15

--- [PAGE BREAK: PAGE 6 OF 15] ---

## LIST OF FIGURES AND TABLES

### LIST OF TABLES

| Table Number | Table Title | Page |
| :--- | :--- | :--- |
| Table 1.1 | Candidate and Training Profile | Page 3 |
| Table 1.2 | Executive Project Summary Specifications | Page 5 |
| Table 1.3 | 8-Week Summer Internship Milestone Schedule | Page 8 |
| Table 2.1 | Social Engineering Attack Vector Categories & Signatures | Page 9 |
| Table 2.2 | Threat Dataset Distribution & Domain Allocation | Page 10 |
| Table 2.3 | Classifier Hyperparameter Specifications | Page 12 |
| Table 2.4 | Model Performance Telemetry & Comparison Matrix | Page 13 |
| Table 2.5 | Random Forest Confusion Matrix Breakdown | Page 13 |
| Table 3.1 | Technical Challenges & Resolution Diagnostic Matrix | Page 14 |

---

### LIST OF FIGURES

| Figure Number | Figure Title | Page |
| :--- | :--- | :--- |
| Figure 1.1 | End-to-End System Pipeline and Threat Scoring Architecture | Page 9 |
| Figure 2.1 | TF-IDF Sublinear Feature Extraction Flowchart | Page 11 |
| Figure 2.2 | Random Forest Ensemble Decision Tree Aggregation | Page 12 |
| Figure 2.3 | Explainable AI (XAI) Token Attribution and Threat Gauge | Page 13 |

--- [PAGE BREAK: PAGE 7 OF 15] ---

## CHAPTER 1: INTRODUCTION & TRAINING OBJECTIVES

### 1.1 Background & Threat Landscape Formulation
As enterprise digital transformation expands, human communication channels (e-mails, SMS, corporate messaging) have emerged as the softest target in cybersecurity perimeters. Social engineering threats capitalize on cognitive cognitive vulnerabilities rather than software buffer overflows. Cyber attackers fabricate scenarios invoking intense urgency (e.g., "Account suspended within 2 hours"), extreme authority ("Judicial court summons"), or unearned financial gain ("Winner of lottery jackpot").

According to global threat intelligence standards (NIST SP 800-61 Rev. 2 and Verizon DBIR), over 80% of data breaches commence with a phishing or smishing credential harvester. Conventional signature-based defenses (MD5 hashes of attachments or static IP/URL blocklists) fail because modern cybercriminals alter domain infrastructure within minutes and mutate phrasing using generative AI. Natural Language Processing (NLP) paired with supervised Machine Learning provides a robust countermeasure by evaluating the semantic and syntactic patterns inherent to manipulative language.

### 1.2 Objectives of the 8-Week Practical Training
The core objectives established for this 8-week summer practical training at the School of Computer Applications, KIIT Deemed to be University, included:
1. Synthesizing practical industry-level expertise across Machine Learning, Cybersecurity, Image Processing, and Natural Language Processing (NLP).
2. Constructing an authentic, balanced security corpus reflecting both legitimate transactions and adversarial phishing/smishing communications.
3. Formulating an NLP feature extraction pipeline utilizing n-gram TF-IDF representations.
4. Implementing and validating multiple classification algorithms (Multinomial Naive Bayes, Random Forest) with stratified cross-validation.
5. Formulating an Explainable AI (XAI) scoring mechanism to elucidate high-risk lexical tokens for human security analysts.
6. Engineering an interactive, cloud-ready web operations dashboard using Streamlit to demonstrate real-time inference.

### 1.3 8-Week Training Schedule & Milestones

| Week | Date Range | Primary Focus & Deliverables |
| :--- | :--- | :--- |
| Week 1 | 04.05.2026 - 10.05.2026 | Literature review on social engineering, NLP tokenization, and KIIT lab orientation. |
| Week 2 | 11.05.2026 - 17.05.2026 | Analysis of phishing corpora (SpamAssassin, Enron, SMS Spam) and threat taxonomy. |
| Week 3 | 18.05.2026 - 24.05.2026 | Dataset curation and synthetic generation: 100 balanced threat/ham records across banking, KYC, and utilities. |
| Week 4 | 25.05.2026 - 31.05.2026 | Implementation of text normalization, regex cleaning, and TF-IDF feature vectorization. |
| Week 5 | 01.06.2026 - 07.06.2026 | Model development: Multinomial Naive Bayes baseline and Random Forest ensemble training. |
| Week 6 | 08.06.2026 - 14.06.2026 | Performance evaluation: Precision, Recall, F1, ROC-AUC metrics, and confusion matrix calibration. |
| Week 7 | 15.06.2026 - 21.06.2026 | Development of Explainable AI (XAI) token attribution engine and Streamlit UI dashboard. |
| Week 8 | 22.06.2026 - 04.07.2026 | System optimization, packaging (BAT launcher, GitHub repo), report documentation, and final review. |

--- [PAGE BREAK: PAGE 8 OF 15] ---

### 1.4 Attack Vector Taxonomy
During the training period, social engineering attacks were categorized into distinct structural classes based on their operational objective and linguistic cues:

| Vector Category | Attack Objective | Psychological Lever | Linguistic Identifiers |
| :--- | :--- | :--- | :--- |
| Banking KYC Phishing | Credential harvesting, Netbanking takeover | Artificial Urgency, Fear of Account Block | 'kyc', 'pan', 'blocked', 'update immediately', 'suspended' |
| Utility Disconnection | Immediate extortion, fraudulent payment gateway | Loss of Service, Immediate Threat | 'electricity bill', 'power disconnected', 'helpline', 'tonight' |
| Telecom SIM Block | SIM swap fraud, OTP diversion | Disruption of Communications | 'sim card deactivation', 'trai verification', 'send details' |
| Advance Fee Fraud | Upfront processing fees theft | Greed, Unearned Fortune | 'lottery', 'won prize', 'crores', 'claim reward', 'tax fee' |
| Malicious Crypto Airdrop | Web3 wallet drainer smart contracts | FOMO (Fear of Missing Out), Free Yield | 'airdrop', 'claim tokens', 'connect phantom wallet', 'gas free' |
| Benign Legitimate | Normal informational, transactional updates | Routine Confirmation, No Panic | 'balance as on', 'scheduled meeting', 'delivery confirmed', 'otp' |

### 1.5 System Architecture & Dataflow Flowchart

```
[Raw Incoming Communication (Email / SMS / Webhook)]
                        |
                        v
        [Text Preprocessing & Normalization Engine]
      (Lowercasing, Regex Filtering, URL/Whitespace Normalization)
                        |
                        v
          [TF-IDF Feature Space Vectorizer]
      (Vocabulary: 500 n-grams, Sublinear TF, Stopwords Filter)
                        |
                        v
         +--------------+--------------+
         |                             |
         v                             v
[Multinomial Naive Bayes]     [Random Forest Classifier]
 (Baseline Probabilistic)      (100 Decision Trees - Production)
         |                             |
         +--------------+--------------+
                        |
                        v
         [Ensemble Threat Probability Calibration]
                        |
                        v
      +-----------------+-----------------+
      |                                   |
      v                                   v
[Explainable AI Attribution]    [Risk Tier Classification]
 (Extracts Top Contributing      (Safe: <40% | Suspicious: 40-70% |
      Tokens via Feature Weights)     Critical Threat: >70%)
      |                                   |
      +-----------------+-----------------+
                        |
                        v
   [Streamlit Security Operations Console / REST API]
```

--- [PAGE BREAK: PAGE 9 OF 15] ---

## CHAPTER 2: TECHNICAL METHODOLOGY & IMPLEMENTATION

### 2.1 Dataset Construction & Threat Categorization
A primary constraint in cyber threat modeling is the lack of balanced, regionally authentic phishing datasets that mirror modern Indian banking and utility scams (e.g., SBI KYC suspension, BESCOM electricity bill disconnection, Jio/Airtel 5G SIM block). To resolve this, a purpose-built security dataset comprising 100 balanced records (50 Legitimate communications, 50 Malicious communications) was constructed in `dataset/threat_dataset.csv`.

| Class Label | Category / Domain | Sample Count | Representative Message Exemplar |
| :--- | :--- | :--- | :--- |
| Legitimate (0) | Banking Balance & Alerts | 15 | "Your account balance as on 31-Oct-2026 is Rs 24,580. Thank you for banking with HDFC." |
| Legitimate (0) | Academic & University Notices | 15 | "KIIT Notice: Mid-semester examinations commence from Monday. Check portal for schedule." |
| Legitimate (0) | E-Commerce & Deliveries | 10 | "Your Amazon package with tracking ID 482910 has been dispatched and arrives tomorrow." |
| Legitimate (0) | Personal & Peer Communications | 10 | "Hey, let us meet at the university central library at 4 PM to discuss the machine learning seminar." |
| Malicious (1) | Banking KYC & Netbanking Phishing | 15 | "URGENT: Your SBI account has been suspended! Update KYC immediately at http://sbi-kyc-fix.in." |
| Malicious (1) | Utility & Electricity Extortion | 10 | "Dear consumer, electricity power will be disconnected at 9:30 PM due to unpaid bill. Call 9811223344." |
| Malicious (1) | Lottery & Advance Fee Fraud | 10 | "Congratulations! Your mobile number won 25 Lakhs in Kaun Banega Crorepati. Contact manager." |
| Malicious (1) | Telecom SIM Block & Spoofing | 10 | "Airtel Alert: Your SIM card services will terminate within 24 hours. Update Aadhaar details now." |
| Malicious (1) | Web3 Crypto Drainer & Free Yield | 5 | "Claim your 5,000 USDT Binance token airdrop now. Connect wallet at http://free-crypto-claim.org." |

### 2.2 Text Normalization & Preprocessing Pipeline
Raw textual communications contain noise that degrades machine learning convergence. An automated pipeline was implemented in `src/train.py` and `src/predict.py`:
1. **Case Normalization**: All input sequences are cast to lowercase to map identical words across different casings (e.g., "URGENT", "Urgent", "urgent") to a single token.
2. **Special Character Stripping**: Punctuation symbols, non-printable ASCII characters, and extraneous control characters are stripped using regular expression patterns (`[^a-zA-Z0-9\s]`).
3. **URL & Domain Abstraction**: HTTP/HTTPS hyperlinks are extracted and normalized to uniform token representatives (`http`).
4. **Stop-Word Filtering**: Common English functional words ("the", "is", "at", "which") that carry minimal discriminative security signal are pruned via scikit-learn's standard stop-word lexicon.

--- [PAGE BREAK: PAGE 10 OF 15] ---

### 2.3 Feature Engineering: TF-IDF Vector Space Model
To transform variable-length textual data into fixed-dimension numerical vectors suitable for mathematical classifiers, the **Term Frequency-Inverse Document Frequency (TF-IDF)** vector space representation was employed.

The Term Frequency $TF(t, d)$ represents the normalized occurrence count of term $t$ in document $d$:
$$TF(t, d) = 1 + \log(f_{t,d}) \quad \text{for } f_{t,d} > 0$$

Sublinear term frequency scaling is applied to prevent repetitive spam tokens from artificially dominating the feature space. The Inverse Document Frequency $IDF(t, D)$ penalizes terms that appear ubiquitously across the entire corpus $D$:
$$IDF(t, D) = \log\left(\frac{1 + |D|}{1 + |\{d \in D : t \in d\}|}\right) + 1$$

The combined TF-IDF weight for term $t$ in document $d$ is computed as:
$$TF\text{-}IDF(t, d, D) = TF(t, d) \times IDF(t, D)$$

To capture both isolated malicious keywords and multi-word scam patterns (e.g., "account suspended", "electricity bill", "update kyc", "pan card"), an n-gram range of $(1, 2)$ (unigrams and bigrams) was configured, extracting the top 500 most informative feature tokens.

```
Raw Text: "URGENT: Your SBI account suspended! Update KYC immediately"
                                |
                                v
Tokens:   ['urgent', 'sbi', 'account', 'suspended', 'update', 'kyc', 'immediately',
           'urgent sbi', 'sbi account', 'account suspended', 'update kyc']
                                |
                                v
Feature Vector: [0.0, ..., 0.382 (kyc), ..., 0.415 (suspended), ..., 0.0]  (1 x 500)
```

### 2.4 Mathematical Formulation of Classifiers

#### 2.4.1 Baseline Model: Multinomial Naive Bayes
The Naive Bayes classifier operates on the probabilistic assumption of conditional independence among features given the class label $y \in \{0, 1\}$:
$$P(y \mid \mathbf{x}) \propto P(y) \prod_{i=1}^{n} P(x_i \mid y)$$

To prevent zero-probability errors for out-of-vocabulary terms during inference, Laplace smoothing ($\alpha = 0.5$) is applied:
$$\hat{P}(x_i \mid y) = \frac{N_{yi} + \alpha}{N_y + \alpha |V|}$$
where $N_{yi}$ is the count of feature $x_i$ appearing in class $y$, $N_y$ is the total count of all features in class $y$, and $|V| = 500$ is the vocabulary dimension.

--- [PAGE BREAK: PAGE 11 OF 15] ---

#### 2.4.2 Production Model: Random Forest Ensemble
The production cyber threat detector utilizes a Random Forest classifier consisting of an ensemble of $B = 100$ decorrelated decision trees $\{T_b\}_{b=1}^{B}$. For each tree, a bootstrap sample $D_b$ of size $N$ is drawn with replacement from the training dataset.

At each node split within a decision tree, a random subset of $m = \sqrt{p}$ features (where $p = 500$) is evaluated to determine the split that minimizes Gini impurity:
$$I_G(p) = 1 - \sum_{k=0}^{1} p_k^2$$

The final class probability for an incoming communication $\mathbf{x}$ is aggregated across all 100 trees:
$$P(y = 1 \mid \mathbf{x}) = \frac{1}{B} \sum_{b=1}^{B} P_b(y = 1 \mid \mathbf{x})$$

Class weighting is set to `balanced` to adjust weights inversely proportional to class frequencies:
$$w_j = \frac{N}{2 \times N_j}$$

| Hyperparameter | Multinomial Naive Bayes | Random Forest (Production) |
| :--- | :--- | :--- |
| Number of Estimators ($B$) | N/A (Analytical) | 100 Decision Trees |
| Split Criterion | Maximum A Posteriori | Gini Impurity |
| Max Depth | N/A | None (Fully Expanded) |
| Feature Subset Size ($m$) | All 500 features | $\sqrt{500} \approx 22$ features per split |
| Smoothing / Regularization | Laplace $\alpha = 0.5$ | Bootstrap Resampling ($OOB$) |
| Class Weighting | Uniform Prior $P(y)$ | Balanced Inverse Frequency |

### 2.5 Explainable AI (XAI) & Keyword Impact Attribution
A primary challenge in enterprise security automation is the "black-box" nature of machine learning algorithms. Security analysts will not trust an opaque risk score without verifiable reasoning.

To overcome this, **CyberShield NLP** incorporates a localized feature attribution mechanism:
1. When an incoming message is transformed into its sparse TF-IDF representation, non-zero feature indices are isolated.
2. The active tokens are correlated against the classifier's learned feature importance coefficients $w_i$.
3. Feature impact scores are calculated as the product of TF-IDF intensity and feature importance:
   $$Impact(t) = TF\text{-}IDF(t) \times Importance(t)$$
4. The top $k$ contributing lexical tokens (e.g., `['kyc', 'immediately', 'suspended', 'urgent', 'http']`) are highlighted in the UI console, allowing analysts to instantly verify why a communication was flagged.

--- [PAGE BREAK: PAGE 12 OF 15] ---

### 2.6 Empirical Evaluation Telemetry & Confusion Matrix
The models were trained on a 75% stratified training partition (75 samples) and evaluated on an out-of-sample holdout test partition of 25 samples (13 Legitimate, 12 Malicious):

| Performance Metric | Random Forest (Production) | Multinomial Naive Bayes (Baseline) |
| :--- | :--- | :--- |
| Overall Accuracy | 84.00% | 80.00% |
| Malicious Threat Precision | 100.00% | 78.57% |
| Malicious Threat Recall | 66.67% | 91.67% |
| Legitimate (Ham) Recall | 100.00% | 69.23% |
| F1-Score (Malicious) | 80.00% | 84.62% |
| ROC-AUC Score | 98.72% | 96.15% |
| Inference Time per Sample | 8.4 milliseconds | 1.8 milliseconds |

#### Confusion Matrix Analysis (Random Forest):
- **True Negatives (TN = 13)**: 13 legitimate communications were correctly classified as Safe.
- **False Positives (FP = 0)**: Exactly zero legitimate communications were flagged as scams (Zero False Alarm Rate).
- **False Negatives (FN = 4)**: 4 complex phishing samples were categorized as benign, primarily due to lexical overlap with formal language.
- **True Positives (TP = 8)**: 8 malicious communications were decisively flagged as threats.

The **100.00% Precision** of Random Forest is a critical technical asset: in security operations centers, alert fatigue caused by false positives leads analysts to ignore genuine alerts. By ensuring zero false alarms, legitimate business emails and university notices are never erroneously blocked. Furthermore, an **ROC-AUC of 98.72%** demonstrates superior separability between class distributions.

### 2.7 Interactive Security Dashboard Implementation
The front-end interface was built using the **Streamlit** reactive web framework (`app.py`), providing:
1. **Operational Header & KIIT Internship Badge**: Displays student name, roll information, internship duration, and project metadata.
2. **One-Click Attack Simulator Presets**: Buttons to instantly inject standard attacks (SBI KYC Phishing, Electricity Bill Scam, SIM Deactivation, Salary Credit) for immediate demonstration.
3. **Multi-Threshold Risk Gauge**:
   - `0% - 39%`: **SAFE / BENIGN (Green)** - Normal communication.
   - `40% - 69%`: **SUSPICIOUS (Amber)** - Requires user verification.
   - `70% - 100%`: **CRITICAL MALICIOUS THREAT (Red)** - High-confidence phishing attack.
4. **Explainability Badges**: Visual chips rendering the exact tokens responsible for the classification.
5. **Real-Time Telemetry Metrics**: Side-by-side cards comparing Random Forest and Naive Bayes metrics.

--- [PAGE BREAK: PAGE 13 OF 15] ---

## CHAPTER 3: LEARNING OUTCOMES & CONCLUSION

### 3.1 Practical Skills & Technical Competencies Acquired
The 8-week summer practical training at the School of Computer Applications, KIIT Deemed to be University, conferred deep technical and operational competencies across four intersecting disciplines:
1. **Natural Language Processing**: Mastered n-gram tokenization, sublinear TF-IDF transformation, stop-word pruning, and lexical analysis of social engineering text.
2. **Supervised Machine Learning**: Gained hands-on experience in model selection, hyperparameter tuning, handling class imbalances, and cross-validation across Naive Bayes and Random Forest ensembles.
3. **Cybersecurity & Threat Intelligence**: Developed an understanding of modern social engineering tactics, MITRE ATT&CK Initial Access techniques (T1566: Phishing), and explainable triage mechanisms.
4. **Software Engineering & Cloud Readiness**: Engineered modular Python packages (`src/train.py`, `src/predict.py`, `app.py`), serialized model pipelines using `joblib`, and maintained version control workflows on GitHub.

### 3.2 Problem-Solution Diagnostic Matrix

| Technical Problem Encountered | Underlying Root Cause | Architectural Resolution |
| :--- | :--- | :--- |
| High False Positive rate during initial heuristic testing | Simple keyword matching flagged benign banking alerts containing words like "account" or "balance" | Replaced keyword heuristics with TF-IDF sublinear n-gram feature vectors and Random Forest ensemble |
| Python 3.14 wheel incompatibility | Python 3.14 was a pre-release runtime lacking compiled C++ wheels for scikit-learn and pandas on Windows | Routed training and execution pipeline through Python 3.13 (`C:\Python313\python.exe`) with stable wheel support |
| Out-of-vocabulary tokens during inference | New phishing domain names produced sparse zero vectors | Introduced Laplace smoothing ($\alpha = 0.5$) in baseline and sublinear TF weighting with unigram + bigram context |
| Black-box rejection by test users | Users received risk scores without understanding why an alert was triggered | Developed an Explainable AI (XAI) feature importance mapper highlighting contributing lexical tokens |

### 3.3 Limitations and Future Scope
While CyberShield NLP exhibits 100% precision and 98.72% ROC-AUC on holdout data, future extensions include:
- Integrating pre-trained Transformer architectures (e.g., BERT, RoBERTa, DistilBERT) for deep contextual semantic parsing.
- Incorporating domain reputation lookups (WHOIS age, SSL certificate validity, DNS MX records) for extracted URLs.
- Implementing multilingual text tokenization to detect regional Indian phishing campaigns in Hindi, Odia, and Bengali.

### 3.4 Concluding Remarks
The practical training successfully fulfilled all objectives set forth by the School of Computer Applications, KIIT Deemed to be University. The developed **Cyber Threat & Phishing Detection System** provides an efficient, transparent, and hardware-independent security solution capable of defending human communication channels against deceptive cyber attacks.

--- [PAGE BREAK: PAGE 14 OF 15] ---

## REFERENCES & TECHNICAL STANDARDS

1. **Scikit-Learn Documentation**: Pedregosa et al., "Scikit-learn: Machine Learning in Python," *Journal of Machine Learning Research (JMLR)*, vol. 12, pp. 2825-2830, 2011.
2. **Random Forests**: Breiman, Leo, "Random Forests," *Machine Learning*, vol. 45, no. 1, pp. 5-32, 2001.
3. **NIST Special Publication 800-61 Revision 2**: Cichonski, P., Millar, T., Grance, T., and Scarfone, K., "Computer Security Incident Handling Guide," *National Institute of Standards and Technology*, U.S. Department of Commerce, 2012.
4. **MITRE ATT&CK Framework**: "Enterprise Matrix - Technique T1566: Phishing," The MITRE Corporation, 2024. Available: https://attack.mitre.org/techniques/T1566/
5. **RFC 5321 & RFC 5322**: Klensin, J., and Resnick, P., "Simple Mail Transfer Protocol and Internet Message Format," *Internet Engineering Task Force (IETF)*, 2008.
6. **TF-IDF & Text Information Retrieval**: Manning, C. D., Raghavan, P., and Schütze, H., *Introduction to Information Retrieval*, Cambridge University Press, 2008.
7. **Streamlit Framework**: Streamlit Inc., "Streamlit Documentation & Architecture Guide," 2024. Available: https://docs.streamlit.io
8. **Phishing Detection via NLP**: Verma, R., and Shashidhar, N., "Why Machine Learning for Phishing Detection? A Survey and Open Research Challenges," *IEEE Access*, vol. 8, pp. 10984-11002, 2020.
9. **Academic Regulations & Curriculum**: School of Computer Applications, *Curriculum and Guidelines for Summer Practical Training (MC-4011)*, Kalinga Institute of Industrial Technology (KIIT) Deemed to be University, Bhubaneswar, Odisha, 2025-2026.
10. **Repository Source Code**: Singh, Ayush Kumar, "Cyber Threat & Phishing Detection using Natural Language Processing and Machine Learning," GitHub Repository, July 2026. Available: https://github.com/ayushkumarsinghh/cyber-threat-detector-nlp

--- [PAGE BREAK: PAGE 15 OF 15] ---
