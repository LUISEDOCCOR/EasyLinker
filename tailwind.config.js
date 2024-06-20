/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/templates/*.html",
    "./src/templates/*/*.html"
  ],
  theme: {
    extend: {
      colors:{
        pastelGreen: "#90EE90",
        pastelPink: "#FFB2EF",
        pastelOrange: "#E3A018",
        pastelBlue: "#87CEFF",
        pastelYellow: "#FFDB58",
        pastelRed: "#FF7A5C",
        neonRed: "#ff4911",
        neonYellow: "#FFFF00",

      },
    },
  },
  plugins: [],
}

