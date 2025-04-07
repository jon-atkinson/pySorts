import { Box, IconButton, useTheme } from "@mui/material";
import { useContext } from "react";
import { ColorModeContext, tokens } from "../../theme";
import InputBase from "@mui/material/InputBase";
import LightModeOutlinedIcon from "@mui/icons-material/LightModeOutlined";
import DarkModeOutlinedIcon from "@mui/icons-material/DarkModeOutlined";
import SearchIcon from "@mui/icons-material/Search";
import Fuse from "fuse.js";
import { useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";

const Topbar = () => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);
  const ColorMode = useContext(ColorModeContext);

  const navigate = useNavigate();

  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);

  const searchableLinks = [
    {
      id: "dashboard",
      title: "Dashboard",
      path: "/",
      content: "App dashboard and how-to section",
    },
    {
      id: "algorithms",
      title: "Compare Algorithms",
      path: "/algorithms",
      content: "Algorithm comparison functionality",
    },
    {
      id: "sortedness",
      title: "Compare Array Types",
      path: "/sortedness",
      content: "Input array comparison functionality",
    },
    {
      id: "previous",
      title: "Previous Runs",
      path: "/previous",
      content: "Cache of previous run results",
    },
    {
      id: "about",
      title: "About pySorts",
      path: "/about",
      content: "Outline of the purpose and features of pySorts",
    },
    {
      id: "results",
      title: "Results",
      path: "/graph",
      content: "Graph of the most recently selected comparison",
    },
  ];

  const fuse = new Fuse(searchableLinks, {
    keys: ["title", "content"],
    threshold: 0.3,
  });

  useEffect(() => {
    if (query) {
      const matches = fuse.search(query);
      setResults(matches.map((match) => match.item));
    } else {
      setResults([]);
    }
  }, [query]);

  return (
    <Box display="flex" justifyContent="space-between" p={2}>
      {/* Search Bar */}
      <Box
        display="flex"
        backgroundColor={colors.primary[400]}
        borderColor={colors.grey[600]}
        borderRadius="3px"
        position="relative"
      >
        <InputBase
          width="300px"
          sx={{ ml: 2, flex: 1 }}
          placeholder="Search"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
        <IconButton type="button" sx={{ p: 1 }}>
          <SearchIcon />
        </IconButton>
        {results.length > 0 && (
          <Box
            position="absolute"
            top="100%"
            left={0}
            width="300px"
            border="1px solid"
            borderColor={colors.primary[400]}
            borderRadius="4px"
            boxShadow={3}
            zIndex={1300}
            backgroundColor={colors.primary[400]}
          >
            {results.map((result) => (
              <Box
                key={result.id}
                p={1}
                sx={{
                  cursor: "pointer",
                  ":hover": { backgroundColor: colors.greenAccent[600] },
                }}
                onClick={() => {
                  setQuery("");
                  setResults([]);
                  navigate(result.path);
                }}
              >
                <strong>{result.title}</strong>
                <div
                  style={{ fontSize: "0.8em", color: colors.redAccent[400] }}
                >
                  {result.content}
                </div>
              </Box>
            ))}
          </Box>
        )}
      </Box>
      <Box display="flex">
        <IconButton onClick={ColorMode.toggleColorMode}>
          {theme.palette.mode === "dark" ? (
            <DarkModeOutlinedIcon />
          ) : (
            <LightModeOutlinedIcon />
          )}
        </IconButton>
      </Box>
    </Box>
  );
};

export default Topbar;
