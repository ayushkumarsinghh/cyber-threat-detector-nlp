import os
import joblib
import numpy as np

class ThreatDetector:
    def __init__(self, models_dir=None):
        if models_dir is None:
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            models_dir = os.path.join(base_dir, "models")
        
        self.models_dir = models_dir
        self.rf_model = joblib.load(os.path.join(models_dir, "classifier_rf.joblib"))
        self.nb_model = joblib.load(os.path.join(models_dir, "classifier_nb.joblib"))
        self.vectorizer = joblib.load(os.path.join(models_dir, "tfidf_vectorizer.joblib"))
        
        try:
            self.metrics = joblib.load(os.path.join(models_dir, "model_metrics.joblib"))
        except Exception:
            self.metrics = {}

        # Feature names and RF importances for explainability
        self.feature_names = np.array(self.vectorizer.get_feature_names_out())
        self.importances = self.rf_model.feature_importances_

    def analyze(self, text):
        if not text or not str(text).strip():
            return {
                "error": "Input text is empty."
            }
        
        cleaned_text = str(text).strip()
        vec = self.vectorizer.transform([cleaned_text])
        
        # Probabilities
        prob_rf = self.rf_model.predict_proba(vec)[0]
        prob_nb = self.nb_model.predict_proba(vec)[0]
        
        malicious_score = float(prob_rf[1])
        benign_score = float(prob_rf[0])
        
        # Risk Category
        if malicious_score >= 0.70:
            risk_level = "CRITICAL THREAT"
            label = "MALICIOUS (SCAM / PHISHING)"
            color = "red"
        elif malicious_score >= 0.35:
            risk_level = "SUSPICIOUS / ELEVATED"
            label = "SUSPICIOUS (PROCEED WITH CAUTION)"
            color = "orange"
        else:
            risk_level = "LOW RISK"
            label = "LEGITIMATE (SAFE / BENIGN)"
            color = "green"

        # Explainability: Extract active keywords present in the text with highest model importance
        feature_indices = vec.nonzero()[1]
        active_features = []
        for idx in feature_indices:
            feat_name = self.feature_names[idx]
            tfidf_weight = vec[0, idx]
            importance_weight = self.importances[idx]
            impact_score = tfidf_weight * (importance_weight + 0.01)
            active_features.append({
                "keyword": feat_name,
                "tfidf_weight": round(float(tfidf_weight), 4),
                "model_importance": round(float(importance_weight), 4),
                "impact_score": round(float(impact_score), 4)
            })

        active_features = sorted(active_features, key=lambda x: x["impact_score"], reverse=True)

        return {
            "text": cleaned_text,
            "label": label,
            "risk_level": risk_level,
            "color": color,
            "malicious_probability": round(malicious_score * 100, 2),
            "legitimate_probability": round(benign_score * 100, 2),
            "nb_malicious_probability": round(float(prob_nb[1]) * 100, 2),
            "detected_keywords": active_features[:10]
        }

if __name__ == "__main__":
    detector = ThreatDetector()
    test_samples = [
        "Your account balance as on 31-Oct-2026 is Rs 24,580. Thank you for banking with HDFC.",
        "URGENT: Your SBI bank account has been suspended! Update your KYC immediately at http://sbi-kyc-verify.net or your card will be blocked."
    ]
    for sample in test_samples:
        result = detector.analyze(sample)
        print("\n--- SAMPLE TEST ---")
        print("Text   :", result["text"][:75])
        print("Verdict:", result["label"])
        print(f"Risk   : {result['malicious_probability']}% Malicious Risk")
        print("Keywords Triggered:", [k['keyword'] for k in result['detected_keywords']])
