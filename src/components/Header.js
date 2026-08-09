// Header Component: Navigation, Textbook Problem Switcher, Custom Input, Quiz Mode & Theme Toggle

window.Header = function({ activeTopic, setActiveTopic, selectedProblem, setSelectedProblem, onOpenCustomInput, isQuizMode, setIsQuizMode, theme, toggleTheme }) {
  const topics = [
    { id: 'lpp', label: 'Linear Programming (LPP)', icon: 'bar-chart-3', color: 'var(--color-lpp)' },
    { id: 'transportation', label: 'Transportation Problem', icon: 'truck', color: 'var(--color-transport)' },
    { id: 'assignment', label: 'Assignment Problem', icon: 'users', color: 'var(--color-assign)' },
    { id: 'shortestPath', label: 'Shortest Path', icon: 'navigation', color: 'var(--color-shortest)' },
    { id: 'mst', label: 'Minimum Spanning Tree', icon: 'git-merge', color: 'var(--color-mst)' }
  ];

  const currentProblems = window.TEXTBOOK_PROBLEMS[activeTopic] || [];

  return (
    <header className="main-header">
      <div className="brand-section">
        <div className="brand-icon">OR</div>
        <div className="brand-title">
          <h1>Optimization Learning Hub</h1>
          <p>Great Lakes PGDM / MBA Interactive Guide</p>
        </div>
      </div>

      <nav className="nav-tabs">
        {topics.map(t => (
          <button
            key={t.id}
            className={`nav-tab-btn ${activeTopic === t.id && !isQuizMode ? 'active' : ''}`}
            onClick={() => {
              setActiveTopic(t.id);
              setIsQuizMode(false);
              if (window.TEXTBOOK_PROBLEMS[t.id]) {
                setSelectedProblem(window.TEXTBOOK_PROBLEMS[t.id][0]);
              }
            }}
          >
            <span>{t.label}</span>
          </button>
        ))}
      </nav>

      <div className="header-actions">
        <button
          className={`action-btn ${isQuizMode ? 'primary' : ''}`}
          onClick={() => setIsQuizMode(!isQuizMode)}
          title="Self-Assessment Quiz Mode"
        >
          <span>🎯 Practice Quiz</span>
        </button>

        <button
          className="action-btn"
          onClick={onOpenCustomInput}
          title="Create Custom Problem"
        >
          <span>➕ Custom Input</span>
        </button>

        <button
          className="action-btn"
          onClick={toggleTheme}
          title="Toggle Light/Dark Theme"
        >
          <span>{theme === 'dark' ? '☀️ Light' : '🌙 Dark'}</span>
        </button>
      </div>
    </header>
  );
};
