import { ColorModeContext, useMode } from "./theme.js";
import { CssBaseline, ThemeProvider } from "@mui/material";
import { Routes, Route } from "react-router-dom";
import Topbar from "./scenes/global/Topbar";
import Sidebar from "./scenes/global/Sidebar";
// import Dashboard from "./scenes/Dashboard";
// import CompareAlgorithms from "./scenes/CompareAlgorithms";
// import CompareSortedness from "./scenes/CompareSortedness";
// import Previous from "./scenes/Previous";
// import About from "./scenes/About";
// import FAQ from "./scenes/FAQ";
import Graph from "./scenes/graph";
// import Languages from "./scenes/Languages";

function App() {
  const [theme, colorMode] = useMode();

  return (
    <ColorModeContext.Provider value={colorMode}>
      <ThemeProvider theme={theme}>
        <CssBaseline />
        <div className="app">
          <Sidebar />
          <main className="content">
            <Topbar />
            <Routes>
              {/* <Route path="/" element={<Dashboard />} /> */}
              {/* <Route path="/algorithms" element={<CompareAlgorithms />} /> */}
              {/* <Route path="/sortedness" element={<CompareSortedness />} /> */}
              {/* <Route path="/previous" element={<Previous />} /> */}
              {/* <Route path="/about" element={<About />} /> */}
              {/* <Route path="/faq" element={<FAQ />} /> */}
              <Route path="/graph" element={<Graph />} />
              {/* <Route path="/languages" element={<Languages />} /> */}
            </Routes>
          </main>
        </div>
      </ThemeProvider>
    </ColorModeContext.Provider>
  );
}

export default App;
