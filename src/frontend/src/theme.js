import { createContext, useState, useMemo } from "react";
import { createTheme } from "@mui/material/styles";

// color design tokens
export const tokens = (mode) => ({
   green: {
          100: "#d2f2dd",
          200: "#a6e5bb",
          300: "#79d999",
          400: "#4dcc77",
          500: "#20bf55",
          600: "#1a9944",
          700: "#137333",
          800: "#0d4c22",
          900: "#062611"
}
   indigo: {
          100: "#cddce2",
          200: "#9bb9c4",
          300: "#6895a7",
          400: "#367289",
          500: "#044f6c",
          600: "#033f56",
          700: "#022f41",
          800: "#02202b",
          900: "#011016"
},
   teal: {
          100: "#ccf1fc",
          200: "#99e3f9",
          300: "#67d6f5",
          400: "#34c8f2",
          500: "#01baef",
          600: "#0195bf",
          700: "#01708f",
          800: "#004a60",
          900: "#002530"
},
   white: {
          100: "#fefeff",
          200: "#fdfdff",
          300: "#fdfdff",
          400: "#fcfcff",
          500: "#fbfbff",
          600: "#c9c9cc",
          700: "#979799",
          800: "#646466",
          900: "#323233"
},
   indigo: {
          100: "#e3e3e3",
          200: "#c8c8c8",
          300: "#acacac",
          400: "#919191",
          500: "#757575",
          600: "#5e5e5e",
          700: "#464646",
          800: "#2f2f2f",
          900: "#171717"
},
});

// mui theme settins
export const themeSettings = (mode) => {
  const colors = tokens(mode);

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
              dark: colors.grey[700],
              main: colors.grey[500],
              light: colors.grey[100],
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
              dark: colors.grey[700],
              main: colors.grey[500],
              light: colors.grey[100],
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
