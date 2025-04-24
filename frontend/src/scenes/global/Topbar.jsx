import { Box, IconButton, useTheme } from "@mui/material";
import { useContext, useEffect, useMemo, useState, useRef } from "react";
import { ColorModeContext, tokens } from "../../theme";
import InputBase from "@mui/material/InputBase";
import LightModeOutlinedIcon from "@mui/icons-material/LightModeOutlined";
import DarkModeOutlinedIcon from "@mui/icons-material/DarkModeOutlined";
import SearchIcon from "@mui/icons-material/Search";
import Fuse from "fuse.js";
import { useNavigate } from "react-router-dom";

const Topbar = () => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);
  const ColorMode = useContext(ColorModeContext);
  const navigate = useNavigate();

  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);
  const [highlightedIndex, setHighlightedIndex] = useState(-1);
  const inputRef = useRef();

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

  const fuse = useMemo(
    () =>
      new Fuse(searchableLinks, {
        keys: ["title", "content"],
        threshold: 0.3,
      }),
  );

  useEffect(() => {
    if (query) {
      const matches = fuse.search(query).map((match) => match.item);

      if (JSON.stringify(matches) !== JSON.stringify(results)) {
        setResults(matches);
        setHighlightedIndex(0);
      }
    } else {
      setResults([]);
      setHighlightedIndex(-1);
    }
  }, [query, fuse]);

  useEffect(() => {
    const handleSlashFocus = (e) => {
      const target = e.target;
      const isInput =
        target.tagName === "INPUT" ||
        target.tagName === "TEXTAREA" ||
        target.isContentEditable;

      if (e.key === "/" && !isInput) {
        e.preventDefault();
        inputRef.current?.focus();
      }
    };

    window.addEventListener("keydown", handleSlashFocus);
    return () => window.removeEventListener("keydown", handleSlashFocus);
  }, []);

  const handleKeyDown = (e) => {
    if (!results.length) return;

    if (e.key === "ArrowDown") {
      e.preventDefault();
      setHighlightedIndex((prev) => (prev + 1) % results.length);
    } else if (e.key === "ArrowUp") {
      e.preventDefault();
      setHighlightedIndex((prev) => (prev - 1) % results.length);
    } else if (e.key === "Enter" && highlightedIndex >= 0) {
      const selected = results[highlightedIndex];
      if (selected) {
        navigate(selected.path);
        setQuery("");
        setResults([]);
      }
    }
  };

  return (
    <Box display="flex" justifyContent="space-between" p={2}>
      {/* Search Bar */}
      <Box
        display="flex"
        backgroundColor={theme.palette.accent}
        borderColor={colors.darkPastelGreen[600]}
        borderRadius="3px"
        position="relative"
      >
        <InputBase
          inputRef={inputRef}
          width="300px"
          sx={{ ml: 2, flex: 1 }}
          placeholder="Search"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Escape") {
              e.target.blur();
              return;
            }
            handleKeyDown(e);
          }}
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
            borderColor={theme.palette.accent}
            borderRadius="4px"
            boxShadow={3}
            zIndex={1300}
            backgroundColor={theme.palette.accent}
          >
            {results.map((result, index) => (
              <Box
                key={result.id}
                p={1}
                sx={{
                  cursor: "pointer",
                  backgroundColor:
                    index === highlightedIndex
                      ? colors.processCyan[600]
                      : "transparent",
                  ":hover": { backgroundColor: colors.processCyan[600] },
                }}
                onMouseEnter={() => setHighlightedIndex(index)}
                onClick={() => {
                  setQuery("");
                  setResults([]);
                  navigate(result.path);
                }}
              >
                <strong>{result.title}</strong>
                <div
                  // style={{ fontSize: "0.8em", color: colors.redAccent[400] }}
                  style={{ fontSize: "0.8em", color: colors.processCyan[500] }}
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
