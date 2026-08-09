// Main Application Engine & Root React Component

function App() {
  const [activeTopic, setActiveTopic] = React.useState('lpp');
  const [selectedProblem, setSelectedProblem] = React.useState(() => {
    return window.TEXTBOOK_PROBLEMS.lpp[0];
  });

  const [currentStepIndex, setCurrentStepIndex] = React.useState(0);
  const [isPlaying, setIsPlaying] = React.useState(false);
  const [playSpeed, setPlaySpeed] = React.useState(1000);

  const [isQuizMode, setIsQuizMode] = React.useState(false);
  const [theme, setTheme] = React.useState('light');

  const [modalData, setModalData] = React.useState(null);
  const [isModalOpen, setIsModalOpen] = React.useState(false);
  const [isCustomModalOpen, setIsCustomModalOpen] = React.useState(false);

  const [customProblems, setCustomProblems] = React.useState([]);

  // Ensure default HTML data-theme attribute is light
  React.useEffect(() => {
    document.documentElement.setAttribute('data-theme', theme);
  }, [theme]);

  // Compute Total Steps for current active module solver
  const totalSteps = React.useMemo(() => {
    if (!selectedProblem) return 1;
    let stepsCount = 1;
    if (activeTopic === 'lpp') {
      const res = window.solveLPPSimplex(selectedProblem);
      stepsCount = res.steps.length;
    } else if (activeTopic === 'transportation') {
      const res = window.solveTransportation(selectedProblem, 'VAM');
      stepsCount = res.steps.length;
    } else if (activeTopic === 'assignment') {
      const res = window.solveAssignment(selectedProblem);
      stepsCount = res.steps.length;
    } else if (activeTopic === 'shortestPath') {
      const res = window.solveShortestPath(selectedProblem);
      stepsCount = res.steps.length;
    } else if (activeTopic === 'mst') {
      const res = window.solveMST(selectedProblem, 'Kruskal');
      stepsCount = res.steps.length;
    }
    return Math.max(1, stepsCount);
  }, [activeTopic, selectedProblem]);

  // Handle Step Auto-Play Animation Interval
  React.useEffect(() => {
    let timer = null;
    if (isPlaying) {
      timer = setInterval(() => {
        setCurrentStepIndex(prev => {
          if (prev >= totalSteps - 1) {
            setIsPlaying(false);
            return prev;
          }
          return prev + 1;
        });
      }, playSpeed);
    }
    return () => { if (timer) clearInterval(timer); };
  }, [isPlaying, totalSteps, playSpeed]);

  // Reset Step Index when problem or topic changes
  const handleSelectProblem = (prob) => {
    setSelectedProblem(prob);
    setCurrentStepIndex(0);
    setIsPlaying(false);
  };

  const handleCellClick = (data) => {
    setModalData(data);
    setIsModalOpen(true);
  };

  const toggleTheme = () => {
    const nextTheme = theme === 'dark' ? 'light' : 'dark';
    setTheme(nextTheme);
    document.documentElement.setAttribute('data-theme', nextTheme);
  };

  const availableProblems = [
    ...(window.TEXTBOOK_PROBLEMS[activeTopic] || []),
    ...customProblems.filter(p => p.id.includes(activeTopic))
  ];

  return (
    <div className="app-container">
      <window.Header
        activeTopic={activeTopic}
        setActiveTopic={(t) => {
          setActiveTopic(t);
          setCurrentStepIndex(0);
          setIsPlaying(false);
          const probs = [
            ...(window.TEXTBOOK_PROBLEMS[t] || []),
            ...customProblems.filter(p => p.id.includes(t))
          ];
          if (probs.length > 0) setSelectedProblem(probs[0]);
        }}
        selectedProblem={selectedProblem}
        setSelectedProblem={handleSelectProblem}
        onOpenCustomInput={() => setIsCustomModalOpen(true)}
        isQuizMode={isQuizMode}
        setIsQuizMode={setIsQuizMode}
        theme={theme}
        toggleTheme={toggleTheme}
      />

      {isQuizMode ? (
        <div style={{ padding: '1.5rem', flex: 1 }}>
          <window.QuizModeView />
        </div>
      ) : (
        <main className="workspace">
          {/* Sidebar Problem Repository Panel */}
          <aside className="sidebar-panel">
            <div className="card">
              <h3 className="card-title">
                <span>📚</span> Problem Repository ({availableProblems.length})
              </h3>
              <div className="problem-selector-list">
                {availableProblems.map(prob => (
                  <div
                    key={prob.id}
                    className={`problem-card ${selectedProblem && selectedProblem.id === prob.id ? 'active' : ''}`}
                    onClick={() => handleSelectProblem(prob)}
                  >
                    <h4>{prob.title}</h4>
                    <p>{prob.description}</p>
                    <span className="source-badge">{prob.source}</span>
                  </div>
                ))}
              </div>
            </div>

            {/* Problem Overview Card */}
            {selectedProblem && (
              <div className="card">
                <h3 className="card-title">
                  <span>⚙️</span> Problem Formulation
                </h3>
                <div style={{ fontSize: '0.85rem', color: 'var(--text-primary)', lineHeight: 1.5 }}>
                  <p style={{ marginBottom: '0.5rem' }}>{selectedProblem.description}</p>
                  {selectedProblem.objective && (
                    <div style={{ background: 'rgba(2, 132, 199, 0.06)', padding: '0.5rem', borderRadius: '6px', fontFamily: 'var(--font-family-mono)', color: 'var(--accent-blue)', marginTop: '0.4rem', border: '1px solid rgba(2, 132, 199, 0.2)' }}>
                      <strong>{selectedProblem.objectiveType ? selectedProblem.objectiveType.toUpperCase() : 'MAX'} Z:</strong> {selectedProblem.objective[0]}x₁ + {selectedProblem.objective[1]}x₂
                    </div>
                  )}
                  {selectedProblem.supply && (
                    <div style={{ fontSize: '0.8rem', color: 'var(--text-secondary)', marginTop: '0.4rem' }}>
                      Supply: [{selectedProblem.supply.join(', ')}] | Demand: [{selectedProblem.demand.join(', ')}]
                    </div>
                  )}
                </div>
              </div>
            )}
          </aside>

          {/* Visualization Workspace Panel */}
          <section className="visualizer-panel">
            <window.StepControls
              currentStepIndex={currentStepIndex}
              totalSteps={totalSteps}
              onStepChange={setCurrentStepIndex}
              isPlaying={isPlaying}
              onTogglePlay={() => setIsPlaying(!isPlaying)}
              playSpeed={playSpeed}
              setPlaySpeed={setPlaySpeed}
            />

            {/* Active Topic View Rendering */}
            {activeTopic === 'lpp' && selectedProblem && (
              <window.LPPView
                problem={selectedProblem}
                currentStepIndex={currentStepIndex}
                onCellClick={handleCellClick}
              />
            )}

            {activeTopic === 'transportation' && selectedProblem && (
              <window.TransportationView
                problem={selectedProblem}
                currentStepIndex={currentStepIndex}
                onCellClick={handleCellClick}
              />
            )}

            {activeTopic === 'assignment' && selectedProblem && (
              <window.AssignmentView
                problem={selectedProblem}
                currentStepIndex={currentStepIndex}
                onCellClick={handleCellClick}
              />
            )}

            {activeTopic === 'shortestPath' && selectedProblem && (
              <window.ShortestPathView
                problem={selectedProblem}
                currentStepIndex={currentStepIndex}
                onCellClick={handleCellClick}
              />
            )}

            {activeTopic === 'mst' && selectedProblem && (
              <window.MSTView
                problem={selectedProblem}
                currentStepIndex={currentStepIndex}
                onCellClick={handleCellClick}
              />
            )}
          </section>
        </main>
      )}

      {/* Inspection Modal Overlay */}
      <window.InspectionModal
        isOpen={isModalOpen}
        onClose={() => setIsModalOpen(false)}
        data={modalData}
      />

      {/* Custom Problem Input Modal */}
      <window.CustomInputModal
        isOpen={isCustomModalOpen}
        onClose={() => setIsCustomModalOpen(false)}
        activeTopic={activeTopic}
        onSaveCustomProblem={(newProb) => {
          setCustomProblems([...customProblems, newProb]);
          setSelectedProblem(newProb);
          setCurrentStepIndex(0);
        }}
      />
    </div>
  );
}

// Render Root
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);
