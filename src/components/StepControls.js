// StepControls Component: Interactive Step-by-Step Playback Controls

window.StepControls = function({ currentStepIndex, totalSteps, onStepChange, isPlaying, onTogglePlay, playSpeed, setPlaySpeed }) {
  const isFirst = currentStepIndex === 0;
  const isLast = currentStepIndex === totalSteps - 1;

  return (
    <div className="step-control-bar">
      <div className="step-buttons">
        <button
          className="step-btn"
          onClick={() => onStepChange(0)}
          disabled={isFirst}
          title="First Step"
        >
          ⏮
        </button>
        <button
          className="step-btn"
          onClick={() => onStepChange(currentStepIndex - 1)}
          disabled={isFirst}
          title="Previous Step"
        >
          ◀
        </button>

        <button
          className="step-btn"
          style={{ background: isPlaying ? 'var(--accent-rose)' : 'var(--accent-blue)', color: '#0b0f19', fontWeight: 700 }}
          onClick={onTogglePlay}
          title={isPlaying ? 'Pause Animation' : 'Auto Play Steps'}
        >
          {isPlaying ? '⏸' : '▶'}
        </button>

        <button
          className="step-btn"
          onClick={() => onStepChange(currentStepIndex + 1)}
          disabled={isLast}
          title="Next Step"
        >
          ▶
        </button>
        <button
          className="step-btn"
          onClick={() => onStepChange(totalSteps - 1)}
          disabled={isLast}
          title="Final Solution"
        >
          ⏭
        </button>
      </div>

      <div className="step-progress-info">
        <div className="step-counter">
          <span>Step {currentStepIndex + 1} of {totalSteps}</span>
          <span style={{ color: 'var(--text-muted)' }}>
            {Math.round(((currentStepIndex + 1) / totalSteps) * 100)}% Completed
          </span>
        </div>
        <div className="progress-bar-track">
          <div
            className="progress-bar-fill"
            style={{ width: `${((currentStepIndex + 1) / totalSteps) * 100}%` }}
          />
        </div>
      </div>

      <div style={{ display: 'flex', alignItems: 'center', gap: '0.4rem', fontSize: '0.8rem', color: 'var(--text-secondary)' }}>
        <span>Speed:</span>
        <select
          value={playSpeed}
          onChange={(e) => setPlaySpeed(Number(e.target.value))}
          style={{
            background: 'var(--bg-card)',
            border: '1px solid var(--bg-card-border)',
            color: 'var(--text-primary)',
            padding: '0.25rem 0.5rem',
            borderRadius: '6px',
            cursor: 'pointer'
          }}
        >
          <option value={2000}>0.5x (2s)</option>
          <option value={1000}>1.0x (1s)</option>
          <option value={500}>2.0x (0.5s)</option>
        </select>
      </div>
    </div>
  );
};
