"""
Meta Ad Library API — Prospection Studio IA Pub
------------------------------------------------
Trouve automatiquement les marques françaises avec 10+ pubs vidéo actives.

SETUP :
1. Créer un compte sur developers.facebook.com
2. Créer une app (type "Business")
3. Générer un User Access Token avec la permission "ads_read"
4. Coller le token dans ACCESS_TOKEN ci-dessous
5. pip install requests pandas
6. python meta_ads_scraper.py
"""

import requests
import pandas as pd
import time
from collections import defaultdict

# ─── CONFIG ───────────────────────────────────────────────────────────────────

ACCESS_TOKEN = "COLLE_TON_TOKEN_ICI"
API_VERSION  = "v19.0"
BASE_URL     = f"https://graph.facebook.com/{API_VERSION}/ads_archive"

# Seuil minimum de pubs actives pour garder une marque
MIN_ADS = 10

# ─── MOTS-CLÉS PAR SECTEUR ───────────────────────────────────────────────────

KEYWORDS = {
    "Sport / Récupération": [
        "récupération musculaire",
        "pistolet de massage",
        "ice bath",
        "bain froid",
        "compléments sportifs",
    ],
    "Nutrition / Alimentation": [
        "smoothie",
        "compléments alimentaires",
        "lyophilisé",
        "snack healthy",
        "superaliments",
        "sans sucre ajouté",
        "protéines végétales",
    ],
    "Cosmétique / Hygiène": [
        "routine visage",
        "soin naturel",
        "cosmétique solide",
        "zéro déchet",
        "sans sulfate",
        "vegan",
    ],
    "Animaux": [
        "alimentation fraîche chien",
        "croquettes naturelles",
        "sans conservateur chien",
    ],
    "Éco-responsable / Maison": [
        "rechargeable",
        "sans plastique",
        "consigne",
        "entretien naturel",
        "produit ménager concentré",
    ],
    "Boissons": [
        "sans alcool",
        "kombucha",
        "kéfir",
    ],
}

# ─── FONCTIONS ────────────────────────────────────────────────────────────────

def fetch_ads(keyword, max_pages=5):
    """Récupère les pubs actives françaises en vidéo pour un mot-clé."""
    ads = []
    params = {
        "access_token":        ACCESS_TOKEN,
        "search_terms":        keyword,
        "ad_reached_countries": "FR",
        "ad_type":             "ALL",
        "media_type":          "VIDEO",
        "ad_active_status":    "ACTIVE",
        "limit":               100,
        "fields":              "page_name,page_id,ad_delivery_start_time,impressions,spend,currency",
    }

    page = 0
    while page < max_pages:
        try:
            response = requests.get(BASE_URL, params=params, timeout=15)
            data = response.json()

            if "error" in data:
                print(f"  ⚠️  Erreur API : {data['error']['message']}")
                break

            ads.extend(data.get("data", []))

            # Pagination
            next_url = data.get("paging", {}).get("next")
            if not next_url:
                break

            params = {"access_token": ACCESS_TOKEN}
            BASE_URL_NEXT = next_url
            page += 1
            time.sleep(0.5)  # Rate limit

        except Exception as e:
            print(f"  ⚠️  Exception : {e}")
            break

    return ads


def count_ads_per_brand(ads):
    """Compte le nombre de pubs par marque."""
    counts = defaultdict(lambda: {"count": 0, "page_id": ""})
    for ad in ads:
        name = ad.get("page_name", "Inconnu")
        pid  = ad.get("page_id", "")
        counts[name]["count"] += 1
        counts[name]["page_id"] = pid
    return counts


def run():
    print("\n🚀 Démarrage prospection Meta Ad Library\n")
    results = []

    for secteur, keywords in KEYWORDS.items():
        print(f"\n📂 Secteur : {secteur}")

        brand_totals = defaultdict(lambda: {"count": 0, "page_id": "", "secteur": secteur, "keywords": []})

        for kw in keywords:
            print(f"  🔍 Mot-clé : \"{kw}\"", end=" ... ")
            ads = fetch_ads(kw)
            counts = count_ads_per_brand(ads)
            print(f"{len(ads)} pubs trouvées")

            for brand, info in counts.items():
                brand_totals[brand]["count"]    += info["count"]
                brand_totals[brand]["page_id"]   = info["page_id"]
                brand_totals[brand]["secteur"]   = secteur
                brand_totals[brand]["keywords"].append(kw)

            time.sleep(1)  # Rate limit entre les requêtes

        # Filtre : garder uniquement les marques avec MIN_ADS pubs ou plus
        for brand, info in brand_totals.items():
            if info["count"] >= MIN_ADS:
                results.append({
                    "Marque":    brand,
                    "Secteur":   secteur,
                    "Nb pubs":   info["count"],
                    "Page ID":   info["page_id"],
                    "Mots-clés": ", ".join(set(info["keywords"])),
                    "Ad Library": f"https://www.facebook.com/ads/library/?id={info['page_id']}" if info["page_id"] else "",
                })

    # ─── Export ───────────────────────────────────────────────────────────────
    if not results:
        print("\n❌ Aucune marque trouvée. Vérifie ton access token.")
        return

    df = pd.DataFrame(results)
    df = df.sort_values("Nb pubs", ascending=False)

    output_file = "prospects_meta_auto.csv"
    df.to_csv(output_file, index=False, encoding="utf-8-sig")

    print(f"\n✅ {len(df)} marques qualifiées exportées dans {output_file}")
    print(f"\n🏆 Top 10 :")
    print(df[["Marque", "Secteur", "Nb pubs"]].head(10).to_string(index=False))


if __name__ == "__main__":
    run()
