# Script to update ITALY_SUBJECTS and CURATED_CONCEPT_TOPICS with exact text from Riassunti_Completi_Tutte_Materie.docx
import re

html_path = r'c:\Users\Enrico\Desktop\Giada\the_irish_year.html'
with open(html_path, 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update ITALY_SUBJECTS
new_italy_subjects = """    const ITALY_SUBJECTS = [
      {
        id: "history",
        name: "Storia (History)",
        type: "Umanistico",
        image: IMAGES.subjects.history,
        summary: "Ondata rivoluzionaria europea del 1848, le 5 giornate di Milano e la diplomazia di Cavour, le guerre d'indipendenza italiana, il Risorgimento con la Spedizione dei Mille e le grandi ideologie dell'800.",
        keywords: ["Moti del 1848", "Risorgimento", "Guerre d'Indipendenza", "Ideologie dell'800"],
        topics: [
          "I moti rivoluzionari del 1848",
          "Le 5 giornate di Milano e la diplomazia di Cavour",
          "Il Risorgimento e la Spedizione dei Mille",
          "Le guerre d'indipendenza italiana",
          "Le grandi ideologie dell'800"
        ],
        reflection: "Analisi approfondita dei processi storici, delle trasformazioni geopolitiche e delle grandi correnti di pensiero dell'Ottocento.",
        detailedTopics: [
          {
            title: "I moti rivoluzionari del 1848",
            desc: "Ondata rivoluzionaria europea del 1848. Cause: tensioni sociali, nazionalismo, liberalismo, crisi economica. Partecipazione di borghesia, operai, intellettuali. Francia: fine monarchia, II Repubblica, poi Napoleone III. Austria: richieste di autonomia delle nazionalità, represse ma fine servitù della gleba. Germania: unificazione e costituzione liberale, fallimento. Italia: indipendenza dall'Austria, costituzioni concesse poi revocate."
          },
          {
            title: "Le 5 giornate di Milano e la diplomazia di Cavour",
            desc: "5 Giornate di Milano (18-22 marzo 1848): insurrezione popolare contro l'occupazione austriaca con i leader Cattaneo e Manara; Radetzky si ritira temporaneamente. Cavour: modernizza il Piemonte, cerca alleanze internazionali, partecipa alla Guerra di Crimea (1855) e stringe gli Accordi di Plombières (1858) con Napoleone III."
          },
          {
            title: "Il Risorgimento e la Spedizione dei Mille",
            desc: "Risorgimento (1815-1871): unificazione italiana tra corrente democratica (Mazzini, Garibaldi), moderata (Cavour) e neoguelfa (Gioberti). Spedizione dei Mille (1860): partenza da Quarto (5 maggio), sbarco a Marsala (11 maggio), battaglie in Sicilia, risalita verso Napoli e incontro a Teano con Vittorio Emanuele II."
          },
          {
            title: "Le guerre d'indipendenza italiana",
            desc: "Quadro delle guerre d'indipendenza: Prima Guerra (1848-49, Regno di Sardegna, sconfitta, Carlo Alberto abdica); Seconda Guerra (1859, Francia + Piemonte, vittoria, annessione della Lombardia al Piemonte); Terza Guerra (1866, Prussia + Italia, vittoria diplomatica, Veneto all'Italia); Presa di Roma (1870, vittoria e proclamazione di Roma capitale)."
          },
          {
            title: "Le grandi ideologie dell'800",
            desc: "Le correnti di pensiero ottocentesche: Liberalismo (libertà individuale, proprietà, stato limitato con Locke, Smith, Mill); Nazionalismo (nazione come comunità, autodeterminazione); Socialismo (proprietà collettiva, uguaglianza con Marx, Engels); Conservatorismo (tradizione, ordine, autorità con Burke, Metternich); Democrazia (sovranità popolare, suffragio); Anarchismo (abolizione dello stato, libertà assoluta con Bakunin)."
          }
        ]
      },
      {
        id: "literature",
        name: "Letteratura Italiana",
        type: "Letteratura",
        image: IMAGES.subjects.literature,
        summary: "L'Illuminismo italiano e Il Caffè, il Neoclassicismo e il Romanticismo a confronto, Ugo Foscolo con le passioni e i Sepolcri, Alessandro Manzoni e la Provvidenza, e Giacomo Leopardi con la poetica del pessimismo.",
        keywords: ["Illuminismo & Caffè", "Ugo Foscolo", "Alessandro Manzoni", "Giacomo Leopardi"],
        topics: [
          "L'illuminismo italiano e 'Il Caffè'",
          "Ugo Foscolo: passioni e 'Dei Sepolcri'",
          "Alessandro Manzoni e la provvidenza",
          "Neoclassicismo e Romanticismo",
          "Giacomo Leopardi e la poetica del pessimismo"
        ],
        reflection: "Approfondimento critico sui testi fondativi della letteratura italiana, sulle passioni civili e sulle grandi poetiche dell'Ottocento.",
        detailedTopics: [
          {
            title: "L'illuminismo italiano e 'Il Caffè'",
            desc: "Seconda metà del '700, con centro a Milano. La rivista 'Il Caffè' (1764-66) fondata dai fratelli Verri e da Cesare Beccaria. Obiettivi fondamentali: diffondere le idee illuministe, promuovere il progresso civile ed economico, riformare la giustizia e sostenere l'abolizione della tortura e della pena di morte."
          },
          {
            title: "Ugo Foscolo: passioni e 'Dei Sepolcri'",
            desc: "Vita e poetica (1778-1827): nato a Zante, esule politico, muore a Londra. Grandi temi foscoliani: patriottismo, passioni civili, funzione delle illusioni, morte e memoria. Il carme 'Dei Sepolcri' (1807): le tombe come legame sacro tra vivi e morti ed eternatrice memoria storica attraverso la poesia."
          },
          {
            title: "Alessandro Manzoni e la provvidenza",
            desc: "Vita e pensiero (1785-1873): Milano, conversione religiosa (1810), senatore del Regno. Il concetto di Provvidenza: Dio guida la storia umana verso il bene anche attraverso il dolore. Nei 'Promessi Sposi': fede, giustizia divina, conversione dell'Innominato e redenzione degli umili."
          },
          {
            title: "Neoclassicismo e Romanticismo",
            desc: "Confronto analitico tra Neoclassicismo e Romanticismo: Ragione (Neoclassicismo) vs. Sentimento (Romanticismo); Bellezza Ideale vs. Sublime; Natura Ordinata vs. Natura Selvaggia; Eroe Virtuoso vs. Eroe Tormentato e ribelle."
          },
          {
            title: "Giacomo Leopardi e la poetica del pessimismo",
            desc: "L'evoluzione del pensiero leopardiano: Pessimismo individuale (sofferenza personale e solitudine); Pessimismo storico (gli antichi felici grazie alle illusioni della natura, i moderni infelici a causa della ragione); Pessimismo cosmico (la Natura come matrigna indifferente per tutti gli esseri viventi, universo indifferente, solidarietà de 'La Ginestra')."
          }
        ]
      },
      {
        id: "printing",
        name: "Tecnologie dei Processi di Produzione (Stampa)",
        type: "Tecnologia Industriale",
        image: IMAGES.subjects.printing,
        summary: "Principi e meccanica della stampa offset, materiali polimerici, impianti di stampa flessografica, stampa digitale con sistemi CTP e cartotecnica con fustellatura e packaging.",
        keywords: ["Stampa Offset", "Polimeri (PE/PP/PET)", "Flessografia", "Digitale & CTP"],
        topics: [
          "Principi e meccanica della stampa offset",
          "Materiali polimerici",
          "Impianti di stampa flessografia",
          "Stampa digitale e sistemi CTP",
          "Cartotecnica, fustellatura e packaging"
        ],
        reflection: "Comprensione approfondita delle tecnologie di produzione grafica, dei supporti polimerici e dei processi industriali di cartotecnica e packaging.",
        detailedTopics: [
          {
            title: "Principi e meccanica della stampa offset",
            desc: "Tecnica planografica indiretta basata sul principio di repulsione chimica tra acqua e inchiostro grasso. Componenti della macchina: lastra matrice, gruppo di bagnatura, rulli inchiostratori, cilindro gommato di caucciù (offset) e cilindro di contropressione."
          },
          {
            title: "Materiali polimerici",
            desc: "Proprietà e impieghi dei principali polimeri per imballaggio e stampa: PE (polietilene, flessibile per sacchetti), PP (polipropilene, resistente al calore per confezioni alimentari), PET (polietilene tereftalato, trasparente per bottiglie), PVC (cloruro di polivinile, rigido/flessibile) e PS (polistirene, rigido per vaschette)."
          },
          {
            title: "Impianti di stampa flessografia",
            desc: "Stampa rotativa diretta a rilievo con matrici fotopolimeriche flessibili per packaging e supporti flessibili. Componenti dell'impianto: svolgitore, rullo anilox ceramico microinciso, lastra fotopolimerica, essiccatoio e riavvolgitore."
          },
          {
            title: "Stampa digitale e sistemi CTP",
            desc: "Stampa digitale: processo diretto senza matrice da file elettronico (elettrofotografia a toner e inkjet industriale). Sistemi CTP (Computer-to-Plate): incisione diretta laser della lastra da file digitale, eliminando pellicole fotografiche con maggiore qualità e velocità."
          },
          {
            title: "Cartotecnica, fustellatura e packaging",
            desc: "Cartotecnica: lavorazione e trasformazione di carta e cartoncino in scatole e astucci. Fustellatura: operazione di taglio sagomato e cordonatura (piega) con fustella a lame d'acciaio. Livelli di packaging: primario (contatto diretto col prodotto), secondario (vendita e raggruppamento) e terziario (trasporto logistico)."
          }
        ]
      },
      {
        id: "graphicDesign",
        name: "Progettazione Multimediale (Grafica & Comunicazione)",
        type: "Progettazione Visiva",
        image: IMAGES.subjects.graphicDesign,
        summary: "Design editoriale e grid system, manifesti per affissione esterna (Out-of-Home), composizione advertising con principi della Gestalt, corporate identity e pieghevoli promozionali.",
        keywords: ["Grid System", "Manifesti OOH", "Principi Gestalt", "Corporate Identity"],
        topics: [
          "Design editoriale e grid system",
          "Manifesti out-of-home",
          "Composizione advertising e Gestalt",
          "Corporate identity e pieghevoli"
        ],
        reflection: "Padronanza delle gabbie editoriali, della psicologia visiva della Gestalt, dei grandi formati OOH e dell'identità aziendale coordinata.",
        detailedTopics: [
          {
            title: "Design editoriale e grid system",
            desc: "Organizzazione dei contenuti visivi e testuali tramite griglie strutturate: gestione di margini, colonne, righe e moduli per garantire coerenza visiva, gerarchia e massima leggibilità."
          },
          {
            title: "Manifesti out-of-home",
            desc: "Progettazione di formati per la comunicazione visiva esterna: manifesti 6x3 m per strade principali, 12x3 m per autostrade, poster per pensiline alle fermate dei bus e schermi dinamici Digital DOOH."
          },
          {
            title: "Composizione advertising e Gestalt",
            desc: "Applicazione delle leggi della percezione visiva: Prossimità (elementi vicini percepiti come gruppo), Somiglianza (elementi simili percepiti come correlati), Chiusura (la mente completa automaticamente le forme) e Continuità (l'occhio segue naturalmente linee e percorsi visivi)."
          },
          {
            title: "Corporate identity e pieghevoli",
            desc: "Corporate identity: costruzione dell'identità coordinata aziendale attraverso logo, palette colori, font tipografici e tone of voice. Pieghevoli: progettazione di formati a 2 ante, a 3 ante (a portafoglio o a fisarmonica), gatefold (a finestra) e z-fold."
          }
        ]
      },
      {
        id: "photography",
        name: "Linguaggio Audiovisivo e Fotografia",
        type: "Audiovisivo",
        image: IMAGES.subjects.photography,
        summary: "Still life e schemi di luce in studio, montaggio video professionale con Premiere Pro, grammatica dell'inquadratura, ritmo visivo, stacchi di montaggio e colonna sonora.",
        keywords: ["Luce in Studio", "Premiere Pro", "Grammatica Inquadratura", "Montaggio & Audio"],
        topics: [
          "Still life e luce in studio",
          "Montaggio video con Premiere Pro",
          "Grammatica dell'inquadratura",
          "Ritmo visivo, stacchi, colonna sonora"
        ],
        reflection: "Sviluppo della narrazione visiva: gestione professionale delle luci in studio, sintassi dell'inquadratura e montaggio audiovisivo.",
        detailedTopics: [
          {
            title: "Still life e luce in studio",
            desc: "Gestione delle sorgenti di illuminazione in studio: Key Light (luce principale), Fill Light (luce di riempimento per schiarire le ombre), Backlight (controluce per staccare il soggetto dallo sfondo) e Rim Light (luce di taglio per evidenziare i contorni)."
          },
          {
            title: "Montaggio video con Premiere Pro",
            desc: "Flusso di lavoro nell'editing video digitale non lineare: importazione file e media bin, montaggio su timeline multitraccia, correzione colore (Lumetri), missaggio di audio e musica ed esportazione nei formati standard."
          },
          {
            title: "Grammatica dell'inquadratura",
            desc: "Scala dei piani: CLL (Campo Lunghissimo), CL (Campo Lungo), FI (Figura Intera), PA (Piano Americano), PM (Primo Mezzo), PP (Primo Piano), PPP (Primissimo Piano), Dettaglio. Angoli di ripresa: normale, plongée (dall'alto), contre-plongée (dal basso), olandese. Movimenti di camera: panoramica, carrello, zoom, steadicam."
          },
          {
            title: "Ritmo visivo, stacchi, colonna sonora",
            desc: "Tecniche di transizione: cut (stacco netto), dissolve (dissolvenza incrociata), fade (a nero/bianco), wipe (tendina), match cut (raccordo grafico), jump cut (stacco discontinuo). Componenti audio: colonna sonora musicale, SFX ed effetti foley, dialoghi, voiceover e pause narrative di silenzio."
          }
        ]
      },
      {
        id: "mathsIt",
        name: "Matematica (Analisi Matematica)",
        type: "STEM",
        image: IMAGES.subjects.maths,
        summary: "Studio di funzione analitico, sistemi esponenziali e logaritmici, funzioni razionali intere e fratte, funzioni esponenziali e logaritmiche.",
        keywords: ["Studio di Funzione", "Esponenziali & Logaritmi", "Funzioni Razionali", "Asintoti & Grafici"],
        topics: [
          "Studio di funzione",
          "Sistemi esponenziali e logaritmici",
          "Funzioni razionali",
          "Funzioni esponenziali e logaritmiche"
        ],
        reflection: "Esercizio di rigore analitico, formalizzazione algebrica e tracciamento qualitativo dei comportamenti asintotici nel piano cartesiano.",
        detailedTopics: [
          {
            title: "Studio di funzione",
            desc: "Procedura analitica in 7 passaggi: 1. Calcolo del Dominio (campo di esistenza); 2. Intersezioni con gli assi cartesiani; 3. Studio del Segno (positività e negatività); 4. Limiti agli estremi e ricerca degli Asintoti; 5. Derivata prima per crescenza/decrescenza e punti stazionari; 6. Derivata seconda per concavità e flessi; 7. Tracciamento del Grafico qualitativo."
          },
          {
            title: "Sistemi esponenziali e logaritmici",
            desc: "Equazioni e disequazioni esponenziali (a^x = b) e logaritmiche (log_a(x) = b). Proprietà fondamentali dei logaritmi: logaritmo del prodotto, logaritmo del quoziente, logaritmo della potenza e formula del cambio di base."
          },
          {
            title: "Funzioni razionali",
            desc: "Razionali intere: polinomi con Dominio su tutto l'insieme dei numeri reali R. Razionali fratte: rapporto di polinomi P(x)/Q(x) con condizione di esistenza Q(x) ≠ 0, calcolo degli asintoti verticali, orizzontali e obliqui."
          },
          {
            title: "Funzioni esponenziali e logaritmiche",
            desc: "Studio e confronto delle funzioni trascendenti: Funzione Esponenziale y = a^x (forma a^x, Dominio R, asintoto orizzontale y = 0); Funzione Logaritmica y = log_a(x) (forma log_a(x), Dominio x > 0, asintoto verticale x = 0)."
          }
        ]
      },
      {
        id: "englishIt",
        name: "Lingua e Letteratura Inglese (Programma Italia)",
        type: "Lingua Straniera",
        image: IMAGES.subjects.english,
        summary: "Oscar Wilde e l'esteticismo, Alan Turing e la decifrazione di Enigma, Charles Dickens e la critica sociale, e analisi comparata dei sistemi politici UK vs USA.",
        keywords: ["Oscar Wilde", "Alan Turing & Enigma", "Charles Dickens", "Sistemi Politici UK/USA"],
        topics: [
          "Oscar Wilde e l'esteticismo",
          "Alan Turing e Enigma",
          "Charles Dickens",
          "Sistemi politici UK vs USA"
        ],
        reflection: "Studio della letteratura e della civiltà anglosassone: estetica vittoriana, rivoluzione industriale, storia dell'informatica e istituzioni comparate.",
        detailedTopics: [
          {
            title: "Oscar Wilde e l'esteticismo",
            desc: "Tardo '800 e movimento 'Art for Art's Sake'. Oscar Wilde (1854-1900): 'The Picture of Dorian Gray' e 'The Importance of Being Earnest'. Temi: culto della bellezza, dualismo tra maschera sociale e coscienza, estetismo e decadenza morale."
          },
          {
            title: "Alan Turing e Enigma",
            desc: "Alan Turing (1912-1954): genio matematico a Bletchley Park, progettazione della macchina Bombe per decifrare i codici cifrati nazisti Enigma. Considerato il padre dell'informatica moderna e dell'intelligenza artificiale (Test di Turing)."
          },
          {
            title: "Charles Dickens",
            desc: "Charles Dickens (1812-1870): autore di 'Oliver Twist', 'A Christmas Carol' e 'Great Expectations'. Temi centrali: denuncia della povertà nelle città industriali, sfruttamento del lavoro minorile, orrori delle workhouses e critica sociale vittoriana."
          },
          {
            title: "Sistemi politici UK vs USA",
            desc: "Analisi istituzionale comparata: Regno Unito (Monarchia parlamentare, Sovrano + Primo Ministro, Parlamento con House of Commons e House of Lords, Costituzione non scritta) vs. Stati Uniti d'America (Repubblica federale presidenziale, Presidente, Congresso con House of Representatives e Senate, Costituzione scritta del 1787)."
          }
        ]
      },
      {
        id: "pe",
        name: "Scienze Motorie e Sportive",
        type: "Attività Motoria",
        image: IMAGES.bjjGym,
        summary: "Capacità motorie e controllo neuromuscolare, fisiologia dell'esercizio e apparato cardiorespiratorio, regolamenti ed etica sportiva.",
        keywords: ["Capacità Motorie", "Fisiologia dell'Esercizio", "Coordinazione", "Fair Play"],
        topics: [
          "Capacità motorie e controllo neuromuscolare",
          "Fisiologia dell'esercizio e apparato cardiorespiratorio",
          "Regolamenti, etica sportiva e tattica di gioco"
        ],
        reflection: "Sviluppo dell'efficienza fisica, della salute cardiorespiratoria, della disciplina sportiva e dei valori etici del fair play.",
        detailedTopics: [
          {
            title: "Capacità motorie e controllo neuromuscolare",
            desc: "Sviluppo e potenziamento delle capacità condizionali (forza, resistenza, velocità) e coordinative (equilibrio, orientamento spaziale, ritmo, destrezza oculo-manuale)."
          },
          {
            title: "Fisiologia dell'esercizio e apparato cardiorespiratorio",
            desc: "Funzionamento e adattamento del sistema cardiovascolare, polmonare e muscolare sotto sforzo; metabolismo energetico aerobico e anaerobico; importanza del riscaldamento, defaticamento e prevenzione degli infortuni."
          },
          {
            title: "Regolamenti, etica sportiva e tattica di gioco",
            desc: "Valori del fair play, rispetto dell'avversario e delle regole di gara; schemi tattici e dinamiche di collaborazione negli sport di squadra (pallavolo, basket) e individuali."
          }
        ]
      }
    ];"""

# Replace ITALY_SUBJECTS array
start_marker = "    const ITALY_SUBJECTS = ["
end_marker = "    const MAP_LOCATIONS = ["

italy_section = code.split(start_marker)[1].split(end_marker)[0]
code = code.replace(start_marker + italy_section, new_italy_subjects + "\n\n    ")

# 2. Add complete Curated Topics for all Italian topics into CURATED_CONCEPT_TOPICS
new_italian_curated = """      // Storia
      "I moti rivoluzionari del 1848": [
        { name: "Primavera dei Popoli", cat: "Contesto Europeo", exp: "Ondata insurrezionale europea del 1848 generata da tensioni sociali, aspirazioni nazionaliste, ideali liberali e crisi economica.", items: ["Tensioni Sociali & Crisi Economica", "Aspirazioni Liberali & Nazionali", "Mobilitazione Popolare Urbana", "Richiesta di Costituzioni"] },
        { name: "Francia & II Repubblica", cat: "Rivoluzione a Parigi", exp: "Caduta della monarchia orleanista di Luigi Filippo, proclamazione della Seconda Repubblica, riforme sociali e successiva ascesa di Napoleone III.", items: ["Caduta di Luigi Filippo", "Proclamazione della II Repubblica", "Ateliers Nationaux per il Lavoro", "Ascesa di Luigi Napoleone"] },
        { name: "Austria & Germania", cat: "Insurrezioni Centrali", exp: "Sollevazioni a Vienna e Budapest con richieste di autonomia delle nazionalità (fine della servitù della gleba) e tentativi costituzionali a Francoforte.", items: ["Insurrezione di Vienna e Budapest", "Abolizione della Servitù della Gleba", "Assemblea Costituente a Francoforte", "Riflusso Autoritario Asburgico"] },
        { name: "Moti Italiani del 1848", cat: "Indipendenza & Statuti", exp: "Lotta per l'indipendenza dal dominio austriaco e concessione iniziale delle carte costituzionali (Statuto Albertino) poi revocate negli altri stati.", items: ["Concessione dello Statuto Albertino", "Insurrezioni Antiasburgiche", "Revoca delle Costituzioni", "Eredità Istituzionale Piemontese"] }
      ],
      "Le 5 giornate di Milano e la diplomazia di Cavour": [
        { name: "5 Giornate di Milano", cat: "Insurrezione Popolare", exp: "L'epica rivolta popolare del 18-22 marzo 1848 guidata da Carlo Cattaneo e Luciano Manara che costrinse il maresciallo Radetzky alla ritirata.", items: ["Barricate Cittadine (18-22 Marzo)", "Consiglio di Guerra di Cattaneo", "Cacciata dell'Esercito Austriaco", "Ritirata verso il Quadrilatero"] },
        { name: "Modernizzazione Piemontese", cat: "Riforme di Cavour", exp: "L'azione politica di Camillo Benso di Cavour: sviluppo delle ferrovie, libero scambio, riforme bancarie e crescita economica del Regno di Sardegna.", items: ["Sviluppo Rete Ferroviaria", "Trattati Commerciali di Libero Scambio", "Riforma del Sistema Bancario", "Potenziamento dell'Esercito Sabaudo"] },
        { name: "Guerra di Crimea (1855)", cat: "Diplomazia Internazionale", exp: "Partecipazione piemontese al conflitto di Crimea per portare la questione italiana al Congresso di Parigi del 1856 davanti alle potenze europee.", items: ["Corpo di Spedizione a Cernaia", "Partecipazione al Congresso di Parigi", "Denuncia della Questione Italiana", "Accreditamento Internazionale"] },
        { name: "Accordi di Plombières (1858)", cat: "Alleanza Strategica", exp: "Patto segreto tra Cavour e Napoleone III: intervento militare francese a fianco del Piemonte in cambio della cessione di Nizza e Savoia.", items: ["Incontro Segreto di Plombières", "Alleanza Difensiva Franco-Piemontese", "Cessione di Nizza e della Savoia", "Creazione del Regno dell'Alta Italia"] }
      ],
      "Il Risorgimento e la Spedizione dei Mille": [
        { name: "Correnti Risorgimentali", cat: "Ideali di Unificazione", exp: "Il dibattito sull'unità: corrente democratica e repubblicana (Mazzini, Garibaldi), moderata liberale (Cavour) e neoguelfa (Gioberti).", items: ["Democratica (Mazzini & Garibaldi)", "Moderata Diplomatica (Cavour)", "Neoguelfa Papale (Gioberti)", "Federalismo Democratico (Cattaneo)"] },
        { name: "Partenza & Sbarco a Marsala", cat: "Impresa Garibaldina", exp: "La partenza da Quarto la notte del 5 maggio 1860 con mille volontari e lo sbarco a Marsala l'11 maggio sotto la guida di Giuseppe Garibaldi.", items: ["Partenza da Quarto (5 Maggio)", "Sbarco a Marsala (11 Maggio)", "Proclama di Salemi", "Vittoria Campale di Calatafimi"] },
        { name: "Liberazione del Mezzogiorno", cat: "Campagna Militare", exp: "Le vittorie garibaldine in Sicilia, la presa di Palermo, l'attraversamento dello Stretto di Messina e l'ingresso trionfale a Napoli.", items: ["Presa di Palermo e Milazzo", "Attraversamento dello Stretto", "Ingresso Trionfale a Napoli", "Battaglia del Volturno"] },
        { name: "Incontro di Teano (1860)", cat: "Unità Nazionale", exp: "Lo storico incontro del 26 ottobre 1860 a Teano tra Garibaldi e Vittorio Emanuele II, con la proclamazione del Regno d'Italia il 17 marzo 1861.", items: ["Incontro a Teano (26 Ottobre)", "Consegna del Sud al Re Sabaudo", "Plebisciti di Annessione", "Proclamazione del Regno (1861)"] }
      ],
      "Le guerre d'indipendenza italiana": [
        { name: "Prima Guerra (1848-49)", cat: "Iniziativa Sabauda", exp: "Guerra del Regno di Sardegna contro l'Austria: prime vittorie, poi sconfitte di Custoza e Novara che costrinsero Carlo Alberto all'abdicazione.", items: ["Dichiarazione di Guerra all'Austria", "Vittorie di Goito e Pastrengo", "Sconfitta Decisiva di Novara", "Abdicazione di Carlo Alberto"] },
        { name: "Seconda Guerra (1859)", cat: "Alleanza Francese", exp: "Conflitto condotto da Francia e Piemonte contro l'Austria: gloriose vittorie a Magenta, Solferino e San Martino con annessione della Lombardia.", items: ["Intervento di Napoleone III", "Vittorie di Magenta e Solferino", "Armistizio di Villafranca", "Annessione della Lombardia"] },
        { name: "Terza Guerra (1866)", cat: "Alleanza Prussiana", exp: "Alleanza italo-prussiana contro l'Austria: nonostante le sconfitte di Custoza e Lissa, l'Italia ottiene l'annessione del Veneto per via diplomatica.", items: ["Patto Militare Italo-Prussiano", "Scontri di Custoza e Lissa", "Vittoria Prussiana a Sadowa", "Cessione del Veneto all'Italia"] },
        { name: "Presa di Roma (1870)", cat: "Roma Capitale", exp: "La Breccia di Porta Pia del 20 settembre 1870: fine dello Stato Pontificio, annessione di Roma e sua proclamazione definitiva come Capitale d'Italia.", items: ["Caduta di Napoleone III a Sedan", "Breccia di Porta Pia (20 Settembre)", "Fine del Potere Temporale Papale", "Proclamazione di Roma Capitale"] }
      ],
      "Le grandi ideologie dell'800": [
        { name: "Liberalismo & Nazionalismo", cat: "Libertà & Identità", exp: "Liberalismo (libertà individuale, proprietà, stato limitato con Locke, Smith, Mill) e Nazionalismo (nazione come comunità e autodeterminazione).", items: ["Libertà Individuali e Civili", "Libero Mercato e Proprietà Privata", "Comunità Nazionale Autonoma", "Stato di Diritto Costituzionale"] },
        { name: "Socialismo Scientifico", cat: "Uguaglianza Sociale", exp: "La dottrina di Karl Marx e Friedrich Engels: abolizione della proprietà privata dei mezzi di produzione, lotta di classe e superamento del capitalismo.", items: ["Materialismo Storico", "Teoria del Plusvalore", "Lotta di Classe del Proletariato", "Società Senza Classi"] },
        { name: "Conservatorismo", cat: "Ordine & Tradizione", exp: "Dottrina politica basata sulla difesa della tradizione, dell'ordine costituito, dell'autorità e della stabilità sociale (Burke, Metternich).", items: ["Difesa delle Tradizioni Storiche", "Mantenimento dell'Ordine Sociale", "Principio di Autorità Istituzionale", "Rifiuto delle Rotture Rivoluzionarie"] },
        { name: "Democrazia & Anarchismo", cat: "Potere & Libertà Assoluta", exp: "Democrazia (sovranità popolare e suffragio universale) e Anarchismo (rifiuto totale di ogni stato e autorità gerarchica con Michail Bakunin).", items: ["Sovranità Popolare & Suffragio", "Rifiuto Totale dello Stato (Bakunin)", "Autogestione Sociale dal Basso", "Libertà Assoluta dell'Individuo"] }
      ],

      // Letteratura
      "L'illuminismo italiano e 'Il Caffè'": [
        { name: "La Rivista 'Il Caffè'", cat: "Milano Illuminista", exp: "Pubblicata a Milano tra il 1764 e il 1766 dai fratelli Pietro e Alessandro Verri e da Cesare Beccaria come organo dell'Accademia dei Pugni.", items: ["Milano Centro Illuminista", "Fratelli Pietro & Alessandro Verri", "Accademia dei Pugni", "Divulgazione Culturale Utile"] },
        { name: "Cesare Beccaria", cat: "Riforma della Giustizia", exp: "L'opera rivoluzionaria 'Dei delitti e delle pene' (1764): condanna razionale della tortura e della pena di morte a favore della rieducazione della pena.", items: ["'Dei delitti e delle pene' (1764)", "Abolizione della Tortura", "Condanna della Pena di Morte", "Funzione Rieducativa della Pena"] },
        { name: "Progresso Civile & Scienze", cat: "Ideali dei Lumi", exp: "Promozione della ragione, del metodo scientifico sperimentale e del rinnovamento economico e sociale a beneficio della collettività.", items: ["Primato della Ragione Critica", "Applicazione Scientifica ed Economica", "Rinnovamento dei Costumi Sociali", "Cosmopolitismo Intellettuale"] },
        { name: "Rinnovamento Linguistico", cat: "Stile & Comunicazione", exp: "Rottura con il pedantismo accademico e adozione di una lingua chiara, moderna e diretta ('cose, non parole') per comunicare con il pubblico.", items: ["Rifiuto del Purismo Accademico", "Principio 'Cose, non Parole'", "Prosa Semplice e Pragmatica", "Accessibilità al Vasto Pubblico"] }
      ],
      "Ugo Foscolo: passioni e 'Dei Sepolcri'": [
        { name: "Vita & Esilio Politico", cat: "Biografia Foscoliana", exp: "Nato a Zante nel 1778, patriota deluso dal Trattato di Campoformio, visse una vita tormentata da esule fino alla morte a Londra nel 1827.", items: ["Nascita a Zante (1778)", "Delusione di Campoformio", "Esilio Perpetuo in Europa", "Morte a Londra (1827)"] },
        { name: "Passioni & Illusioni", cat: "Poetica & Filosofia", exp: "Il contrasto tra la ragione materialista (che vede la morte come nulla eterno) e il valore vitale delle 'illusioni' (patria, amore, poesia, bellezza).", items: ["Materialismo Meccanicista", "Nulla Eterno della Morte", "Funzione Vitale delle Illusioni", "Fede nella Bellezza e nell'Amore"] },
        { name: "Carme 'Dei Sepolcri' (1807)", cat: "Capolavoro Poetico", exp: "Carme in endecasillabi sciolti in cui la tomba rappresenta il legame affettivo tra vivi e morti e il monumento alla memoria civile e morale di un popolo.", items: ["Composizione in Endecasillabi", "Legame Affettivo con i Defunti", "Esempio Civile di Santa Croce", "Ispirazione per le Future Generazioni"] },
        { name: "Poesia Eternatrice", cat: "Immortalità della Poesia", exp: "La poesia come custode immortale della memoria degli eroi e dei valori umani oltre il tempo e la distruzione materiale, celebrata nel mito di Omero ed Ettore.", items: ["Superamento della Distruzione Fisica", "Canto Eterno della Poesia", "Mito di Omero ed Ettore a Troia", "Trionfo Morale sulla Morte"] }
      ],
      "Alessandro Manzoni e la provvidenza": [
        { name: "Conversione & Fede", cat: "Spiritualità Manzoniana", exp: "La conversione religiosa del 1810 e la visione della fede come guida morale imprescindibile nella vita personale e nell'impegno letterario e civile.", items: ["Conversione Religiosa (1810)", "Cristianesimo Evangelico e Rigoroso", "Impegno Etico e Civile", "Fede come Luce nella Storia"] },
        { name: "La Provvidenza Divina", cat: "Disegno nella Storia", exp: "La convinzione che Dio guidi la storia umana verso un disegno di bene supremo ('il sugo di tutta la storia'), anche attraverso la sofferenza degli innocenti.", items: ["Dio Guida della Storia Umana", "Mistero del Dolore degli Innocenti", "Il 'Sugo di Tutta la Storia'", "Fiducia nell'Intervento Divino"] },
        { name: "I Promessi Sposi", cat: "Romanzo Storico", exp: "Il capolavoro manzoniano: la vicenda degli umili Renzo e Lucia nella Lombardia del '600 tra peste, carestia, prepotenze feudali e conversione dell'Innominato.", items: ["Protagonisti gli Umili (Renzo e Lucia)", "Quadro Storico del Seicento", "Conversione dell'Innominato", "Giustizia Divina ed Umana"] },
        { name: "Rivoluzione Linguistica", cat: "Lingua Nazionale", exp: "La scelta del fiorentino parlato colto come modello di lingua unitaria per tutta la nazione italiana ('risciacquatura dei panni in Arno').", items: ["Fiorentino Parlato Colto", "Risciacquatura in Arno (1840)", "Superamento dei Dialetti Locali", "Creazione della Lingua Nazionale"] }
      ],
      "Neoclassicismo e Romanticismo": [
        { name: "Ragione vs. Sentimento", cat: "Facoltà Umane", exp: "Il Neoclassicismo pone al centro il controllo razionale e la misura formale, mentre il Romanticismo esalta l'irrazionale, la passione e il sentimento puro.", items: ["Neoclassicismo: Primato Razionale", "Romanticismo: Impeto del Sentimento", "Controllo Formale vs. Passione", "Misura vs. Espressione Libera"] },
        { name: "Bellezza Ideale vs. Sublime", cat: "Canone Estetico", exp: "La Bellezza Ideale neoclassica (armonia, grazia, compostezza con Winckelmann e Canova) a confronto con il Sublime romantico (emozione grandiosa e vertiginosa).", items: ["Bellezza Ideale (Winckelmann & Canova)", "Armonia e Grazia Greca", "Sublime Romantico (Orrore Dilettevole)", "Vertigine dell'Infinito"] },
        { name: "Natura Ordinata vs. Selvaggia", cat: "Visione della Natura", exp: "La natura serena, armoniosa e geometrica del Neoclassicismo opposta alla natura selvaggia, tempestosa, misteriosa e vivente dei romantici.", items: ["Natura Pacificata e Solare", "Natura Selvaggia e Notturna", "Tempeste, Rupi e Abissi", "Specchio delle Tensioni dell'Anima"] },
        { name: "Eroe Virtuoso vs. Tormentato", cat: "Modello Umano", exp: "L'eroe classico virtuoso che domina le passioni sacrificandosi per il dovere vs. l'eroe romantico ribelle, solitario, incompreso e tragicamente tormentato.", items: ["Eroe Virtuoso e Composto", "Sacrificio per la Polis e il Dovere", "Eroe Romantico Ribelle (Titanismo)", "Vittima del 'Mal del Secolo'"] }
      ],
      "Giacomo Leopardi e la poetica del pessimismo": [
        { name: "Pessimismo Individuale", cat: "Fase Giovanile", exp: "La sofferenza personale legata all'isolamento di Recanati, alla malattia fisica e all'incomprensione familiare ('studio matto e disperatissimo').", items: ["Isolamento a Recanati", "Sofferenza Fisica e Malattia", "Incomprensione dell'Ambiente", "Ricerca Disperata della Gloria"] },
        { name: "Pessimismo Storico", cat: "Natura Madre Benigna", exp: "La Natura creata come madre benigna che donava illusioni e felicità agli antichi; la ragione moderna ha svelato la realtà rendendo l'uomo infelice.", items: ["Antichi Felici con le Illusioni", "Natura Madre Buona e Provvida", "Ragione Moderna Distruttrice", "Perdita dell'Innocenza Naturale"] },
        { name: "Pessimismo Cosmico", cat: "Natura Matrigna", exp: "Il passaggio decisivo (Dialogo della Natura e di un Islandese): la Natura è una matrigna indifferente al dolore, e l'infelicità è legge universale per tutti gli esseri.", items: ["Natura Matrigna Cieca e Crudele", "Indifferenza per la Sofferenza Umana", "Infelicità Condizione Universale", "Meccanicismo Materialista"] },
        { name: "La Ginestra & Solidarietà", cat: "Testamento Spirituale", exp: "Il messaggio finale de 'La Ginestra': l'invito agli esseri umani a stringersi in una 'social catena' di solidarietà e fratellanza contro la comune nemica Natura.", items: ["Fiore Gentile sulle Lave del Vesuvio", "Accettazione Nobile del Destino", "Social Catena di Fratellanza", "Dignità Umana contro la Natura"] }
      ],

      // Stampa
      "Principi e meccanica della stampa offset": [
        { name: "Tecnica Planografica Indiretta", cat: "Principio Fisico-Chimico", exp: "Processo indiretto basato sulla repulsione tra acqua e inchiostro grasso su una matrice planografica in alluminio microzincato.", items: ["Matrice Planografica in Alluminio", "Repulsione Acqua-Inchiostro Grasso", "Zone Grafiche Lipofile (Inchiostro)", "Zone Contrografiche Idrofile (Acqua)"] },
        { name: "Gruppo di Bagnatura & Inchiostrazione", cat: "Alimentazione Chimica", exp: "Rulli bagnatori che applicano la soluzione acquosa e rulli inchiostratori che distribuiscono un film uniforme di inchiostro sulla matrice.", items: ["Soluzione di Bagnatura Acquosa", "Controllo Alcool Isopropilico", "Rulli Bagnatori e Inchiostratori", "Dosaggio Micronico dell'Inchiostro"] },
        { name: "Cilindro di Caucciù (Offset)", cat: "Trasferimento Elastico", exp: "Il telo di caucciù gommato riceve l'inchiostro dalla matrice e lo trasferisce sul supporto con elevata morbidezza ed elasticità.", items: ["Telo di Caucciù Microstrutturato", "Trasferimento Indiretto Elastico", "Adattamento a Qualsiasi Carta", "Compensazione delle Irregolarità"] },
        { name: "Cilindro di Contropressione", cat: "Pressione di Stampa", exp: "Cilindro in acciaio che comprime il foglio di carta contro il caucciù con precisione micrometrica per garantire un'impronta perfetta.", items: ["Acciaio Rettificato ad Alta Resistenza", "Regolazione Micrometrica Pressione", "Trasporto Continuo a Pinze", "Stabilità del Registro di Stampa"] }
      ],
      "Materiali polimerici": [
        { name: "Polietilene (PE)", cat: "Polimero Flessibile", exp: "Polimero termoplastico altamente flessibile, impermeabile e resistente agli agenti chimici, ideale per sacchetti, pellicole e film estensibili.", items: ["PE ad Alta Densità (HDPE)", "PE a Bassa Densità (LDPE)", "Impermeabilità all'Umidità", "Sacchetti e Film da Imballaggio"] },
        { name: "Polipropilene (PP)", cat: "Resistenza Termica", exp: "Polimero con elevata rigidità, trasparenza e resistenza termica, ampiamente impiegato per confezioni alimentari sterilizzabili e film orientati BOPP.", items: ["Elevata Resistenza al Calore", "Pellicole Trasparenti BOPP", "Packaging Alimentare Termoretraibile", "Resistenza Meccanica e Flessione"] },
        { name: "Polietilene Tereftalato (PET)", cat: "Barriera & Trasparenza", exp: "Polimero trasparente, brillante e con eccezionali proprietà di barriera ai gas, impiegato per bottiglie di bevande e vaschette termoformate.", items: ["Elevata Trasparenza Ottica", "Barriera ai Gas e all'Ossigeno", "Bottiglie e Flaconi di Plastica", "Riciclabilità Totale (R-PET)"] },
        { name: "PVC e Polistirene (PS)", cat: "Polimeri Rigidi", exp: "PVC (cloruro di polivinile per supporti rigidi o flessibili resistenti) e PS (polistirene per vaschette, termoformati e imballaggi antiurto).", items: ["PVC Rigido per Tessere e Supporti", "PVC Flessibile per Guaine", "Polistirene Rigido (PS)", "Polistirene Espanso Antiurto (EPS)"] }
      ],
      "Impianti di stampa flessografia": [
        { name: "Stampa Rotativa Diretta a Rilievo", cat: "Tecnologia Flessografica", exp: "Stampa diretta su supporti flessibili (film plastici, cartone ondulato, etichette) mediante matrici fotopolimeriche morbide in rilievo.", items: ["Stampa Diretta a Rilievo", "Matrici Fotopolimeriche Flessibili", "Supporti Flessibili e Imballaggi", "Inchiostri Liquidi ad Alta Resa"] },
        { name: "Rullo Anilox Ceramico", cat: "Dosaggio Inchiostro", exp: "Cilindro con superficie ceramica microincisa a laser con cellette esagonali per trasferire una quantità esatta e costante di inchiostro.", items: ["Superficie Ceramica Laser-Incisa", "Volume delle Cellette in cm³/m²", "Racla a Camera Chiusa", "Uniformità Assoluta di Inchiostrazione"] },
        { name: "Svolgitore & Riavvolgitore", cat: "Gestione della Bobina", exp: "Sistemi di svolgimento e riavvolgimento continuo della bobina con controllo automatico della tensione e dell'allineamento del nastro.", items: ["Svolgitore Bobina Automatico", "Controllo Elettronico Tensione", "Guida Nastro Ottica", "Riavvolgitore a Tensione Costante"] },
        { name: "Forni di Essiccazione", cat: "Asciugatura Rapida", exp: "Tunnel ad aria calda e lampade UV/LED che polimerizzano o asciugano istantaneamente l'inchiostro tra un gruppo stampa e l'altro.", items: ["Tunnel ad Aria Calda Forzata", "Polimerizzazione UV e LED", "Evaporazione Rapida dei Solventi", "Stampa ad Altissima Velocità"] }
      ],
      "Stampa digitale e sistemi CTP": [
        { name: "Stampa Digitale Diretta", cat: "Flusso Senza Matrice", exp: "Riproduzione diretta da file elettronico senza lastre fisiche tramite elettrofotografia a toner secco/liquido o inkjet industriale.", items: ["Nessuna Lastra o Matrice Fisica", "Elettrofotografia Laser a Toner", "Inkjet Industriale Piezoelettrico", "Tirature Brevi e Personalizzate"] },
        { name: "Stampa a Dati Variabili", cat: "Personalizzazione di Massa", exp: "Capacità di stampare copie identiche nella struttura ma diverse nei contenuti (codici a barre, QR code, nominativi, grafiche personalizzate).", items: ["Dati Variabili (VDP)", "Codici QR e Barcode Progressivi", "Personalizzazione di Ogni Copia", "On-Demand Printing Senza Scarti"] },
        { name: "Sistemi CTP (Computer-to-Plate)", cat: "Incisione Laser Diretta", exp: "Tecnologia che incide direttamente la lastra offset tramite raggio laser partendo dal file digitale RIP, eliminando pellicole fotografiche.", items: ["Incisione Laser Termica/Violet", "Eliminazione Pellicole e Film", "Controllo RIP Digitale dei Retini", "Perfetto Registro tra le Lastre"] },
        { name: "Qualità & Velocità di Prestampa", cat: "Vantaggi Operativi", exp: "I sistemi CTP garantiscono massima definizione del punto retino, costanza cromatica e tempi di avviamento macchina estremamente ridotti.", items: ["Punto Retino ad Altissima Precisione", "Riduzione Tempi di Avviamento", "Costanza di Riproduzione Cromatica", "Ottimizzazione dei Costi di Impianto"] }
      ],
      "Cartotecnica, fustellatura e packaging": [
        { name: "Cartotecnica Industriale", cat: "Trasformazione Carta", exp: "Progettazione e trasformazione di carta, cartoncino teso e cartone ondulato in scatole, astucci, espositori e contenitori rigidi.", items: ["Cartoncino Teso per Astucci", "Cartone Ondulato per Scatole", "Studio della Fibra e Grammatura", "Resistenza Meccanica e Schiacciamento"] },
        { name: "Fustellatura & Cordonatura", cat: "Taglio e Piega", exp: "Operazione meccanica che intaglia il perimetro della scatola con lame affilate e traccia le linee di piega (cordonatura) con lame smussate.", items: ["Fustella Piana o Rotativa", "Lame di Taglio in Acciaio", "Lame di Cordonatura per Piega", "Estrazione Automatica degli Sfridi"] },
        { name: "Piega-Incolla Industriale", cat: "Montaggio Finale", exp: "Linea automatizzata che piega i lembi dell'astuccio e applica colla a caldo (hot-melt) o colla a freddo per sigillare la scatola.", items: ["Linea Automatica Piega-Incolla", "Colla Hot-Melt Termofusibile", "Controllo Elettronico del Punto Colla", "Confezionamento Piatto per Spedizione"] },
        { name: "I Tre Livelli di Packaging", cat: "Gerarchia dell'Imballo", exp: "Packaging Primario (a contatto col prodotto), Secondario (raggruppamento per il punto vendita) e Terziario (imballo logistico su pallet).", items: ["Primario (Contatto e Conservazione)", "Secondario (Marketing e Vendita)", "Terziario (Pallet e Trasporto)", "Sostenibilità e Riciclo Ambientale"] }
      ],

      // Progettazione Multimediale
      "Design editoriale e grid system": [
        { name: "Griglie & Gabbie Strutturate", cat: "Organizzazione Spaziale", exp: "Costruzione di layout geometrici con margini, colonne, righe di flusso e moduli per ordinare gerarchicamente testi e immagini.", items: ["Margini Interni ed Esterni", "Colonne e Canali di Spaziatura", "Moduli Geometrici di Impaginazione", "Righe di Allineamento Baseline"] },
        { name: "Gerarchia Tipografica", cat: "Leggibilità del Testo", exp: "Gestione ordinata di titoli, occhielli, sottotitoli, corpo del testo, didascalie e note a piè di pagina con contrasti di peso e corpo.", items: ["Corpo, Peso e Stile del Font", "Gerarchia Titolo/Sottotitolo/Testo", "Interlinea e Spaziatura Kerning", "Leggibilità e Flusso di Lettura"] },
        { name: "Coerenza Visiva & Ritmo", cat: "Armonia Editoriale", exp: "Mantenimento di un ritmo costante e armonioso attraverso le pagine di un libro, di una rivista o di un catalogo aziendale coordinato.", items: ["Ritmo Visivo tra Pagine Pari e Dispari", "Gabbia Modulare per Pubblicazioni", "Equilibrio Pieni e Vuoti (Spazio Bianco)", "Coerenza di Stile Editoriale"] },
        { name: "Preparazione alla Prestampa", cat: "Standard di Stampa", exp: "Verifica dei parametri tecnici prima della stampa: abbondanze (bleed), crocini di registro, profili colore CMYK e risoluzione a 300 DPI.", items: ["Abbondanze (Bleed 3-5mm)", "Crocini di Taglio e Registro", "Conversione CMYK e Profili Fogra", "Risoluzione Ottimale a 300 DPI"] }
      ],
      "Manifesti out-of-home": [
        { name: "Grandi Formati 6x3 & 12x3 m", cat: "Cartellonistica Stradale", exp: "Progettazione per poster stradali ad alto impatto su grandi arterie di traffico, pensati per una lettura rapida da veicoli in movimento.", items: ["Formato Standard 6x3 m", "Impianti Autostradali 12x3 m", "Sintesi Estrema del Messaggio", "Lettura Rapida in Pochi Secondi"] },
        { name: "Pensiline & Arredo Urbano", cat: "Spazi Pubblici Cittadini", exp: "Poster per fermate di bus, tram e stazioni ferroviarie (120x180 cm), progettati per un tempo di visione più lungo da parte dei pedoni.", items: ["Formato Mupi / Pensilina (120x180 cm)", "Dettagli Informativi Aggiuntivi", "Illuminazione Posteriore Backlight", "Integrazione nell'Arredo Urbano"] },
        { name: "Digital DOOH", cat: "Schermi Dinamici", exp: "Cartellonistica digitale dinamica su display a LED urbani con grafiche animate, contenuti in tempo reale e messaggi contestuali.", items: ["Display a LED ad Alta Luminosità", "Animazioni Grafiche Brevi", "Contenuti Aggiornati in Tempo Reale", "Interattività e Geotargeting"] },
        { name: "Contrasto & Leggibilità", cat: "Efficacia Visiva", exp: "Scelta di font netti ad alta visibilità, forti contrasti cromatici e composizione essenziale per garantire un impatto immediato a distanza.", items: ["Tipografia Bastone ad Alto Spessore", "Forti Contrasti di Colore", "Pochi Elementi Visivi Forti", "Impatto Mnemonico Immediato"] }
      ],
      "Composizione advertising e Gestalt": [
        { name: "Legge della Prossimità", cat: "Principio Percettivo", exp: "Gli elementi visivi posizionati vicini nello spazio vengono automaticamente percepiti dalla mente come un gruppo coerente e correlato.", items: ["Vicinanza Spaziale degli Elementi", "Percezione di Gruppo Unitario", "Raggruppamento delle Informazioni", "Ordine Naturale di Lettura"] },
        { name: "Legge della Somiglianza", cat: "Correlazione Visiva", exp: "Elementi che condividono forma, colore, dimensione o stile visivo vengono interpretati come collegati tra loro nella funzione.", items: ["Uguaglianza di Colore e Forma", "Costanza di Dimensione e Peso", "Identificazione di Pattern Ripetuti", "Collegamento Concettuale Immediato"] },
        { name: "Legge della Chiusura", cat: "Completamento Mentale", exp: "La mente umana tende a chiudere e completare automaticamente le figure geometriche e i contorni aperti o interrotti.", items: ["Completamento di Forme Aperte", "Coinvolgimento Attivo dell'Osservatore", "Loghi e Grafiche Sintetiche", "Economia Visiva del Messaggio"] },
        { name: "Legge della Continuità", cat: "Percorsi Visivi", exp: "L'occhio umano segue naturalmente linee rette o curve continue, guidando lo sguardo lungo i percorsi di lettura a 'Z' o ad 'F' nell'advertising.", items: ["Traiettorie e Linee Guida", "Flussi Visivi a 'Z' e ad 'F'", "Punto Focale Primario e Call-to-Action", "Armonia Dinamica della Composizione"] }
      ],
      "Corporate identity e pieghevoli": [
        { name: "Elementi di Corporate Identity", cat: "Identità Coordinata", exp: "Costruzione del sistema identitario di un brand: marchio/logo, colori istituzionali, font ufficiali, tono di voce e corporate manual.", items: ["Disegno del Marchio e del Logo", "Palette Colori Istituzionali", "Font Tipografici Ufficiali", "Manuale di Immagine Coordinata"] },
        { name: "Pieghevoli a 2 Ante", cat: "Singola Piega", exp: "Depliant a 4 facciate con un'unica piega centrale (a quartino), ideale per presentazioni sintetiche, menu e inviti aziendali.", items: ["Unica Piega Centrale", "4 Facciate di Lettura", "Copertina, Interni e Retro", "Design Pulito e Diretto"] },
        { name: "Pieghevoli a 3 Ante", cat: "Portafoglio & Z-Fold", exp: "Brochure a 6 facciate con piega a portafoglio (ante che si chiudono verso l'interno) o piega a fisarmonica (z-fold a zig-zag).", items: ["Piega a Portafoglio (Roll Fold)", "Piega a Fisarmonica (Z-Fold)", "6 Facciate Tematiche Organizzate", "Progressione Narrativa delle Ante"] },
        { name: "Gatefold & Formati Speciali", cat: "Aperture Scenografiche", exp: "Pieghevoli con apertura centrale a finestra (gatefold) per rivelare una grande visuale interna ad alto impatto emotivo.", items: ["Apertura Centrale a Finestra", "Grande Visuale Interna Panoramica", "Impatto Scenografico ed Elegante", "Materiali Speciali e Nobilitazioni"] }
      ],

      // Linguaggio Audiovisivo
      "Still life e luce in studio": [
        { name: "Key Light (Luce Principale)", cat: "Modellazione Primaria", exp: "La sorgente luminosa fondamentale che definisce la direzione della luce, modella i volumi del soggetto e crea le ombre primarie.", items: ["Sorgente Primaria di Luce", "Definizione di Forme e Texture", "Posizionamento a 45 Gradi", "Controllo delle Ombre Portate"] },
        { name: "Fill Light (Luce di Riempimento)", cat: "Controllo del Contrasto", exp: "Luce secondaria posizionata sul lato opposto per schiarire le ombre profonde generate dalla Key Light e regolare il rapporto di contrasto.", items: ["Schiarimento delle Ombre Scure", "Pannelli Riflettenti o Softbox", "Regolazione del Rapporto di Contrasto", "Dettaglio nelle Zone d'Ombra"] },
        { name: "Backlight (Controluce)", cat: "Stacco dallo Sfondo", exp: "Sorgente posta dietro il soggetto per illuminarne i bordi posteriori e staccarlo nettamente dallo sfondo, creando profondità tridimensionale.", items: ["Posizionamento Posteriore", "Creazione di Profondità Tridimensionale", "Stacco dal Fondale di Studio", "Profilo Luminoso Elegante"] },
        { name: "Rim Light (Luce di Taglio)", cat: "Luce d'Accento", exp: "Luce radente concentrata che delinea con precisione i contorni, le silhouette o i dettagli lucidi degli oggetti in still life.", items: ["Luce Radente Angolata", "Delineazione dei Contorni Netti", "Esalta Metalli e Superfici Lucide", "Accento Scenografico di Alta Precisione"] }
      ],
      "Montaggio video con Premiere Pro": [
        { name: "Importazione & Organizzazione", cat: "Gestione Media NLE", exp: "Acquisizione dei file video grezzi, creazione di bin tematici, sincronizzazione delle tracce audio e impostazione delle sequenze di lavoro.", items: ["Importazione File Video e Audio", "Organizzazione in Bin e Cartelle", "Sincronizzazione Tracce Separate", "Impostazione Risoluzione Sequenza"] },
        { name: "Editing su Timeline Multitraccia", cat: "Costruzione Narrativa", exp: "Taglio, accostamento e rifinitura delle clip sulla timeline utilizzando raccordi visivi, transizioni e tagli ritmici (J-cut ed L-cut).", items: ["Trimming e Montaggio su Timeline", "Tagli J-Cut ed L-Cut", "Raccordi sul Movimento e sull'Asse", "Gestione Tracce Video e Sovrapposizioni"] },
        { name: "Color Correction & Lumetri", cat: "Trattamento Cromatico", exp: "Bilanciamento del bianco, regolazione dell'esposizione, contrasto e applicazione di color grading per definire l'atmosfera visiva del film.", items: ["Bilanciamento del Bianco e Tinte", "Regolazione Esposizione e Curve", "Lumetri Color Scopes e Waveform", "Color Grading Emotivo con LUT"] },
        { name: "Audio & Esportazione Finale", cat: "Mastering & Output", exp: "Missaggio dei canali audio, pulizia del rumore di fondo, masterizzazione della colonna sonora ed esportazione nei codec ottimali (H.264/ProRes).", items: ["Missaggio Tracce Vocali e Musica", "Filtri Audio e Riduzione Rumore", "Regolazione Livelli in Decibel (dB)", "Esportazione H.264 / ProRes Master"] }
      ],
      "Grammatica dell'inquadratura": [
        { name: "Scala dei Campi (Spazio)", cat: "Rapporto con l'Ambiente", exp: "Inquadrature incentrate sull'ambiente: Campo Lunghissimo (CLL per paesaggi immensi) e Campo Lungo (CL per contesti ambientali definiti).", items: ["Campo Lunghissimo (CLL)", "Campo Lungo (CL)", "Predominanza del Paesaggio", "Contestualizzazione Ambientale"] },
        { name: "Scala dei Piani (Figura Umana)", cat: "Piani sul Personaggio", exp: "Inquadrature sulla figura: Figura Intera (FI), Piano Americano (PA dalle ginocchia in su), Primo Mezzo (PM dalla cintola in su).", items: ["Figura Intera (FI)", "Piano Americano (PA)", "Primo Mezzo (PM)", "Interazione Umana e Corporea"] },
        { name: "Primi Piani & Dettagli", cat: "Intimità ed Emozione", exp: "Inquadrature ravvicinate: Primo Piano (PP spalle e volto), Primissimo Piano (PPP solo occhi e bocca), Dettaglio (oggetto singolo ravvicinato).", items: ["Primo Piano (PP)", "Primissimo Piano (PPP)", "Dettaglio / Particolare", "Massima Espressione Emotiva"] },
        { name: "Angolazioni & Movimenti Camera", cat: "Dinamismo di Ripresa", exp: "Angolazioni (normale, plongée dall'alto, contre-plongée dal basso, olandese) e movimenti (panoramica, carrello, zoom, steadicam).", items: ["Plongée (Dall'Alto / Debolezza)", "Contre-Plongée (Dal Basso / Potenza)", "Angolo Olandese Inclinato", "Panoramica, Carrello e Steadicam"] }
      ],
      "Ritmo visivo, stacchi, colonna sonora": [
        { name: "Tipologie di Stacco (Tagli)", cat: "Transizioni di Montaggio", exp: "Cut netto (passaggio istantaneo), dissolve (dissolvenza incrociata), fade (dissolvenza a nero o a bianco), wipe (tendina grafica).", items: ["Cut Netto Istantaneo", "Dissolvenza Incrociata (Dissolve)", "Dissolvenza a Nero/Bianco (Fade)", "Transizione a Tendina (Wipe)"] },
        { name: "Raccordi di Montaggio", cat: "Continuità Narrativa", exp: "Match cut (raccordo grafico o analogico tra due forme simili) e jump cut (stacco discontinuo sulla stessa inquadratura per accelerare il tempo).", items: ["Match Cut Grafico ed Analogico", "Jump Cut Discontinuo ed Energetico", "Raccordo sull'Azione e sullo Sguardo", "Montaggio Invisibile Classico"] },
        { name: "Colonna Sonora & Musica", cat: "Commento Sonoro", exp: "La traccia musicale extradiegetica o diegetica che supporta le emozioni, scandisce il ritmo della narrazione e crea leitmotiv tematici.", items: ["Musica Diegetica (nella Scena)", "Musica Extradiegetica (Commento)", "Leitmotiv Tematico dei Personaggi", "Sincronizzazione Ritmica con le Immagini"] },
        { name: "Effetti Sonori (SFX) & Foley", cat: "Realismo Acustico", exp: "Effetti sonori ambientali, rumoristica foley registrata in sala, dialoghi in presa diretta, voiceover narrativo e uso drammatico del silenzio.", items: ["Rumoristica Foley Realistica", "Effetti Sonori di Sintesi (SFX)", "Dialoghi in Presa Diretta e Voiceover", "Valore Espressivo del Silenzio"] }
      ],

      // Matematica
      "Studio di funzione": [
        { name: "Dominio & Intersezioni Assi", cat: "Fase 1: Condizioni Base", exp: "Determinazione del campo di esistenza della funzione (denominatori ≠ 0, argomenti dei logaritmi > 0) e calcolo delle intersezioni con gli assi X e Y.", items: ["Campo di Esistenza (Dominio)", "Condizioni di Esistenza Algebriche", "Intersezione con Asse Y (f(0))", "Zeri della Funzione (f(x) = 0)"] },
        { name: "Segno & Positività", cat: "Fase 2: Intervalli di Segno", exp: "Risoluzione della disequazione f(x) > 0 per individuare le regioni del piano cartesiano in cui il grafico della funzione è sopra o sotto l'asse X.", items: ["Disequazione f(x) > 0", "Regioni del Piano da Cancellare", "Intervalli di Positività (+)", "Intervalli di Negatività (-)"] },
        { name: "Limiti & Asintoti", cat: "Fase 3: Comportamento Asintotico", exp: "Calcolo dei limiti per x tendente agli estremi del dominio e a infinito per individuare asintoti verticali, orizzontali e obliqui.", items: ["Limiti Destri e Sinistri", "Asintoti Verticali (x = c)", "Asintoti Orizzontali (y = l)", "Asintoti Obliqui (y = mx + q)"] },
        { name: "Derivate & Grafico Finale", cat: "Fase 4: Andamento e Flessi", exp: "Studio della derivata prima per massimi e minimi, derivata seconda per concavità e flessi, e tracciamento finale del grafico qualitativo.", items: ["Derivata Prima f'(x) (Crescenza)", "Punti di Massimo e Minimo Relativi", "Derivata Seconda f''(x) (Concavità)", "Tracciamento del Grafico Qualitativo"] }
      ],
      "Sistemi esponenziali e logaritmici": [
        { name: "Equazioni Esponenziali", cat: "Forma a^x = b", exp: "Risoluzione di equazioni in cui l'incognita compare all'esponente: riconduzione alla stessa base o applicazione dei logaritmi.", items: ["Forma Elementare a^x = b", "Riconduzione alla Stessa Base", "Sostituzione di Variabile (t = a^x)", "Disequazioni Esponenziali"] },
        { name: "Equazioni Logaritmiche", cat: "Forma log_a(x) = b", exp: "Risoluzione di equazioni con logaritmi, previa verifica delle condizioni di esistenza dell'argomento (strettamente maggiore di zero).", items: ["Condizioni di Esistenza (Argomento > 0)", "Forma Elementare log_a(x) = b", "Uguaglianza tra Logaritmi", "Verifica delle Soluzioni Accettabili"] },
        { name: "Proprietà dei Logaritmi", cat: "Regole Algebriche", exp: "Le quattro proprietà fondamentali: logaritmo del prodotto, logaritmo del quoziente, logaritmo della potenza e formula del cambio di base.", items: ["Logaritmo del Prodotto: log(A*B)", "Logaritmo del Quoziente: log(A/B)", "Logaritmo della Potenza: log(A^k)", "Formula del Cambio di Base"] },
        { name: "Applicazioni Pratiche", cat: "Modelli di Crescita", exp: "Utilizzo di modelli esponenziali e logaritmici per descrivere fenomeni reali: crescita demografica, decadimento radioattivo, scale sismiche (Richter).", items: ["Modelli di Crescita Esponenziale", "Decadimento Radioattivo", "Scale Logaritmiche (pH, Richter, dB)", "Calcolo Finanziario di Interesse"] }
      ],
      "Funzioni razionali": [
        { name: "Razionali Intere (Polinomi)", cat: "Dominio su tutto R", exp: "Funzioni polinomiali del tipo P(x): continue e derivabili su tutto l'insieme dei numeri reali R, prive di asintoti verticali od orizzontali.", items: ["Polinomi di Grado n", "Dominio Illimitato R", "Continuità e Derivabilità Ovunque", "Comportamento all'Infinito (Gradi)"] },
        { name: "Razionali Fratte: Dominio", cat: "Condizione Q(x) ≠ 0", exp: "Funzioni del tipo P(x)/Q(x): il dominio è formato da tutti i numeri reali escludendo i punti che annullano il denominatore (zeri di Q(x)).", items: ["Rapporto di Polinomi P(x)/Q(x)", "Condizione di Esistenza Q(x) ≠ 0", "Punti di Discontinuità / Singolarità", "Esclusione di Valori dal Dominio"] },
        { name: "Asintoti Verticali & Orizzontali", cat: "Comportamento Asintotico", exp: "Se il limite per x tendente a un punto del dominio è infinito si ha un asintoto verticale; per x all'infinito, se il limite è finito si ha un asintoto orizzontale.", items: ["Asintoti Verticali nei Poli di Q(x)", "Asintoti Orizzontali per x -> ∞", "Confronto tra Gradi di P(x) e Q(x)", "Comportamento Asintotico ai Limiti"] },
        { name: "Asintoti Obliqui", cat: "Rapporto tra Gradi", exp: "Se il grado del numeratore P(x) supera di 1 il grado del denominatore Q(x), la funzione ammette un asintoto obliquo di equazione y = mx + q.", items: ["Grado(Numeratore) = Grado(Denominatore) + 1", "Calcolo del Coefficiente Angolare m", "Calcolo del Termine Noto q", "Rette Asintotiche Oblique"] }
      ],
      "Funzioni esponenziali e logaritmiche": [
        { name: "Funzione Esponenziale y = a^x", cat: "Proprietà Trascendenti", exp: "Curva esponenziale con base a > 0: Dominio R, codominio (0, +∞), sempre positiva, passa per il punto (0, 1) con asintoto orizzontale y = 0.", items: ["Forma Elementare y = a^x", "Dominio su Tutto R", "Asintoto Orizzontale y = 0", "Crescente per a > 1, Decrescente per 0 < a < 1"] },
        { name: "Funzione Logaritmica y = log_a(x)", cat: "Funzione Inversa", exp: "La funzione inversa dell'esponenziale: definita solo per argomenti positivi (x > 0), passa per (1, 0) con asintoto verticale x = 0.", items: ["Forma Elementare y = log_a(x)", "Dominio Limitato a x > 0", "Asintoto Verticale x = 0", "Simmetria rispetto alla Bisettrice y = x"] },
        { name: "Confronto e Simmetria", cat: "Dualità Inversa", exp: "I grafici di y = a^x e y = log_a(x) sono perfettamente simmetrici rispetto alla retta bisettrice del primo e terzo quadrante (y = x).", items: ["Simmetria Assiale rispetto a y = x", "Inversione di Dominio e Codominio", "Punto Chiave (0,1) vs. Punto (1,0)", "Crescita e Decadimento Logaritmico"] },
        { name: "Casi Speciali: Base e & Base 10", cat: "Logaritmi Naturali", exp: "L'esponenziale naturale y = e^x (con numero di Eulero e ≈ 2.718) e il logaritmo naturale y = ln(x), pilastri dell'analisi matematica e della fisica.", items: ["Numero di Eulero e ≈ 2.71828", "Funzione Esponenziale Naturale e^x", "Logaritmo Naturale ln(x)", "Logaritmo Decimale log10(x)"] }
      ],

      // Inglese
      "Oscar Wilde e l'esteticismo": [
        { name: "Aestheticism & Art for Art's Sake", cat: "Movimento Artistico", exp: "Movimento estetico tardo-vittoriano: primato assoluto della bellezza e dell'arte libera da qualsiasi scopo morale, didattico o utilitaristico.", items: ["Motto 'Art for Art's Sake'", "Culto Assoluto della Bellezza", "Rifiuto del Moralismo Vittoriano", "Autonomia dell'Opera d'Arte"] },
        { name: "Oscar Wilde (1854-1900)", cat: "Vita & Opere", exp: "Brillante autore, drammaturgo e dandy irlandese: celebre per 'The Picture of Dorian Gray' (1891) e la commedia 'The Importance of Being Earnest'.", items: ["Figura del Dandy Raffinato", "Capolavoro 'The Picture of Dorian Gray'", "Commedia 'The Importance of Being Earnest'", "Aforismi e Brillantezza Verbale"] },
        { name: "Il Tema del Doppio & Dorian Gray", cat: "Dualismo & Maschera", exp: "Dorian Gray mantiene una giovinezza immutata mentre il suo ritratto dipinto invecchia e mostra i segni orribili dei suoi peccati e della sua corruzione.", items: ["Patto Faustiano per la Giovinezza", "Ritratto come Specchio dell'Anima", "Dualismo tra Apparenza e Peccato", "Tragica Punizione Finale"] },
        { name: "Decadenza & Critica Sociale", cat: "Società Vittoriana", exp: "Critica pungente all'ipocrisia della società vittoriana, dove l'apparenza formale e la rispettabilità borghese nascondevano segreti e immoralità.", items: ["Ipocrisia Borghese Vittoriana", "Maschera Sociale e Rispettabilità", "Estetica della Decadenza", "Condanna e Solitudine dell'Autore"] }
      ],
      "Alan Turing e Enigma": [
        { name: "Alan Turing (1912-1954)", cat: "Genio Matematico", exp: "Matematico, logico e crittografo britannico, pioniere fondamentale della scienza informatica teorica e dell'intelligenza artificiale.", items: ["Genio Matematico e Logico", "Attività a Bletchley Park", "Padre dell'Informatica Moderna", "Teorizzazione dell'Intelligenza Artificiale"] },
        { name: "La Macchina Enigma", cat: "Cifrario Elettromeccanico", exp: "Complesso dispositivo a rotori impiegato dalle forze armate tedesche durante la Seconda Guerra Mondiale per cifrare le comunicazioni militari.", items: ["Sistema Cifrante a Rotori Mobili", "Comunicazioni Militari Segrete Tedesche", "Miliardi di Combinazioni Possibili", "Ritenuta Inviolabile dai Nazisti"] },
        { name: "La Macchina Bombe", cat: "Decifrazione Crittografica", exp: "Il monumentale calcolatore elettromeccanico ideato da Turing a Bletchley Park per decifrare in tempo reale i messaggi crittografati di Enigma.", items: ["Macchina Elettromeccanica Bombe", "Ricerca Automatica delle Chiavi Cifrate", "Operazione Segreta Ultra", "Salvataggio di Milioni di Vite Umane"] },
        { name: "Macchina di Turing & Test di Turing", cat: "Fondamenti Informatici", exp: "La Macchina Universale di Turing (modello teorico del computer moderno) e il Test di Turing per valutare l'intelligenza di un sistema artificiale.", items: ["Macchina Universale di Turing (1936)", "Modello Teorico di Algoritmo e Computer", "Test di Turing sull'Intelligenza delle Macchine", "Pietra Miliare dell'AI"] }
      ],
      "Charles Dickens": [
        { name: "Charles Dickens (1812-1870)", cat: "Romanzo Sociale", exp: "Il più celebre romanziere dell'era vittoriana: autore di capolavori immortali come 'Oliver Twist', 'A Christmas Carol' e 'Great Expectations'.", items: ["Massimo Romanziere Vittoriano", "'Oliver Twist' e le Workhouses", "'A Christmas Carol' e la Redenzione", "'Great Expectations' e la Crescita"] },
        { name: "Rivoluzione Industriale & Povertà", cat: "Contesto Sociale", exp: "Denuncia delle drammatiche conseguenze dell'industrializzazione: inquinamento urbano, slum sovraffollati e condizioni disumane della classe operaia.", items: ["Metropoli Industriale Inquinata (Coketown)", "Slum e Quartieri Sovraffollati", "Condizioni Disumane degli Operai", "Povertà e Malattie Diffuse"] },
        { name: "Sfruttamento Minorile & Workhouses", cat: "Denuncia Sociale", exp: "La crudele realtà del lavoro minorile nelle fabbriche e delle case di lavoro (Workhouses) istituite dalla legge Poor Law del 1834.", items: ["Lavoro Minorile nelle Fabbriche", "Workhouses della Poor Law (1834)", "Bambini Orfani e Abbandonati", "Critica all'Insensibilità Istituzionale"] },
        { name: "Umorismo, Pathos & Riforma", cat: "Stile Narrativo", exp: "Straordinaria abilità nel combinare umorismo, caricature indimenticabili, profondo pathos e un potente appello morale alla coscienza civile.", items: ["Caricature e Personaggi Indimenticabili", "Equilibrio tra Umorismo e Pathos", "Coscienza Morale Collettiva", "Spinta alle Riforme Sociali"] }
      ],
      "Sistemi politici UK vs USA": [
        { name: "Forma di Stato: Monarchia vs. Repubblica", cat: "Assetto Istituzionale", exp: "Il Regno Unito è una Monarchia Parlamentare guidata dal Sovrano e dal Primo Ministro, mentre gli USA sono una Repubblica Federale Presidenziale.", items: ["UK: Monarchia Parlamentare", "USA: Repubblica Federale Presidenziale", "Capo dello Stato: Re/Regina vs. Presidente", "Principio Federale degli Stati Americani"] },
        { name: "Potere Esecutivo: PM vs. Presidente", cat: "Guida del Governo", exp: "Nel Regno Unito il Primo Ministro è espressione della maggioranza parlamentare; negli USA il Presidente è eletto dai cittadini (Grandi Elettori).", items: ["UK: Primo Ministro (Capo della Maggioranza)", "USA: Presidente Eletto con Grandi Elettori", "Nomina dei Ministri / Segretari di Stato", "Ruolo di Capo del Governo e Forze Armate"] },
        { name: "Parlamento: Westminster vs. Congresso", cat: "Potere Legislativo", exp: "UK: Parlamento bicamerale con House of Commons (eletta) e House of Lords (nobiltà/nomina); USA: Congresso con House of Representatives e Senate.", items: ["UK: House of Commons & House of Lords", "USA: House of Representatives & Senate", "Bicameralsimo Perfetto vs. Imperfetto", "Procedura di Approvazione delle Leggi"] },
        { name: "Costituzione: Non Scritta vs. Scritta", cat: "Quadro Costituzionale", exp: "Il Regno Unito ha una Costituzione consuetudinaria basata su atti storici e tradizioni; gli USA hanno la Costituzione scritta del 1787.", items: ["UK: Costituzione Consuetudinaria Non Scritta", "USA: Costituzione Scritta del 1787", "Bill of Rights e Separazione dei Poteri", "Controllo di Costituzionalità della Corte Suprema"] }
      ],

      // Scienze Motorie
      "Capacità motorie e controllo neuromuscolare": [
        { name: "Capacità Condizionali", cat: "Efficienza Fisica", exp: "Capacità fisiche legate ai processi metabolici ed energetici dell'organismo: forza muscolare, resistenza aerobica/anaerobica e velocità.", items: ["Forza Massimale, Resistente ed Esplosiva", "Resistenza Generale e Specifica", "Velocità di Reazione ed Esecuzione", "Flessibilità e Mobilità Articolare"] },
        { name: "Capacità Coordinative", cat: "Controllo del Movimento", exp: "Capacità governate dal sistema nervoso: equilibrio statico/dinamico, orientamento spaziale, ritmo, destrezza e differenziazione cinestesica.", items: ["Equilibrio Statico e Dinamico", "Orientamento Spazio-Temporale", "Coordinazione Oculo-Manuale e Ritmo", "Adattamento e Trasformazione Motoria"] },
        { name: "Controllo Neuromuscolare & Propriocezione", cat: "Sistema Nervoso", exp: "Integrazione dei recettori sensoriali e dei fusi neuromuscolari per percepire la posizione del corpo e garantire movimenti precisi e sicuri.", items: ["Recettori Propriocettivi e Articolari", "Feedback Sensoriale e Risposta Motoria", "Stabilità del Core e Allineamento Posturale", "Prevenzione di Traumi e Distorsioni"] },
        { name: "Apprendimento del Gesto Tecnico", cat: "Didattica Motoria", exp: "Fasi progressive di acquisizione del movimento: coordinazione grezza iniziale, coordinazione fine e disponibilità variabile in gara.", items: ["Fase di Coordinazione Grezza", "Fase di Coordinazione Fine", "Disponibilità Variabile del Gesto", "Automatizzazione del Movimento"] }
      ],
      "Fisiologia dell'esercizio e apparato cardiorespiratorio": [
        { name: "Apparato Cardiovascolare sotto Sforzo", cat: "Circolazione Sanguigna", exp: "Aumento della frequenza cardiaca, della gittata sistolica e della pressione arteriosa per trasportare ossigeno e nutrienti ai muscoli attivi.", items: ["Aumento della Frequenza Cardiaca", "Incremento della Gittata Sistolica", "Vasodilatazione nei Muscoli Attivi", "Adattamento Cardiaco all'Allenamento"] },
        { name: "Apparato Respiratorio & VO2 Max", cat: "Scambio dei Gas", exp: "Aumento della ventilazione polmonare e della capacità di assorbimento dell'ossigeno (VO2 Max) durante l'attività fisica aerobica prolungata.", items: ["Ventilazione Polmonare e Frequenza", "Consumo Massimo di Ossigeno (VO2 Max)", "Scambio Gassoso Alveolo-Capillare", "Soglia Anaerobica e Accumulo di Lattato"] },
        { name: "Metabolismi Energetici Muscolari", cat: "Produzione di Energia", exp: "I tre sistemi di risintesi dell'ATP: anaerobico alattacido (fosfocreatina), anaerobico lattacido (glicolisi) e aerobico ossidativo (carboidrati/grassi).", items: ["Anaerobico Alattacido (ATP-CP)", "Anaerobico Lattacido (Glicolisi)", "Aerobico Ossidativo (Ciclo di Krebs)", "Recupero e Debito di Ossigeno"] },
        { name: "Riscaldamento, Defaticamento & Salute", cat: "Prevenzione Infortuni", exp: "Importanza del riscaldamento graduale per preparare muscoli e tendini, e del defaticamento attivo per smaltire le scorie metaboliche.", items: ["Riscaldamento Generale e Specifico", "Aumento della Temperatura Muscolare", "Defaticamento Attivo e Allungamento", "Idratazione e Recupero Muscolare"] }
      ],
      "Regolamenti, etica sportiva e tattica di gioco": [
        { name: "Fair Play & Rispetto delle Regole", cat: "Valori Educativi", exp: "Il rispetto incondizionato delle regole, degli avversari, dei compagni e delle decisioni arbitrali come fondamento etico dello sport.", items: ["Rispetto delle Regole di Gioco", "Lealtà verso gli Avversari e l'Arbitro", "Rifiuto del Doping e della Violenza", "Inclusione e Spirito di Squadra"] },
        { name: "Schemi Tattici & Collaborazione", cat: "Strategia Sportiva", exp: "Progettazione di strategie di attacco e difesa negli sport di squadra (basket, pallavolo) basate su ruoli, comunicazione e supporto reciproco.", items: ["Transizioni Attacco e Difesa", "Occupazione Razionale dello Spazio", "Comunicazione Verbale e Visiva in Campo", "Supporto e Copertura dei Compagni"] },
        { name: "Discipline Individuali & Autocontrollo", cat: "Resilienza Mentale", exp: "Gestione della concentrazione, della respirazione e della tensione emotiva negli sport individuali (arti marziali, atletica, ginnastica).", items: ["Concentrazione e Gestione dell'Ansia", "Autocontrollo e Disciplina Personale", "Focalizzazione sul Gesto Tecnico", "Resilienza e Accettazione della Sconfitta"] },
        { name: "Ruolo Sociale dello Sport", cat: "Crescita Personale", exp: "Lo sport come strumento primario di socializzazione, benessere psicofisico permanente, cooperazione e sviluppo del senso civico.", items: ["Socializzazione e Spirito di Comunità", "Benessere Psicofisico Globale", "Sviluppo dell'Autostima e del Carattere", "Stile di Vita Attivo e Sano"] }
      ]"""

# In CURATED_CONCEPT_TOPICS, replace all Italian topic keys
curated_start_marker = "    const CURATED_CONCEPT_TOPICS = {\n      // Accounting (Irish Leaving Certificate)"
curated_middle_marker = "      // Storia\n"
curated_end_marker = "    };\n\n    /**\n     * Helper to retrieve or generate complete concept map"

before_curated = code.split(curated_middle_marker)[0]
after_curated = code.split(curated_end_marker)[1]

new_curated_full = before_curated + new_italian_curated.strip() + "\n    };\n\n    /**\n     * Helper to retrieve or generate complete concept map" + after_curated

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_curated_full)

print("Saved updated the_irish_year.html with complete Italian subjects and concept topics.")
