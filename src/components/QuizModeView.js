// QuizModeView Component: Interactive Self-Assessment Quiz for MBA/PGDM Students

window.QuizModeView = function() {
  const quizQuestions = [
    {
      id: 1,
      topic: 'Linear Programming (LPP)',
      question: 'In the Simplex Method for a Maximization problem, when is the current basic feasible solution optimal?',
      options: [
        'A) All Cj - Zj indicators are positive (> 0)',
        'B) All Cj - Zj indicators are non-positive (≤ 0)',
        'C) When slack variables equal zero',
        'D) When artificial variables enter the basis'
      ],
      correctAnswer: 1,
      explanation: 'Optimality Criterion: For a maximization problem, if all net evaluations Cj - Zj ≤ 0, no non-basic variable can enter the basis to increase Z further.'
    },
    {
      id: 2,
      topic: 'Transportation Problem',
      question: 'In Vogel\'s Approximation Method (VAM), how is the row/column penalty calculated?',
      options: [
        'A) Maximum cost minus minimum cost in that line',
        'B) Difference between the two lowest costs in that row or column',
        'C) Average of all costs in that row or column',
        'D) Total supply minus total demand'
      ],
      correctAnswer: 1,
      explanation: 'VAM penalties represent opportunity loss: the difference between the lowest unit cost and the next lowest unit cost in a line.'
    },
    {
      id: 3,
      topic: 'Transportation Problem (MODI)',
      question: 'In the u-v (MODI) method, an unallocated cell has opportunity cost Δij = cij - (ui + vj). If Δij < 0 for a cell in a minimization problem, what does it signify?',
      options: [
        'A) The current solution is optimal',
        'B) Allocating units to this cell will INCREASE total shipping cost',
        'C) Allocating units to this cell will DECREASE total shipping cost',
        'D) The problem is degenerate'
      ],
      correctAnswer: 2,
      explanation: 'In MODI, a negative opportunity cost Δij < 0 indicates that introducing this route will reduce total transportation cost.'
    },
    {
      id: 4,
      topic: 'Assignment Problem',
      question: 'In the Hungarian Method for an N×N cost matrix, when is the current matrix optimal?',
      options: [
        'A) When every row has at least two zeros',
        'B) When minimum lines needed to cover all zeros equals N',
        'C) When all entries in the matrix are non-negative',
        'D) When all diagonal elements equal zero'
      ],
      correctAnswer: 1,
      explanation: 'König\'s theorem: Maximum number of independent zero assignments equals the minimum number of lines covering all zeros. When lines = N, a complete 1-to-1 optimal assignment exists.'
    },
    {
      id: 5,
      topic: 'Network Models (MST vs Shortest Path)',
      question: 'What is the primary distinction between a Minimum Spanning Tree (MST) and a Shortest Path between two nodes?',
      options: [
        'A) MST minimizes total edge weight connecting ALL nodes; Shortest Path minimizes weight along a path between a specific SOURCE and TARGET',
        'B) MST allows cycles; Shortest Path is strictly acyclic',
        'C) Dijkstra algorithm solves MST; Kruskal solves Shortest Path',
        'D) MST requires directed graphs; Shortest Path requires undirected graphs'
      ],
      correctAnswer: 0,
      explanation: 'MST spans the entire graph with minimum total weight. Shortest path optimizes distance between a specific pair of nodes.'
    }
  ];

  const [currentQ, setCurrentQ] = React.useState(0);
  const [selectedOpt, setSelectedOpt] = React.useState(null);
  const [score, setScore] = React.useState(0);
  const [showResult, setShowResult] = React.useState(false);

  const q = quizQuestions[currentQ];

  const handleSelectOption = (idx) => {
    if (selectedOpt !== null) return; // Prevent re-click
    setSelectedOpt(idx);
    if (idx === q.correctAnswer) {
      setScore(score + 1);
    }
  };

  const handleNext = () => {
    if (currentQ < quizQuestions.length - 1) {
      setCurrentQ(currentQ + 1);
      setSelectedOpt(null);
    } else {
      setShowResult(true);
    }
  };

  const handleRestart = () => {
    setCurrentQ(0);
    setSelectedOpt(null);
    setScore(0);
    setShowResult(false);
  };

  if (showResult) {
    return (
      <div className="card" style={{ maxWidth: '700px', margin: '2rem auto', textAlign: 'center' }}>
        <h2 style={{ color: 'var(--accent-blue)', marginBottom: '1rem' }}>🎉 Quiz Completed!</h2>
        <div style={{ fontSize: '2.5rem', fontWeight: 800, color: 'var(--accent-emerald)', margin: '1rem 0' }}>
          {score} / {quizQuestions.length}
        </div>
        <p style={{ color: 'var(--text-secondary)', marginBottom: '1.5rem' }}>
          {score === quizQuestions.length
            ? '🏆 Outstanding! Perfect score in Operations Research concepts.'
            : score >= 3
            ? '👍 Great effort! Review step-by-step solver explanations to master remaining concepts.'
            : '📚 Keep practicing! Use the step-by-step guide to review algorithms.'}
        </p>
        <button className="action-btn primary" style={{ margin: '0 auto' }} onClick={handleRestart}>
          Try Quiz Again
        </button>
      </div>
    );
  }

  return (
    <div className="card" style={{ maxWidth: '800px', margin: '1rem auto' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem', borderBottom: '1px solid var(--bg-card-border)', paddingBottom: '0.5rem' }}>
        <span className="source-badge">Concept Quiz {currentQ + 1} of {quizQuestions.length}</span>
        <span style={{ fontSize: '0.85rem', color: 'var(--accent-indigo)', fontWeight: 600 }}>{q.topic}</span>
      </div>

      <h3 style={{ fontSize: '1.1rem', marginBottom: '1.25rem', color: 'var(--text-primary)', lineHeight: 1.5 }}>
        {q.question}
      </h3>

      <div style={{ display: 'flex', flexDirection: 'column', gap: '0.6rem', marginBottom: '1.25rem' }}>
        {q.options.map((opt, idx) => {
          let stateClass = '';
          if (selectedOpt !== null) {
            if (idx === q.correctAnswer) stateClass = 'correct';
            else if (idx === selectedOpt) stateClass = 'wrong';
          }
          return (
            <button
              key={idx}
              className={`quiz-option-btn ${stateClass}`}
              onClick={() => handleSelectOption(idx)}
            >
              {opt}
            </button>
          );
        })}
      </div>

      {selectedOpt !== null && (
        <div style={{ background: 'rgba(56, 189, 248, 0.1)', border: '1px solid var(--accent-blue)', borderRadius: '8px', padding: '0.9rem', marginBottom: '1rem' }}>
          <div style={{ fontWeight: 700, color: selectedOpt === q.correctAnswer ? 'var(--accent-emerald)' : 'var(--accent-rose)', marginBottom: '0.3rem' }}>
            {selectedOpt === q.correctAnswer ? '✅ Correct Answer!' : '❌ Incorrect'}
          </div>
          <div style={{ fontSize: '0.85rem', color: 'var(--text-primary)' }}>
            {q.explanation}
          </div>
        </div>
      )}

      {selectedOpt !== null && (
        <div style={{ display: 'flex', justifyContent: 'flex-end' }}>
          <button className="action-btn primary" onClick={handleNext}>
            {currentQ < quizQuestions.length - 1 ? 'Next Question ▶' : 'See Results 🏆'}
          </button>
        </div>
      )}
    </div>
  );
};
