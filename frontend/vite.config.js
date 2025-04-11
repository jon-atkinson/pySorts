import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
  },
  // resolve: {
  //   alias: {
  //     crypto: "crypto-browserify",
  //     stream: "stream-browserify",
  //   },
  // },
});
