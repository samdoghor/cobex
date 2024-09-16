/** @type {import('tailwindcss').Config} */
const flowbite = require("flowbite-react/tailwind");

export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}", flowbite.content()],
  darkMode: "selector",
  theme: {
    extend: {
      colors: {
        themeOne: "#01251d",
        themeTwo: "#072b35",
        themeThree: "#025744",
        themeFour: "#14aea1",
        themeFive: "#03896B",
        themeSix: "#011712",
      },
    },
  },
  plugins: [flowbite.plugin()],
};
