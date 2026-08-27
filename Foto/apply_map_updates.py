# Script to update IrishYearExperience with concept map modal triggers and state
with open(r'c:\Users\Enrico\Desktop\Giada\the_irish_year.html', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Add state and helper
old_state = """      // Overlay modal states
      const [modalSubject, setModalSubject] = useState(null);
      const [modalViewMode, setModalViewMode] = useState('overview'); // 'overview' | 'deepdive'
      const [hoveredPerson, setHoveredPerson] = useState(null);"""

new_state = """      // Overlay modal states
      const [modalSubject, setModalSubject] = useState(null);
      const [modalViewMode, setModalViewMode] = useState('overview'); // 'overview' | 'deepdive'
      const [hoveredPerson, setHoveredPerson] = useState(null);
      const [conceptMapData, setConceptMapData] = useState(null);

      // Open Concept Map helper
      const openConceptMap = (subject, topic) => {
        const map = getConceptMapForTopic(subject, topic, activeTab === 'italy');
        setConceptMapData(map);
      };"""

code = code.replace(old_state, new_state)

# 2. Update scroll lock
old_lock = """      // Lock background scroll when modal is open
      useEffect(() => {
        if (modalSubject) {
          const originalOverflow = document.body.style.overflow;
          document.body.style.overflow = 'hidden';
          return () => {
            document.body.style.overflow = originalOverflow;
          };
        } else {
          document.body.style.overflow = '';
        }
      }, [modalSubject]);"""

new_lock = """      // Lock background scroll when modal or concept map is open
      useEffect(() => {
        if (modalSubject || conceptMapData) {
          const originalOverflow = document.body.style.overflow;
          document.body.style.overflow = 'hidden';
          return () => {
            document.body.style.overflow = originalOverflow;
          };
        } else {
          document.body.style.overflow = '';
        }
      }, [modalSubject, conceptMapData]);"""

code = code.replace(old_lock, new_lock)

# 3. Update Section 07 Topics list on main page
old_topics_list = """                    {/* Topics List */}
                    <div className="mb-6">
                      <h4 className="text-xs font-mono uppercase text-[#D8CDBD] mb-3">
                        {activeTab === 'ireland' ? 'CURRICULAR TOPICS STUDIED:' : 'ARGOMENTI PRINCIPALI STUDIATI:'}
                      </h4>
                      <ul className="grid grid-cols-1 md:grid-cols-2 gap-2 text-sm text-[#E7E9E3]/80 font-sans">
                        {selectedSubject.topics.map((top, idx) => (
                          <li key={idx} className="flex items-start space-x-2">
                            <span className="text-[#B79A63] font-mono text-xs">•</span>
                            <span>{top}</span>
                          </li>
                        ))}
                      </ul>
                    </div>"""

new_topics_list = """                    {/* Topics List */}
                    <div className="mb-6">
                      <div className="flex justify-between items-center mb-3">
                        <h4 className="text-xs font-mono uppercase text-[#D8CDBD]">
                          {activeTab === 'ireland' ? 'CURRICULAR TOPICS STUDIED:' : 'ARGOMENTI PRINCIPALI STUDIATI:'}
                        </h4>
                        <span className="text-[10px] font-mono text-[#B79A63]">
                          {activeTab === 'ireland' ? '✨ Click topic for Concept Map' : '✨ Clicca per Mappa Concettuale'}
                        </span>
                      </div>
                      <ul className="grid grid-cols-1 md:grid-cols-2 gap-2 text-sm text-[#E7E9E3]/90 font-sans">
                        {(selectedSubject.detailedTopics || selectedSubject.topics).map((top, idx) => {
                          const topObj = typeof top === 'string' ? { title: top, desc: selectedSubject.summary } : top;
                          return (
                            <li 
                              key={idx} 
                              onClick={() => openConceptMap(selectedSubject, topObj)}
                              className="flex items-center justify-between p-2 rounded bg-[#171817]/60 hover:bg-[#18352B] border border-[#A8B3A0]/20 hover:border-[#B79A63]/60 cursor-pointer transition-all group"
                              title={activeTab === 'ireland' ? 'Click to open Concept Map' : 'Clicca per aprire la Mappa Concettuale'}
                            >
                              <div className="flex items-start space-x-2">
                                <span className="text-[#B79A63] font-mono text-xs">•</span>
                                <span className="group-hover:text-[#F5F1E8] transition-colors">{topObj.title || top}</span>
                              </div>
                              <span className="text-xs font-mono text-[#B79A63] opacity-60 group-hover:opacity-100 transition-opacity">🗺️</span>
                            </li>
                          );
                        })}
                      </ul>
                    </div>"""

code = code.replace(old_topics_list, new_topics_list)

# 4. Update Topic-by-Topic Breakdown in Subject Modal
old_modal_topics = """                      {/* Topic-by-Topic Breakdown Cards */}
                      <div className="space-y-4">
                        {modalSubject.detailedTopics && modalSubject.detailedTopics.map((item, dIdx) => (
                          <div 
                            key={dIdx} 
                            className="p-4 bg-[#171817]/60 border border-[#A8B3A0]/20 rounded-sm hover:border-[#B79A63]/50 transition-colors"
                          >
                            <div className="flex items-center space-x-2 mb-2">
                              <span className="text-[11px] font-mono text-[#B79A63] font-semibold">
                                {dIdx + 1 < 10 ? `0${dIdx + 1}` : dIdx + 1}.
                              </span>
                              <h5 className="font-serif text-lg text-[#F5F1E8] font-medium">
                                {item.title}
                              </h5>
                            </div>
                            <p className="text-xs md:text-sm font-sans text-[#E7E9E3]/85 leading-relaxed pl-6 border-l border-[#B79A63]/30">
                              {item.desc}
                            </p>
                          </div>
                        ))}
                      </div>"""

new_modal_topics = """                      {/* Topic-by-Topic Breakdown Cards */}
                      <div className="space-y-4">
                        {modalSubject.detailedTopics && modalSubject.detailedTopics.map((item, dIdx) => (
                          <div 
                            key={dIdx} 
                            className="p-5 bg-[#171817]/70 border border-[#A8B3A0]/20 rounded-sm hover:border-[#B79A63]/70 transition-all space-y-3 shadow-lg"
                          >
                            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-[#A8B3A0]/20 pb-2.5">
                              <div className="flex items-center space-x-2">
                                <span className="text-[11px] font-mono text-[#B79A63] font-semibold">
                                  {dIdx + 1 < 10 ? `0${dIdx + 1}` : dIdx + 1}.
                                </span>
                                <h5 
                                  onClick={() => openConceptMap(modalSubject, item)}
                                  className="font-serif text-lg text-[#F5F1E8] font-medium hover:text-[#B79A63] cursor-pointer transition-colors flex items-center space-x-1.5"
                                  title={activeTab === 'ireland' ? 'Click to open Concept Map' : 'Clicca per aprire la Mappa Concettuale'}
                                >
                                  <span>{item.title}</span>
                                  <span className="text-xs font-mono text-[#B79A63]">↗</span>
                                </h5>
                              </div>

                              {/* Button to open Concept Map & Generated Schematics */}
                              <button
                                onClick={() => openConceptMap(modalSubject, item)}
                                className="inline-flex items-center space-x-1.5 px-3 py-1.5 bg-[#B79A63]/20 hover:bg-[#B79A63] text-[#F5F1E8] hover:text-[#171817] border border-[#B79A63]/60 rounded-sm text-[11px] font-mono uppercase tracking-wider transition-colors shadow self-start sm:self-auto"
                              >
                                <span>🗺️</span>
                                <span>{activeTab === 'ireland' ? 'Concept Map & Schematics' : 'Mappa Concettuale & Schemi'}</span>
                                <span>&rarr;</span>
                              </button>
                            </div>

                            <p className="text-xs md:text-sm font-sans text-[#E7E9E3]/85 leading-relaxed pl-4 border-l-2 border-[#B79A63]/40">
                              {item.desc}
                            </p>
                          </div>
                        ))}
                      </div>"""

code = code.replace(old_modal_topics, new_modal_topics)

# 5. Render Concept Map Modal overlay at the end of the return statement
old_bottom = """          )}

        </div>
      );
    }"""

new_bottom = """          )}

          {/* ==================================================================== */}
          {/* OVERLAY: INTERACTIVE CONCEPT MAP & KEYWORD SCHEMATICS DRAWER         */}
          {/* ==================================================================== */}
          {conceptMapData && (
            <TopicConceptMapModal 
              mapData={conceptMapData} 
              onClose={() => setConceptMapData(null)} 
            />
          )}

        </div>
      );
    }"""

code = code.replace(old_bottom, new_bottom)

with open(r'c:\Users\Enrico\Desktop\Giada\the_irish_year.html', 'w', encoding='utf-8') as f:
    f.write(code)

print("Applied all concept map updates successfully.")
