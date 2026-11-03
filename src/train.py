import os
import sys
import csv
import joblib
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report, roc_auc_score
)

def train_pipeline():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dataset_path = os.path.join(base_dir, "dataset", "threat_dataset.csv")
    models_dir = os.path.join(base_dir, "models")
    os.makedirs(models_dir, exist_ok=True)

    print("=" * 65)
    print("CYBERSHIELD NLP: TRAINING THREAT CLASSIFICATION MODELS")
    print("=" * 65)

    # 1. Load Dataset
    print(f"[*] Loading dataset from: {dataset_path}")
    df = pd.read_csv(dataset_path)
    print(f"[+] Loaded {len(df)} total records ({sum(df['label'] == 0)} Ham, {sum(df['label'] == 1)} Malicious)")

    # 2. Stratified Train-Test Split (75% Train, 25% Test)
    X = df["text"]
    y = df["label"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )
    print(f"[+] Training Split: {len(X_train)} samples | Testing Split: {len(X_test)} samples")

    # 3. Text Vectorization via TF-IDF (Unigrams + Bigrams)
    print("[*] Extracting NLP features via TF-IDF Vectorizer...")
    vectorizer = TfidfVectorizer(
        lowercase=True,
        stop_words="english",
        ngram_range=(1, 2),
        max_features=500,
        sublinear_tf=True
    )
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)
    print(f"[+] Vocabulary Size: {len(vectorizer.vocabulary_)} features extracted.")

    # 4. Train Model 1: Multinomial Naive Bayes (Fast Baseline)
    print("\n[*] Training Baseline Model: Multinomial Naive Bayes (alpha=0.5)...")
    model_nb = MultinomialNB(alpha=0.5)
    model_nb.fit(X_train_vec, y_train)
    preds_nb = model_nb.predict(X_test_vec)
    acc_nb = accuracy_score(y_test, preds_nb)
    print(f"[+] Naive Bayes Accuracy: {acc_nb * 100:.2f}%")

    # 5. Train Model 2: Random Forest Classifier (Production Ensemble)
    print("\n[*] Training Production Model: Random Forest (n_estimators=100)...")
    model_rf = RandomForestClassifier(n_estimators=100, random_state=42, class_weight="balanced")
    model_rf.fit(X_train_vec, y_train)
    preds_rf = model_rf.predict(X_test_vec)
    probs_rf = model_rf.predict_proba(X_test_vec)[:, 1]

    acc_rf = accuracy_score(y_test, preds_rf)
    prec_rf = precision_score(y_test, preds_rf)
    rec_rf = recall_score(y_test, preds_rf)
    f1_rf = f1_score(y_test, preds_rf)
    roc_rf = roc_auc_score(y_test, probs_rf)
    cm_rf = confusion_matrix(y_test, preds_rf)

    print("\n" + "=" * 65)
    print("PRODUCTION MODEL EVALUATION REPORT (RANDOM FOREST)")
    print("=" * 65)
    print(f"Accuracy         : {acc_rf * 100:.2f}%")
    print(f"Precision        : {prec_rf * 100:.2f}%")
    print(f"Recall           : {rec_rf * 100:.2f}%")
    print(f"F1-Score         : {f1_rf * 100:.2f}%")
    print(f"ROC-AUC Score    : {roc_rf * 100:.2f}%")
    print("\nConfusion Matrix (True Negative, False Positive / False Negative, True Positive):")
    print(cm_rf)
    print("\nDetailed Classification Report:")
    print(classification_report(y_test, preds_rf, target_names=["Legitimate (Ham)", "Malicious Scam"]))

    # 6. Export Models and Artifacts
    print("\n[*] Exporting trained model artifacts to disk...")
    rf_path = os.path.join(models_dir, "classifier_rf.joblib")
    nb_path = os.path.join(models_dir, "classifier_nb.joblib")
    vec_path = os.path.join(models_dir, "tfidf_vectorizer.joblib")

    joblib.dump(model_rf, rf_path)
    joblib.dump(model_nb, nb_path)
    joblib.dump(vectorizer, vec_path)

    # Save metrics JSON for the dashboard telemetry
    metrics = {
        "dataset_size": len(df),
        "vocab_size": len(vectorizer.vocabulary_),
        "rf_accuracy": float(acc_rf),
        "rf_precision": float(prec_rf),
        "rf_recall": float(rec_rf),
        "rf_f1": float(f1_rf),
        "rf_roc_auc": float(roc_rf),
        "nb_accuracy": float(acc_nb),
        "confusion_matrix": cm_rf.tolist()
    }
    joblib.dump(metrics, os.path.join(models_dir, "model_metrics.joblib"))

    print(f"[+] Saved Random Forest Model  -> {rf_path}")
    print(f"[+] Saved Naive Bayes Model    -> {nb_path}")
    print(f"[+] Saved TF-IDF Vectorizer    -> {vec_path}")
    print("=" * 65)
    print("[SUCCESS] All training artifacts ready for production inference.")

if __name__ == "__main__":
    train_pipeline()
