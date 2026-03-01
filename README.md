# **Spam Detection: Ein Vergleich zwischen klassischem und moderernem Ansatz**

Dieses Projekt untersucht zwei grundlegend verschiedene Ansätze der Textklassifizierung, um Spam-Mails zu identizfizieren. 

**Einen klassischen statistischen Ansatz:**

Bag-of-Words mit Naive Bayes.

**Einen modernen NLP-Ansatz:**

Sentence-Transformer mit logistischer Regression


# **Projektziel**
Das Ziel ist die Implementierung, Evaluation und vergleichende Analyse zweier Modelle zur Spam-Erkennung.
Dabei wird untersucht, ob das moderne Modell einen signifikanten Mehrwert gegenüber einem klassisischen probabilisitschen Verfahren bietet.


# **Daten preperation**

**Quelle**: 

Autor: Gokul Raja
der Autor hat keine Lizens angegeben
Links: https://www.kaggle.com/datasets/gokulraja84/emails-dataset-for-spam-detection

**Umfang**: 

Ursprünglich ca. 5.728 E-Mails

# Preprocessing-Schritte

**Deduplizierung:**

Identische Daten bzw. Texte wurden entfernt, um Verzerrung zu vermeiden

**Label Encoding:**

Transformation der Labels (Spam/Nicht-Spam) in ein binäres Format (1/0)

**Data Split:**

Aufteilung in 60% Training, 20% Validation und 20% Test.
Aufgrund der hohen Datenmenge wurde 60% für das Trainig verwendet, da es für das Training ausreichend ist. Da der Vergleich im Fokus stand, war es für dieses Projekt wichtig, dass die Validation und Testfälle genügend Daten und die Metriken Aussagekraft haben.

# **Methodik**

Wie erwähnt wurden zwei unterschiedliche Ansätze implementiert, um diese miteiander zu vergleichen.

# 1. Verfahren: Bag-of-Words mit Naive Bayes
Dieses Verfahren repräsentiert die "altmodische" Art des Machine Learning für Text.

**Vektorisierung**: Dabei wurde das Bag-of-Word via "CountVectorizer" mit dem Biagramme "ngram_range(1,2) verwendet, um Wortkombinationen zu erfassen.


**Klassifikationsalgorithmus**: Hier wurde Multinomial Naive Bayes "MultinomialNB" verwendet.

**Funktionsweise**

Das Modell sieht den Text als ein "Beutel voller Wörter". Die Reihenfolge ist irrelevant. Die Anzahl jedoch nicht.
Der Naive Bayes Ansatz nutzt die Wahrscheinlichkeitsrechnung (Satz von Bayes). Damit wurd berechnet die hoch die Wahrscheinlicht ist, dass der ausgewählte Text Spam ist.

**Begrüdundung der Auswahl**

Das Verfahren ist effizienz und benötigt wenig Speicherplatz. Auch ist es standard seit jahrzenten und funktoniert gut, da Spam oft eindeutige Signalwörter enthält, die statisitsch signifikanter häufiger vorkommen.

# 2. Verfahren: Sentence-Transformer mit logitistschen Regression
Die Idee dieses Verfahren basiert auf modernen Deep-Leaning-Ansatz, die auch in NLP (Natural Language Processing) stecken.

**Vektorisierung**: Dabei wurde der SentenceTransformer mit dem Modell "all-MiniLM-L6-v2" verwendet,
da es eine Balance zwischen Geschwingifkeit und semnatischer Genauigkeit bietet.

**Klassifikationsalgorithmus**: Hier wurde die logistische Regression verwendet.

**Funktionsweise**

Das Modell erzeugt Embeddings, das bedeuted, die Mail wird in einen 384-dimensionalen Vektor umgewandelt. Dieser Vektor stellt die Semantik (Bedeutung) des Textes dar. Wörter mit ähnlicher Bedeutung landen im mathematischen Razm nah beieinander.
Dies wurde mit dem SBERT-Modell umgesetzt.

**Begrüdundung der Auswahl**

Dieses Verfahren erkennt  Spam auch wenn keine klassisische Signalwörter vorkommen. Somit ist das Modell robuster gegen das abwandeln der Wörter in Synonyme. Auch wird dabei das Transer Leaerning benutzt, das Modell weiß also schon wie messchliche Sprache funktoniert.

# **Metriken**

**Accuracy**
wurde bewusst weggelassen da aufgrund der imbalance (siehe EDA Balkendiagramm) andere Metriken aussagekräftiger sind

**Matthews Correlation Coefficient (MCC)**
Datensätze sind oft imbalanciert. Der MCC bewertet die Vorhersagequalität beider Klassen gleichermaßen und wurde deswegen zum vergleichen benutzt.

**Precission**
Damit wird ermittelt, wie viele von den vorhergesgaten Spams auch wirklich Spams sind. Somit kann verglichen werden, ob die Modelle wichtige Mails nicht fälschlicher als Spam einordnen.

**Recall**
Damit wird ermittelt, wie viele von den echten Spam Nachrichten erkannt wurden. Somit kann verglichen werden, wie oft die Modelle Spams übersehen.


**Confusiom Matrix**
zur visuellen Kontrolle der Fehlklassifikationen.

# **Ergebnisse**

Im Folgenden werden die Ergebnisse grafisch aufbereitet dargestellt. Dabei liegt der Fokus auf der Veranschaulichung. Die vollständigen Tabellen und alle exakten Werten für Training, Validierung und Test sind in beigefüten Notebook unter 'main/notebook/SpamDetection.ipynb' im Abschnitt "Metriken" einsehbar.

**EDA Verteilung der Mails in Daten**

<img width="715" height="479" alt="download-2" src="https://github.com/user-attachments/assets/c6c0b528-8255-4ad5-9623-6e62a041d203" />

Dieses Diagramm zeigt eine klare imbalance. Es sind deutlich mehr Nicht-Spam als Spams vorhanden.

**Confusion-Matrix für Verfahren 1**

<img width="1240" height="484" alt="Verfahren-1" src="https://github.com/user-attachments/assets/f70c4135-e188-42f8-b7d4-dfbbe1200e73" />

Es gibt 0 bis 1 False Positives und auch nur eine handvolle False Negatives


**Confusion-Matrix für Verfahren 2**

<img width="1240" height="484" alt="Verfahren-2" src="https://github.com/user-attachments/assets/71b411ad-a8bc-4156-911f-22baf0375d2a" />

Es gibt handvolle Anzahl False Positives und True Positives

**Balkendiagramm der Metriken für Testset**

<img width="855" height="479" alt="download-1" src="https://github.com/user-attachments/assets/b00579c4-d135-4702-97fe-4c4c52abc1c7" />
In allen benutzen Metriken liegt das erste Verfahren vorne, jedoch liegt das zweite Verfahren nicht weit hinten und hat immer noch gut Werte.



# Interpreation

Insgesamt konnte das erste Verfahren durch herausragende Effizienz und Treffsicherheit überzeugen.  Besonders hervorzuheben ist die extrem geringe Rate an False Positives. Jedoch bleibt zu beachten, dass dieses Modell ein reiner „Wortzähler“ ist. Es erkennt statistische Auffälligkeiten zwar perfekt, stößt aber an seine Grenzen, sobald Spam-Inhalte keine klassischen Signalwörter enthalten oder semantisch geschickt getarnt sind. 

Das zweite Verfahren ist technisch deutlich fortschrittlicher, schnitt jedoch in den Metriken minimal schlechter ab. Zwar kann es Kontext und Bedeutung verstehen, aber benötigt einen massiv höheren Ressourcenbedarf.

Das Projekt zeigt deutlich: Neu ist nicht automatisch besser 


# **Kritik und Grenzen des Projekts**

**Grenzen der Daten**

Obwohl der Datensatz umfangreich ist, stellt er lediglich einen statistischen Snapshot von Kaggle dar. Es ist möglich, dass die enthaltenen E-Mails „zu einfach“ strukturiert waren und nicht die volle Komplexität moderner, vielfältiger Spam-Strategien abbilden. 
In der Realität wandelt sich Spam täglich. Spammer entwickeln ständig kreative Methoden, um Filter zu umgehen. Ein rein statistisches Modell wie Naive Bayes kann solche Muster ohne ständige Updates kaum abfangen. Da auch Scam-Methoden technologisch aufrüsten, sind Modelle auf Basis statischer Altdaten in der Praxis mit Vorsicht zu genießen.
Insgesamt können diese Daten nur verwendet werden, um die Modelle zu miteinander zu vergleichen und keinen realen Spam-Detector zu implmentieren.

**Rechenkosten und Latenz**

Der Transformer beraucht eine GPU und viel Zeit für die Embeddings. In der Realen Welt spielt Effizienz aber eine wichtige Rolle



