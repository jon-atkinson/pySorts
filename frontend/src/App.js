import { ColorModeContext, useMode } from "./theme.js";
import { CssBaseline, ThemeProvider, Typography } from "@mui/material";
import { Routes, Route } from "react-router-dom";
import Topbar from "./scenes/global/Topbar";
import Sidebar from "./scenes/global/Sidebar";
import Dashboard from "./scenes/dashboard";
import { useEffect, useState } from "react";
import axios from "axios";
import CompareAlgorithms from "./scenes/compareAlgorithms";
import CompareArrays from "./scenes/compareArrays";
import Previous from "./scenes/previous";
import About from "./scenes/about";
import FAQ from "./scenes/faq";
import Graph from "./scenes/graph";
// import Languages from "./scenes/Languages";

function App() {
  const [theme, colorMode] = useMode();
  const [loading, setLoading] = useState(true);
  const [config, setConfig] = useState(null);
  const [error, setError] = useState(null);
  const [graphData, setGraphData] = useState([
    { color: "black", data: [{ x: 0, y: 0 }], id: "empty" },
  ]);

  // every time the raw comparison data is updated the processed data base should also update
  const [originalGraphData, setOriginalGraphDataBase] = useState([
    //const [originalGraphData, setOriginalGraphData] = useState([
    { color: "black", data: [{ x: 0, y: 0 }], id: "empty" },
  ]);
  const setOriginalGraphData = (newData) => {
    setGraphData(newData);
    setOriginalGraphDataBase(JSON.parse(JSON.stringify(newData)));
    // setOriginalGraphDataBase(newData);
  };

  const [selected, setSelected] = useState("Dashboard");

  useEffect(() => {
    const fetchConfig = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:8000/config");
        setConfig(response.data);
      } catch (err) {
        setError(err.message);
        console.log(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchConfig();
  }, []);

  if (loading) {
    return <Typography>Requesting config...</Typography>;
  }

  if (error) {
    return <Typography color="red">Error: {error}</Typography>;
  }

  return (
    <ColorModeContext.Provider value={colorMode}>
      <ThemeProvider theme={theme}>
        <CssBaseline />
        <div className="app">
          <Sidebar selected={selected} setSelected={setSelected} />
          <main className="content">
            <Topbar />
            <Routes>
              <Route path="/" element={<Dashboard />} />
              <Route
                path="/algorithms"
                element={
                  <CompareAlgorithms
                    config={config}
                    setOriginalGraphData={setOriginalGraphData}
                    setSelected={setSelected}
                  />
                }
              />
              <Route
                path="/sortedness"
                element={
                  <CompareArrays
                    config={config}
                    setOriginalGraphData={setOriginalGraphData}
                    setSelected={setSelected}
                  />
                }
              />
              <Route
                path="/previous"
                element={
                  <Previous
                    setOriginalGraphData={setOriginalGraphData}
                    setSelected={setSelected}
                  />
                }
              />
              <Route path="/about" element={<About />} />
              <Route path="/faq" element={<FAQ />} />
              <Route
                path="/graph"
                element={
                  <Graph
                    graphData={graphData}
                    setGraphData={setGraphData}
                    originalGraphData={originalGraphData}
                  />
                }
              />
              {/* <Route path="/languages" element={<Languages />} /> */}
            </Routes>
          </main>
        </div>
      </ThemeProvider>
    </ColorModeContext.Provider>
  );
}

export default App;
