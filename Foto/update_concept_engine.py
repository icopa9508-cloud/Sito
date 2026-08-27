# Script to update the_irish_year.html with the perfect Concept Map engine and readable visual cards
import re

with open(r'c:\Users\Enrico\Desktop\Giada\the_irish_year.html', 'r', encoding='utf-8') as f:
    code = f.read()

# Helper replacement for visual cards and concept maps
new_concept_engine = """    // ============================================================================
    // RICH CONCEPT MAPS & FULLY LEGIBLE GENERATED VISUAL SCHEMATICS (SECTION 07)
    // Covers all topics for both Ireland (English) and Italy (Italian)
    // ============================================================================

    const wrapSvgText = (text, maxChars = 16) => {
      if (!text) return [''];
      const words = text.split(' ');
      const lines = [];
      let current = [];
      let curLen = 0;
      for (let i = 0; i < words.length; i++) {
        const w = words[i];
        if (curLen + w.length + (current.length > 0 ? 1 : 0) <= maxChars) {
          current.push(w);
          curLen += w.length + (current.length > 1 ? 1 : 0);
        } else {
          if (current.length > 0) {
            lines.push(current.join(' '));
          }
          current = [w];
          curLen = w.length;
        }
      }
      if (current.length > 0) {
        lines.push(current.join(' '));
      }
      return lines.slice(0, 3);
    };

    /**
     * Generated Visual Schematic Card Component: 100% Legible, Responsive, Word-Wrapped
     */
    const GeneratedVisualCard = ({ visual, index }) => {
      return (
        <div className="bg-[#18352B] border border-[#B79A63]/50 rounded-sm p-4 space-y-3 shadow-xl">
          {/* Header */}
          <div className="flex justify-between items-center text-[10px] font-mono text-[#D8CDBD] border-b border-[#A8B3A0]/30 pb-2">
            <span className="text-[#B79A63] font-semibold tracking-wider">
              FIG. 0{index + 1} · {visual.badge || 'SCHEMATIC'}
            </span>
            <span className="bg-[#171817] px-2 py-0.5 rounded border border-[#A8B3A0]/30 text-[#A8B3A0]">
              {(visual.type || 'DIAGRAM').toUpperCase()}
            </span>
          </div>

          {/* Diagram Title */}
          <div>
            <h5 className="font-serif text-base text-[#F5F1E8] font-normal leading-snug">
              {visual.title}
            </h5>
            {visual.caption && (
              <p className="text-xs font-sans text-[#E7E9E3]/80 leading-relaxed mt-1">
                {visual.caption}
              </p>
            )}
          </div>

          {/* Responsive Visual Schematic Box */}
          <div className="bg-[#171817] p-3.5 rounded border border-[#A8B3A0]/25 space-y-2.5">
            {visual.type === 'flow' && (
              <div className="space-y-2">
                {(visual.items || ['Definizione', 'Analisi', 'Applicazione', 'Sintesi']).map((step, sIdx, arr) => (
                  <div key={sIdx} className="space-y-1">
                    <div className="flex items-center space-x-2.5">
                      <span className="shrink-0 w-6 h-6 rounded bg-[#18352B] border border-[#B79A63] text-[#F5F1E8] flex items-center justify-center text-[10px] font-mono font-bold">
                        0{sIdx + 1}
                      </span>
                      <div className="flex-1 bg-[#18352B]/40 px-3 py-1.5 rounded border border-[#A8B3A0]/20 text-xs font-sans text-[#F5F1E8] font-medium leading-normal break-words">
                        {step}
                      </div>
                    </div>
                    {sIdx < arr.length - 1 && (
                      <div className="pl-3 py-0.5 text-[#B79A63] text-xs font-mono">
                        ↓
                      </div>
                    )}
                  </div>
                ))}
              </div>
            )}

            {visual.type === 'matrix' && (
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
                {(visual.items || ['Parametro A', 'Metodologia', 'Applicazione', 'Risultato']).map((item, mIdx) => (
                  <div key={mIdx} className="p-2.5 bg-[#18352B]/50 rounded border border-[#A8B3A0]/30 space-y-1">
                    <div className="text-[9px] font-mono text-[#B79A63] uppercase tracking-wider">
                      PARAMETRO 0{mIdx + 1}
                    </div>
                    <div className="text-xs font-sans text-[#F5F1E8] font-medium leading-snug break-words">
                      {item}
                    </div>
                  </div>
                ))}
              </div>
            )}

            {visual.type === 'structural' && (
              <div className="space-y-2">
                {(visual.items || ['Fondamenti Teorici', 'Livello Operativo', 'Sintesi Complessiva']).map((lyr, lIdx) => (
                  <div key={lIdx} className="p-2.5 bg-[#18352B]/40 rounded border border-[#A8B3A0]/20 flex items-center justify-between gap-3">
                    <div className="flex items-center space-x-2.5 min-w-0">
                      <span className="shrink-0 text-[10px] font-mono text-[#B79A63] font-bold">
                        L0{lIdx + 1}
                      </span>
                      <span className="text-xs font-sans text-[#F5F1E8] font-medium leading-snug break-words">
                        {lyr}
                      </span>
                    </div>
                    <span className="shrink-0 text-[9px] font-mono text-[#A8B3A0] uppercase bg-[#171817] px-2 py-0.5 rounded border border-[#A8B3A0]/20">
                      STRATO {lIdx + 1}
                    </span>
                  </div>
                ))}
              </div>
            )}
          </div>
        </div>
      );
    };

    /**
     * Curated, High-Rigor Concept Maps Knowledge Base
     */
    const CURATED_CONCEPT_TOPICS = {
      // Storia
      "I moti rivoluzionari del 1848 in Europa": [
        { name: "Primavera dei Popoli", cat: "Contesto Storico", exp: "L'ondata insurrezionale che nel 1848 ha attraversato contemporaneamente Parigi, Vienna, Berlino, Budapest e Milano, richiedendo costituzioni liberali, sovranità popolare e diritti sociali.", items: ["Insurrezione di Parigi (Febbraio)", "Sollevazione di Vienna e Budapest", "Moti a Berlino e Francoforte", "Richiesta di Carte Costituzionali"] },
        { name: "Seconda Repubblica Francese", cat: "Modello Politico", exp: "La caduta della monarchia orleanista di Luigi Filippo, la proclamazione della repubblica, l'introduzione degli Ateliers Nationaux per il lavoro e il suffragio universale maschile.", items: ["Caduta della Monarchia Orleanista", "Istituzione degli Ateliers Nationaux", "Suffragio Universale Maschile", "Ascesa di Luigi Napoleone Bonaparte"] },
        { name: "Riforme & Costituzioni", cat: "Diritto e Istituzioni", exp: "La concessione di carte costituzionali concesse dai sovrani (come lo Statuto Albertino nel Regno di Sardegna) per arginare la spinta repubblicana e democratica.", items: ["Statuto Albertino (Marzo 1848)", "Costituzione Francese del 1848", "Tentativi Costituzionali a Francoforte", "Eredità Istituzionale Permanente"] },
        { name: "Conflitti di Classe", cat: "Sociologia Storica", exp: "La prima netta divergenza tra le rivendicazioni della borghesia liberale e quelle del nascente proletariato operaio, culminata nelle tragiche giornate di giugno a Parigi.", items: ["Borghesia Imprenditoriale", "Proletariato e Artigiani Urbani", "Chiusura degli Opifici Nazionali", "Spaccatura tra Moderati e Socialisti"] }
      ],
      "Le Guerre d'Indipendenza italiane": [
        { name: "Prima Guerra d'Indipendenza", cat: "Campagne Militari", exp: "Il conflitto del 1848-1849 condotto da Carlo Alberto contro l'Austria, caratterizzato dalle vittorie iniziali a Goito e Pastrengo, fino alla sconfitta decisiva di Novara.", items: ["Mobilitazione degli Stati Italiani", "Vittorie di Goito e Pastrengo", "Ritiro delle Truppe Papali e Borboniche", "Sconfitta di Custoza e Novara"] },
        { name: "Accordi di Plombières", cat: "Diplomazia Strategica", exp: "L'alleanza segreta tra Cavour e Napoleone III stipulata nel 1858: sostegno militare francese al Piemonte in cambio della cessione di Nizza e della Savoia.", items: ["Incontro Segreto di Plombières", "Provocazioni Militari sul Ticino", "Mobilitazione dell'Esercito Austriaco", "Intervento Armato di Napoleone III"] },
        { name: "Solferino e San Martino", cat: "Battaglie Decisive", exp: "Le cruente battaglie del 24 giugno 1859 che portarono alla liberazione della Lombardia e ispirarono Henry Dunant alla fondazione della Croce Rossa Internazionale.", items: ["Scontro Generale Franco-Piemontese", "Ritirata dell'Esercito Austriaco", "Armistizio di Villafranca", "Nascita della Croce Rossa (Dunant)"] },
        { name: "Annessione della Lombardia", cat: "Assetto Geopolitico", exp: "Il passaggio della Lombardia al Regno di Sardegna nel 1859 tramite i plebisciti popolari dell'Italia centrale, passo decisivo verso l'unificazione.", items: ["Trattato di Zurigo", "Plebisciti in Emilia e Toscana", "Cessione di Nizza e Savoia", "Espansione Territoriale Sabauda"] }
      ],
      "Le 5 Giornate di Milano e la diplomazia di Cavour": [
        { name: "Insurrezione Popolare", cat: "Resistenza Civile", exp: "Le leggendarie giornate dal 18 al 22 marzo 1848: il popolo milanese costrinse l'esercito austriaco del maresciallo Radetzky ad abbandonare la città.", items: ["Costruzione delle Barricate Cittadine", "Consiglio di Guerra di Carlo Cattaneo", "Assalto al Palazzo del Broletto", "Cacciata delle Truppe Austriache"] },
        { name: "Radetzky & Barricate", cat: "Tattica Militare", exp: "La ritirata delle truppe asburgiche verso le fortezze del Quadrilatero (Verona, Peschiera, Legnago, Mantova) sotto la pressione popolare.", items: ["Controllo delle Porte Cittadine", "Uso strategico dei Palloni Aerostatici", "Ritirata verso il Quadrilatero", "Difesa Territoriale Asburgica"] },
        { name: "Modernizzazione Cavouriana", cat: "Politica Economica", exp: "La visione liberista di Camillo Benso di Cavour: potenziamento della rete ferroviaria piemontese, apertura al commercio estero e riforme del sistema bancario.", items: ["Canalizzazione Agricola e Canale Cavour", "Sviluppo della Rete Ferroviaria", "Trattati Commerciali di Libero Scambio", "Banca Nazionale degli Stati Sardi"] },
        { name: "Guerra di Crimea", cat: "Diplomazia Europea", exp: "La partecipazione piemontese alla guerra di Crimea (1855) che permise a Cavour di portare la 'questione italiana' all'attenzione del Congresso di Parigi.", items: ["Invio del Corpo di Spedizione a Cernaia", "Partecipazione al Congresso di Parigi (1856)", "Denuncia del Malgoverno Borbonico", "Accreditamento Internazionale del Piemonte"] }
      ],
      "Le grandi ideologie dell'Ottocento": [
        { name: "Liberalismo Politico & Economico", cat: "Dottrina Politica", exp: "Dottrina incentrata sulla libertà individuale, la separazione dei poteri (Montesquieu), lo stato di diritto, il libero mercato e la proprietà privata.", items: ["Libertà Individuali e Civili", "Divisione dei Poteri Istituzionali", "Libero Mercato e Concorrenza (Smith)", "Stato Minimo e Garanzia Giuridica"] },
        { name: "Socialismo Scientifico", cat: "Materialismo Storico", exp: "La teoria rivoluzionaria di Karl Marx e Friedrich Engels: analisi delle leggi del capitale, sfruttamento del plusvalore e superamento del capitalismo.", items: ["Manifesto del Partito Comunista (1848)", "Materialismo Storico e Struttura", "Teoria del Plusvalore e Sfruttamento", "Dittatura del Proletariato e Società Senza Classi"] },
        { name: "Lotta di Classe", cat: "Dinamiche Sociali", exp: "Il motore della storia individuato da Marx nello scontro insanabile tra la borghesia proprietaria dei mezzi di produzione e il proletariato salariato.", items: ["Borghesia Industriale", "Proletariato di Fabbrica", "Alienazione del Lavoro", "Coscienza di Classe Collettiva"] },
        { name: "Anarchismo Bakuniano", cat: "Pensiero Libertario", exp: "La corrente di Michail Bakunin che individuava nello Stato e nella religione le principali fonti di oppressione umana, promuovendo l'autogestione.", items: ["Rifiuto Totale dello Stato", "Abolizione della Proprietà Privata", "Autogestione e Federazione dal Basso", "Insurrezionalismo Rivoluzionario"] }
      ],
      "Il Risorgimento e la Spedizione dei Mille": [
        { name: "Moderati vs. Democratici", cat: "Dibattito Risorgimentale", exp: "Il confronto politico tra la linea monarchico-diplomatica di Cavour e l'ideale repubblicano e rivoluzionario di Giuseppe Mazzini e Carlo Cattaneo.", items: ["Linea Diplomatica Sabauda (Cavour)", "Progetto Repubblicano Unitario (Mazzini)", "Federalismo Democratico (Cattaneo)", "Società Nazionale Italiana"] },
        { name: "Spedizione dei Mille", cat: "Epopea Garibaldina", exp: "La partenza da Quarto il 5 maggio 1860, lo sbarco a Marsala, la vittoria a Calatafimi e la liberazione progressiva della Sicilia e del Mezzogiorno.", items: ["Partenza da Quarto (5 Maggio 1860)", "Sbarco a Marsala e Proclama di Salemi", "Vittoria Campale a Calatafimi", "Presa di Palermo e Napoli"] },
        { name: "Incontro di Teano", cat: "Unificazione Politica", exp: "Lo storico incontro del 26 ottobre 1860 tra Giuseppe Garibaldi e il re Vittorio Emanuele II, con la consegna dei territori liberati alla Corona sabauda.", items: ["Avanzata dell'Esercito Sabaudo", "Incontro a Teano (26 Ottobre 1860)", "Accettazione della Corona Sabauda", "Cessazione delle Ostilità Garibaldine"] },
        { name: "Proclamazione del Regno d'Italia", cat: "Nascita dello Stato", exp: "Il 17 marzo 1861 il primo Parlamento nazionale riunito a Torino proclama ufficialmente la nascita del Regno d'Italia con capitale provvisoria Torino.", items: ["Riunione del Primo Parlamento a Torino", "Proclamazione Ufficiale (17 Marzo 1861)", "Vittorio Emanuele II Re d'Italia", "Estensione dello Statuto Albertino"] }
      ]
    };

    /**
     * Helper to retrieve or generate complete concept map with 4-5 keywords and 1-5 generated visuals
     */
    const getConceptMapForTopic = (subject, topic, isItalian) => {
      const title = topic.title || topic;
      const desc = topic.desc || '';
      
      let keywords = [];

      // Check if we have curated data for this specific topic
      if (CURATED_CONCEPT_TOPICS[title]) {
        const raw = CURATED_CONCEPT_TOPICS[title];
        keywords = raw.map((k, idx) => ({
          id: `kw-${idx + 1}`,
          name: k.name,
          category: k.cat,
          coords: [
            { x: 22, y: 26 },
            { x: 78, y: 26 },
            { x: 78, y: 74 },
            { x: 22, y: 74 }
          ][idx % 4],
          explanation: k.exp,
          images: [
            {
              type: idx % 2 === 0 ? 'flow' : 'matrix',
              badge: isItalian ? 'SCHEMA OPERATIVO' : 'OPERATIONAL SCHEMA',
              title: `${k.name}: ${isItalian ? 'Struttura Concettuale' : 'Conceptual Structure'}`,
              caption: isItalian 
                ? `Quadro sintetico dei componenti chiave relativi a ${k.name}.`
                : `Comprehensive breakdown of key parameters relating to ${k.name}.`,
              items: k.items
            },
            {
              type: 'structural',
              badge: isItalian ? 'ANALISI GERARCHICA' : 'HIERARCHICAL ANALYSIS',
              title: `${k.name}: ${isItalian ? 'Livelli di Approfondimento' : 'Depth Layers'}`,
              caption: isItalian
                ? `Progressione metodologica e livelli di apprendimento per ${k.name}.`
                : `Methodological progression and mastery levels for ${k.name}.`,
              items: [
                isItalian ? `Fondamenti di ${k.name}` : `Foundations of ${k.name}`,
                isItalian ? `Applicazione Analitica` : `Analytical Application`,
                isItalian ? `Sintesi e Padronanza` : `Synthesis & Mastery`
              ]
            }
          ]
        }));
      } else {
        // High quality intelligent synthesis for any other topic
        const cleanWords = title.replace(/[^\w\sàèéìòùáéíóú-]/gi, '').split(/\s+/).filter(w => w.length > 2);
        
        const terms = isItalian ? [
          { name: cleanWords.slice(0, 2).join(' ') || "Principi Guida", cat: "Inquadramento Teorico" },
          { name: cleanWords.slice(2, 4).join(' ') || "Metodi di Analisi", cat: "Metodologia & Tecniche" },
          { name: cleanWords.slice(4, 6).join(' ') || "Esecuzione Pratica", cat: "Applicazione Didattica" },
          { name: "Competenze & Sintesi", cat: "Valutazione Critica" }
        ] : [
          { name: cleanWords.slice(0, 2).join(' ') || "Core Principles", cat: "Theoretical Framework" },
          { name: cleanWords.slice(2, 4).join(' ') || "Methodological Tools", cat: "Techniques & Analysis" },
          { name: cleanWords.slice(4, 6).join(' ') || "Applied Execution", cat: "Practical Application" },
          { name: "Critical Synthesis", cat: "Academic Evaluation" }
        ];

        keywords = terms.map((t, idx) => ({
          id: `kw-${idx + 1}`,
          name: t.name,
          category: t.cat,
          coords: [
            { x: 22, y: 26 },
            { x: 78, y: 26 },
            { x: 78, y: 74 },
            { x: 22, y: 74 }
          ][idx % 4],
          explanation: isItalian
            ? `Trattazione approfondita del nucleo tematico "${t.name}" all'interno di "${title}". Questa sezione esamina i presupposti teorici, le procedure operative e gli standard didattici affrontati nel programma di studi.`
            : `Comprehensive breakdown of the thematic core "${t.name}" within "${title}". This section investigates theoretical assumptions, operative procedures, and curricular learning standards.`,
          images: [
            {
              type: idx % 2 === 0 ? 'flow' : 'matrix',
              badge: isItalian ? 'SCHEMA CONCETTUALE' : 'CONCEPTUAL SCHEMA',
              title: `${t.name}: ${isItalian ? 'Articolazione Didattica' : 'Curricular Pipeline'}`,
              caption: isItalian
                ? `Fasi progressive di studio e applicazione relative a ${t.name}.`
                : `Sequential progression of study and empirical application for ${t.name}.`,
              items: isItalian ? [
                `Inquadramento di ${t.name}`,
                `Analisi dei Dati e dei Testi`,
                `Elaborazione e Verifica`,
                `Valutazione dei Risultati`
              ] : [
                `Framework of ${t.name}`,
                `Data & Textual Analysis`,
                `Empirical Validation`,
                `Synthesis & Evaluation`
              ]
            },
            {
              type: 'structural',
              badge: isItalian ? 'STRUTTURA DELLE COMPETENZE' : 'COMPETENCY STRUCTURE',
              title: `${t.name}: ${isItalian ? 'Quadro delle Abilità' : 'Skill Hierarchy'}`,
              caption: isItalian
                ? `Competenze specifiche acquisite attraverso l'approfondimento di ${t.name}.`
                : `Core academic and practical competencies mastered through ${t.name}.`,
              items: isItalian ? [
                `Conoscenza Teorica Rigorosa`,
                `Padronanza Tecnica ed Espressiva`,
                `Autonomia Critica e Problem Solving`
              ] : [
                `Foundational Knowledge`,
                `Technical & Analytical Fluency`,
                `Autonomous Critical Problem Solving`
              ]
            }
          ]
        }));
      }

      return {
        centralTitle: title,
        subjectName: subject.name,
        isItalian: isItalian,
        desc: desc,
        keywords: keywords
      };
    };

    /**
     * Overlay Concept Map Modal with Multi-Line SVG Wrapping and Click-Away Side Drawer
     */
    const TopicConceptMapModal = ({ mapData, onClose }) => {
      const [selectedKeyword, setSelectedKeyword] = useState(null);

      useEffect(() => {
        const handleKeyDown = (e) => {
          if (e.key === 'Escape') {
            if (selectedKeyword) {
              setSelectedKeyword(null);
            } else {
              onClose();
            }
          }
        };
        window.addEventListener('keydown', handleKeyDown);
        return () => window.removeEventListener('keydown', handleKeyDown);
      }, [selectedKeyword, onClose]);

      const titleLines = wrapSvgText(mapData.centralTitle, 16);

      return (
        <div 
          className="fixed inset-0 z-[70] flex items-center justify-center bg-black/90 backdrop-blur-md animate-fade-in select-none"
          onClick={() => {
            if (selectedKeyword) setSelectedKeyword(null);
            else onClose();
          }}
        >
          {/* Main Modal Container */}
          <div 
            className="relative w-full h-full max-w-7xl max-h-[94vh] m-4 md:m-8 bg-[#171817] border border-[#B79A63]/50 rounded-sm shadow-2xl overflow-hidden flex flex-col"
            onClick={(e) => {
              if (!e.target.closest('#keyword-side-drawer')) {
                if (selectedKeyword) setSelectedKeyword(null);
              }
              e.stopPropagation();
            }}
          >
            {/* Top Bar Header */}
            <div className="px-6 py-4 bg-[#18352B] border-b border-[#A8B3A0]/20 flex justify-between items-center shrink-0">
              <div className="flex items-center space-x-3">
                <span className="text-[10px] font-mono uppercase tracking-widest text-[#B79A63] bg-[#171817] px-2.5 py-1 rounded border border-[#B79A63]/40">
                  {mapData.isItalian ? 'MAPPA CONCETTUALE INTERATTIVA' : 'INTERACTIVE CONCEPT MAP'}
                </span>
                <span className="text-xs font-mono text-[#A8B3A0]">
                  {mapData.subjectName}
                </span>
              </div>

              <div className="flex items-center space-x-4">
                <span className="hidden sm:inline text-[11px] font-mono text-[#E7E9E3]/70">
                  {mapData.isItalian 
                    ? '💡 Clicca su un nodo per aprire il riquadro laterale' 
                    : '💡 Click any node to open the side explanation drawer'}
                </span>
                <button 
                  onClick={onClose}
                  className="w-8 h-8 rounded-full bg-[#171817] hover:bg-[#B79A63] hover:text-[#171817] text-[#F5F1E8] flex items-center justify-center transition-colors font-mono text-sm border border-[#A8B3A0]/30 shadow"
                  title="Close Map"
                >
                  ✕
                </button>
              </div>
            </div>

            {/* Map Canvas + Interactive SVG */}
            <div className="relative flex-1 bg-[#121312] overflow-hidden flex items-center justify-center">
              
              {/* Background Ambient Celestial Rings & Grid */}
              <svg className="absolute inset-0 w-full h-full pointer-events-none opacity-20">
                <circle cx="50%" cy="50%" r="35%" fill="none" stroke="#A8B3A0" strokeWidth="0.5" strokeDasharray="2 6" />
                <circle cx="50%" cy="50%" r="20%" fill="none" stroke="#B79A63" strokeWidth="0.5" strokeDasharray="3 5" />
                <line x1="10%" y1="50%" x2="90%" y2="50%" stroke="#A8B3A0" strokeWidth="0.3" strokeDasharray="2 6" />
                <line x1="50%" y1="10%" x2="50%" y2="90%" stroke="#A8B3A0" strokeWidth="0.3" strokeDasharray="2 6" />
              </svg>

              {/* Main SVG Interactive Graph */}
              <svg viewBox="0 0 100 100" className="w-full h-full max-w-4xl max-h-[80vh] overflow-visible">
                {/* Connecting Lines between Central Hub and Keyword Nodes */}
                {mapData.keywords.map((kw, i) => {
                  const isSelected = selectedKeyword && selectedKeyword.id === kw.id;
                  return (
                    <g key={`line-${kw.id}`}>
                      {isSelected && (
                        <line 
                          x1="50" y1="50" 
                          x2={kw.coords.x} y2={kw.coords.y} 
                          stroke="#FFFFFF" strokeWidth="2.5" opacity="0.3" strokeLinecap="round" 
                        />
                      )}
                      <line 
                        x1="50" y1="50" 
                        x2={kw.coords.x} y2={kw.coords.y} 
                        stroke={isSelected ? "#FFFFFF" : "#B79A63"} 
                        strokeWidth={isSelected ? 1.5 : 0.8} 
                        strokeDasharray={isSelected ? "none" : "2 3"}
                        className={`transition-all duration-300 ${isSelected ? 'opacity-100' : 'opacity-40'}`} 
                      />
                    </g>
                  );
                })}

                {/* Cross-linking routes between neighboring keywords */}
                {mapData.keywords.map((kw, i) => {
                  const nextKw = mapData.keywords[(i + 1) % mapData.keywords.length];
                  return (
                    <line 
                      key={`cross-${i}`}
                      x1={kw.coords.x} y1={kw.coords.y} 
                      x2={nextKw.coords.x} y2={nextKw.coords.y} 
                      stroke="#A8B3A0" strokeWidth="0.5" strokeDasharray="1 4" opacity="0.25"
                    />
                  );
                })}

                {/* Central Hub Node (Topic Title with Multi-Line Wrapping) */}
                <g transform="translate(50, 50)" className="cursor-default select-none">
                  <circle r="14" fill="#18352B" stroke="#B79A63" strokeWidth="1.2" className="shadow-lg" />
                  <circle r="16" fill="none" stroke="#B79A63" strokeWidth="0.5" opacity="0.4" />
                  <text y="-6" textAnchor="middle" fill="#B79A63" fontSize="2.4" fontFamily="monospace" fontWeight="bold" letterSpacing="0.1em">
                    {mapData.isItalian ? 'ARGOMENTO' : 'TOPIC'}
                  </text>
                  {titleLines.map((line, lIdx, arr) => (
                    <text 
                      key={lIdx} 
                      y={-1.5 + (lIdx - (arr.length - 1) / 2) * 3.4} 
                      textAnchor="middle" 
                      fill="#F5F1E8" 
                      fontSize="2.7" 
                      fontFamily="serif" 
                      fontWeight="bold"
                    >
                      {line}
                    </text>
                  ))}
                </g>

                {/* Interactive Keyword Nodes */}
                {mapData.keywords.map((kw, idx) => {
                  const isSelected = selectedKeyword && selectedKeyword.id === kw.id;
                  const kwLines = wrapSvgText(kw.name, 14);

                  return (
                    <g 
                      key={kw.id} 
                      onClick={(e) => {
                        e.stopPropagation();
                        setSelectedKeyword(kw);
                      }}
                      className="cursor-pointer group select-none"
                    >
                      {/* Outer Glow Halo on Hover */}
                      <circle 
                        cx={kw.coords.x} cy={kw.coords.y} 
                        r={isSelected ? 5 : 4} 
                        fill={isSelected ? "#FFFFFF" : "#B79A63"} 
                        opacity={isSelected ? "0.3" : "0.1"} 
                        className="transition-all duration-300 group-hover:opacity-30" 
                      />

                      {/* Main Node Body */}
                      <circle 
                        cx={kw.coords.x} cy={kw.coords.y} 
                        r={isSelected ? 3.5 : 2.6} 
                        fill={isSelected ? "#FFFFFF" : "#171817"} 
                        stroke={isSelected ? "#FFFFFF" : "#B79A63"} 
                        strokeWidth="0.8" 
                        className="transition-all duration-300 group-hover:scale-110 shadow-md" 
                      />

                      {/* Node Number */}
                      <text 
                        x={kw.coords.x} y={kw.coords.y + 0.9} 
                        textAnchor="middle" 
                        fill={isSelected ? "#171817" : "#B79A63"} 
                        fontSize="2.4" 
                        fontFamily="monospace" 
                        fontWeight="bold"
                      >
                        0{idx + 1}
                      </text>

                      {/* Keyword Label Tag with Multi-Line Badges */}
                      <g transform={`translate(${kw.coords.x}, ${kw.coords.y + 5.5})`}>
                        {kwLines.map((line, lIdx) => (
                          <g key={lIdx} transform={`translate(0, ${lIdx * 4})`}>
                            <rect 
                              x={-(line.length * 1.4 + 4)} y="-2.2" 
                              width={(line.length * 2.8 + 8)} height="4.4" 
                              rx="1.2" 
                              fill="#171817" 
                              fillOpacity={isSelected ? "1" : "0.95"}
                              stroke={isSelected ? "#FFFFFF" : "#A8B3A0"} 
                              strokeWidth="0.4"
                              className="transition-all duration-300"
                            />
                            <text 
                              y="0.8" textAnchor="middle" 
                              fill={isSelected ? "#FFFFFF" : "#F5F1E8"} 
                              fontSize="2.4" 
                              fontFamily="sans-serif" 
                              fontWeight={isSelected ? "bold" : "normal"}
                            >
                              {line}
                            </text>
                          </g>
                        ))}
                      </g>
                    </g>
                  );
                })}
              </svg>
            </div>

            {/* Modal Bottom Bar */}
            <div className="px-6 py-3 bg-[#18352B] border-t border-[#A8B3A0]/20 flex justify-between items-center text-xs font-mono text-[#A8B3A0] shrink-0">
              <span>{mapData.centralTitle}</span>
              <span className="text-[#B79A63]">
                {mapData.keywords.length} {mapData.isItalian ? 'PAROLE CHIAVE COLLEGATE' : 'CONNECTED KEYWORDS'}
              </span>
            </div>

            {/* ==================================================================== */}
            {/* SIDE DRAWER (RIQUADRO LATERALE): APRE LA SPIEGAZIONE & SCHEMI        */}
            {/* ==================================================================== */}
            {selectedKeyword && (
              <div 
                id="keyword-side-drawer"
                className="absolute top-0 right-0 bottom-0 w-full sm:w-[480px] lg:w-[540px] bg-[#171817] border-l border-[#B79A63]/50 shadow-2xl z-30 flex flex-col animate-slide-left select-text"
                onClick={(e) => e.stopPropagation()}
              >
                {/* Drawer Header */}
                <div className="p-6 bg-[#18352B] border-b border-[#A8B3A0]/20 flex justify-between items-start shrink-0">
                  <div>
                    <span className="text-[10px] font-mono uppercase tracking-widest text-[#B79A63] bg-[#171817] px-2.5 py-1 rounded border border-[#B79A63]/30 inline-block mb-1.5 font-semibold">
                      {selectedKeyword.category}
                    </span>
                    <h4 className="font-serif text-2xl text-[#F5F1E8] font-normal leading-snug">
                      {selectedKeyword.name}
                    </h4>
                  </div>
                  <button 
                    onClick={() => setSelectedKeyword(null)}
                    className="w-8 h-8 rounded-full bg-[#171817] hover:bg-[#B79A63] hover:text-[#171817] text-[#F5F1E8] flex items-center justify-center transition-colors font-mono text-sm border border-[#A8B3A0]/30 shadow shrink-0 ml-4"
                    title="Close Drawer"
                  >
                    ✕
                  </button>
                </div>

                {/* Drawer Scrollable Content */}
                <div className="p-6 overflow-y-auto space-y-6 flex-1 bg-[#171817]">
                  {/* Detailed Explanation */}
                  <div className="space-y-2">
                    <h5 className="text-[10px] font-mono uppercase tracking-widest text-[#B79A63] font-semibold">
                      {mapData.isItalian ? 'SPIEGAZIONE DETTAGLIATA' : 'DETAILED EXPLANATION'}
                    </h5>
                    <p className="text-sm font-sans text-[#E7E9E3]/95 leading-relaxed bg-[#18352B] p-4 rounded border border-[#A8B3A0]/20 shadow-inner">
                      {selectedKeyword.explanation}
                    </p>
                  </div>

                  {/* Generated Visual Schematics (1-5) */}
                  <div className="space-y-3">
                    <div className="flex justify-between items-center">
                      <h5 className="text-[10px] font-mono uppercase tracking-widest text-[#B79A63] font-semibold">
                        {mapData.isItalian ? 'SCHEMI E ILLUSTRAZIONI GRAFICHE' : 'GENERATED SCHEMATICS & VISUALS'}
                      </h5>
                      <span className="text-[10px] font-mono text-[#A8B3A0]">
                        {selectedKeyword.images ? selectedKeyword.images.length : 0} {mapData.isItalian ? 'SCHEMI' : 'VISUALS'}
                      </span>
                    </div>

                    <div className="space-y-4">
                      {selectedKeyword.images && selectedKeyword.images.map((vis, vIdx) => (
                        <GeneratedVisualCard key={vIdx} visual={vis} index={vIdx} />
                      ))}
                    </div>
                  </div>
                </div>

                {/* Drawer Footer */}
                <div className="p-4 bg-[#18352B] border-t border-[#A8B3A0]/20 flex justify-between items-center text-[10px] font-mono text-[#A8B3A0] shrink-0">
                  <span>{mapData.isItalian ? 'SCHEDA PAROLA CHIAVE' : 'KEYWORD ANALYSIS'}</span>
                  <button 
                    onClick={() => setSelectedKeyword(null)}
                    className="text-[#B79A63] hover:underline font-semibold"
                  >
                    {mapData.isItalian ? 'CHIUDI RIQUADRO [✕]' : 'CLOSE DRAWER [✕]'}
                  </button>
                </div>
              </div>
            )}
          </div>
        </div>
      );
    };"""

# Replace the old section
old_start_marker = "    // ============================================================================\n    // RICH CONCEPT MAPS & GENERATED VISUAL SCHEMATICS (SECTION 07)"
old_end_marker = "    // ============================================================================\n    // 3. MAIN COMPONENT ARCHITECTURE & SECTIONS\n    // ============================================================================"

pattern = re.compile(re.escape(old_start_marker) + r".*?" + re.escape(old_end_marker), re.DOTALL)

if pattern.search(code):
    code = pattern.sub(new_concept_engine.strip() + "\n\n" + old_end_marker, code)
    print("Replaced concept map engine successfully.")
else:
    print("Error: Could not match old concept map engine.")

with open(r'c:\Users\Enrico\Desktop\Giada\the_irish_year.html', 'w', encoding='utf-8') as f:
    f.write(code)

print("Saved updated the_irish_year.html.")
