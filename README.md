# **spam-detection**

Dieses Projekt untersucht zwei grundlegend verschiedene Ansätze der Textklassifizierung, um Spam-Mails zu identizfizieren. 
Einmal einen klassischen statistischen Ansatz:
Bag-of-Words mit Naive Bayes.
und einen modernen Deel-Learnung-Ansatz:
.......

# **Projektziel**
Das Ziel ist der Aufbau .. vom Modellen und dabei liegt der Fokus auf dem Vergleich dieser Modelle.
Dabei wird gepürft ob das moderne Modell einen signifikanten Mehrwert als das statistische Modell liefert.

# **Daten preperation**

**Quelle**: 

Kaggle (link)
**Umfang**: 

Ursprünglich ca. 5.728 E-Mails

**Preprocessing-Schritte**
Deduplizierung: Identische Daten bzw. Texte wurden entfernt, um Bias im Training zu vermeiden

Label Encoding: Transformation der Labels (Spam/Nicht-Spam) in ein binäres Format (1/0)

Data Split: Saubere Aufteilung in 60% Training, 20% Validation und 20% Test, um die Genereliserungsfähigkeit sicherzuerstellen.
Auggrund der hohen Datenmenge wurde 60% für das Trainig verwendet, da es ausreichend ist. Da der Vergleich im Fokus stand, war es für dieses Projekt wichtig, dass die Validation und Testfälle genügend Daten und die Metriken Aussagekraft haben.

# **Methodik**
Wie erwähnt wurden zwei unterschiedliche Ansätze implementiert, um diese miteiander zu vergleichen.

# 1. Verfahren: Bag-of-Words mit Naive Bayes
Dieses Verfahren repräsentiert die "altmodische" Art des Machine Learning für Text.

Dabei wurde für die Vektori....

**Funktionsweise**

Das Modell sieht den Text als ein "Beutel voller Wörter". Die Reihenfolge ist irrelevant. Die Anzahl jedoch nicht.
Der Naive Bayes Ansatz nutzt die Wahrscheinlichkeitsrechnung (Satz von Bayes). Damit wurd berechnet die hoch die Wahrscheinlicht ist, dass der ausgewählte Text Spam ist.

**Begrüdundung der Auswahl**

Das Verfahren ist effizienz und benötigt wenig Speicherplatz. Auch ist es standad seit jahrzenten und funktoniert gut, da Spam oft eindeutigr Signalwörter enthält, die statisitsch auffallen.

# 2. Verfahren: Sentence-Transformer mit logitistschen Regression
Die Idee dieses Verfahren basiert auf modernen Deep-Leaning-Ansatz, die auch in NLP (Natural Language Processing) stecken.

Dabei wurde für die Vektorisierung der SentenceTransformer mit dem Modell "all-MiniLM-L6-v2" verwendet BGRÜDNUNG!!
Als Algorithmus wurde die logitische Regression verwendet.

**Funktionsweise**

Das Modell erzeugt Embeddings (ERKLÄFUNG!!). Das SBERT-Modell wandelt dabei eine komplette E-Mail in einen mathematischen Vektor mit 384 Dimensionen um. Diese Vektor stellt die Semantik (Bedeutung) des Txtes dar.(wurde das im notebook eröwhnt?)
Wörter mit ähnlicher Bedeutung landen im mathematischen Razm nah beieinander.

**Begrüdundung der Auswahl**

Dieses Verfahren erkennt  Spam auch wenn keine klassisische Signalwörter vorkommen. Somit ist das Modell robuster gegen das abwandeln der Wörter in Synonyme. Auch wird dabei das Transer Leaerning benutzt, das Modell weiß also schon wie Sprache funktoniert.

# **Metriken**

**Accuracy**
wurde bewusst weggelassen da andere metriken aussagekräftiger sind

**Matthews Correlation Coefficient (MCC)**
Datensätze sind oft imbalanciert. Der MCC bewertet die Vorhersagequalität beider Klassen gleichermaßen und wurde deswegen zum vergleichen benutzt.

**Precission**
Damit wird ermittelt, wie viele von den vorhergesgaten Spams auch wirklich Spam ist. Dies wurde verwednet um zu vergleichen ??

**Recall**
Damit wird ermittelt, wie viele von den echten Spam Nachrichten erkannt wurden.
...

**Confusiom Matrix**
....

# **Ergebnisse**
Im folgenden Verlauf werden die graphische Darstellungen vorgestellt. Diese sind aber nur eine Zusammenfassung, da diese reichen um das allgemine Muster zu erkennen. Die genauen Werte für train validation und testset sind im notebook zu finden.

**Confusion-Matrix für Verfahren 1**

<img width="1240" height="484" alt="Verfahren-1" src="https://github.com/user-attachments/assets/f70c4135-e188-42f8-b7d4-dfbbe1200e73" />

**Confusion-Matrix für Verfahren 1**

<img width="1240" height="484" alt="Verfahren-2" src="https://github.com/user-attachments/assets/71b411ad-a8bc-4156-911f-22baf0375d2a" />


**Balkendiagramm der Metriken für Testset**

<img width="855" height="479" alt="download-1" src="https://github.com/user-attachments/assets/b00579c4-d135-4702-97fe-4c4c52abc1c7" />




visualiseurng
