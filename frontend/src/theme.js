import { createContext, useState, useMemo } from "react";
import { createTheme } from "@mui/material/styles";

// all themes
const allTokens = {
  default: (mode) =>
    mode === "dark"
      ? {
          background: {
            100: "#d2f2dd",
            200: "#a6e5bb",
            300: "#79d999",
            400: "#4dcc77",
            500: "#20bf55",
            600: "#1a9944",
            700: "#137333",
            800: "#0d4c22",
            900: "#062611",
          },
          primary: {
            100: "#cddce2",
            200: "#9bb9c4",
            300: "#6895a7",
            400: "#367289",
            500: "#044f6c",
            600: "#033f56",
            700: "#022f41",
            800: "#02202b",
            900: "#011016",
          },
          accent1: {
            100: "#ccf1fc",
            200: "#99e3f9",
            300: "#67d6f5",
            400: "#34c8f2",
            500: "#01baef",
            600: "#0195bf",
            700: "#01708f",
            800: "#004a60",
            900: "#002530",
          },
          accent2: {
            100: "#fefeff",
            200: "#fdfdff",
            300: "#fdfdff",
            400: "#fcfcff",
            500: "#fbfbff",
            600: "#c9c9cc",
            700: "#979799",
            800: "#646466",
            900: "#323233",
          },
          accent3: {
            100: "#e3e3e3",
            200: "#c8c8c8",
            300: "#acacac",
            400: "#919191",
            500: "#757575",
            600: "#5e5e5e",
            700: "#464646",
            800: "#2f2f2f",
            900: "#171717",
          },
        }
      : {
          background: {
            100: "#062611",
            200: "#0d4c22",
            300: "#137333",
            400: "#1a9944",
            500: "#20bf55",
            600: "#4dcc77",
            700: "#79d999",
            800: "#a6e5bb",
            900: "#d2f2dd",
          },
          primary: {
            100: "#011016",
            200: "#02202b",
            300: "#022f41",
            400: "#033f56",
            500: "#044f6c",
            600: "#367289",
            700: "#6895a7",
            800: "#9bb9c4",
            900: "#cddce2",
          },
          accent1: {
            100: "#002530",
            200: "#004a60",
            300: "#01708f",
            400: "#0195bf",
            500: "#01baef",
            600: "#34c8f2",
            700: "#67d6f5",
            800: "#99e3f9",
            900: "#ccf1fc",
          },
          accent2: {
            100: "#323233",
            200: "#646466",
            300: "#979799",
            400: "#c9c9cc",
            500: "#fbfbff",
            600: "#fcfcff",
            700: "#fdfdff",
            800: "#fdfdff",
            900: "#fefeff",
          },
          accent3: {
            100: "#171717",
            200: "#2f2f2f",
            300: "#464646",
            400: "#5e5e5e",
            500: "#757575",
            600: "#919191",
            700: "#acacac",
            800: "#c8c8c8",
            900: "#e3e3e3",
          },
        },
  kanagawa: (mode) =>
    mode === "dark"
      ? {
          background: {
            100: "",
            200: "",
            300: "",
            400: "",
            500: "",
            600: "",
            700: "",
            800: "",
            900: "",
          },
          primary: {
            100: "",
            200: "",
            300: "",
            400: "",
            500: "",
            600: "",
            700: "",
            800: "",
            900: "",
          },
          accent1: {
            100: "",
            200: "",
            300: "",
            400: "",
            500: "",
            600: "",
            700: "",
            800: "",
            900: "",
          },
          accent2: {
            100: "#fefeff",
            200: "#fdfdff",
            300: "#fdfdff",
            400: "#fcfcff",
            500: "#fbfbff",
            600: "#c9c9cc",
            700: "#979799",
            800: "#646466",
            900: "#323233",
          },
          accent3: {
            100: "#e3e3e3",
            200: "#c8c8c8",
            300: "#acacac",
            400: "#919191",
            500: "#757575",
            600: "#5e5e5e",
            700: "#464646",
            800: "#2f2f2f",
            900: "#171717",
          },
        }
      : {
          background: {
            100: "#062611",
            200: "#0d4c22",
            300: "#137333",
            400: "#1a9944",
            500: "#20bf55",
            600: "#4dcc77",
            700: "#79d999",
            800: "#a6e5bb",
            900: "#d2f2dd",
          },
          primary: {
            100: "#011016",
            200: "#02202b",
            300: "#022f41",
            400: "#033f56",
            500: "#044f6c",
            600: "#367289",
            700: "#6895a7",
            800: "#9bb9c4",
            900: "#cddce2",
          },
          accent1: {
            100: "#002530",
            200: "#004a60",
            300: "#01708f",
            400: "#0195bf",
            500: "#01baef",
            600: "#34c8f2",
            700: "#67d6f5",
            800: "#99e3f9",
            900: "#ccf1fc",
          },
          accent2: {
            100: "#323233",
            200: "#646466",
            300: "#979799",
            400: "#c9c9cc",
            500: "#fbfbff",
            600: "#fcfcff",
            700: "#fdfdff",
            800: "#fdfdff",
            900: "#fefeff",
          },
          accent3: {
            100: "#171717",
            200: "#2f2f2f",
            300: "#464646",
            400: "#5e5e5e",
            500: "#757575",
            600: "#919191",
            700: "#acacac",
            800: "#c8c8c8",
            900: "#e3e3e3",
          },
        },
};

// color design tokens
export const tokens = (themeName, mode) => {
  const theme = allTokens[themeName] || allTokens["default"];
  return theme(mode);
};

// mui theme settings
export const themeSettings = (theme, mode) => {
  const colors = tokens(theme, mode);

  return {
    palette: {
      mode: mode,
      ...(mode === "dark"
        ? {
            primary: {
              main: colors.primary[500],
            },
            secondary: {
              main: colors.greenAccent[500],
            },
            neutral: {
              dark: colors.background[700],
              main: colors.background[500],
              light: colors.background[100],
            },
            background: {
              default: colors.primary[500],
            },
          }
        : {
            primary: {
              main: colors.primary[100],
            },
            secondary: {
              main: colors.greenAccent[500],
            },
            neutral: {
              dark: colors.background[700],
              main: colors.background[500],
              light: colors.background[100],
            },
            background: {
              default: "#fcfcfc",
            },
          }),
    },
    typography: {
      fontFamily: ["Source Sans 3", "sans-serif"].join("*"),
      fontSize: 12,
      h1: {
        fontFamily: ["Source Sans 3", "sans-serif"].join("*"),
        fontSize: 40,
      },
      h2: {
        fontFamily: ["Source Sans 3", "sans-serif"].join("*"),
        fontSize: 32,
      },
      h3: {
        fontFamily: ["Source Sans 3", "sans-serif"].join("*"),
        fontSize: 24,
      },
      h4: {
        fontFamily: ["Source Sans 3", "sans-serif"].join("*"),
        fontSize: 20,
      },
      h5: {
        fontFamily: ["Source Sans 3", "sans-serif"].join("*"),
        fontSize: 16,
      },
      h6: {
        fontFamily: ["Source Sans 3", "sans-serif"].join("*"),
        fontSize: 14,
      },
    },
  };
};

// context for color mode
export const ColorModeContext = createContext({
  toggleColorMode: () => {},
});

export const useMode = () => {
  const [mode, setMode] = useState("dark");

  const colorMode = useMemo(
    () => ({
      toggleColorMode: () =>
        setMode((prev) => (prev === "light" ? "dark" : "light")),
    }),
    [],
  );

  const theme = useMemo(() => createTheme(themeSettings(mode)), [mode]);

  return [theme, colorMode];
};
