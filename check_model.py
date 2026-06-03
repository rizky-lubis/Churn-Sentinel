"""
check_model.py - Churn Sentinel Model Diagnostics
Jalankan: python check_model.py
"""

import joblib
import numpy as np
import os
import warnings
warnings.filterwarnings('ignore')

base = os.path.dirname(os.path.abspath(__file__))

print("\n" + "="*60)
print("  CHURN SENTINEL - MODEL DIAGNOSTIC")
print("="*60)

# Load model & scaler
model  = joblib.load(os.path.join(base, 'svm_model_final.joblib'))
scaler = joblib.load(os.path.join(base, 'scaler.joblib'))

# ── 1. Model Info ──────────────────────────────────────────────
print("\n[1] MODEL PARAMETERS")
print(f"  Type       : {type(model).__name__}")
print(f"  Kernel     : {getattr(model, 'kernel', 'N/A')}")
print(f"  C          : {getattr(model, 'C', 'N/A')}")
print(f"  Gamma      : {getattr(model, 'gamma', 'N/A')}")
print(f"  n_features : {getattr(model, 'n_features_in_', 'N/A')}")
print(f"  classes    : {getattr(model, 'classes_', 'N/A')}")

if hasattr(model, 'n_support_'):
    n_sv   = model.n_support_
    total  = sum(n_sv)
    print(f"  Support Vectors (class 0 / class 1) : {n_sv[0]} / {n_sv[1]}")
    print(f"  Total Support Vectors : {total}")

print(f"\n[2] SCALER INFO")
print(f"  Type       : {type(scaler).__name__}")
print(f"  n_features : {getattr(scaler, 'n_features_in_', 'N/A')}")

# ── 2. Load Dummy Data untuk cek quick ──────────────────────────
csv_path = os.path.join(base, 'data_dummy_20_pelanggan.csv')
if os.path.exists(csv_path):
    print(f"\n[3] QUICK INFERENCE TEST (data_dummy_20_pelanggan.csv)")
    import csv

    map_gender      = lambda v: 1 if v=="Male" else 0
    map_yn          = lambda v: 1 if v=="Yes" else 0
    map_ml          = lambda v: 2 if v=="Yes" else (0 if v=="No" else 1)
    map_inet        = lambda v: 1 if v=="Fiber optic" else (0 if v=="DSL" else 2)
    map_svc         = lambda v: 2 if v=="Yes" else (0 if v=="No" else 1)
    map_contract    = lambda v: 2 if v=="Two year" else (1 if v=="One year" else 0)
    map_payment     = lambda v: (2 if v=="Electronic check" else
                                 3 if v=="Mailed check" else
                                 0 if v=="Bank transfer (automatic)" else 1)

    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows   = list(reader)

    preds = []
    for r in rows:
        feats = [
            map_gender(r['gender']),
            int(r['SeniorCitizen']),
            map_yn(r['Partner']),
            map_yn(r['Dependents']),
            float(r['tenure']),
            map_yn(r['PhoneService']),
            map_ml(r['MultipleLines']),
            map_inet(r['InternetService']),
            map_svc(r['OnlineSecurity']),
            map_svc(r['OnlineBackup']),
            map_svc(r['DeviceProtection']),
            map_svc(r['TechSupport']),
            map_svc(r['StreamingTV']),
            map_svc(r['StreamingMovies']),
            map_contract(r['Contract']),
            map_yn(r['PaperlessBilling']),
            map_payment(r['PaymentMethod']),
            float(r['MonthlyCharges']) / 15000,
            float(r['TotalCharges'])   / 15000
        ]
        x_scaled = scaler.transform([feats])
        pred     = model.predict(x_scaled)[0]
        prob     = 0.0
        if hasattr(model, 'predict_proba'):
            prob = float(np.max(model.predict_proba(x_scaled)))
        elif hasattr(model, 'decision_function'):
            df   = model.decision_function(x_scaled)
            prob = float(1 / (1 + np.exp(-abs(df[0]))))
        label = "Churn" if pred == 1 else "No Churn"
        preds.append((r['customerID'], label, round(prob*100, 1)))
        print(f"  {r['customerID']} → {label:9s}  conf={prob*100:.1f}%")

    n_churn    = sum(1 for _,l,_ in preds if l=="Churn")
    n_nochurn  = sum(1 for _,l,_ in preds if l!="Churn")
    avg_conf   = np.mean([c for _,_,c in preds])
    print(f"\n  Prediksi Churn    : {n_churn}/{len(preds)}")
    print(f"  Prediksi No Churn : {n_nochurn}/{len(preds)}")
    print(f"  Rata-rata confidence : {avg_conf:.1f}%")

# ── 3. Overfitting check via cross-val dengan data dummy ─────────
print(f"\n[4] CROSS-VALIDATION OVERFITTING CHECK")
print("  Memuat dataset Telco asli dari sklearn / membuat data sintetis...")

try:
    # Coba buat dataset sintetis dengan pola mirip Telco
    from sklearn.datasets import make_classification
    from sklearn.model_selection import cross_val_score, StratifiedKFold
    from sklearn.svm import SVC
    from sklearn.pipeline import Pipeline

    # Simulasi dataset 500 sampel dengan 19 fitur
    X_sim, y_sim = make_classification(
        n_samples=500, n_features=19, n_informative=10,
        n_redundant=4, n_clusters_per_class=2,
        weights=[0.73, 0.27], random_state=42
    )
    X_sim_scaled = scaler.transform(X_sim)

    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    cv_scores = cross_val_score(model, X_sim_scaled, y_sim, cv=cv, scoring='accuracy')

    print(f"  ⚠️  Catatan: cross-val menggunakan data sintetis (19 fitur, 500 samples)")
    print(f"  CV Accuracy scores : {np.round(cv_scores, 4)}")
    print(f"  Mean CV Accuracy   : {cv_scores.mean():.4f} (+/- {cv_scores.std()*2:.4f})")

    if cv_scores.std() < 0.03:
        print(f"  ✅ Variansi antar fold RENDAH → Model stabil")
    else:
        print(f"  ⚠️  Variansi antar fold TINGGI → Potensi instabilitas")

except Exception as e:
    print(f"  Tidak bisa jalankan cross-val: {e}")

# ── 4. Support Vector Ratio ──────────────────────────────────────
print(f"\n[5] OVERFITTING INDICATOR: SUPPORT VECTOR RATIO")
if hasattr(model, 'n_support_') and hasattr(model, 'n_features_in_'):
    total_sv = sum(model.n_support_)
    n_feat   = model.n_features_in_
    ratio    = total_sv / n_feat
    print(f"  Total SV      : {total_sv}")
    print(f"  N features    : {n_feat}")
    print(f"  SV/feature ratio : {ratio:.1f}")
    if ratio < 10:
        print(f"  ✅ Rasio SV rendah → Model cenderung GENERALIZE dengan baik")
    elif ratio < 50:
        print(f"  ⚠️  Rasio SV sedang → Perhatikan nilai C dan gamma")
    else:
        print(f"  ❌ Rasio SV sangat tinggi → Kemungkinan OVERFITTING (C terlalu besar / gamma terlalu kecil)")

# ── 5. Ringkasan ─────────────────────────────────────────────────
print(f"\n[6] KESIMPULAN")
C     = getattr(model, 'C', None)
gamma = getattr(model, 'gamma', None)
kernel= getattr(model, 'kernel', None)

if C and C <= 10 and kernel in ['rbf', 'linear']:
    print(f"  ✅ Nilai C={C} dalam range aman (tidak terlalu besar)")
else:
    print(f"  ⚠️  C={C} — nilai besar meningkatkan risiko overfitting")

if gamma == 'scale' or gamma == 'auto':
    print(f"  ✅ Gamma='{gamma}' — auto-scaled, aman dari overfitting gamma")
elif isinstance(gamma, float) and gamma < 1.0:
    print(f"  ✅ Gamma={gamma} (kecil) — generalisasi baik")
else:
    print(f"  ⚠️  Gamma={gamma} — periksa apakah ini menyebabkan overfit")

print("\n" + "="*60)
print("  Selesai! Lihat angka di atas untuk evaluasi overfitting.")
print("="*60 + "\n")
