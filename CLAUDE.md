# CLAUDE.md — Contexte Session Studio IA Pub

Ce fichier est chargé automatiquement à chaque session Claude Code.
**Ne pas modifier manuellement** — mis à jour au fil des sessions.

---

## Projet : Studio IA Pub (side project)

Service de création de vidéos publicitaires IA pour e-commerce/SaaS français.
**Positionnement verrouillé :** "Meta recommande 5+ créatifs/mois — on automatise ça en 48h."

**Phase actuelle :** MVP Validation (semaine 1, avril 2026)
**Objectif immédiat :** 2 clients à 500€ en 2 semaines

---

## Décisions stratégiques actées — NE PAS REMETTRE EN QUESTION

### ❌ LinkedIn écarté définitivement
**Raison :** Le profil LinkedIn contient les informations de l'emploi salarié (sans rapport avec le studio). Contacter des prospects depuis ce profil = confusion + zéro crédibilité.
**Cette décision est définitive pour la phase MVP. Ne pas relancer ce débat.**

### ✅ Canal acquisition : Email + Landing Page
- Domaine : **timeline-ai.fr**
- Taux réponse cible : 15-25%
- Séquence : email hyper-personnalisé → Calendly → call découverte → sprint 500€

### ✅ Angle email : Production bottleneck (pas éducation Meta)
**Contexte :** Les prospects ciblés tournent déjà 15+ pubs actives (critère de qualification Meta Ad Library).
**Conséquence :** Inutile de les éduquer sur Dynamic Creative ou Advantage+ — ils savent déjà pourquoi ils ont besoin de variants.
**Leur vraie douleur :** La production est trop lente et trop chère, pas le budget ou la conviction.
**Hook email acté :** "Tu tournes déjà [X] pubs — le goulot c'est la prod, pas le budget. 48h pour 5 vidéos."
**Ce qu'on évite :** Tout argumentaire pédagogique Meta dans les emails froids → sonne amateur face à des pros.

---

## État actuel

### Fait
- Stratégie complète documentée
- 32 prospects qualifiés identifiés (`MVP_PROSPECTS_TRACKER.md`)
- Workflow livraison client défini (sprint 48h, 5 vidéos)
- Templates emails par secteur rédigés (`STRATEGIE_ACQUISITION_EMAIL_LANDING.md`)
- Script scraping Meta Ad Library (`meta_ads_scraper.py`)

### À faire (dans l'ordre)
1. **Landing page `timeline-ai.fr`** — crédibilité + destination emails (4-6h setup)
2. **Trouver les emails** des décideurs — outil retenu : **Dropcontact** (100 crédits gratuits, RGPD, algo FR)
3. **Écrire 10 emails personnalisés** par secteur
4. **Envoyer** + tracker les réponses (Google Sheet)

### Métrique de validation MVP
2-3 réponses sur 10 emails envoyés = MVP validé

---

## Contexte personnel
- Side project, pas activité principale
- Budget : zéro pour la phase MVP (outils gratuits uniquement)
- Outils OK : Hunter.io (50 recherches gratuites), Dropcontact (100 crédits gratuits), Meta Ad Library, LinkedIn (lecture seule)

---

## Fichiers clés du repo
| Fichier | Contenu |
|---------|---------|
| `STRATEGIE_ACQUISITION_EMAIL_LANDING.md` | Stratégie email + templates + calendrier |
| `MVP_PROSPECTS_TRACKER.md` | 32 prospects qualifiés semaine 1 |
| `PROSPECTS_VALIDES_COMPLET.md` | Liste complète prospects validés |
| `CLIENT_BRIEF_WORKFLOW.md` | Process livraison sprint 48h |
| `HOOK_SHEETS_BY_SECTOR.md` | Angles créatifs par vertical |
| `meta_ads_scraper.py` | Script scraping Meta Ad Library |

---

## Historique décisions importantes
| Date | Décision |
|------|----------|
| Avril 2026 | Pivot LinkedIn → Email + landing page (profil LinkedIn = emploi salarié) |
| Avril 2026 | Positionnement "Meta 5+ créatifs" adopté |
| Avril 2026 | Dropcontact retenu pour enrichissement emails (pas encore utilisé) |
| Avril 2026 | Pivot angle email : éducation Meta → production bottleneck (prospects = déjà 15+ pubs actives) |
