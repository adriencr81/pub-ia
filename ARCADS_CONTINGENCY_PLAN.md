# Contingency Plan — Si Arcads "échoue" le test crédibilité

**But:** Anticiper les scénarios où Arcads ne passe pas le test "vendable", avec actions rapides

---

## 🚨 Scénario 1 : Avatar looks "trop IA" (uncanny valley)

**Symptôme:** En regardant la vidéo générée, tu sens que c'est pas vraiment une personne. Lips mal synchronisées, expressions figées, ou juste... fake-feeling.

**Probabilité:** 15-20% (test sur 2-3 avatars réduit le risque)

### Action rapide (< 2h)

```
Plan A: Autre avatar Arcads
├─ Tester 2-3 autres avatars (même script)
├─ Chercher ceux avec:
│  ├─ Plus d'expressions faciales naturelles
│  ├─ Arrière-plan casual (pas studio blanc)
│  └─ Avatar légèrement plus vieux (30-40 > 25-30)
└─ Si UN devient crédible → Continue

Plan B: Vitessse voix réduite
├─ Réduire débit Arcads de 1.0 → 0.85
├─ Parler plus lent = paraît plus naturel/humain
├─ Re-générer même script
└─ Souvent fixe le "robot feel" immédiatement

Plan C: HeyGen (Plan B alternatif)
├─ HeyGen free tier: 3 min gratuit/mois
├─ Générer 1 vidéo HeyGen avec même script
├─ Comparer directement Arcads vs HeyGen
├─ Si HeyGen meilleur → bascule stack (redo jour 2, moins efficace mais possible)
└─ Timing: 30 min test, +4h si pivot
```

**Decision:** 
- Si une alternative Arcads devient crédible → Continue (minimal delay)
- Si tout échoue → Pivot HeyGen (72h → 96h, mais réalisable)

---

## 🚨 Scénario 2 : Lip-sync décalé

**Symptôme:** Avatar parle, mais ses lèvres bougent en retard ou en avance par rapport aux mots. Ça crée un sentiment "cheap".

**Probabilité:** 5-10% (dépend avatar + script language mix)

### Action rapide (< 30 min)

```
Plan A: Arcads settings
├─ Vérifier: voice language = Français (pas anglais avec FR text)
├─ Re-générer même vidéo
├─ Parfois c'est un bug Arcads qui se corrige en re-génération
└─ Timing: 5 min

Plan B: Autre avatar + même script
├─ Quelques avatars Arcads ont lip-sync meilleur
├─ Tester 2 autres avatars
├─ (rare que lip-sync soit ENTIÈREMENT pourri, généralement OK)
└─ Timing: 10 min

Plan C: Accept et cache dans montage
├─ Si lip-sync décalé que de 0.3 sec (invisible vraiment)
├─ Poursuivre production (acceptable)
├─ Mention client: "Avatar légèrement compressé pour timing vidéo"
└─ La majorité des viewers ne remarquent pas

DECISION: C'est moins grave qu'on le pense. Continue.
```

---

## 🚨 Scénario 3 : "Script pas assez vendable" (client feedback après démo)

**Symptôme:** Tu montres la vidéo à client / ami, il dit "Ouais c'est OK mais c'est pas assez... choc. C'est trop soft."

**Probabilité:** 10-15% (dépend angle + persona match)

### Action rapide (< 2h redo)

```
Plan A: Script plus agressif
├─ Ajouter des chiffres spécifiques dans hook
│  ├─ Avant: "Tes créas passent inaperçues"
│  ├─ Après: "70% de tes créas passent inaperçues"
├─ Problem statement plus dramatique
│  ├─ Avant: "Engagement suit pas"
│  ├─ Après: "Ton CTR est tombé de 8% à 3% en 6 mois"
├─ CTA plus urgente
│  ├─ Avant: "Calendly pour appel"
│  ├─ Après: "Slots pleins d'ici jeudi. Calendly vite."
└─ Re-générer Arcads avec script amélioré
└─ Timing: 30 min script + 5 min re-generate

Plan B: Différent angle entièrement
├─ Essayer une des 2 autres scripts prépare
│  ├─ Si tu as nutrition script #1 (engagement)
│  └─ Tester nutrition script #2 (ROI problem = plus hard-sell)
├─ Souvent angle #2 convertit mieux anyway
└─ Timing: 5 min re-generate

Plan C: Tester avec cosmétique au lieu nutrition
├─ Si angle nutrition vraiment pas fonctionnant
├─ Pivot secteur: faire cosmétique test #1
├─ Cosmétique = audience plus réactive anyway (conversion +15%)
└─ Timing: 45 min (nouveau script + generate)
```

**Decision:**
- Plan A généralement fixe le problème
- Plan B = essayer angle différent (rapide)
- Plan C = si vraiment on accroche pas, changer secteur (OK même pour MVP)

---

## 🚨 Scénario 4 : Production timeline "trop long" (5h montage au lieu de 1h)

**Symptôme:** Tu lancestyle production et réalises que montage CapCut prend plus long que prévu (trouver bons clips produit, ajustements b-roll, etc.)

**Probabilité:** 35-40% (courant pour première vidéo)

### Action rapide (acceleration tactics)

```
Plan A: Simplifier montage
├─ Réduire variété B-roll (2 clips au lieu de 5)
├─ Moins de transitions
├─ Moins d'ajustements couleur/brightness
└─ Sauvegarder 30-45 min

Plan B: Utiliser Pexels B-roll generique
├─ Si client assets limités
├─ Pexels déjà téléchargé → drag & drop immédiat
├─ Génériques "nutrition workout" suffisent pour test
└─ Sauvegarder 20 min (vs chercher assets client manquants)

Plan C: Utiliser template CapCut pre-built
├─ CapCut a templates "UGC avatar + b-roll"
├─ Réduire montage de scratch à juste customization
├─ (moins flexible mais x3 plus rapide)
└─ Sauvegarder 30 min

REALITY CHECK:
Première vidéo = 1.5-2h montage (normal)
Vidéo 2 = 45 min (muscle memory)
Vidéo 3 = 30 min (routine)

Decision: Si on dépasse 72h, c'est accepta BLE pour MVP test.
L'important = résultat vendable, pas speed parfaite yet.
```

---

## 🚨 Scénario 5 : Client dit "Non" à la démo

**Symptôme:** Tu envoies vidéo de test, client regarde et dit "C'est pas notre style" ou "Trop IA-y" ou "Pas adapté notre audience".

**Probabilité:** 20-25% (courant en prospection, pas une failure)

### Action rapide (< pivot vers prospect #2)

```
Pas une failure, c'est NORMAL.
Raison courant:
├─ Avatar pas match audience du client (couleur peau, age, gender)
├─ Angle pas match leur problème réel (pensaient ROI, cherchaient brand)
├─ Script trop corporate ou pas assez corporate
└─ Juste pas interested (OK, move on)

Quick actions:
1. Documenter feedback exact ("Trop synth'," "Avatar pas relatable")
2. Note secteur + personas pour next test
3. Envoyer 2-3 prospects AUTRE secteur (cosmétique > nutrition parfois)
4. Ou tester AUTRE angle nutrition (script #2 vs #1)

Reality:
├─ MVP = 2 réponses positives sur 10 emails
├─ 1 "Non" = 10% normal fallout
├─ Continue scaling prospect list
└─ La vidéo TEST n'est pas perdue:
   ├─ Landing page: "Exemples secteur"
   ├─ Next prospect nutrition: "Voici ce qu'on produit"
   └─ Réutilisable x 10 fois

Decision: C'est OK. Move to prospect #2 immédiatement.
```

---

## 🚨 Scénario 6 : Arcads "bloqué" ou quota dépassé

**Symptôme:** Arcads Starter plan = 10 vidéos/mois. Tu as généré 8 pour tests, et maintenant besoin pour client = plus de crédits.

**Probabilité:** 5% (si tu gères pas les crédits)

### Action rapide (< 1h solution)

```
Plan A: Achat crédits supplémentaires
├─ Arcads vend extra crédits à la demande
├─ ~€20-30 pour 5 vidéos supplémentaires
├─ Paiement immédiat, accès en 5 min
└─ Continue sans delay

Plan B: HeyGen Plan B
├─ HeyGen free tier: 3 min de génération gratuites
├─ Peut générer 2-3 vidéos HeyGen avec crédit gratuit
├─ Mix Arcads + HeyGen = acceptable pour client
└─ Qualité HeyGen légèrement moins "UGC" mais OK

Plan C: Négocier délai client
├─ "Crédits recharge lundi, livraison lundi end-of-day"
├─ Rarement problèmes pour client (24h extra acceptable)
└─ Achète temps de restock crédits

Decision: Plan A (buy credits) = meilleur, €30 >> perte 500€ contract.
```

---

## 🚨 Scénario 7 : "Arcads works OK but HeyGen / Synthesia better"

**Symptôme:** Tu as généré avec Arcads, puis tu testes HeyGen/Synthesia en parallèle, et le résultat là semble meilleur.

**Probabilité:** 10% (possible que autre outil soit mieux)

### Decision framework

```
COMPARE 3 dimensions:
├─ UGC Authenticity (0-10):
│  ├─ Arcads: 8-9 (très crédible, format UGC)
│  ├─ HeyGen: 6-7 (bon mais moins "vrai")
│  └─ Synthesia: 4-5 (trop polished, corporate feel)
│
├─ Speed (vidéos/jour):
│  ├─ Arcads: 5-6 vidéos/jour possible
│  ├─ HeyGen: 4-5 vidéos/jour
│  └─ Synthesia: 2-3 vidéos/jour
│
└─ Cost (monthly):
   ├─ Arcads: €100
   ├─ HeyGen: €50 (free tier) / €100 paid
   └─ Synthesia: €225 minimum

FOR THIS STUDIO (UGC NUTRITION/BEAUTY):
Arcads > HeyGen > Synthesia

Reason:
"UGC avatar qui semble vrai" = LE différenciateur
vs "Polished corporate avatar" = concurrence forte

Decision: Stick Arcads sauf si:
- Client spécifiquement demande "plus polished" (rara)
- Arcads indisponible
- HeyGen déjà payé (use it)
```

---

## 🚨 Scénario 8 : Temps 72h "pas suffisant" pour client impatient

**Symptôme:** Client dit "J'ai besoin des vidéos DEMAIN, pas dans 3 jours".

**Probabilité:** 10% (impatient prospects)

### Action rapide

```
Plan A: Accélérer timeline
├─ Jour 1: Lancer Arcads générations + paralléliser montage
├─ Jour 2 (instead of Day 3): Livrer 3 vidéos (au lieu de 5)
│  ├─ 3 vidéos = 48h possible
│  ├─ 5 vidéos = 72h optimal
├─ "On livre 3 maintenant, 2 demain EOD"
└─ Timing: réalisable

Plan B: Réduire variantes
├─ Proposer 2 vidéos hyper-ciblées (au lieu de 5 diversifiées)
├─ Budget: au lieu 500€/5 vidéos → 300€/2 vidéos
├─ Livraison: demain 18h
└─ Timing: 24h possible

Plan C: Refuser poliment
├─ "Notre processus demande 72h pour qualité optimal"
├─ "Option rush = 2 videos à moindre qualité"
├─ "Je peux pas garantir résultats sinon"
└─ Often client accepte 72h plutôt que qualité compromise

DECISION:
├─ Client payé premium (750€) → livrer 48h
├─ Client budget standard → "72h c'est notre process"
├─ Impatience clients = common, nego first
```

---

## 📊 Decision tree: Arcads continue ou pivot?

```
Arcads vidéo généré ✓

EVALUATE:
├─ Avatar crédibilité: ⭐⭐⭐⭐ ou meilleur?
│  ├─ OUI → Continue Arcads
│  ├─ NON (trop plastique) → Test Plan A/B (autre avatar / débit réduit)
│  └─ STILL NO → Pivot HeyGen Plan C
│
├─ Script pertinence: ⭐⭐⭐⭐ ou meilleur?
│  ├─ OUI → Continue
│  ├─ NON → Tester script #2 ou #3 (autre angle)
│  └─ STILL NO → Changer secteur (nutrition → cosmétique)
│
└─ Production quality: ⭐⭐⭐⭐ ou meilleur?
   ├─ OUI → Continue
   ├─ NON (montage rough) → Polish CapCut (10 min)
   └─ ACCEPTABLE FOR MVP → Continue quand-même

DECISION:
3/3 dimensions ⭐⭐⭐⭐ → LAUNCH (pitchez client)
2/3 dimensions ⭐⭐⭐⭐ → CONTINUE (acceptable MVP)
1/3 dimensions ⭐⭐⭐⭐ → ADJUST ou PIVOT
0/3 dimensions → Rethink stratégie entièrement (rare)
```

---

## 🎯 Reality check: Fallback timeline

```
IF Arcads test fails completely:

Jour 0-1: Decide HeyGen ou restructure brief
Jour 2-4: Generate HeyGen (slower but possible)
Jour 4-5: CapCut montage (identical process)
Jour 5-6: Client présentation
         
Total: ~6-7 days (vs 72h ideal)

Coût supplémentaire: €0 (HeyGen gratuit 3 min)

Outcome: Still viable pour premier client,
juste moins "overnight success", plus "3-4 jours"
```

---

## 💡 Key learnings if pivot needed

```
Write down immédiatement:
├─ Pourquoi Arcads a échoué (avatar? angle? production?)
├─ Quel alternative on a testé (HeyGen / Synthesia / autre)
├─ Pourquoi Plan B mieux (ou moins bon)
├─ Timing réel vs 72h théorique
├─ Coût réel vs €100 budget
└─ Prochaines amélioration pour prospect #2

Ce document devient ton playbook pour scaling.
```

---

**REMINDER:** Ces scénarios couvrent 95% des edge cases. 
La plupart du temps: Arcads works, montage clean, client dit yes.
Mais si non: tu as un plan B (et C, et D).

Prêt?

