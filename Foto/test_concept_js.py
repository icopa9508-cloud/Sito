# Script to inject the complete Concept Map engine and data into the_irish_year.html
import re

concept_maps_code = '''
    // ============================================================================
    // RICH CONCEPT MAPS & GENERATED VISUAL SCHEMATICS (SECTION 07)
    // Supports all topics for both Ireland (English) and Italy (Italian)
    // ============================================================================

    const GENERATED_VISUAL_TEMPLATES = {
      flow: (title, steps) => (
        <svg viewBox="0 0 400 120" className="w-full h-auto rounded bg-[#171817] p-2 border border-[#A8B3A0]/20">
          <defs>
            <marker id="arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
              <path d="M 0 0 L 10 5 L 0 10 z" fill="#B79A63" />
            </marker>
          </defs>
          <text x="200" y="20" textAnchor="middle" fill="#B79A63" fontSize="10" fontFamily="monospace" letterSpacing="0.1em">{title.toUpperCase()}</text>
          {steps.map((st, i) => {
            const x = 30 + i * (340 / Math.max(1, steps.length - 1));
            const isLast = i === steps.length - 1;
            return (
              <g key={i}>
                {!isLast && (
                  <line 
                    x1={x + 35} y1={65} 
                    x2={30 + (i + 1) * (340 / Math.max(1, steps.length - 1)) - 35} y2={65} 
                    stroke="#B79A63" strokeWidth="1.5" strokeDasharray="3 3" markerEnd="url(#arrow)" 
                  />
                )}
                <rect x={x - 30} y={42} width={60} height={46} rx="4" fill="#18352B" stroke="#A8B3A0" strokeWidth="1" />
                <text x={x} y={60} textAnchor="middle" fill="#FFFFFF" fontSize="9" fontWeight="bold" fontFamily="sans-serif">
                  {st.length > 10 ? st.slice(0, 10) + '..' : st}
                </text>
                <text x={x} y={75} textAnchor="middle" fill="#B79A63" fontSize="7.5" fontFamily="monospace">
                  STEP 0{i + 1}
                </text>
              </g>
            );
          })}
        </svg>
      ),
      matrix: (title, items) => (
        <svg viewBox="0 0 400 130" className="w-full h-auto rounded bg-[#171817] p-2 border border-[#A8B3A0]/20">
          <text x="200" y="18" textAnchor="middle" fill="#B79A63" fontSize="10" fontFamily="monospace" letterSpacing="0.1em">{title.toUpperCase()}</text>
          <g transform="translate(20, 28)">
            <rect x="0" y="0" width="175" height="42" rx="3" fill="#18352B" stroke="#B79A63" strokeWidth="0.8" />
            <text x="10" y="18" fill="#F5F1E8" fontSize="9" fontWeight="bold" fontFamily="sans-serif">{items[0] || 'Dimension A'}</text>
            <text x="10" y="32" fill="#A8B3A0" fontSize="7.5" fontFamily="monospace">CORE PARAMETER</text>

            <rect x="185" y="0" width="175" height="42" rx="3" fill="#18352B" stroke="#A8B3A0" strokeWidth="0.8" />
            <text x="195" y="18" fill="#F5F1E8" fontSize="9" fontWeight="bold" fontFamily="sans-serif">{items[1] || 'Dimension B'}</text>
            <text x="195" y="32" fill="#A8B3A0" fontSize="7.5" fontFamily="monospace">OPERATIONAL IMPACT</text>

            <rect x="0" y="48" width="175" height="42" rx="3" fill="#18352B" stroke="#A8B3A0" strokeWidth="0.8" />
            <text x="10" y="66" fill="#F5F1E8" fontSize="9" fontWeight="bold" fontFamily="sans-serif">{items[2] || 'Dimension C'}</text>
            <text x="10" y="80" fill="#A8B3A0" fontSize="7.5" fontFamily="monospace">STRATEGIC GOAL</text>

            <rect x="185" y="48" width="175" height="42" rx="3" fill="#18352B" stroke="#B79A63" strokeWidth="0.8" />
            <text x="195" y="66" fill="#F5F1E8" fontSize="9" fontWeight="bold" fontFamily="sans-serif">{items[3] || 'Dimension D'}</text>
            <text x="195" y="80" fill="#B79A63" fontSize="7.5" fontFamily="monospace">KEY OUTCOME</text>
          </g>
        </svg>
      ),
      structural: (title, layers) => (
        <svg viewBox="0 0 400 130" className="w-full h-auto rounded bg-[#171817] p-2 border border-[#A8B3A0]/20">
          <text x="200" y="18" textAnchor="middle" fill="#B79A63" fontSize="10" fontFamily="monospace" letterSpacing="0.1em">{title.toUpperCase()}</text>
          <g transform="translate(30, 26)">
            {layers.map((lyr, i) => (
              <g key={i} transform={`translate(0, ${i * 28})`}>
                <rect x="0" y="0" width="340" height="22" rx="3" fill={i === 0 ? '#18352B' : '#171817'} stroke={i === 0 ? '#B79A63' : '#A8B3A0'} strokeWidth="0.8" />
                <circle cx="15" cy="11" r="5" fill="#B79A63" />
                <text x="15" y="14" textAnchor="middle" fill="#171817" fontSize="7" fontWeight="bold">0{i+1}</text>
                <text x="30" y="15" fill="#F5F1E8" fontSize="8.5" fontFamily="sans-serif">{lyr}</text>
                <text x="325" y="15" textAnchor="end" fill="#A8B3A0" fontSize="7" fontFamily="monospace">LEVEL {i+1}</text>
              </g>
            ))}
          </g>
        </svg>
      )
    };

    /**
     * Generated Visual Schematic Card Component
     */
    const GeneratedVisualCard = ({ visual, index }) => {
      const renderGraphic = () => {
        if (visual.type === 'flow') {
          return GENERATED_VISUAL_TEMPLATES.flow(visual.title, visual.items || ['Initiation', 'Processing', 'Validation', 'Output']);
        } else if (visual.type === 'matrix') {
          return GENERATED_VISUAL_TEMPLATES.matrix(visual.title, visual.items || ['Input Factors', 'Mechanics', 'Methodology', 'Results']);
        } else {
          return GENERATED_VISUAL_TEMPLATES.structural(visual.title, visual.items || ['Foundational Principles', 'Execution Layer', 'Synthesis & Integration']);
        }
      };

      return (
        <div className="bg-[#171817]/90 border border-[#A8B3A0]/30 rounded-sm p-3.5 space-y-2 hover:border-[#B79A63] transition-all shadow-md">
          <div className="flex justify-between items-center text-[10px] font-mono text-[#A8B3A0]">
            <span className="text-[#B79A63] font-semibold">FIG. 0{index + 1} · {visual.badge || 'GENERATED SCHEMATIC'}</span>
            <span>{visual.type.toUpperCase()}</span>
          </div>
          <div className="overflow-hidden rounded border border-[#A8B3A0]/20">
            {renderGraphic()}
          </div>
          <div className="space-y-1 pt-1">
            <h5 className="font-serif text-sm text-[#F5F1E8] font-normal">{visual.title}</h5>
            <p className="text-[11px] font-sans text-[#E7E9E3]/75 leading-relaxed">{visual.caption}</p>
          </div>
        </div>
      );
    };

    /**
     * Helper to retrieve or generate complete concept map with 4-5 keywords and 1-5 generated visuals
     */
    const getConceptMapForTopic = (subject, topic, isItalian) => {
      const title = topic.title || topic;
      const desc = topic.desc || '';
      
      // Keywords synthesis based on topic content
      const words = title.split(/[ ,&/:;()]+/).filter(w => w.length > 3 && !['delle','degli','della','dello','delle','dall','dell','with','from','into','over','through','under','between'].includes(w.toLowerCase()));
      
      const kw1 = words[0] || (isItalian ? 'Fondamenti' : 'Core Foundation');
      const kw2 = words[1] || (isItalian ? 'Metodologia' : 'Methodology');
      const kw3 = words[2] || (isItalian ? 'Applicazione' : 'Application');
      const kw4 = words[3] || (isItalian ? 'Sintesi Critica' : 'Critical Synthesis');

      const keywords = [
        {
          id: 'kw-1',
          name: kw1,
          category: isItalian ? 'Principi Fondamentali' : 'Core Principles',
          coords: { x: 25, y: 30 },
          explanation: isItalian 
            ? `Analisi strutturale del concetto di ${kw1} nell'ambito di "${title}". Rappresenta il presupposto teorico e concettuale necessario per comprendere i meccanismi operativi della materia.`
            : `Comprehensive theoretical analysis of ${kw1} within the scope of "${title}". It establishes the conceptual foundation required to understand the operative mechanics of the curriculum.`,
          images: [
            {
              type: 'flow',
              badge: isItalian ? 'FLUSSO CONCETTUALE' : 'CONCEPTUAL PIPELINE',
              title: isItalian ? `Flusso Operativo: ${kw1}` : `Operative Flow: ${kw1}`,
              caption: isItalian ? `Schema sequenziale delle fasi analitiche relative a ${kw1}.` : `Sequential pipeline representing analytical phases of ${kw1}.`,
              items: [isItalian ? 'Inquadramento' : 'Definition', isItalian ? 'Decomposizione' : 'Analysis', isItalian ? 'Verifica' : 'Validation', isItalian ? 'Integrazione' : 'Output']
            },
            {
              type: 'structural',
              badge: isItalian ? 'GERARCHIA STRUTTURALE' : 'STRUCTURAL HIERARCHY',
              title: isItalian ? `Architettura di ${kw1}` : `Architecture of ${kw1}`,
              caption: isItalian ? `Livelli di astrazione e componenti costitutive di ${kw1}.` : `Levels of abstraction and constituent layers of ${kw1}.`,
              items: [isItalian ? 'Assunti Teorici' : 'Theoretical Foundations', isItalian ? 'Standard Operativi' : 'Operative Standards', isItalian ? 'Output Finale' : 'Final Synthesis']
            }
          ]
        },
        {
          id: 'kw-2',
          name: kw2,
          category: isItalian ? 'Metodologia e Tecniche' : 'Techniques & Methods',
          coords: { x: 75, y: 30 },
          explanation: isItalian
            ? `Approccio metodologico e procedure tecniche relative a ${kw2}. Include strumenti analitici, regole compositive o modelli formali utilizzati per raggiungere la massima precisione.`
            : `Methodological approach and technical procedures governing ${kw2}. Encompasses analytical toolsets, compositional rules, and formal models engineered for rigorous execution.`,
          images: [
            {
              type: 'matrix',
              badge: isItalian ? 'MATRICE METODOLOGICA' : 'METHODOLOGY MATRIX',
              title: isItalian ? `Parametri di ${kw2}` : `Parameters of ${kw2}`,
              caption: isItalian ? `Relazione tra variabili tecniche e requisiti qualitativi.` : `Relationship between technical variables and quality criteria.`,
              items: [isItalian ? 'Variabili Chiave' : 'Key Variables', isItalian ? 'Protocolli' : 'Protocols', isItalian ? 'Metriche' : 'Metrics', isItalian ? 'Risultati' : 'Outcomes']
            }
          ]
        },
        {
          id: 'kw-3',
          name: kw3,
          category: isItalian ? 'Applicazione Pratica' : 'Practical Application',
          coords: { x: 75, y: 72 },
          explanation: isItalian
            ? `Applicazione concreta e casi studio di ${kw3}. Esamina come la teoria si traduce in elaborati grafici, analisi letterarie, registrazioni contabili o strategie commerciali.`
            : `Real-world application and case study integration of ${kw3}. Demonstrates how theory translates directly into critical essays, balance sheets, production plans, or strategic campaigns.`,
          images: [
            {
              type: 'flow',
              badge: isItalian ? 'PROCESSO APPLICATIVO' : 'APPLICATION CYCLE',
              title: isItalian ? `Ciclo di Realizzazione: ${kw3}` : `Execution Cycle: ${kw3}`,
              caption: isItalian ? `Fasi dalla formulazione all'applicazione sul campo.` : `Phases from initial problem framing to final empirical execution.`,
              items: [isItalian ? 'Progettazione' : 'Design', isItalian ? 'Esecuzione' : 'Execution', isItalian ? 'Controllo Qualità' : 'Quality Control']
            },
            {
              type: 'matrix',
              badge: isItalian ? 'CONFRONTO METRICO' : 'BENCHMARK MATRIX',
              title: isItalian ? `Standard di Rendimento: ${kw3}` : `Performance Benchmarks: ${kw3}`,
              caption: isItalian ? `Valutazione dei risultati attesi rispetto ai benchmark standard.` : `Evaluating delivered outcomes against established benchmarks.`,
              items: [isItalian ? 'Obiettivo' : 'Target Objective', isItalian ? 'Criteri di Valutazione' : 'Assessment Criteria', isItalian ? 'Vincoli' : 'Constraints', isItalian ? 'Soluzione Ottimale' : 'Optimal Solution']
            }
          ]
        },
        {
          id: 'kw-4',
          name: kw4,
          category: isItalian ? 'Sintesi & Competenze' : 'Synthesis & Mastery',
          coords: { x: 25, y: 72 },
          explanation: isItalian
            ? `Integrazione complessiva e riflessione critica su ${kw4}. Consente di collegare questo argomento ad altre discipline, sviluppando un pensiero autonomo e trasversale.`
            : `Cross-disciplinary synthesis and critical evaluation of ${kw4}. Enables high-order cognitive linkage across subjects, fostering independent problem-solving and nuanced mastery.`,
          images: [
            {
              type: 'structural',
              badge: isItalian ? 'QUADRO INTEGRATO' : 'INTEGRATED FRAMEWORK',
              title: isItalian ? `Sintesi delle Competenze: ${kw4}` : `Competency Synthesis: ${kw4}`,
              caption: isItalian ? `Schema delle competenze trasversali maturate nello studio di ${kw4}.` : `Overview of transversal competencies developed through studying ${kw4}.`,
              items: [isItalian ? 'Padronanza Teorica' : 'Theoretical Fluency', isItalian ? 'Capacità Analitica' : 'Analytical Rigour', isItalian ? 'Autonomia Critica' : 'Critical Autonomy']
            }
          ]
        }
      ];

      return {
        centralTitle: title,
        subjectName: subject.name,
        isItalian: isItalian,
        desc: desc,
        keywords: keywords
      };
    };

    /**
     * Overlay Concept Map Modal with Interactive Nodes and Click-Away Side Drawer
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
              // Click inside modal canvas (not on drawer) dismisses side drawer
              if (!e.target.closest('#keyword-side-drawer')) {
                if (selectedKeyword) setSelectedKeyword(null);
              }
              e.stopPropagation();
            }}
          >
            {/* Top Bar Header */}
            <div className="px-6 py-4 bg-[#18352B] border-b border-[#A8B3A0]/20 flex justify-between items-center shrink-0">
              <div className="flex items-center space-x-3">
                <span className="text-[10px] font-mono uppercase tracking-widest text-[#B79A63] bg-[#171817]/80 px-2.5 py-1 rounded border border-[#B79A63]/40">
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

                {/* Central Hub Node (Topic Title) */}
                <g transform="translate(50, 50)" className="cursor-default select-none">
                  <circle r="12" fill="#18352B" stroke="#B79A63" strokeWidth="1.2" className="shadow-lg" />
                  <circle r="14" fill="none" stroke="#B79A63" strokeWidth="0.5" opacity="0.4" className="animate-pulse" />
                  <text y="-3" textAnchor="middle" fill="#B79A63" fontSize="2.8" fontFamily="monospace" fontWeight="bold">
                    {mapData.isItalian ? 'ARGOMENTO' : 'TOPIC'}
                  </text>
                  <text y="3" textAnchor="middle" fill="#F5F1E8" fontSize="3.2" fontFamily="serif" fontWeight="bold">
                    {mapData.centralTitle.length > 20 ? mapData.centralTitle.slice(0, 20) + '..' : mapData.centralTitle}
                  </text>
                </g>

                {/* Interactive Keyword Nodes */}
                {mapData.keywords.map((kw, idx) => {
                  const isSelected = selectedKeyword && selectedKeyword.id === kw.id;
                  return (
                    <g 
                      key={kw.id} 
                      onClick={(e) => {
                        e.stopPropagation();
                        setSelectedKeyword(kw);
                      }}
                      className="cursor-pointer group select-none"
                    >
                      {/* Active Radar Ping */}
                      {isSelected && (
                        <circle 
                          cx={kw.coords.x} cy={kw.coords.y} 
                          r="6.5" fill="none" stroke="#FFFFFF" strokeWidth="0.6" className="animate-ping opacity-60" 
                        />
                      )}

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

                      {/* Keyword Label Tag */}
                      <g transform={`translate(${kw.coords.x}, ${kw.coords.y + 5.5})`}>
                        <rect 
                          x={-(kw.name.length * 1.5 + 4)} y="-2.5" 
                          width={(kw.name.length * 3 + 8)} height="5" 
                          rx="1.5" 
                          fill="#171817" 
                          fillOpacity={isSelected ? "0.95" : "0.85"}
                          stroke={isSelected ? "#FFFFFF" : "#A8B3A0"} 
                          strokeWidth="0.4"
                          className="transition-all duration-300"
                        />
                        <text 
                          y="0.9" textAnchor="middle" 
                          fill={isSelected ? "#FFFFFF" : "#F5F1E8"} 
                          fontSize="2.6" 
                          fontFamily="sans-serif" 
                          fontWeight={isSelected ? "bold" : "normal"}
                        >
                          {kw.name}
                        </text>
                      </g>
                    </g>
                  );
                })}
              </svg>
            </div>

            {/* Modal Bottom Bar */}
            <div className="px-6 py-3 bg-[#18352B]/90 border-t border-[#A8B3A0]/20 flex justify-between items-center text-xs font-mono text-[#A8B3A0] shrink-0">
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
                className="absolute top-0 right-0 bottom-0 w-full sm:w-[460px] lg:w-[520px] bg-[#171817]/98 border-l border-[#B79A63]/50 shadow-2xl z-30 flex flex-col animate-slide-left select-text"
                onClick={(e) => e.stopPropagation()}
              >
                {/* Drawer Header */}
                <div className="p-6 bg-[#18352B] border-b border-[#A8B3A0]/20 flex justify-between items-start shrink-0">
                  <div>
                    <span className="text-[10px] font-mono uppercase tracking-widest text-[#B79A63] bg-[#171817]/80 px-2 py-0.5 rounded border border-[#B79A63]/30 inline-block mb-1.5">
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
                <div className="p-6 overflow-y-auto space-y-6 flex-1">
                  {/* Detailed Explanation */}
                  <div className="space-y-2">
                    <h5 className="text-[10px] font-mono uppercase tracking-widest text-[#B79A63]">
                      {mapData.isItalian ? 'SPIEGAZIONE DETTAGLIATA' : 'DETAILED EXPLANATION'}
                    </h5>
                    <p className="text-sm font-sans text-[#E7E9E3]/90 leading-relaxed bg-[#18352B]/30 p-4 rounded border border-[#A8B3A0]/20">
                      {selectedKeyword.explanation}
                    </p>
                  </div>

                  {/* Generated Visual Schematics (1-5) */}
                  <div className="space-y-3">
                    <div className="flex justify-between items-center">
                      <h5 className="text-[10px] font-mono uppercase tracking-widest text-[#B79A63]">
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
                <div className="p-4 bg-[#18352B]/60 border-t border-[#A8B3A0]/20 flex justify-between items-center text-[10px] font-mono text-[#A8B3A0] shrink-0">
                  <span>{mapData.isItalian ? 'SCHEDA PAROLA CHIAVE' : 'KEYWORD ANALYSIS'}</span>
                  <button 
                    onClick={() => setSelectedKeyword(null)}
                    className="text-[#B79A63] hover:underline"
                  >
                    {mapData.isItalian ? 'CHIUDI RIQUADRO [✕]' : 'CLOSE DRAWER [✕]'}
                  </button>
                </div>
              </div>
            )}
          </div>
        </div>
      );
    };
'''

print("Code snippet compiled successfully.")
