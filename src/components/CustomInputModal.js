// CustomInputModal Component: Ultra-Easy Student Problem Builder with Visual Grid & Templates

window.CustomInputModal = function({ isOpen, onClose, activeTopic, onSaveCustomProblem }) {
  if (!isOpen) return null;

  const [title, setTitle] = React.useState('Student Custom Problem');
  const [template, setTemplate] = React.useState('custom');

  // LPP visual state
  const [lppObjType, setLppObjType] = React.useState('max');
  const [c1, setC1] = React.useState(40);
  const [c2, setC2] = React.useState(50);
  const [var1Name, setVar1Name] = React.useState('x1 (Chairs)');
  const [var2Name, setVar2Name] = React.useState('x2 (Tables)');

  const [rows, setRows] = React.useState([
    { name: 'Raw Material', a: 1, b: 1, type: '<=', rhs: 64 },
    { name: 'Labor Hours', a: 3, b: 1, type: '<=', rhs: 120 },
    { name: 'Machine Capacity', a: 1, b: 0, type: '<=', rhs: 28 }
  ]);

  // Transportation state
  const [transSupply, setTransSupply] = React.useState('1000, 1500, 1200');
  const [transDemand, setTransDemand] = React.useState('2300, 1400');
  const [transCosts, setTransCosts] = React.useState('80, 215\n100, 108\n102, 68');

  // Assignment state
  const [assignCosts, setAssignCosts] = React.useState('13, 16, 12, 11\n15, 99, 13, 20\n5, 7, 10, 6\n0, 0, 0, 0');

  // Load Preset Templates
  const handleTemplateChange = (tplKey) => {
    setTemplate(tplKey);
    if (tplKey === 'chair-table') {
      setTitle('Product Mix: Chairs & Tables');
      setLppObjType('max');
      setC1(40); setC2(50);
      setVar1Name('x1 (Chairs)'); setVar2Name('x2 (Tables)');
      setRows([
        { name: 'Raw Material Availability', a: 1, b: 1, type: '<=', rhs: 64 },
        { name: 'Labor Hours', a: 3, b: 1, type: '<=', rhs: 120 },
        { name: 'Machine Capacity', a: 1, b: 0, type: '<=', rhs: 28 }
      ]);
    } else if (tplKey === 'diet') {
      setTitle('Diet Mix: Corn & Soybean');
      setLppObjType('min');
      setC1(0.30); setC2(0.90);
      setVar1Name('x1 (Corn lbs)'); setVar2Name('x2 (Soybean Meal lbs)');
      setRows([
        { name: 'Min Weight', a: 1, b: 1, type: '>=', rhs: 800 },
        { name: 'Min Protein (30%)', a: -0.21, b: 0.30, type: '>=', rhs: 0 },
        { name: 'Max Fiber (5%)', a: -0.03, b: 0.01, type: '<=', rhs: 0 }
      ]);
    }
  };

  const handleAddRow = () => {
    setRows([...rows, { name: `Constraint ${rows.length + 1}`, a: 1, b: 1, type: '<=', rhs: 50 }]);
  };

  const handleRemoveRow = (idx) => {
    setRows(rows.filter((_, i) => i !== idx));
  };

  const handleRowChange = (idx, field, val) => {
    const nextRows = [...rows];
    nextRows[idx][field] = val;
    setRows(nextRows);
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    if (activeTopic === 'lpp') {
      const parsedConstraints = rows.map(r => ({
        coeffs: [parseFloat(r.a) || 0, parseFloat(r.b) || 0],
        type: r.type,
        rhs: parseFloat(r.rhs) || 0,
        name: `${r.name} (${r.a}*x1 + ${r.b}*x2 ${r.type} ${r.rhs})`
      }));

      onSaveCustomProblem({
        id: `custom-lpp-${Date.now()}`,
        title: title || 'Student Custom LPP',
        source: 'Interactive Student Builder',
        description: 'Student-formulated Linear Programming Model',
        objectiveType: lppObjType,
        objective: [parseFloat(c1) || 0, parseFloat(c2) || 0],
        variables: [var1Name, var2Name],
        constraints: parsedConstraints
      });
    } else if (activeTopic === 'transportation') {
      const supply = transSupply.split(',').map(v => parseFloat(v.trim()) || 0);
      const demand = transDemand.split(',').map(v => parseFloat(v.trim()) || 0);
      const costs = transCosts.split('\n').filter(l => l.trim()).map(l => l.split(',').map(v => parseFloat(v.trim()) || 0));

      onSaveCustomProblem({
        id: `custom-trans-${Date.now()}`,
        title: title || 'Custom Transportation Problem',
        source: 'Interactive Student Builder',
        description: 'Student-formulated Transportation Problem',
        sources: supply.map((_, i) => `Plant / Source ${i + 1}`),
        destinations: demand.map((_, i) => `Dest / Center ${i + 1}`),
        supply,
        demand,
        costs
      });
    } else if (activeTopic === 'assignment') {
      const costs = assignCosts.split('\n').filter(l => l.trim()).map(l => l.split(',').map(v => parseFloat(v.trim()) || 0));
      const N = costs.length;

      onSaveCustomProblem({
        id: `custom-assign-${Date.now()}`,
        title: title || 'Custom Assignment Problem',
        source: 'Interactive Student Builder',
        description: 'Student-formulated Assignment Problem',
        agents: Array.from({ length: N }, (_, i) => `Agent / Machine ${i + 1}`),
        tasks: Array.from({ length: N }, (_, i) => `Task / Location ${i + 1}`),
        costs
      });
    }

    onClose();
  };

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content" style={{ maxWidth: '780px' }} onClick={(e) => e.stopPropagation()}>
        <div className="modal-header">
          <h3 style={{ color: 'var(--accent-blue)', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
            <span>✏️</span> Interactive Student Problem Builder ({activeTopic.toUpperCase()})
          </h3>
          <button className="modal-close-btn" onClick={onClose}>✕</button>
        </div>

        <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
          {/* Quick Preset Selector */}
          {activeTopic === 'lpp' && (
            <div style={{ background: 'rgba(2, 132, 199, 0.06)', padding: '0.75rem', borderRadius: '8px', border: '1px solid rgba(2, 132, 199, 0.2)' }}>
              <label style={{ fontSize: '0.85rem', fontWeight: 600, color: 'var(--accent-blue)', display: 'block', marginBottom: '0.3rem' }}>
                🚀 Load Class Template (Quick Start):
              </label>
              <select
                value={template}
                onChange={(e) => handleTemplateChange(e.target.value)}
                style={{ width: '100%', padding: '0.5rem', background: 'var(--bg-surface)', border: '1px solid var(--bg-card-border)', color: 'var(--text-primary)', borderRadius: '6px', cursor: 'pointer' }}
              >
                <option value="custom">Blank Custom Problem</option>
                <option value="chair-table">Factory Chair & Table (OTDM Class Example)</option>
                <option value="diet">Diet Mix Problem (Corn & Soybean)</option>
              </select>
            </div>
          )}

          <div>
            <label style={{ fontSize: '0.85rem', color: 'var(--text-secondary)', display: 'block', marginBottom: '0.2rem' }}>
              Problem Title:
            </label>
            <input
              type="text"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              style={{ width: '100%', padding: '0.5rem', background: 'var(--bg-surface)', border: '1px solid var(--bg-card-border)', color: 'var(--text-primary)', borderRadius: '6px' }}
            />
          </div>

          {activeTopic === 'lpp' && (
            <>
              {/* Objective Function Row */}
              <div style={{ background: 'rgba(15,23,42,0.03)', padding: '0.8rem', borderRadius: '8px', border: '1px solid var(--bg-card-border)' }}>
                <label style={{ fontSize: '0.85rem', fontWeight: 600, color: 'var(--text-primary)', display: 'block', marginBottom: '0.4rem' }}>
                  Objective Function:
                </label>
                <div style={{ display: 'flex', alignItems: 'center', gap: '0.6rem' }}>
                  <select
                    value={lppObjType}
                    onChange={(e) => setLppObjType(e.target.value)}
                    style={{ padding: '0.5rem', background: 'var(--bg-surface)', border: '1px solid var(--bg-card-border)', color: 'var(--text-primary)', borderRadius: '6px', fontWeight: 700 }}
                  >
                    <option value="max">Maximize Z =</option>
                    <option value="min">Minimize Z =</option>
                  </select>
                  <input
                    type="number" step="any"
                    value={c1} onChange={(e) => setC1(e.target.value)}
                    style={{ width: '70px', padding: '0.5rem', background: 'var(--bg-surface)', border: '1px solid var(--bg-card-border)', color: 'var(--text-primary)', borderRadius: '6px', textAlign: 'center' }}
                  />
                  <span>x₁ +</span>
                  <input
                    type="number" step="any"
                    value={c2} onChange={(e) => setC2(e.target.value)}
                    style={{ width: '70px', padding: '0.5rem', background: 'var(--bg-surface)', border: '1px solid var(--bg-card-border)', color: 'var(--text-primary)', borderRadius: '6px', textAlign: 'center' }}
                  />
                  <span>x₂</span>
                </div>
              </div>

              {/* Variable Names */}
              <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '0.75rem' }}>
                <div>
                  <label style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>Variable x₁ Name:</label>
                  <input
                    type="text" value={var1Name} onChange={(e) => setVar1Name(e.target.value)}
                    style={{ width: '100%', padding: '0.4rem', background: 'var(--bg-surface)', border: '1px solid var(--bg-card-border)', color: 'var(--text-primary)', borderRadius: '6px' }}
                  />
                </div>
                <div>
                  <label style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>Variable x₂ Name:</label>
                  <input
                    type="text" value={var2Name} onChange={(e) => setVar2Name(e.target.value)}
                    style={{ width: '100%', padding: '0.4rem', background: 'var(--bg-surface)', border: '1px solid var(--bg-card-border)', color: 'var(--text-primary)', borderRadius: '6px' }}
                  />
                </div>
              </div>

              {/* Interactive Resource Constraints Grid */}
              <div>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '0.4rem' }}>
                  <label style={{ fontSize: '0.85rem', fontWeight: 600, color: 'var(--text-primary)' }}>
                    Resource Constraints Table:
                  </label>
                  <button type="button" className="action-btn" onClick={handleAddRow} style={{ fontSize: '0.75rem', padding: '0.2rem 0.5rem' }}>
                    + Add Constraint Row
                  </button>
                </div>

                <div className="matrix-container">
                  <table className="custom-table" style={{ fontSize: '0.85rem' }}>
                    <thead>
                      <tr>
                        <th>Resource Name</th>
                        <th>x₁ Coeff (a)</th>
                        <th>x₂ Coeff (b)</th>
                        <th>Type</th>
                        <th>RHS (b_i)</th>
                        <th>Action</th>
                      </tr>
                    </thead>
                    <tbody>
                      {rows.map((r, idx) => (
                        <tr key={idx}>
                          <td>
                            <input
                              type="text" value={r.name} onChange={(e) => handleRowChange(idx, 'name', e.target.value)}
                              style={{ width: '100%', padding: '0.3rem', background: 'transparent', border: 'none', color: 'var(--text-primary)', fontWeight: 600 }}
                            />
                          </td>
                          <td>
                            <input
                              type="number" step="any" value={r.a} onChange={(e) => handleRowChange(idx, 'a', e.target.value)}
                              style={{ width: '60px', padding: '0.3rem', background: 'transparent', border: 'none', textAlign: 'center', color: 'var(--text-primary)' }}
                            />
                          </td>
                          <td>
                            <input
                              type="number" step="any" value={r.b} onChange={(e) => handleRowChange(idx, 'b', e.target.value)}
                              style={{ width: '60px', padding: '0.3rem', background: 'transparent', border: 'none', textAlign: 'center', color: 'var(--text-primary)' }}
                            />
                          </td>
                          <td>
                            <select
                              value={r.type} onChange={(e) => handleRowChange(idx, 'type', e.target.value)}
                              style={{ padding: '0.2rem', background: 'transparent', border: 'none', color: 'var(--text-primary)', fontWeight: 700 }}
                            >
                              <option value="<=">&le; (<=)</option>
                              <option value=">=">&ge; (>=)</option>
                              <option value="=">= (=)</option>
                            </select>
                          </td>
                          <td>
                            <input
                              type="number" step="any" value={r.rhs} onChange={(e) => handleRowChange(idx, 'rhs', e.target.value)}
                              style={{ width: '70px', padding: '0.3rem', background: 'transparent', border: 'none', textAlign: 'center', color: 'var(--accent-amber)', fontWeight: 700 }}
                            />
                          </td>
                          <td>
                            {rows.length > 1 && (
                              <button type="button" onClick={() => handleRemoveRow(idx)} style={{ background: 'transparent', border: 'none', color: 'var(--accent-rose)', cursor: 'pointer', fontWeight: 800 }}>
                                ✕
                              </button>
                            )}
                          </td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              </div>
            </>
          )}

          {activeTopic === 'transportation' && (
            <>
              <div>
                <label style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>Plant Capacities / Supply (Comma-separated):</label>
                <input
                  type="text" value={transSupply} onChange={(e) => setTransSupply(e.target.value)}
                  style={{ width: '100%', padding: '0.5rem', background: 'var(--bg-surface)', border: '1px solid var(--bg-card-border)', color: 'var(--text-primary)', borderRadius: '6px' }}
                />
              </div>

              <div>
                <label style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>Distribution Demands (Comma-separated):</label>
                <input
                  type="text" value={transDemand} onChange={(e) => setTransDemand(e.target.value)}
                  style={{ width: '100%', padding: '0.5rem', background: 'var(--bg-surface)', border: '1px solid var(--bg-card-border)', color: 'var(--text-primary)', borderRadius: '6px' }}
                />
              </div>

              <div>
                <label style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>Transportation Costs Matrix (Rows by line, comma-separated):</label>
                <textarea
                  rows={3} value={transCosts} onChange={(e) => setTransCosts(e.target.value)}
                  style={{ width: '100%', padding: '0.5rem', background: 'var(--bg-surface)', border: '1px solid var(--bg-card-border)', color: 'var(--text-primary)', borderRadius: '6px', fontFamily: 'var(--font-family-mono)' }}
                />
              </div>
            </>
          )}

          {activeTopic === 'assignment' && (
            <div>
              <label style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>Assignment Cost Matrix N×N (Rows by line, comma-separated):</label>
              <textarea
                rows={4} value={assignCosts} onChange={(e) => setAssignCosts(e.target.value)}
                style={{ width: '100%', padding: '0.5rem', background: 'var(--bg-surface)', border: '1px solid var(--bg-card-border)', color: 'var(--text-primary)', borderRadius: '6px', fontFamily: 'var(--font-family-mono)' }}
              />
            </div>
          )}

          <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '0.5rem', marginTop: '0.5rem' }}>
            <button type="button" className="action-btn" onClick={onClose}>Cancel</button>
            <button type="submit" className="action-btn primary">✨ Generate Interactive Solution</button>
          </div>
        </form>
      </div>
    </div>
  );
};
