import os

# Read generate_app_html.py base
with open('generate_app_html.py', 'r', encoding='utf-8') as f:
    html_head = f.read().split('print("Loading data definitions...")')[0]

# Read master_builder.py
with open('master_builder.py', 'r', encoding='utf-8') as f:
    lpp_data = f.read().split('lpp_code = """')[1].split('"""')[0]

# Read build_entire_75_hub.py
with open('build_entire_75_hub.py', 'r', encoding='utf-8') as f:
    rest_data = f.read()

# Assemble JavaScript
js_code = lpp_data + '\n' + rest_data

# Combine HTML
full_html = html_head + js_code + '\n' + """
// ====================================================================
// MAIN APP COMPONENT
// ====================================================================
function App(){
  const [tab,setTab]=useState('home');
  const [selMod,setSelMod]=useState(null);
  const [selProb,setSelProb]=useState(null);

  const tabs=[{id:'home',label:'🏠 Home'},...MODULES.map(m=>({id:m.id,label:`${m.icon} ${m.title.split('(')[0].trim()}`}))];

  const gotoTab=(id)=>{setTab(id);setSelProb(null);if(id==='home') setSelMod(null);else setSelMod(MODULES.find(m=>m.id===id)||null);};

  let content;
  if(tab==='home') content=<ModuleHome modules={MODULES} onSelect={m=>{setSelMod(m);setTab(m.id);}}/>;
  else{
    const mod=selMod||MODULES.find(m=>m.id===tab);
    if(!mod) content=<div>Not found</div>;
    else if(selProb) content=<ProblemDetail problem={selProb} onBack={()=>setSelProb(null)} moduleColor={mod.color}/>;
    else content=<ProblemList module={mod} onSelect={setSelProb} onBack={()=>gotoTab('home')}/>;
  }

  return(
    <div>
      <div id="app-header">
        <div className="header-inner">
          <div className="header-left">
            <div className="header-logo">📐</div>
            <div className="header-text">
              <h1>OR Learning Hub – OTDM</h1>
              <p>PGDM 2024-2026 · Great Lakes Institute of Management</p>
            </div>
          </div>
        </div>
        <div className="nav-strip">
          <div className="nav-strip-inner">
            {tabs.map(t=><button key={t.id} className={`ntab ${tab===t.id?'active':''}`} onClick={()=>gotoTab(t.id)}>{t.label}</button>)}
          </div>
        </div>
      </div>
      <main className="main">{content}</main>
    </div>
  );
}

ReactDOM.render(React.createElement(App), document.getElementById('root'));
</script>
</body>
</html>
"""

with open('app.html', 'w', encoding='utf-8') as f:
    f.write(full_html)

print(f"✅ app.html successfully generated! File size: {os.path.getsize('app.html')} bytes")
