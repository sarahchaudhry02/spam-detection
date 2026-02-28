# **spam-detection**

Dieses Projekt untersucht zwei grundlegend verschiedene Ansätze der Textklassifizierung, um Spam-Mails zu identizfizieren. 
Einmal einen klassischen statistischen Ansatz:
Bag-of-Words mit Naive Bayes.
und einen modernen Deel-Learnung-Ansatz:
.......

#**Projektziel**
Das Ziel ist der Aufbau .. vom Modellen und dabei liegt der Fokus auf dem Vergleich dieser Modelle.
Dabei wird gepürft ob das moderne Modell einen signifikanten Mehrwert als das statistische Modell liefert.

#**Daten preperation**

**Quelle**: Kaggle (link)
**Umfang**: Ursprünglich ca. 5.728 E-Mails

**Preprocessing-Schritte**
Deduplizierung: Identische Daten bzw. Texte wurden entfernt, um Bias im Training zu vermeiden

Label Encoding: Transformation der Labels (Spam/Nicht-Spam) in ein binäres Format (1/0)

Data Split: Saubere Aufteilung in 60% Training, 20% Validation und 20% Test, um die Genereliserungsfähigkeit sicherzuerstellen.
Auggrund der hohen Datenmenge wurde 60% für das Trainig verwendet, da es ausreichend ist. Da der Vergleich im Fokus stand, war es für dieses Projekt wichtig, dass die Validation und Testfälle genügend Daten und die Metriken Aussagekraft haben.

#**Methodik**
Wie erwähnt wurden zwei unterschiedliche Ansätze implementiert, um diese miteiander zu vergleichen.

**1. Verfahren: Bag-of-Words mit Naive Bayes**
Dieses Verfahren repräsentiert die "altmodische" Art des Machine Learning für Text.

methoden 
beide verfahren

metriken

ergebnisse


visualiseurng
