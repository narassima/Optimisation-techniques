// InspectionModal Component: Click-to-Explain Detailed Educational Modal

window.InspectionModal = function({ isOpen, onClose, data }) {
  if (!isOpen || !data) return null;

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content" onClick={(e) => e.stopPropagation()}>
        <div className="modal-header">
          <h3 style={{ color: 'var(--accent-blue)', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
            <span>💡</span> {data.title || 'Interactive Step Explanation'}
          </h3>
          <button className="modal-close-btn" onClick={onClose}>✕</button>
        </div>

        <div style={{ display: 'flex', flexDirection: 'column', gap: '0.8rem' }}>
          {data.formula && (
            <div className="formula-box">
              <strong>Formula / Rule:</strong>
              <div>{data.formula}</div>
            </div>
          )}

          <div style={{ fontSize: '0.95rem', color: 'var(--text-primary)', lineHeight: 1.6 }}>
            {data.description}
          </div>

          {data.calculation && (
            <div style={{ background: 'rgba(255,255,255,0.04)', padding: '0.75rem', borderRadius: '8px', border: '1px solid var(--bg-card-border)', fontFamily: 'var(--font-family-mono)', fontSize: '0.85rem' }}>
              <div style={{ color: 'var(--accent-amber)', fontWeight: 600, marginBottom: '0.3rem' }}>Step-by-Step Math Derivation:</div>
              <div>{data.calculation}</div>
            </div>
          )}

          {data.textbookNote && (
            <div style={{ fontSize: '0.8rem', color: 'var(--text-muted)', fontStyle: 'italic', borderTop: '1px dashed var(--bg-card-border)', paddingTop: '0.5rem' }}>
              📚 <strong>Textbook Context:</strong> {data.textbookNote}
            </div>
          )}
        </div>

        <div style={{ display: 'flex', justifyContent: 'flex-end', marginTop: '0.5rem' }}>
          <button className="action-btn primary" onClick={onClose}>
            Got it!
          </button>
        </div>
      </div>
    </div>
  );
};
